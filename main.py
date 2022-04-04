#import flask libraries and os libraries 
from flask import Flask, render_template, request, jsonify, make_response, Response, redirect, url_for
import os
import json
from json import JSONEncoder

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
      return render_template('cpuprogram.html', result="")

@app.route('/stream')
def stream():
      return render_template('stream.html')

@app.route('/faq')
def faq():
      return render_template('faq.html')

#define class for one instruction
class instruction():
      def __init__(self, address, instruct, value):
            self.address = address
            self.instruct = instruct
            self.value = value

      def get_instruct(self):
            return "%s %s %s" % (self.address, self.instruct, self.value)
      def serialize(self):
            return {
                  'address': self.address,
                  'instruction': self.instruct,
                  'value': self.value
            }

instruct0 = instruction('0000','NOP','0000')
instruct1 = instruction('0001','NOP','0000')
#define class that is created to contain one set of instructions
class program():
      def __init__(self, id, position, program):
            self.id = id,
            self.position = position
            self.program = program

      def serialize(self):
            return {
                  'id': self.id,
                  'position': self.position,
                  'program': self.program.serialize()
            }

class programEncoder(JSONEncoder):
      def default(self, o):
            return o.__dict__
            
temp = program(1, 1, [instruct0, instruct1])

test = ""
@app.route('/api/test', methods=['POST'])
def i():
      if request.method == 'POST':
            global test
            test = request.form
            return redirect(url_for('.cpuprogram', result="Success!"))
     

@app.route('/test')
def t():
      return test
#This will call Flask to run the application to run on the VAPOR link. If the file name is main, it will run the application
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=(os.environ.get('VAPOR_LOCAL_PORT')))
