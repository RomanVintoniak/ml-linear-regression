import pickle
from flask import Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

from .api import api
app.register_blueprint(api)

from app import views
