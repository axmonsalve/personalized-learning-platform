from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models.user import db
from routes.auth import auth

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'my$up3rS3cr3tK3y!@2024'

db.init_app(app)
jwt = JWTManager(app)

# Registrar los Blueprints
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Personalized Learning Platform API!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True)
