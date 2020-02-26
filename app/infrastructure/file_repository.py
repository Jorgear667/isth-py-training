"""Service methods for file endpoints"""
import os
from app.common import Constants

class fileRepository:

    def get_file(self, id):
        return NotImplementedError

    def post_file(self, nombre, data):
        filepath = os.path.join(Constants.FILE_UPLOAD_PATH, nombre)
        if not os.path.exists(Constants.FILE_UPLOAD_PATH):
            os.makedirs(Constants.FILE_UPLOAD_PATH)
        
        archivo = open(filepath, "a")

        test = data.provide()

        return NotImplementedError