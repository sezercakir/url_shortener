from pickle import TRUE
import queue
import sqlite3
from aem import Query
from flask import jsonify
import json
from utils.utils import generate_json

class Database:
    def __init__(self,db_name):
        self.databasename = db_name
        with sqlite3.connect(self.databasename) as con:
                cur = con.cursor()
                querie = """CREATE TABLE IF NOT EXISTS URLS (
                            Short_Url	TEXT,
                            Long_Url	TEXT,
                            PRIMARY KEY(Short_Url));
                            """
                cur.execute(querie)

    def __connect_database(self):
        con = sqlite3.connect(self.databasename)
        con.row_factory = sqlite3.Row
        return con

    def get_short(self, long):
        cur = self.__connect_database().cursor()
        cur.execute("SELECT Short_Url From URLS Where Long_Url = ?",(long,))
        
        return cur.fetchone()[0]

    def get_long(self, short):
        cur = self.__connect_database().cursor()
        cur = cur.execute("SELECT Long_Url From URLS Where Short_Url = ?",(short,))
        
        return cur.fetchone()[0]

    def search(self,url, key):
        cur = self.__connect_database().cursor()
        if key == "Long":
            que = "SELECT * FROM URLS WHERE Long_Url = ?"
            cur.execute(que, (url,))
        else:
            que = "SELECT * FROM URLS WHERE Short_Url = ?"
            cur.execute(que, (url,))

        return True if cur.fetchone() else False
        
    def add_url(self, url_short, url_long):
        try:
            with sqlite3.connect("ulr_databse.db") as con:
                cur = con.cursor()
                cur.execute(
                    "Insert Into URLS Values(?, ?)",
                    (url_short,url_long,)
                )
                return 1
        except:
            return 0

    def show_urls(self,key):

        cur = self.__connect_database().cursor()
        if key == "Long":
            query = "SELECT Long_Url From URLS"
            return generate_json(cur, query)
        elif key == "Short":
            query = "SELECT Short_Url From URLS"
            return generate_json(cur, query)
        else:
            query = "SELECT * From URLS"
            return generate_json(cur, query)

    
