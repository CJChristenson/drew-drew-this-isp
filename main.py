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
#index route that brings user to home page.
@app.route('/')
def home():
      return render_template('index.html')

#route that brings user to the How CPU's work page
@app.route('/howcpuswork')
def howcpuswork():
      return render_template('howcpuswork.html')

#route that brings user to the How 8-bit CPU's work page
@app.route('/how8bitwork')
def how8bitwork():
      return render_template('how8bitwork.html')

#route that brings user to the Programming Page
@app.route('/cpuprogram')
def cpuprogram():
      return render_template('cpuprogram.html', result="")

#route that brings user to page that only displays the stream.
@app.route('/stream')
def stream():
      return render_template('stream.html')

#route that brings user to page that has FAQs.
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



#define class that is created to contain one set of instructions
class program():
      def __init__(self, id, program):
            self.id = id
            self.program = program

      def serialize(self):
            return {
                  'id': self.id,
                  'program': self.program.serialize()
            }
#programEncoder class for JSON encoding
class programEncoder(JSONEncoder):
      def default(self, o):
            return o.__dict__
            


programs = [] #array that holds all programs yet to be executed
ids = [] #array to hold list of all ID's. The index of an ID is it's position in queue.
currentId = 1 #value to keep track of next ID to be assigned.

#function that if a value is nothing, changes it to 0000.
def processInputVal(inp):
      if (inp == ""):
            return "0000"
      else:
            return inp

#function that if a instruction is nothing, it is changed to NOP.      
def processInputInstruct(inst):
      if (inst == ""):
            return "NOP"
      elif (inst == "JC"):
            return "JC "
      else:
            return inst

#API URL for creating a new program. It is a POST method. It takes a request, and processes all the information to create a
#instance of a program and then returns the id and it's position.
@app.route('/api/new-program', methods=['POST'])
def i():
      global currentId
      global ids
      if request.method == 'POST':
            global test
            current_form = request.form
            instructions = []
            for ind in range(0, 16):
                  step = format(ind, "b")
                  
                  inst = instruction(step, processInputInstruct(current_form[f'{step}in']), processInputVal(current_form[f'{step}val']))
                  instructions.append(inst)
                  print(step)

            newProgram = program(currentId,instructions)
            programs.append(newProgram)
            ids.append(currentId)
            currentId += 1
            #print(ids.index(newProgram.id))
            #programs.pop(0)
            #ids.pop(0)
            return jsonify(id=newProgram.id, position=ids.index(newProgram.id))

#API URL for returning the current program. It is a GET method. 
@app.route('/api/current-program')
def current_program():
      if (len(programs) >= 1):
            return json.dumps(programs[0], cls=programEncoder)
      else:
            return json.dumps("No programs")
            
      
#API URL for removing the current program. It is a GET method
@app.route('/api/remove-program')
def remove_program():
      programs.pop(0)
      ids.pop(0)
      return "Success"
      
#API URL for getting the position in queue of an ID. It is a GET method that takes a ID value in.
@app.route('/api/position')
def position():
      args = request.args
      request_id = int(args["id"])
      if request_id in ids:
            return jsonify(str(ids.index(request_id)))
      else:
            return jsonify("Id isn't present")
      
#This will call Flask to run the application to run on the VAPOR link. If the file name is main, it will run the application
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=(os.environ.get('VAPOR_LOCAL_PORT')))
