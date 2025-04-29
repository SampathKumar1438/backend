# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Job
import config

app = Flask(__name__)
CORS(app)  # Allow all origins for now

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB tables
with app.app_context():
    db.create_all()


# Routes
@app.route('/')
def index():
    return "Flask backend is up and running!", 200

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.serialize() for job in jobs])


@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.json

    new_job = Job(
        title=data['title'],
        company_name=data['company_name'],
        location=data['location'],
        job_type=data['job_type'],
        salary_min=data['salary_min'],
        salary_max=data['salary_max'],
        description=data['description'],
    )
    db.session.add(new_job)
    db.session.commit()

    return jsonify({"message": "Job created successfully"}), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
