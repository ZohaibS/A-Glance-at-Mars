from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
import scraping_mars
import json

app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars_db'

client = PyMongo(app, uri=conn)

@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scraping_mars.Scrape()
    
    mars_data_dict = {"result": mars_data}
    #Saving to Mongo
    mars.update(
        {},
        mars_data_dict,
        upsert=True
    )
    
    #return jsonify(mars_data)
    return redirect("http://localhost:5000/", code=302)

@app.route('/')
def index():
    mars = client.db.mars.find_one()
    return render_template("index.html", mars=mars)

if __name__ == "__main__":
    app.run(debug=True)
