
memory = {

}
def ADD(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2)+int(mem[a2],2))[2:]}"[-4:])

def SUB(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2)-int(mem[a2],2))[2:]}"[-4:])

def MUL(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2)*int(mem[a2],2))[2:]}"[-4:])

def DIV(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2)/int(mem[a2],2))[2:]}"[-4:])

def SL(a1,a2:None):
    mem[a1]<<1

def SR(a1,a2:None):
    mem[a1]>>1

def IDLE(a1,a2):
    input()

def COP(a1,a2):
    mem[a2]=mem[a1]

def NOP(a1,a2):
    return(False)

def BR(a1,a2):
    global loop_c
    loop_c=bin(int(a1,2))

def BRIF(a1,a2):
    if mem[a2] != "0000":
        BR(a1,"0000")

def SACC(a1,a2):
    mem[a2]=a1

def AND(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2) and int(mem[a2],2))[2:]}"[-4:])

def OR(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2) or int(mem[a2],2))[2:]}"[-4:])

def XOR(a1,a2):
    mem[a2]=(f"0000{bin(int(mem[a1],2) ^ int(mem[a2],2))[2:]}"[-4:])

def OUT(a1,a2):
    if mem[a2] == "0000":
        print(mem[a1])
    elif mem[a2] == "0001":
        print(bin(mem[a1]))
    elif mem[a2] == "0010":
        print(ord(bin(mem[a1])))

mem = {}

instructions = {
    "0000": ADD,
    "0001": SUB,
    "0010": MUL,
    "0011": DIV,
    "0100": SL,
    "0101": SR,
    "0110": IDLE,
    "0111": COP,
    "1000": NOP,
    "1001": BR,
    "1010": BRIF,
    "1011": SACC,
    "1100": AND,
    "1101": OR,
    "1110": OUT
    "1111": XOR
}



def run(instruction_order: list):
    global loop_c
    loop_c=0
    while True:
        if loop_c > len(instruction_order)-1:
            return False
        inst=instruction_order[loop_c].replace("_","")
        print(inst)
        instructions[inst[0:4]](inst[4:8],inst[8:12])
        input()
        loop_c+=1
        # instruction i[0:4] 
        # address 1 i[4:8]
        # address 2 i[8:12]
        


run(["1000_0001_0001","1000_0001_0011","0000_0011_0001"])

print(mem)