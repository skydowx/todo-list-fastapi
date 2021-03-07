"""
Author: Muhammad Omer Khalil
"""
from utils.MongoConfig import _db, mongo_settings

class TodoListResourceManager:
    def __init__(self):
        self.__collection = _db[mongo_settings.collection]

    def insert(self, _id, data: dict):
        """
        Makes a document inside the collection with the given _id to keep data.

        :param  _id: (int)  The _id of the newly inserted item.        
        :param data: (dict) A dictionary of data to store as document in the collection.

        :returns: (boolean) returns True/False based on the success of the insertion
        """

        document = data.copy()
        document["_id"] = _id
        
        result = self.__collection.insert_one(document)
        
        assert result.acknowledged

        return True #TODO: Error Handling about identifying and communicating failure

    def delete(self, _id):
        """
        Deletes a document inside the collection with the respective id.

        :param _id: (int) id of the document to remove from the collection.

        :returns: (boolean) returns True/False based on the success of the deletion.
        """

        success = True

        result = self.__collection.delete_one({"_id": _id})

        if not result.deleted_count:
            return not success

        return success


    def get(self, _id):
        """
        Get a document with a specific _id from the collection.

        :params _id: (int) id of the document to get.

        :returns:   (boolean) True/False based on the result of the query
                    (dict) the respective document converted to python dictionary
        """

        success = True

        document = self.__collection.find_one({"_id": _id})
        
        if not document:
            return not success, {}
        
        return success, document

    def list_resources(self):
        """
        Get all documents in the collection.

        :returns:   (list) all documents in the collection
        """
        return True, self.__collection.find()