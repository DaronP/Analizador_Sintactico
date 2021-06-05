from libs import *

#Leyendo archivo COCOL

#fn = input("Ingrese el nombre del archivo...")

f = open("Aritmetica.ATG", "r")
lines = []
tokens = []
keywords = []
characters = []
productions = []
char_dict = {"+": "~", "-": "-", "char(13)": "!", "chr(9)": ",", "chr(10)": ";", "chr(34)": "/", "chr(58)": "&", ".": ":"}

for line in f.readlines():
    if line[-1:] == "\n":
        lines.append(line[:-1])
    else:
        lines.append(line)
f.close()

name = lines[0].strip().split(" ")[-1]
print(name)

flag = ""

for line in lines:
    if line != "":
        if line.strip() == "TOKENS":
            flag = "T"
        if line.strip() == "KEYWORDS":
            flag = "K"
        if line.strip() == "CHARACTERS":
            flag = "C"
        if line.strip() == "PRODUCTIONS":
            flag = "P"
        if "END " in line:
            flag = "end"

        if flag == "T":
            tokens.append(line.strip())
        if flag == "C":
            characters.append(line.strip())
        if flag == "K":
            keywords.append(line.strip())
        if flag == "P":
            productions.append(line.strip())


#Creando el nuevo archivo de Python


new_file = open(name + ".py", 'w')

new_file.write("from thomson import *\n")
new_file.write("from subconjuntos import *\n")
new_file.write("from libs import *\n")

kw_list = []
for kw in keywords:
    if keywords.index(kw) == 0:
        new_file.write("#" + kw.strip() + "\n")

    else:
        kyw = kw.replace(chr(34), "")
        kyw = kyw.replace(chr(39), "")
        kyw = kyw.replace(".", "")
        kyw = kyw.replace(" ", "")
        kws = kyw.split("=")
        kw_list.append(kws[-1])

new_file.write("keywords = " + str(kw_list))
new_file.write("\n")

chrs = []
for char in characters:
    if "ANY" in char:
        if "MyANY" in char:
            continue
        c = char.split("=")
        char = c[0] + " = " + characters[1].split("=")[0].strip() + "+" + chr(34) + "|" + chr(34) + "+" + characters[2].split("=")[0].strip()
        if "-" in char:
            char = char.replace("-", "+")
        char = char.replace(".", "")
        new_file.write(char + "\n")
        continue

    if "sign" in char:
        char = char.replace("'+'", chr(34) + "~" + chr(34))
        char = char.replace("'-'", chr(34) + "-" + chr(34))
        char = char.replace("+", "+")
        char = char.replace(".", "")
        new_file.write(char + "\n")
        new_file.write(char.split("=")[0].strip() + " = or_ing(" + char.split("=")[0].strip() + ")\n")
        continue

    if "operadores" in char:
        char = char[:-1]
        new_file.write(char + "\n")
        new_file.write("keywords.append(" + char.split(" = ")[-1] + ")" + "\n")        
        continue

    if characters.index(char) == 0:
        new_file.write("#" + char + "\n")

    

    else:
        if "' '" in char:
            char = char.replace("' '", chr(34) + char_dict['chr(58)'] + chr(34))

        caracter = char.replace(".", "")
        char_list = caracter.split("=")

        if "chr(" in char_list[1] or "CHR(" in char_list[1]:
            if "CHR(13)" in caracter:
                caracter = caracter.replace("CHR(13)", chr(34) + "!" + chr(34))
            if "CHR(34)" in caracter:
                caracter = caracter.replace("CHR(34)", chr(34) + char_dict['chr(34)'] + chr(34))
            if "CHR(9)" in caracter:
                caracter = caracter.replace("CHR(9)", chr(34) + char_dict['chr(9)'] + chr(34))
            if "CHR(10)" in caracter:
                caracter = caracter.replace("CHR(10)", chr(34) + char_dict['chr(10)'] + chr(34))
            
            caracter = caracter.replace("CHR(", "chr(")
            new_file.write(caracter.split("=")[0].strip() + " = " + caracter.split("=")[1].strip() + "\n")
            chrs.append(char_list[1])
            if "whitespace" in caracter:
                new_file.write(caracter.split("=")[0].strip() + " = or_ing(" + caracter.split("=")[0].strip() + ")\n")
        
        else:
            if "'  '" in caracter:
                if chr(65) in char_list[1] and chr(90) in char_list[1]:
                    new_file.write(char_list[0] + " = " + chr(34) + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + chr(34) + "\n")
                    continue
                if chr(97) in char_list[1] and chr(122) in char_list[1]:
                    new_file.write(char_list[0] + " = " + chr(34) + "abcdefghijklmnopqrstuvwxyz" + chr(34) + "\n")
                    continue
            if "0123456789" in caracter:
                new_file.write(caracter + "\n")
                continue
            if "hexterm" in caracter:
                new_file.write(caracter + "\n")
                continue
            if "letter" in caracter and "downletter" in caracter and "upletter" in caracter:
                caracter = caracter.replace(" + downletter", "")
            new_file.write(caracter + "\n")
            new_file.write(char_list[0] + " = or_ing(" + str(char_list[0]) + ")"+ "\n")
            new_file.write("\n")
