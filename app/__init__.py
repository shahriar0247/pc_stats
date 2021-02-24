from flask import Flask


app = Flask(__name__)

from app import main_view
from app import logic_view