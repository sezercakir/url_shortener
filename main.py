"""
    @author:   Talha Sezer Çakır
    @date:     12.03.2022
    @detail:   
"""


from flask import Flask, render_template, redirect, abort, jsonify, request
from Database.database import Database
from url.url import URL
from url.views import * 

if __name__ == '__main__':
    app.debug = True
    app.run()