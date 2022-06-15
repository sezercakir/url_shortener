# URL Shortener API

It is a url shortener application that can work in local. 
It has been prepared as a practical example. <br>

Heroku deletes the data that the sqlite database holds every 24 hours as per their policy. I recommend the services of big service providers like bittly for use as I do. :smile:
## Usage 

It can be accesible as Heroku App from [here](https://urlshortenerr.herokuapp.com/) or locally with cloning this repository.

- Urls to be shortened are taken from home page.
- /encode endpoint encodes the given url and saves it in the database and returns all encoded urls in short and long versions as json output
- /decode&<shortened_part> endpoint decodes the shortend url and return long original url as json output
- /decode endpoint returns all urls in the database as json output
- /<shortened_url> endpoint transfer original url with reading given shortened url from database
- /get endpoint returns all urls in the database as json output



