#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Menu, Series, Movie, Item
from flask import session as login_session
import random
import string
import excel
# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import pandas as pd
from tablib import Dataset




UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['xls', 'xlsb', 'xlsm', 'xlsx', 'xlt', 'xltx', 'xlw'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
                                    #filename=filename))
            file_path = UPLOAD_FOLDER + "/" + filename
            df = pd.read_excel(file_path)
            ## .shape get the len of row first and second number column
            ## it our case not big deal cus our files will be all same number column and rows
            ##print(df.shape[0])
            
            print("")
            array = []
            print(df.shape[0])
            for i in range(df.shape[0]):
                help0 = i
                
                for n in range(df.shape[0]):
                    help1 = n
                    print(i)
                    print(n)
                    if n > 1:
                        continue
                    print(df.iloc[help0][help1])
                    array.append(df.iloc[help0][help1])
                    
                        
                    #n += 1
            #i += 1         
                 
            #print(df.iloc[0][0])
            #print(df.iloc[0][1])
            #print(df.iloc[1][0])
            #print(df.iloc[1][1])

            #for n in df.iloc[0]:
                #print(n)
            #print(df.iloc[0][0])
            #print(df.iloc[0][1])
            #print(df.iloc[1][0])
            #print(df.iloc[1][1])
            #for x in df:
             #   print(x)
                
            #print(df["a"])
            #f = open(file_path, "r")
            #print(f.read())                 
            page = "<style>#request{font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;border-collapse: collapse;width:100%;}"
            page += "#request td, #request th {border: 1px solid #ddd;padding: 8px;}"
            page += "#request tr:nth-child(even){background-color: #f2f2f2;}"
            page += "#request tr:hover {background-color: #ddd;}"
            page += "#request th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #4CAF50;color: white;}"
            page +="</style>"
            page += "<table id='request'><tr><th>Name</th><th>P Number</th></tr>"
            
            print(len(array))
            ## here we change 2 by the cells number we already must know how many cells
            ## in the request or how many fileds don't forget always divide by the cells number 
            #one_request_length = len(array) / 2
            #print(one_request_length)
            cells_index = 0
            got_it = False
            ages = []
            for onetd in range(len(array)):
                help2 = onetd
                
                if onetd % 2 == 1:
                    ages.append(array[onetd])
                    page += "<td>" + str(array[onetd]) + "</td>"
                    #continue
                else:
                    page += "</tr><tr>" + "<td>" + str(array[onetd]) +  "</td>"                 
                    #page += "<br><br>"
                #page += "</tr>"
                #if got_it == False:
                
               # for onecell in range(len(array)):
                #    cells_index                         
               #     help3 = onecell
                   
                 #   "</tr>"          
                
                            
                    #got_it = True
                #page += "</tr>"
           
                                
                #else:
                     #page += "</tr>"
                     #break                
                    
            #for m in range(
            return page

            
                                    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Uploadaaaa new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''











@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=False)
