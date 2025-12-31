from flask import Flask, request, jsonify
import time
import uuid
import logging
from pythonjsonlogger import jsonlogger

app = Flask(__name__)

# ---------- Logging ----------
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# ---------- In-memory storage ----------
tasks = []
request_count = 0
total_response_time = 0.0

def generate_id():
    return len(tasks) + 1

@app.before_request
def start_timer():
    request.start_time = time.time()
    request.trace_id = str(uuid.uuid4())

@app.after_request
def log_request(response):
    global request_count, total_response_time
    duration = time.time() - request.start_time
    request_count += 1
    total_response_time += duration

    logger.info({
        "trace_id": request.trace_id,
        "method": request.method,
        "path": request.path,
        "status": response.status_code,
        "duration_ms": round(duration * 1000, 2)
    })
    return response

# ---------- Routes ----------
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = {
        "id": generate_id(),
        "title": data["title"],
        "completed": False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return "", 204

@app.route("/metrics", methods=["GET"])
def metrics():
    avg_time = total_response_time / request_count if request_count > 0 else 0
    return (
        f"requests_total {request_count}\n"
        f"average_response_time_seconds {avg_time}\n"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
