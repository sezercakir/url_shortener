from app import app, db
from settings import *
from url.url import URL
from flask import Flask
from flask import Flask, render_template, redirect, abort, jsonify, request, send_from_directory

# Memory
url_obj     = URL()


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
        @brief Get Method for all json dict
    """
    #url_obj.json_dict
    return jsonify(list(db.show_urls("All")))


@app.route("/<string:key>")
def redirect_url(key):
    """
        @brief It can be accessed long url using
               encoded short url.
        @:return real long url page with redirect, if shorten
        url is not valid, returns error.
    """
    if url_obj.short_url_dictionary[key]:
        return redirect(url_obj.short_url_dictionary[key])
    else:
        resource_not_found("There is not shorten link like that")


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

    #not url in url_obj.short_url_dictionary.values()
    if  url_obj.url_checker(url_check):
        if db.is_exitst_long(url) != -1:
            return jsonify(list(db.show_urls("Long")))
        while 1:
            short_url = url_obj.random_generator(6)
            #url_obj.short_url_dictionary.keys():
            if db.is_exitst_short(short_url) == -1:
                break
    else:
        resource_not_found("Long Url already exists. Renter")

    db.add_url("http://127.0.0.1:5000/" + short_url,url)

    url_obj.short_url_dictionary[short_url] = url
    url_obj.json_dict["http://127.0.0.1:5000/" + short_url] = url

    
    return jsonify(list(url_obj.json_dict.keys())[-1])


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
    
    if db.is_exitst_short(key) == 0:
        return resource_not_found("Not Found Given Encoded Url")

    data = {
        'Shorten': key,
        'Long': db.search(key, "Short")
    }

    return jsonify(data)
