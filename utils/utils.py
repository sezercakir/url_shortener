"""
    @author:   Talha Sezer Çakır
    @date:     12.03.2022
    @detail:   Utils funcs of project
"""


import json

def generate_json(cur, query):
    cur.execute(query)
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)
