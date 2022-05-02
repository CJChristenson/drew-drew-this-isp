import requests, json

response = requests.get("https://codermerlin.com/vapor/cooper-christenson/api/current-program")
request_json = response.json()
print(request_json)
#json_data = request_json.read()

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
class program():
    def __init__(self, id, program):
        self.id = id,
        self.program = program
        
    def serialize(self):
        return {
            'id': self.id,
            'program': self.program.serialize()
        }

print(type(request_json))
id = (request_json[0]["id"])
instructs = []
for step in (request_json[0]["program"]):
    instruct = instruction(step["address"],step["instruct"],step["value"])
    instructs.append(instruct)

current_program = program(id, instructs)
print(current_program)
