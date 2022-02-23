from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Project Name', db.String())
    date = db.Column('Completion Date', db.DateTime())
    description = db.Column('Description', db.Text)
    skills_list = db.Column('Skills', db.String())
    github = db.Column('GitHub Link', db.String())

    def __repr__(self):
        return f'''<Project(Project Title: {self.title},
                Date: {self.date}
                Description: {self.discription},
                Skills List: {self.skills_list},
                Github Link: {self.github})'''
