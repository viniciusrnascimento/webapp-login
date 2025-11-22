#!/bin/bash
# startup.sh - instala ODBC Driver 18 e inicia Gunicorn com wsgi.py

# Atualiza pacotes
apt-get update

# Instala dependências básicas
apt-get install -y curl apt-transport-https gnupg lsb-release

# Adiciona chave Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Adiciona repositório do Microsoft ODBC
DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
VERSION=$(lsb_release -rs)
echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/${VERSION}/prod ${DISTRO} main" > /etc/apt/sources.list.d/mssql-release.list

# Atualiza pacotes novamente
apt-get update

# Instala ODBC Driver 18
ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev

# Confirma instalação
echo "ODBC Drivers instalados:"
python3 -c "import pyodbc; print(pyodbc.drivers())"

# Inicia Gunicorn apontando para wsgi.py
exec gunicorn --bind 0.0.0.0:8000 wsgi:app