new_file.write("\n")


letter_kw = []
num_kw = []
num_val = []
d_flag = False
b_flag = False
for token in tokens:
    if tokens.index(token) == 0:
        new_file.write("#" + token + "\n")

    else:        
        if chr(34) + "." + chr(34) in token:
            token = token.replace(chr(34) + "." + chr(34), char_dict['.'])
        if "charinterval" in token:
            continue
        if "ANY" in token:
            continue
        if "digit" in token and d_flag == False:
            new_file.write("digit = or_ing(digit)\n")
            d_flag = True
        if "blanco" in token and b_flag == False:
            new_file.write("blanco = or_ing(blanco)\n")
            b_flag = True
        if "(." in token or ".)" in token:
            lst = list(token)
            token = ""
            for i in range(len(lst) - 1):
                token += lst[i]
            t = token
            new_file.write(t + "\n")
            t2 = t.split("=")
            new_file.write("keywords.append(" + t2[0].strip() + ")" + "\n")
            continue

        else:
            t = token.replace(".", "")

        if "CHR(" in t:
            t = t.replace(chr(34) + "CHR(" + chr(34), "(")
            t = t.replace(chr(34) + ")" + chr(34), "")


        t = t.strip()
        t = t.replace(chr(34), "")
        t = t.replace(chr(39), "")
        t = t.replace("(H)", chr(34) + "H" + chr(34))
        t = t.replace("(","+" + chr(34) + "_(" + chr(34) + "+")
        t = t.replace(")","+" + chr(34) + ")" + chr(34))
        t = t.replace("|","+" + chr(34) + "|" + chr(34) + "+")
        t = t.replace(".", "")
        t = t.replace("{", "+" + chr(34) + ")_(" + chr(34) + "+")
        t = t.replace("[", chr(34) + " ((" + chr(34) + "+")
        t = t.replace("}", "+" + chr(34) + ")*" + chr(34))
        t = t.replace("]", "+" + chr(34) + ")*)_" + chr(34) + "+")
        t = t.replace("/", chr(34) + "/" + chr(34))
        if "IGNORE" in t:
            continue

        try:
            buff = ""
            t2 = t.split("=")[1].strip()
            tt = list(t2)
            for i in range(3):
                buff += tt[i]

            if "+" in buff and chr(34) in buff and "_" in buff:
                buff3 = ""
                for i in tt[3:]:
                    buff3 += i
                t = t.split("=")[0] + " = " + chr(34) + buff3
            
        except:
            pass


        
        if " EXCEPT KEYWORDS" in t:
            t_l = t.split("=")
            if " " in t_l[1]:
                t_l[1].replace(" ", "")
            letter_kw.append(t_l[0])
            t = t.replace(" EXCEPT KEYWORDS", "")
        else:
            t_l = t.split("=")
            num_kw.append(t_l[0])
            if " " in t_l[1].strip() and "/" not in t_l[1]:
                b = t_l[1].split()
                b2 = ""
                for i in range(len(b)):
                    if i != len(b) - 1:
                        b2 += b[i] + "+" + chr(34) + "_" + chr(34) + "+"
                    else:
                        b2 += b[i]
                
                t = t_l[0] + " = " + b2
                t_l[1] = b2
                
            num_val.append(t_l[1])
        
        count = 0
        for i in t:
            if i == "(" or i == ")":
                count += 1
        if count % 2 != 0 and "sign" not in t:
            tbuf = t.split(" = ")
            t = tbuf[0] + " = " + chr(34) + "(" + chr(34) + "+" + tbuf[1]
        
        if "hexnumber" in t:
            for i in range(len(t)):
                try:
                    if t[i-1] == "*" and t[i] != "_":
                        t = t[:i] + "_(" + chr(34) + "+" + t[i + 1:] + "+" + chr(34) + ")" + chr(34)
                except:
                    pass
        for i in range(len(t)):
            try:
                if t[i - 1] == "_" and t[i] != "(":
                    t = t[:i] + "(" + t[i:]

                if t[i - 5] == "+" and t[i - 4] == chr(34) and t[i - 3] == "_" and t[i - 2] == "(" and t[i - 1] == chr(34) and t[i] == "+":
                    t = t.replace("+" + chr(34) + "_" + "(" + chr(34) + "+", "")

                if t[i - 1] == ":":
                    t_l = t.split(":")
                    t = t_l[0] + "+" + chr(34) + "_:_(" + chr(34) + "+" + t_l[1]
                    t_l = t.split(" = ")
                    t = t_l[0] + " = " + chr(34) + "(" + chr(34) + "+" + t_l[1]
                    break
            except:
                pass
        
        for i in range(len(t)):
            try:
                if t[i - 2] == "*" and t[i - 1] == chr(34) and t[i] != "+" and "string" in t:
                    t = t[:i] + "+" + chr(34) + "_" + chr(34) + "+" + chr(34) + "(" + chr(34) + "+" + t[i:] + "+" + chr(34) + ")" + chr(34)
                    if "ss" in t:
                        t = t.replace("ss", "s" + "+" + chr(34) + ")_(" + chr(34) + "+" + "s")
            except:
                pass

        new_file.write(t + "\n")
