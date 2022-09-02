from flask_restful import Resource
from models.site import SiteModel
from flask_jwt_extended import jwt_required

class Sites(Resource):

    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()]}

class Site(Resource):

    def get(self, url):
        site = SiteModel.buscar_site(url)
        if site:
            return site.json()
        return {'message': 'Site not found.'}, 404
    
    def post(self, url):
        if SiteModel.buscar_site(url):
            return {"message": "The site '{}' already exists.".format(url)}, 400
        site = SiteModel(url)
        try:
            site.save_site()
        except:
            {'message': 'An internal error ocurred trying to create a new site.'}, 500
        return site.json()

    @jwt_required()
    def delete(self, url):
        site = SiteModel.buscar_site(url)
        if site:
            site.delete_site()
            return {"message": "The site '{}' delete sucessfully.".format(url)}
        return {'message': 'Site not found.'}, 404
        
