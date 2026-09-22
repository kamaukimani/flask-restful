from flask_restful import Resource,Api 
from flask import request,make_response 
from app.models import Newsletter
from app.db import db

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
    def post(self):
        data=request.get_json()
        newsletter=Newsletter()
        allowed_fields=["body","title"]
        for attr,value in data.items():
            if attr in allowed_fields:
                setattr(newsletter,attr,value)
        db.session.add(newsletter)
        db.session.commit()

        newsletter_dict=newsletter.to_dict()

        response=make_response(
            newsletter_dict,
            201
        )
        return response
class NewsletterById(Resource):
    def get(self,id):
        newsletter=Newsletter.query.filter(Newsletter.id == id).first()
        if newsletter is None:
            return {"message":"OOOpps!!!!The record does not exist in our database"},404
        newsletter_dict=newsletter.to_dict()
        response=make_response(
            newsletter_dict,
            200
        )
        return response
    def patch(self,id):
        newsletter=Newsletter.query.filter(Newsletter.id == id).first()
        if newsletter is None:
            return {"message":"OOOpps!!!!The record does not exist in our database"},404
        data=request.get_json()
        allowed_fields=["body","title"]
        for attr in data:
            if attr in allowed_fields:
                setattr(newsletter,attr,data[attr])
        db.session.commit()
        newsletter_dict=newsletter.to_dict()
        response=make_response(
            newsletter_dict,
            200
        )
        return response

