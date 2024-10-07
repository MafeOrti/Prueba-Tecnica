
import sys
import os

# Agregar la ruta del directorio de controllers al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'controller'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'service'))

from flask import Flask
from app.main.controller.product_controller import product_routes


from flask import Flask
from flask_cors import CORS
from database import db
# Importar y registrar blueprints para productos y proveedores
from app.main.controller.product_controller import product_routes
from app.main.controller.supplier_controller import supplier_routes



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route('/')
def home():
    return "¡Hola, mundo!"



app.register_blueprint(product_routes)
app.register_blueprint(supplier_routes)

if __name__ == '__main__':
    app.run(debug=True)

