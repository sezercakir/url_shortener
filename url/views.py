from app import app, db
from settings import *
from url.url import URL
from flask import Flask, flash
from flask import Flask, render_template, redirect, abort, jsonify, request, send_from_directory
from app import url_obj

# @brief Home Page
@app.route('/')
def home():
    """
        @brief  User can enter urls via form.
                Urls entered is encoded into short url. And encoded urls json
                returned /encode endpoint. For decoding, it can shown all
                decoded urls with /decode endpoint as json. Also, it can be
                possible accessing specific url via using shorten url of it
                with /decode&<encoded_part_of_short_url>

                You can access real url page with directly with request using
                shorten url.
    """

    return render_template('index.html')


@app.errorhandler(404)
def resource_not_found(e):
    """
        @brief Error json page
        @:return Json with error message
    """
    return jsonify(error=str(e)), 404

@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(STATIC_DIR, request.path[1:])

@app.route('/get')
def geturls():
    """
        @brief Get Method for all short and long urls as json
    """

    datas = db.show_urls("All")
    return datas


@app.route("/<string:key>")
def redirect_url(key):
    """
        @brief It can be accessed long url using
               encoded short url.
        @:return real long url page with redirect, if shorten
        url is not valid, returns error.
    """
    key = "http://127.0.0.1:5000/" + key

    if db.search(key,"Short"):
        return redirect(db.get_long(key))
    else:
        resource_not_found("There is not shorten link like that")
    
    return redirect("www.google.com")

@app.route("/encode", methods=["POST", "GET"])
def encode():
    """
        @brief Shortened links are not shortened again.
               Same encoded short links are checked to avoid produce
               same short link for same urls. url is also checked wheter is valid or not.

        @:return encoded shorten url
    """

    global short_url
    url         = request.form["url"]
    url_check   = None

    if ("http://" not in url) and ("https://" not in url) : url_check = "http://" + url 
    else: url_check = url

    if  url_obj.url_checker(url_check):
        if db.search(url, "Long"):
            return db.get_short(url)
        while 1:
            short_url = url_obj.random_generator(6)
            if not db.search(short_url,"Short"):
                if db.add_url("http://127.0.0.1:5000/" + short_url,url):
                    break
    else:
        resource_not_found("Unexpected Error. Renter")

    return db.show_urls("All")


@app.route("/decode")
def decodes():
    """
        @brief   Decodes shorten urls to long real urls
        @:return Long urls as json
    """
    return jsonify(db.show_urls("Long"))


@app.route("/decode&<string:key>")
def decode(key):

    """
        @brief   Decodes specific shorten url to real long url
        @:return Decoded shorten url to real long url as json
    """
    
    if not db.search("http://127.0.0.1:5000/"+key,"Short"):
        return resource_not_found("Not Found Given Encoded Url")

    data = {
        'Shorten': key,
        'Long': db.get_long("http://127.0.0.1:5000/"+key)
    }

    return jsonify(data)

#http://127.0.0.1:5000/7cJ8mD