from flask import Flask, render_template, redirect, abort, jsonify, request
from Database.database import Database

app = Flask(__name__)
db  = Database("ulr_databse.db")