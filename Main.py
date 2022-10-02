from flask import Flask, jsonify, request
import csv
all_movies=[]
with open('movies.csv') as f: 
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
liked_movies=[]
disliked_movies=[]
unwatched=[]
app=Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })




if __name__="__main__":
    app.run()