new_file.write("\n")

pila_pr = []
prod_list =[]
funciones = []

for i in range(len(productions)):
    if productions[i] == "PRODUCTIONS":
        new_file.write("#" + productions[i] + "\n")
        pass
    
    elif productions[i] == "":
        pass

    else:
        pila_pr.append(productions[i])

        if productions[i] =="." or productions[i] =="\t.":
            prod_list.append(pila_pr)
            pila_pr = []            
                
#Convirtiendo productions a funciones

for i in range(len(prod_list)):
    if prod_list[i][0] == "\t":
        s = prod_list[i][1].split("=",1)
        x = s[0].replace("<", "(")
        x = x.replace(">", "):")
        x = x.replace("ref int", "")
        s[0] = x

        if s[0].find("(") >=0:
            prod_list[i][1] = "def "+s[0]+s[1]
        else:
            prod_list[i][1] = "\ndef "+s[0]+"():"+s[1]            
                

    else:
        s = prod_list[i][0].split("=",1)
        x = s[0].replace("<", "(")
        x = x.replace(">", "):")
        x = x.replace("ref int", "")
        s[0] = x
        if s[0].find("(") >=0:
            prod_list[i][0] = "def "+s[0]+s[1]
        else:
            
            prod_list[i][0] = "def "+s[0]+"():"+s[1]

    for j in range(len(prod_list[i])):
        prod_list[i][j] = prod_list[i][j].replace("\t", "")
        prod_list[i][j] = prod_list[i][j].replace(".)", "")
        prod_list[i][j] = prod_list[i][j].replace(";", "")
        prod_list[i][j] = prod_list[i][j].replace("<", "(")
        prod_list[i][j] = prod_list[i][j].replace(">", ")")
        prod_list[i][j] = prod_list[i][j].replace("ref int", "")
        prod_list[i][j] = prod_list[i][j].replace("ref", "")
        prod_list[i][j] = prod_list[i][j].replace("(.", "\n")
        prod_list[i][j] = prod_list[i][j].replace(":", ":")


    pila_func = []
    pila_p = []
    flag_prod = 2
    for s in range(len(prod_list[i])):
        po = prod_list[i][s]
        
        #Quitando strings vacios y convirtiendo a funcion
        if len(po)!= 0:
            if po[0] == "{":
                flag_prod = 1

            if po[0] == "}":
                
                str_pila = sacar_lista2(pila_p)
                    
                str_pila = str_pila.replace(" ", "")
                str_pila = str_pila.replace("{","")
                str_pila = str_pila.replace("}","")
                str_pila = str_pila.replace("\n","\n\t\t")
                str_pila = str_pila.split("|")

                p_f = str_pila[0][1]
                p_s = str_pila[1][1]

                str_pila[0] = remS(sacar_lista2(str_pila[0]))
                str_pila[0] = sacar_lista2(str_pila[0])
                str_pila[1] = remS(sacar_lista2(str_pila[1]))                
                str_pila[1] = sacar_lista2(str_pila[1])

                str_pila[0] = production_to_func(str_pila[0])
                str_pila[1] = production_to_func(str_pila[1])


                result = "while follow() == " + chr(39) + p_f + chr(39) + " or follow() == " + chr(39) + p_s+chr(39) + ":\n\t\tif follow() == " + chr(39) + p_f + chr(39) + ":\n\t\t" + sacar_lista2(str_pila[0]) + "\n\t\tif follow() == " + chr(39) + p_s+chr(39) + ":\n\t\t" + sacar_lista2(str_pila[1])
                funciones.append(result)                
                flag_prod = 2
                pila_func = []    


        if flag_prod == 1:
            pila_p.append(prod_list[i][s])

        elif flag_prod == 2:
            funciones.append(prod_list[i][s])
            pila_func.append(pila_p)
            pila_p = []

