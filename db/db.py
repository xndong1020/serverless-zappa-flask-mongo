import pymongo
import json


class Db:
    _instance = None

    @staticmethod
    def create_instance():
        with open('project_settings.json') as f:
            config = json.load(f)

        mongo_client = pymongo.MongoClient(config['dev']['mongodb'], config['dev']['port'])
        Db._instance = mongo_client[config['dev']['db']]
        Db._instance.authenticate(config['dev']['username'], config['dev']['password'])

    @staticmethod
    def get_instance():
        if Db._instance is not None:
            return Db._instance
        else:
            Db.create_instance()
            return Db._instance
