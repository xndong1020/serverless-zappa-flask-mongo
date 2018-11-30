import pymongo


class Db:
    _instance = None

    @staticmethod
    def create_instance():
        mongo_client = pymongo.MongoClient('mongodb://ds121834.mlab.com', 21834)
        Db._instance = mongo_client['webex']
        Db._instance.authenticate('isdance', 'Cc51315704')

    @staticmethod
    def get_instance():
        if Db._instance is not None:
            return Db._instance
        else:
            Db.create_instance()
            return Db._instance
