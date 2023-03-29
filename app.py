# importing flask
from flask import Flask, render_template
import sqlite3

# Here's our web server
app = Flask(__name__)

# create some data
my_data = {'first':'Haroon', 'last':'Ahmad', 'handle':'@HA'}

# create more data
my_list = ['wash the SAAB', 'grab some coffee', 'read a book']

# creating a home route '/'
# using a python decorator
@app.route("/")
def hello_world():
    return render_template('index.html', my_data=my_data, my_list=my_list)

# creating a new route
@app.route('/thebestrouteever')
def the_best():
    
    # create a connection to a database
    conn = sqlite3.connect('database.sqlite')

    # execute database statements
    cursor = conn.cursor()

    # select all the data
    cursor.execute('select * from objects')

    # get a reference to the data
    my_obj_data = cursor.fetchall()
    return render_template('thebestroutever.html', records=my_obj_data)

# running it from a script
if __name__ == '__main__':

    # run our app
    app.run(debug=True)

