from flask_restful import Resource,Api 
from flask import request,make_response 
from app.models import Newsletter

class Home(Resource):
    def get(self):
        return {"message":"Welcome to the Newsletter RESTful API"},200

class Newsletters(Resource):
    def get(self):
        newsletters=[newsletter.to_dict() for newsletter in Newsletter.query.all()]
        response=make_response(
            newsletters,
            200
        )
        return response