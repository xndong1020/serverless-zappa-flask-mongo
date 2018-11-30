from flask import Flask
from flask import jsonify
from flask import request
from db.db import Db

app = Flask(__name__)


@app.route('/requests', methods=['GET'])
def get_all_requests():
    results = []
    requests = Db.get_instance().requests.find({}, {"_id": 0})

    for item in requests:
        results.append(item)

    return jsonify(results), 200


@app.route('/requests/<string:author>', methods=['GET'])
def get_by_name(author):
    request = Db.get_instance().requests.find_one({"author": {"$eq": author}}, {"_id": 0})
    return jsonify(request), 200


@app.route('/requests', methods=['POST'])
def create_request():
    request_object = request.get_json(force=True)
    _id = Db.get_instance().requests.insert_one(request_object).inserted_id
    return jsonify({}), 201


@app.route('/reponses', methods=['GET'])
def get_all_reponses():
    results = []
    reponses = Db.get_instance().reponses.find({}, {"_id": 0})

    for item in reponses:
        results.append(item)

    return jsonify(results), 200


@app.route('/reponses', methods=['POST'])
def create_reponse():
    request_object = request.get_json(force=True)
    _id = Db.get_instance().reponses.insert_one(request_object).inserted_id
    return jsonify({}), 201


if __name__ == '__main__':
    app.run(debug=True)
