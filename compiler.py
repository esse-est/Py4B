def scriptloader(filepath:str,outputfilepath:str):
    lines=[]
    compiled_lines=[]
    with open(filepath,"r") as f:
        for l in f.readlines():
            if not l.startswith("#") and not l.startswith("\n"):
                l=l.replace("\n","")
                lines.append(l)

    variable_translation=[]

    instruction_translation = {
        "add": "0000",
        "sub": "0001",
        "mul": "0010",
        "div": "0011",
        "shl": "0100",
        "shr": "0101",
        "idl": "0110",
        "cop": "0111",
        "nop": "1000",
        "brk": "1001",
        "bif": "1010",
        "sac": "1011",
        "and": "1100",
        "orx": "1101",
        "out": "1110",
        "xor": "1111",
    }

    for i in lines:
        i=i.split(" ")
        while len(i) < 3:
            #add empty lines until at standard length
            i.append("0000")
        
        if i[2].startswith("i("):
            i[2]=bin(int(i[2][2:-1]))[2:]

        for y in i:
            if not y.isnumeric() and y not in instruction_translation:
                if y in variable_translation:
                    i[i.index(y)]=f"0000{bin(variable_translation.index(y))[2:]}"[-4:]
                elif i[0] == "set":
                    variable_translation.append(y)
                    i[i.index(y)]=f"0000{bin(variable_translation.index(y))[2:]}"[-4:]


        if i[0] in instruction_translation:
            i[0]=instruction_translation[i[0]]

        i=f"{i[0]}_{i[1]}_{i[2]}"
        compiled_lines.append(i)


    with open(outputfilepath,"w") as f:
        for l in compiled_lines:
            f.write(f"{l}\n")
    
scriptloader("example_script.pyb4","example_script.pyb4c")