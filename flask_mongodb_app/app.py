from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app= Flask(__name__)
mongo_url = os.getenv("MONGO_URL")

client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)

db = client["student_db"]
collection = db["students"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():    

    try:
        name = request.form.get('name','').strip()
        email = request.form.get('email','').strip()
        course = request.form.get('course','').strip()
       
        if not name or not email or not course:
            return render_template('index.html',
            error="All fields required")

        student_data= {
                "name": name,
                "email": email,
                "course": course
            }

        collection.insert_one(student_data)
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('index.html',
        error= f"error submitting data: {str(e)}")
               
@app.route('/success')
def success():

    return render_template('success.html')      

if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)            