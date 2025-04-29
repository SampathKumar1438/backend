# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    salary_min = db.Column(db.Integer, nullable=False)
    salary_max = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "company_name": self.company_name,
            "location": self.location,
            "job_type": self.job_type,
            "salary_min": self.salary_min,
            "salary_max": self.salary_max,
            "description": self.description,
        }
