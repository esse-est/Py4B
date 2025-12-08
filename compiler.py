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
        "msh": "1000",
        "cpu": "1001",
        "cps": "1010",
        "sac": "1011",
        "and": "1100",
        "orx": "1101",
        "out": "1110",
        "xor": "1111",
    }

    for i in lines:
        i=i.split(" ")

        if len(i) < 3:
            i.append("0000")


        
        if i[2].startswith("i("):
            i[2]=f"{bin(int((i[2]).replace("i(","").replace(")","")))}"[2:]
        
        if i[1].startswith("i("):
            i[1]=f"{bin(int((i[1]).replace("i(","").replace(")","")))}"[2:]
        
        
        if i[1] in variable_translation:
            
            i[1]=f"0000{f"{bin(variable_translation.index(i[1]))}"[2:]}"[-4:]
        elif i[2].isalpha():
            variable_translation.append(i[2])
            i[2]=f"0000{f"{bin(variable_translation.index(i[2]))}"[2:]}"[-4:]        
        if i[2] in variable_translation:
            i[2]=f"0000{f"{bin(variable_translation.index(i[2]))}"[2:]}"[-4:]
        elif i[2].isalpha():
            variable_translation.append(i[2])
            i[2]=f"0000{f"{bin(variable_translation.index(i[2]))}"[2:]}"[-4:]
        
        for x in range(1,len(i)-1):
            while len(i[x]) < 4:
                i[x]=f"0{i[x]}"
        if i[0] in instruction_translation:
            i[0]=instruction_translation[i[0]]
        else:
            print("instruction not found")
            #exit()
        i=f"{i[0]}_{i[1]}_{i[2]}"
        compiled_lines.append(i)

    with open(outputfilepath,"w") as f:
        for l in compiled_lines:
            f.write(f"{l}\n")
    
scriptloader("example_script.pyb4","example_script.pyb4c")
