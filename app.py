import os
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
MONGO_URI_TEST = os.getenv("MONGO_URI")
app.config["MONGO_URI"] = MONGO_URI_TEST

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template('tasks.html', tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP', "0.0.0.0"), port=int(
        os.getenv('PORT', "5000")), debug=True)