#Corrigiendo funciones no convertidas
for func in range(len(funciones)):
    funciones[func] = funciones[func].replace("{", "\n\twhile(True):\n\t\t")
    funciones[func] = funciones[func].replace("}", "")
    funciones[func] = funciones[func].replace("Term( result1)", "\tresult1 = Term(result1)")
    funciones[func] = funciones[func].replace("Term( result2)", "\tresult2 = Term(result2)")
    funciones[func] = funciones[func].replace("Factor( result2)", "\tresult2 = Factor(result2)")
    funciones[func] = funciones[func].replace("Factor( result1)", "\tresult1 = Factor(result1)")
    funciones[func] = funciones[func].replace("Expression(  value)", "value = Factor(value)")
    funciones[func] = funciones[func].replace(chr(34)+"."+chr(34), "\n\tget("+chr(34)+"."+chr(34)+")")
    funciones[func] = funciones[func].replace("["+chr(34)+"-"+chr(34), "if follow() == "+chr(34)+"-"+chr(34)+":\n\t\tsigno = -1")
    funciones[func] = funciones[func].replace("signo = -1]", "")
    funciones[func] = funciones[func].replace("( Number( result) | " + chr(34) + "(" + chr(34) + "Expression(  result)" + chr(34) + ")" + chr(34) + ")", "")

    if funciones[func] == ".":
        if "value =" in funciones[func - 1]:
            funciones[func] = "\n\treturn value\n\n"
        else: 
            funciones[func] = "\n\treturn result\n\n"

new_file.write("\n")
new_file.write("\n")
flag_write = 0
for func in funciones:
    func = func.replace("value = input()", "\tvalue = input()")
    func = func.replace("result1 = 0", "\tresult1 = 0")
    func = func.replace("value = 0", "\tvalue = 0")
    func = func.replace("result2 = 0", "\tresult2 = 0")
    func = func.replace("result=result1", "\tresult=result1")
    func = func.replace("signo=1", "\tsigno=1")
    func = func.replace("result*=signo", "\tresult*=signo")
    func = func.replace("result = int(value)", "\tresult = int(value)")
    func = func.replace("\tresult1 = Factor(result1)", "result1 = Factor(result1)")
    func = func.replace("result1+=result2", "\tresult1+=result2")
    func = func.replace("result1-=result2", "\tresult1-=result2")
    func = func.replace("result1*=result2", "\tresult1*=result2")
    func = func.replace("result1/=result2", "\tresult1/=result2")

    if "def" in func:
        flag_write = 0
    else:
        flag_write = 1
    
    if flag_write == 0:
        new_file.write(func+"\n")
    if flag_write == 1:
        new_file.write("\t"+func+"\n")
         

new_file.write("\n")
new_file.write("minimo = [] \n")

new_file.write("\n")
post = []

for l in letter_kw:
    new_file.write("pos_fx_" + l.strip() + ", alfa_" + l.strip() + " = postfix(" + l.strip() + ") \n")
for n in num_kw:
    new_file.write("pos_fx_" + n.strip() + ", alfa_" + n.strip() + " = postfix(" + n.strip() + ") \n")
new_file.write("\n")


new_file.write("#Iniciando los AFN \n")
new_file.write("print(" + chr(34) + "Iniciando los AFN" + chr(34) + ")\n")
for l in letter_kw:
    new_file.write("trans_t_" + l.strip() + ", strt_end_t_" + l.strip() + " = thomson(pos_fx_" + l.strip() + ", alfa_" + l.strip() + ")\n")
for n in num_kw:
    new_file.write("trans_t_" + n.strip() + ", strt_end_t_" + n.strip() + " = thomson(pos_fx_" + n.strip() + ", alfa_" + n.strip() + ")\n")

new_file.write("#Iniciando los AFD\n")
new_file.write("print(" + chr(34) + "Iniciando los AFD" + chr(34) + ")\n")
for l in letter_kw:
    new_file.write("trans_afd_" + l.strip() + ", strt_end_afd_" + l.strip() + ", min_" + l.strip() + ", min_strt_" + l.strip() + " = subconjuntos(trans_t_" + l.strip() + ", strt_end_t_" + l.strip() + ")\n")
for n in num_kw:
    new_file.write("trans_afd_" + n.strip() + ", strt_end_afd_" + n.strip() + ", min_" + n.strip() + ", min_strt_" + n.strip() + " = subconjuntos(trans_t_" + n.strip() + ", strt_end_t_" + n.strip() + ")\n")

new_file.write("\n")

for l in letter_kw:
    new_file.write("minimo.append([min_" + l.strip() + ", min_strt_" + l.strip() + ", alfa_" + l.strip() + "])\n")
for n in num_kw:
    new_file.write("minimo.append([min_" + n.strip() + ", min_strt_" + n.strip() + ", alfa_" + n.strip() + "])\n")


new_file.write("n_f = input('Ingrese el nombre del archivo... ')\n")
new_file.write("scanner(keywords, minimo, n_f)\n")

new_file.write("\n")
new_file.write("\n")


new_file.close()
