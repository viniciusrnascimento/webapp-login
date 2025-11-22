#!/bin/bash
# startup.sh

# Atualiza certificados CA
sudo update-ca-certificates

# Instala dependências do ODBC Driver 18
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev

# Ativa o virtual environment
source /home/site/wwwroot/antenv/bin/activate

# Inicia o Gunicorn
gunicorn --chdir /home/site/wwwroot --bind=0.0.0.0:8000 wsgi:application
