import flask
import json
from bson import ObjectId
from flask import request, jsonify
from flask import Flask
from pymongo import MongoClient
from flask_pymongo import PyMongo
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGO_DBNAME'] = 'konnect'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/konnect'
mongo = PyMongo(app)

@app.route('/api/v1/resources/msisdn', methods=['GET'])
def msisdn():
	if 'msisdn' in request.args:
		msisdn = request.args['msisdn']
	else:
		return "Error: No msisdn field provided. Please specify a msisdn."
   
    
	client = MongoClient('mongodb://localhost:27017/')
	db=client.konnect.interest
	c = db.find({'msisdn' : msisdn})
	output=[]
	for i in c:
		i['_id'] = str(i['_id'])
		i['last_updated']=str(i['last_updated'])
		del i['last_updated']
		del i['_id']
		output.append(i)
	#return json.dumps(output)
	l=len(output)
	return  jsonify({'Number of records': l},output)

@app.route('/api/v1/resources/provider_id', methods=['GET'])
def provider_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No provider_id field provided. Please specify a provider_id."
   
    
	client = MongoClient('mongodb://localhost:27017/')
	db=client.konnect.interest
	c = db.find({'provider_id' : id})
	output=[]
	for i in c:
		i['_id'] = str(i['_id'])
		i['last_updated']=str(i['last_updated'])
		del i['last_updated']
		del i['_id']
		output.append(i)
	#return json.dumps(output)
	l=len(output)
	return  jsonify({'Number of records': l},output)

@app.route('/api/v1/resources/subscription_name', methods=['GET'])
def subscription_name():
	if 'subscription_name' in request.args:
		subscription_name=request.args['subscription_name']
	else:
		return " Error: No subscription_name field provided. Please specify the a subscriptin name" 
	
	client = MongoClient('mongodb://localhost:27017/')
	db=client.konnect.interest
	c = db.find({'subscription_name' : subscription_name})
	output=[]
	for i in c:
		i['_id'] = str(i['_id'])
		i['last_updated']=str(i['last_updated'])
		del i['last_updated']
		del i['_id']
		output.append(i)
	#return json.dumps(output)
	l=len(output)
	return  jsonify({'Number of records': l},output)

@app.route('/api/v1/resources/economic_value', methods=['GET'])
def economic_value():
	if 'economic_value' in request.args:
		economic_value=request.args['economic_value']
	else:
		return " Error: No economic_value field provided. Please specify the a economic value" 
	
	client = MongoClient('mongodb://localhost:27017/')
	db=client.konnect.economic
	c = db.find({'economic_value' : economic_value})
	output=[]
	for i in c:
		i['_id'] = str(i['_id'])
		i['updated_at']=str(i['updated_at'])
		del i['updated_at']
		del i['_id']
		output.append(i)
	#r=json.dumps(output)
	l=len(output)	
	return  jsonify({'Number of records': l},output)


@app.route('/api/v1/resources/city', methods=['GET'])
def ip_location_city():
	if 'city' in request.args:
		city=request.args['city']
	else:
		return " Error: No city name field provided. Please specify the a city name" 
	
	client = MongoClient('mongodb://localhost:27017/')
	db=client.konnect.iplocations
	c = db.find({'city' : city})
	output=[]
	for i in c:
		i['_id'] = str(i['_id'])
		i['last_updated']=str(i['last_updated'])
		del i['last_updated']
		del i['_id']
		output.append(i)
	#r=json.dumps(output)
	l=len(output)	
	return  jsonify({'Number of records': l},output)

app.run()
