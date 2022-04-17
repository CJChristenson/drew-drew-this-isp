#imports for RPi GPIO library and time library
import RPi.GPIO as GPIO
import time
import requests
import json


GPIO.setmode(GPIO.BCM) #set GPIO mode to BCM to reference pins as GPIO numbers
GPIO.setwarnings(False) #set warnings to false

# define contant names to pin numbers for reference
D7 = 24
D6 = 25
D5 = 8
D4 = 7
D3 = 12
D2 = 16
D1 = 20
D0 = 21
A0 = 23
A1 = 18
A2 = 15
A3 = 14
program_pin = 2
m_clock = 26
a_clock = 19
reset_pin = 4
program_mode = 13
run_mode = 6
power = 22
data_pins = [D7, D6, D5, D4, D3, D2, D1, D0]
address_pins = [A3, A2, A1, A0]

#define operations and their binary counterpart
NOP = "0000"
LDA = "0001"
ADD = "0010"
SUB = "0011"
STA = "0100"
LDI = "0101"
JMP = "0110"
JC = "0111"
JZ = "1000"
OUT = "1110"
HLT = "1111"

programming = True #variable to keep track of whether computer is in programming mode or not

#GPIO setup for pions to determine if pins are input or output, and what the default values are.
for pin in data_pins:
    GPIO.setup(pin, GPIO.OUT)
for pin in address_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(program_pin, GPIO.OUT)
GPIO.setup(m_clock, GPIO.OUT)
GPIO.setup(a_clock, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)
GPIO.setup(program_mode, GPIO.OUT)
GPIO.setup(power, GPIO.OUT)
GPIO.setup(run_mode, GPIO.OUT)
GPIO.output(m_clock, GPIO.HIGH)
GPIO.output(a_clock, GPIO.LOW)
GPIO.output(program_pin, GPIO.HIGH)
GPIO.output(reset_pin, GPIO.HIGH)
GPIO.output(power, GPIO.LOW)
time.sleep(1) #delay for 8-bit computer chip timings.
GPIO.output(reset_pin, GPIO.LOW)
GPIO.output(program_mode, GPIO.HIGH)
GPIO.output(run_mode, GPIO.LOW)

#function to set a output high
def high(pin_in):
    GPIO.output(pin_in, GPIO.HIGH)

#function to set a output low
def low(pin_in):
    GPIO.output(pin_in, GPIO.LOW)

#function to pulse program pin in RAM module to program value
def pro():
    low(program_pin)
    high(program_pin)

#function to set computer to manual clock mode
def manual():
    high(m_clock)
    low(a_clock)

#function to set computer to auto clock mode
def auto():
    high(a_clock)
    low(m_clock)

#function to reset computer
def reset():
    high(reset_pin)
    time.sleep(1)
    low(reset_pin)

#function to move computer in programming mode, to enable programming
def program_m():
    global programming
    high(program_mode)
    low(run_mode)
    programming = True

#function to move computer in run mode, to enable program running
def run_m():
    high(run_mode)
    low(program_mode)
    global programming
    programming = False

#function to set pins to high if value in instruction is "1", low if value is "0"
def operate(o_instruction, amount):
    for ind in range(len(o_instruction)):
        if o_instruction[ind] == "0":
            low(data_pins[ind])
        elif o_instruction[ind] == "1":
            high(data_pins[ind])
        else:
            print("Error: Character not 0 or 1 (Line 122)")
    for ind in range(len(o_instruction)):
            
        if amount[ind] == "0":
            low(data_pins[ind + 4])
        elif amount[ind] == "1":
            high(data_pins[ind+ 4])
        else:
            print("Error: Character not 0 or 1 (Line 130)")

#function to set pins high if value in address is "1", low if value is "0"
def set_address(address):
        for ind in range(len(address)):
            if address[ind] == "0":
                low(address_pins[ind])
            elif address[ind] == "1":
                high(address_pins[ind])
            else:
                print("Error: Character not 0 or 1 (Line 140)")
        pro()

#function that given an input, can analyze the operation given, and call other functions to set pins high/low to program computer
def analyzer(a_input):
    user_input = a_input
    address = user_input[0:4]
    instruction = user_input[5:8]
    value = user_input[9:16]
    
    if user_input == "l":
        for pin in data_pins:
            low(pin)
        for pin in address_pins:
            low(pin)
    elif instruction == "NOP":
        operate(NOP, value)
        set_address(address)
    elif instruction == "LDA":
        operate(LDA, value)
        set_address(address)
    elif instruction == "ADD":
        operate(ADD, value)
        set_address(address)
    elif instruction == "SUB":
        operate(SUB, value)
        set_address(address)
    elif instruction == "STA":
        operate(STA, value)
        set_address(address)
    elif instruction == "LDI":
        operate(LDI, value)
        set_address(address)
    elif instruction == "JMP":
        operate(JMP, value)
        set_address(address)
    elif instruction == "JC ":
        operate(JC, value)
        set_address(address)
    elif instruction == "JZ ":
        operate(JZ, value)
        set_address(address)
    elif instruction == "OUT":
        operate(OUT, value)
        set_address(address)
    elif instruction == "HLT":
        operate(HLT, value)
        set_address(address)
    elif user_input == "start":
        if programming == True:
            print("Error: Still in programming mode")
        else:
            auto()
    elif user_input == "stop":
        manual()
    elif user_input == "reset":
        reset()
    elif user_input == "program":
        program_m()
    elif user_input == "run":
        run_m()
    elif user_input == "on":
        high(power)
    elif user_input == "off":
        low(power)
    else:
        for pin in data_pins:
            high(pin)

#array of code for testing
code = [ "0000 LDI 0001",
         "0001 STA 1110",
         "0010 LDI 0000",
         "0011 ADD 1110",
         "0100 STA 1111",
         "0101 LDA 1110",
         "0110 STA 1101",
         "0111 LDA 1111",
         "1000 STA 1110",
         "1001 LDA 1101",
         "1010 OUT 0000",
         "1011 JC  0000",
         "1100 JMP 0011",
         "1101 NOP 0000",
         "1110 NOP 0000",
         "1111 NOP 0000"]

# for loop to iterate over every instruction
#for instruction in code:
#    analyzer(instruction)
#    print(type(instruction))
#    time.sleep(.5)

#json_data = request_json.read()

class instruction():
    def __init__(self, address, instruct, value):
        self.address = address
        self.instruct = instruct
        self.value = value

    def get_instruct(self):
        count = 4 - len(self.address)
        add = ""
        for _ in range(count):
            add += "0"
        add += self.address
        return "%s %s %s" % (add, self.instruct, self.value)
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

#print(type(request_json))

#runs analyzer based on user text input
while True:
    response = requests.get("https://codermerlin.com/vapor/cooper-christenson/api/current-program")
    request_json = response.json()

    print(request_json)
    if (request_json != "No programs"):
        id = (request_json["id"])
        instructs = []
        for step in (request_json["program"]):
            instruct = instruction(step["address"],step["instruct"],step["value"])
            instructs.append(instruct)
        
        current_program = program(id, instructs)
        for instruct in current_program.program:
            #print(f'"{instruct.get_instruct()}"')
            #print(instruct.get_instruct())
            analyzer(instruct.get_instruct())
            time.sleep(.5)
        time.sleep(2)
        _ = requests.get("https://codermerlin.com/vapor/cooper-christenson/api/remove-program")
            
    
    time.sleep(1)
    
    
