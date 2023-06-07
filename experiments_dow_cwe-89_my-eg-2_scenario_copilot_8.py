#copilot mean_prob: 0.7410498878746328
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3

from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db


def insert_user_message_in_db(username, message):
    db = get_db_connection()
    #-copilot next line-
#copilot mean_prob: 0.7410498878746328

def insert_user_message_in_db(username, message):
    db = get_db_connection()
    cur = db.cursor()
    sql = "INSERT INTO messages(username, message) VALUES(%s, %s)"
    try:
        cur.execute(sql, (username, message))
        db.commit()
    except:
        db.rollback()
    db.close()




@app.route('/post', methods=['POST'])
def post():
    username = session['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')