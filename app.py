from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class Todo(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100))
        complete = db.Column(db.Boolean)
    
    db.create_all()

    @app.get("/")
    def home():
        return "hello from home"
    
    @app.post("/add")
    def add():
        return "add endpoint"
    
    @app.get("/update/<int:todo_id>")
    def update(todo_id):
        return "update"

    @app.get("/delete/<int:todo_id>")
    def delete(todo_id):
        return "delete"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)