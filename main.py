#import flask libraries and os libraries 
from flask import Flask, render_template, request
import os

#define the template directory (html pages) to be the website directory.
template_dir = os.path.abspath('./website/')

#define Flask Application
app = Flask(__name__, template_folder=template_dir)


#create routes for the certain pages. When a user travels to the URL contained withing the quotes, it will call the function.
@app.route('/')
def home():
      return render_template('index.html')

@app.route('/howcpuswork')
def howcpuswork():
      return render_template('howcpuswork.html')
@app.route('/how8bitwork')
def how8bitwork():
      return render_template('how8bitwork.html')
@app.route('/cpuprogram')
def cpuprogram():
      return render_template('cpuprogram.html')

@app.route('/stream')
def stream():
      return render_template('stream.html')

@app.route('/faq')
def faq():
      return render_template('faq.html')


#This will call Flask to run the application to run on the VAPOR link. If the file name is main, it will run the application
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=(os.environ.get('VAPOR_LOCAL_PORT')))
