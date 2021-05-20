from thomson import *
from subconjuntos import *
from libs import *
#KEYWORDS
keywords = ['while', 'do']
#CHARACTERS
digit = "0123456789" 
tab = ","
eol = ";"
blanco = eol+"!"+tab+"&"

#TOKENS
digit = or_ing(digit)
number = "("+digit+")_("+digit+")*"
decnumber = "("+digit+")_("+digit+")*"+"_:_("+digit+")_("+digit+")*"
blanco = or_ing(blanco)
white = "("+blanco+")_("+blanco+")*"


minimo = [] 

pos_fx_number, alfa_number = postfix(number) 
pos_fx_decnumber, alfa_decnumber = postfix(decnumber) 
pos_fx_white, alfa_white = postfix(white) 

#Iniciando los AFN 
print("Iniciando los AFN")
trans_t_number, strt_end_t_number = thomson(pos_fx_number, alfa_number)
trans_t_decnumber, strt_end_t_decnumber = thomson(pos_fx_decnumber, alfa_decnumber)
trans_t_white, strt_end_t_white = thomson(pos_fx_white, alfa_white)
#Iniciando los AFD
print("Iniciando los AFD")
trans_afd_number, strt_end_afd_number, min_number, min_strt_number = subconjuntos(trans_t_number, strt_end_t_number)
trans_afd_decnumber, strt_end_afd_decnumber, min_decnumber, min_strt_decnumber = subconjuntos(trans_t_decnumber, strt_end_t_decnumber)
trans_afd_white, strt_end_afd_white, min_white, min_strt_white = subconjuntos(trans_t_white, strt_end_t_white)

minimo.append([min_number, min_strt_number, alfa_number])
minimo.append([min_decnumber, min_strt_decnumber, alfa_decnumber])
minimo.append([min_white, min_strt_white, alfa_white])
n_f = input('Ingrese el nombre del archivo... ')
scanner(keywords, minimo, n_f)
