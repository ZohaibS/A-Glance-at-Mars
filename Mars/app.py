from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
import scraping_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.mars_db
db.mars.drop()

@app.route("/scrape")
def scrape():
    mars = db.mars
    mars_data = scraping_mars.Scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

@app.route('/')
def index():
    mars = db.mars.find_one()
    return render_template("index.html", mars=mars)

if __name__ == "__main__":
    app.run(debug=True)
