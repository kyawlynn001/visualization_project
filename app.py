from flask import Flask,jsonify
from flask import render_template
from random import sample
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)
MONGODB_HOST = 'localhost'
MONGODB_PORT= 27017
DBS_NAME = "cancer_db"
collection_name = "cancer"
collection_name1= "visualization_project"
FIELDS = {"diagnosis": True, "radius_mean": True,"radius_worst":True,"_id":False}
FIELDB = {"diagnosis": True, "radius_mean": True,"_id":False}
FIELDM = {"diagnosis": "M", "radius_mean": True,"_id":False}
FIELDR = {"radius_mean": True,"radius_worst":True,"_id":False}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cancer_db/cancer")
def cancer_db_cancer():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][collection_name]
    cancer = collection.find(projection=FIELDS)
    json_cancer = []
    for row in cancer:
        json_cancer.append(row)
    json_cancer = json.dumps(json_cancer, default=json_util.default)
    connection.close()
    return json_cancer

@app.route("/cancer_db/malignant")
def cancer_db_malignant():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][collection_name]
    malignant = collection.find(projection=FIELDM)
    json_malignant= []
    for row in malignant:
        json_malignant.append(row)
    json_malignant = json.dumps(json_malignant, default=json_util.default)
    connection.close()
    return json_malignant

@app.route("/cancer_db/benign")
def cancer_db_benign():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][collection_name]
    benign = collection.find(projection=FIELDB)
    json_benign= []
    for row in benign:
        json_benign.append(row)
    json_benign = json.dumps(json_benign, default=json_util.default)
    connection.close()
    return json_benign

@app.route("/cancer_db/radius")
def cancer_db_radius():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][collection_name]
    radius = collection.find(projection=FIELDR)
    json_radius= []
    for row in radius:
        json_radius.append(row)
    json_radius = json.dumps(json_radius, default=json_util.default)
    connection.close()
    return json_radius

if __name__ == "__main__":
    app.run()
   

    