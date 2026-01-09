# Étape 1 : Image Python de base
FROM python:3.12-slim

# Étape 2 : Dossier de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier tous les fichiers dans le conteneur
COPY . .

# Étape 4 : Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port 5000
EXPOSE 5000

# Étape 6 : Lancer l'application
CMD ["python", "app.py"]
