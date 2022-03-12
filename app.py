from flask import Flask, render_template, redirect, abort, jsonify, request
from Database.database import Database
from url.url import URL


app         = Flask(__name__)
db          = Database("ulr_databse.db")
url_obj     = URL()


if __name__ == '__main__':
    app.debug = True
    app.run()