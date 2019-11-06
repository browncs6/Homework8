#!/usr/bin/python3

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# This is for the form submission, don't worry about it being secure.
app.config['SECRET_KEY'] = 'penguinsrulelots'

todo_list = []

class AddForm(FlaskForm):
    # TODO: Add your name, notes, and submit fields here

@app.route() #TODO
def main_page():
    # TODO: Handle serving the main page and AddForm submission here.

@app.route() #TODO
def remove_todo():
    # TODO: Handle the POST request that removes batches of todo items
    # and redirect to "/"

app.run()
