import math
letter_out=list(map(chr, range(97, 123)))
cache="0000"
def ADD(a1,a2):
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2)+int(mem[mem_cell][a2],2))[2:]}"[-4:])

def SUB(a1,a2):
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2)-int(mem[mem_cell][a2],2))[2:]}"[-4:])

def MUL(a1,a2):
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2)*int(mem[mem_cell][a2],2))[2:]}"[-4:])

def DIV(a1,a2):
    print(mem[mem_cell])
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2)//int(mem[mem_cell][a2],2))[2:]}"[-4:])

def SL(a1,a2:None):
    mem[mem_cell][a1]=mem[mem_cell][a1]<<1

def SR(a1,a2:None):
    mem[mem_cell][a1]=mem[mem_cell][a1]>>1

def IDLE(a1,a2):
    input()

def COP(a1,a2):
    mem[mem_cell][a2]=mem[mem_cell][a1]

def MSH(a1,a2):
    global mem_cell
    mem_cell=a1

def CPU(a1,a2):
    global cache
    mem[mem_cell][a1]=cache
def CPS(a1,a2):
    global cache
    cache=mem[mem_cell][a1]
def SACC(a1,a2):
    mem[mem_cell][a2]=a1

def AND(a1,a2):
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2) and int(mem[mem_cell][a2],2))[2:]}"[-4:])

def OR(a1,a2):
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2) or int(mem[mem_cell][a2],2))[2:]}"[-4:])

def XOR(a1,a2):
    mem[mem_cell][a2]=(f"0000{bin(int(mem[mem_cell][a1],2) ^ int(mem[mem_cell][a2],2))[2:]}"[-4:])

def OUT(a1,a2):
    if a2[1:] == "000":
        print(int(mem[mem_cell][a1],2),end="")
    elif a2 == "0001":
        print(mem[mem_cell][a1],end="")
    elif a2 == "0010":
        print(letter_out[int(mem[mem_cell][a1],2)-1],end="")
    if a2[0] == "1":
        print()

mem_cell="0001"
mem = {}

for i in range(0,15):
    mem[f"0000{bin(i)[2:]}"[-4:]] = {}

instructions = {
    "0000": ADD,
    "0001": SUB,
    "0010": MUL,
    "0011": DIV,
    "0100": SL,
    "0101": SR,
    "0110": IDLE,
    "0111": COP,
    "1000": MSH,
    "1001": CPU,
    "1010": CPS,
    "1011": SACC,
    "1100": AND,
    "1101": OR,
    "1110": OUT,
    "1111": XOR
}



def run(instruction_order: list):
    global loop_c
    loop_c=0
    while True:
        if loop_c > len(instruction_order)-1:
            return False
        inst=instruction_order[loop_c].replace("_","")
        
        instructions[inst[0:4]](inst[4:8],inst[8:12])
        loop_c+=1
        # instruction i[0:4] 
        # address 1 i[4:8]
        # address 2 i[8:12]
        


with open("example_script.pyb4c","r") as f:
    inst_formatted=[]
    for l in f.readlines():
        inst_formatted.append(l.replace("\n","").replace(" ",""))
    run(inst_formatted)
