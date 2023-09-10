# Importar las bibliotecas necesarias
from flask import Flask, jsonify
from pymongo import MongoClient
import requests

# Configuración de Flask
app = Flask(__name__)

# Configuración de MongoDB Atlas
client = MongoClient ("mongodb+srv://dbuser:kxepJMSqx3IhLrKY@atlascluster.enwmmib.mongodb.net/?retryWrites=true&w=majority")

db = client.weather_data
collection = db.weather

# Función para obtener datos meteorológicos de una API y almacenarlos en MongoDB
def obtener_y_almacenar_datos():
    api_key = "ydEdfb5nO87zWpME2fkRAx5nJAGTF2Ah"
    ciudad = "SAM"
    url = f"http://dataservice.accuweather.com/locations/v1/7894?apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    # Almacenar datos en MongoDB
    collection.insert_one(data)

# Ruta para obtener los datos almacenados en MongoDB
@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    datos = list(collection.find())
    return jsonify(datos)

if __name__ == '__main__':
    obtener_y_almacenar_datos()
    app.run(debug=True)
