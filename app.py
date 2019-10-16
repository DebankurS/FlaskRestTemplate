from flask import Flask, render_template,request, Response
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api=Api(app)
	


class index(Resource):
	def get(self):
		return {'hello':'world'}
	def get(self):
		content=request.json
		return {'returnval':'POST Response'}

api.add_resource(index,'/')

