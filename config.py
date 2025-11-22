import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mssql+pyodbc://adminsql:Admin!123@svr-lab-app.database.windows.net:1433/db-lab-app?driver=ODBC+Driver+18+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-super-secreta")
