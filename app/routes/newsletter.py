from flask_restful import Resource,Api 
from flask import request,make_response 

class Home(Resource):
    def get(self):
        return {"message":"Welcome to the Newsletter RESTful API"},200