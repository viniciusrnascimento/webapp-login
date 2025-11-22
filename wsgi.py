from app import app, db

# Expor o app como 'application' (padrão compatível com Azure/Gunicorn)
application = app

with app.app_context():
    db.create_all()
