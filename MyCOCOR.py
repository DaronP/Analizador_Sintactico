from thomson import *
from subconjuntos import *
from libs import *
keywords = []
#CHARACTERS
letter = "ABCDEFGHIJKLMN�OPQRSTUVWXYZabcdefghijklmn�opqrstuvwxyz"
letter  = or_ing(letter )

digit = "0123456789"
cr = "!"
lf = ";"
tab = ","
ignore = cr+lf+tab
ignore  = or_ing(ignore )

comillas = "/"
stringletter  = letter+"|"+digit
operadores = "+-=()[]{}|.<>"
keywords.append("+-=()[]{}|.<>")

#TOKENS
digit = or_ing(digit)
ident = "("+letter+")_("+letter+"|"+digit+")*"
string  = "("+comillas+")_("+stringletter+")_("+stringletter+")*"+"_"+"("+comillas+")"
char = " (("+"/"+")*)_("+letter
charnumber  = "("+digit+")_("+digit+")*"
startcode ="(."
keywords.append(startcode)
endcode = ".)"
keywords.append(endcode)


minimo = [] 

pos_fx_ident, alfa_ident = postfix(ident) 
pos_fx_string, alfa_string = postfix(string) 
pos_fx_char, alfa_char = postfix(char) 
pos_fx_charnumber, alfa_charnumber = postfix(charnumber) 

#Iniciando los AFN 
print("Iniciando los AFN")
trans_t_ident, strt_end_t_ident = thomson(pos_fx_ident, alfa_ident)
trans_t_string, strt_end_t_string = thomson(pos_fx_string, alfa_string)
trans_t_char, strt_end_t_char = thomson(pos_fx_char, alfa_char)
trans_t_charnumber, strt_end_t_charnumber = thomson(pos_fx_charnumber, alfa_charnumber)
#Iniciando los AFD
print("Iniciando los AFD")
trans_afd_ident, strt_end_afd_ident, min_ident, min_strt_ident = subconjuntos(trans_t_ident, strt_end_t_ident)
trans_afd_string, strt_end_afd_string, min_string, min_strt_string = subconjuntos(trans_t_string, strt_end_t_string)
trans_afd_char, strt_end_afd_char, min_char, min_strt_char = subconjuntos(trans_t_char, strt_end_t_char)
trans_afd_charnumber, strt_end_afd_charnumber, min_charnumber, min_strt_charnumber = subconjuntos(trans_t_charnumber, strt_end_t_charnumber)

minimo.append([min_ident, min_strt_ident, alfa_ident])
minimo.append([min_string, min_strt_string, alfa_string])
minimo.append([min_char, min_strt_char, alfa_char])
minimo.append([min_charnumber, min_strt_charnumber, alfa_charnumber])
n_f = input('Ingrese el nombre del archivo... ')
scanner(keywords, minimo, n_f)
