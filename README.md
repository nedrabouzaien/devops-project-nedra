# 🚀 DevOps Project – Flask API

This project demonstrates a **complete DevOps pipeline** for a Python Flask API, including **CI/CD**, **containerization**, **security testing (SAST & DAST)**, **observability**, and **Kubernetes deployment**.

---

## 📌 Project Overview

The goal of this project is to apply DevOps and DevSecOps practices on a simple REST API:

* Continuous Integration with **GitHub Actions**
* Continuous Delivery using **Docker**
* Static & Dynamic Security Testing (**SAST / DAST**)
* Local orchestration with **Docker Compose**
* Container orchestration with **Kubernetes**

---

## 🧱 Architecture

```
Developer → GitHub → GitHub Actions (CI/CD)
                       │
                       ├─ Tests (pytest)
                       ├─ SAST (Bandit)
                       └─ Docker Image Build

Local Runtime:
- Docker Compose
- Kubernetes (local cluster)
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Python **3.10+**
* Git
* Docker & Docker Compose
* Docker Desktop (with Kubernetes enabled) or Minikube
* kubectl

---

## 📥 Project Setup (Local – Without Docker)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/devops-project-nedra.git
cd devops-project-nedra
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

Application will be available at:

```
http://localhost:5000
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t devops-project-nedra .
```

### Run Container

```bash
docker run -p 5000:5000 devops-project-nedra
```

---

## 🧩 Docker Compose (Recommended)

Docker Compose simplifies local execution and orchestration.

### Start the application

```bash
docker compose up --build
```

### Run in detached mode

```bash
docker compose up -d
```

### Stop services

```bash
docker compose down
```

Application:

```
http://localhost:5000
```

---

## 🔁 CI/CD Pipeline

The project uses **GitHub Actions** for CI/CD.

### CI (Continuous Integration)

Triggered on:

* push to `main`
* pull request to `main`

CI steps:

* Install dependencies
* Run unit tests
* Run SAST (Bandit)
* Build Docker image

### CD (Continuous Delivery)

* Automatically builds a Docker image ready for deployment
* Image can be deployed using Docker Compose or Kubernetes

---

## 🔐 Security Testing

### SAST – Static Application Security Testing

Tool: **Bandit**

* Analyzes Python source code
* Integrated into CI/CD pipeline
* Pipeline fails only on **high severity** vulnerabilities

### DAST – Dynamic Application Security Testing

Tool: **OWASP ZAP**

Steps:

1. Run the API using Docker Compose
2. Scan `http://localhost:5000` using OWASP ZAP (Automated Scan)
3. Analyze security headers and HTTP issues

---

## 📊 Observability

The application exposes metrics endpoint for monitoring:

```
GET /metrics
```

Can be integrated with Prometheus in advanced setups.

---

## ☸️ Kubernetes Deployment

### Folder Structure

```
k8s/
 ├─ deployment.yaml
 └─ service.yaml
```

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### Check resources

```bash
kubectl get pods
kubectl get services
```

### Access application

```
http://localhost:30007
```

---

## 🔗 API Endpoints (Examples)

### Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Hello from DevOps API"
}
```

### Metrics Endpoint

```http
GET /metrics
```

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── tests/
├── .github/workflows/
│   └── ci.yml
└── README.md
```

---

## ✅ Project Status

* ✔ CI/CD implemented
* ✔ Docker & Docker Compose
* ✔ SAST & DAST
* ✔ Observability
* ✔ Kubernetes deployment

---

## 👩‍💻 Author

**Nedra Bouzaien**
DevOps & Cybersecurity Student

---

## 📜 License

This project is for educational purposes.
