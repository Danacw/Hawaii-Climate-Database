#IMPORTS:
#________________________________________________

#Import Flask
from flask import Flask, jsonify

#Import dependencies
import numpy as np
import datetime as dt

# Import Python SQL Toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#REFLECT TABLES INTO ORM:
#________________________________________________

#Create engine
engine = create_engine('sqlite:///Resources/hawaii.sqlite', connect_args={'check_same_thread': False})
#Reflect existing database to new model
Base = automap_base()
Base.prepare(engine, reflect=True)
#Save references to tables
Station = Base.classes.station
Measurement = Base.classes.measurement
#Create session
session = Session(engine)


#FLASK SETUP:
#________________________________________________

# Create app
app = Flask(__name__)

#DEFINE ROUTES:
#________________________________________________

#Homepage
@app.route("/")
def Homepage():
    return "<h1> Hawaii Climate App | Flask API</h1>"

#Precipitation
@app.route("/api/v1.0/precipitation")
def Precipitation_Results():

    #Convert the query results to a dictionary
    start_date = dt.date(2017, 8, 23)
    query_date = start_date - dt.timedelta(days=365)

    #Retrieve last 12 months of data for preciptiation
    prcp_data = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= query_date)\
        .order_by(Measurement.date).all()

    #Convert to dictionary and return dictionary
    prcp_data_dict=dict(prcp_data)
    #Add title to jsonify function (creates a dictionary {} inside of an array [])
    j = jsonify(["Precipitation Results | August 2016 - August 2017", prcp_data_dict])
    return j 

#Stations
@app.route("/api/v1.0/stations")
def Station_List():

    #Return a JSON list of stations from dataset
    stations = session.query(Station.station).all()
    return jsonify(stations)

#Temperature
@app.route("/api/v1.0/tobs")
def Temperature():

    #Return a JSON list of temperature observations (TOBS) for the previous year.
    start_date = dt.date(2017, 8, 23)
    query_date = start_date - dt.timedelta(days=365)
    temperature = session.query(Measurement.tobs).filter(Measurement.station=="USC00519281").filter(Measurement.date >= query_date).all()
    clean_temp = list(np.ravel(temperature))
    return jsonify(['Previous year temperatures', clean_temp])

#Min, Max, Avg Temperatures
@app.route("/api/v1.0/<start>") 
@app.route("/api/v1.0/<start>/<end>")
def Aggregate_Temps(start=None, end=None):

    #Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    if not end:
        start_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
        clean_start_date = list(np.ravel(start_date))
        return jsonify([f'Min, Avg, and Max Temperatures for {start}', clean_start_date])
    
    range_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    clean_range_date = list(np.ravel(range_date))
    return jsonify([f'Min, Avg, and Max Temperatures for {start} to {end}', clean_range_date])

#RUN ROUTES:
#________________________________________________   

# Define Main Behavior
if __name__ == '__main__':
    app.run(debug=True)




