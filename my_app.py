from flask import Flask
from flask import jsonify
from flask import request
from db.db import Db
from bson import ObjectId

app = Flask(__name__)


@app.route('/requests', methods=['GET'])
def get_all_requests():
    """ Retrieve all requests from MongoDB """
    results = []
    requests = Db.get_instance().requests.find({}, {"_id": 0})  # projection exclude ObjectId
    [results.append(item) for item in requests]
    return jsonify(results), 200


@app.route('/requests/<string:id>', methods=['GET'])
def get_request_by_id(id):
    """ Retrieve a request record by ObjectId """
    request = Db.get_instance().requests.find_one({"_id": ObjectId(id)}, {"_id": 0})  # projection exclude ObjectId
    return jsonify(request), 200


@app.route('/requests', methods=['POST'])
def create_request():
    request_object = request.get_json(force=True)
    _id = Db.get_instance().requests.insert_one(request_object).inserted_id
    return "/requests/" + str(_id), 201


@app.route('/responses', methods=['GET'])
def get_all_responses():
    """ Retrieve all responses from MongoDB """
    results = []
    responses = Db.get_instance().responses.find({}, {"_id": 0})  # projection exclude ObjectId
    [results.append(item) for item in responses]
    return jsonify(results), 200


@app.route('/responses/<string:id>', methods=['GET'])
def get_response_by_id(id):
    """ Retrieve a response record by ObjectId """
    response = Db.get_instance().responses.find_one({"_id": ObjectId(id)}, {"_id": 0})  # projection exclude ObjectId
    Db.get_instance().responses.find_one({"_id": id})
    return jsonify(response), 200


@app.route('/responses', methods=['POST'])
def create_reponse():
    """ Create a record of response, save to MongoDB """
    request_object = request.get_json(force=True)
    _id = Db.get_instance().responses.insert_one(request_object).inserted_id
    return "/responses/" + str(_id), 201


if __name__ == '__main__':
    app.run(debug=True)
