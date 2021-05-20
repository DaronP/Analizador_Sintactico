from thomson import *
from subconjuntos import *
from libs import *
#KEYWORDS
keywords = ['while', 'do']
#CHARACTERS
upletter  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
downletter  = "abcdefghijklmnopqrstuvwxyz"
letter = "abcdefghijklmnopqrstuvwxyz" + upletter
letter  = or_ing(letter )

digit = "0123456789" 
hexdigit = digit + "ABCDEF"
hexdigit  = or_ing(hexdigit )

hexterm = 'H'
tab = ","
eol = ";"
whitespace = "!"+eol+tab+"!"
whitespace = or_ing(whitespace)
sign ="~"+"-"
sign = or_ing(sign)

#TOKENS
digit = or_ing(digit)
ident = "("+letter+")_("+letter+"|"+digit+")*"
hexnumber = "("+hexdigit+")_("+hexdigit+")*_("+hexterm+")"
number = "("+digit+")_("+digit+")*"
signnumber  = "(("+sign+")*)_("+digit+")_("+digit+")*"
whitetoken = "("+whitespace+")_("+whitespace+")*"


minimo = [] 

pos_fx_ident, alfa_ident = postfix(ident) 
pos_fx_hexnumber, alfa_hexnumber = postfix(hexnumber) 
pos_fx_number, alfa_number = postfix(number) 
pos_fx_signnumber, alfa_signnumber = postfix(signnumber) 
pos_fx_whitetoken, alfa_whitetoken = postfix(whitetoken) 

#Iniciando los AFN 
print("Iniciando los AFN")
trans_t_ident, strt_end_t_ident = thomson(pos_fx_ident, alfa_ident)
trans_t_hexnumber, strt_end_t_hexnumber = thomson(pos_fx_hexnumber, alfa_hexnumber)
trans_t_number, strt_end_t_number = thomson(pos_fx_number, alfa_number)
trans_t_signnumber, strt_end_t_signnumber = thomson(pos_fx_signnumber, alfa_signnumber)
trans_t_whitetoken, strt_end_t_whitetoken = thomson(pos_fx_whitetoken, alfa_whitetoken)
#Iniciando los AFD
print("Iniciando los AFD")
trans_afd_ident, strt_end_afd_ident, min_ident, min_strt_ident = subconjuntos(trans_t_ident, strt_end_t_ident)
trans_afd_hexnumber, strt_end_afd_hexnumber, min_hexnumber, min_strt_hexnumber = subconjuntos(trans_t_hexnumber, strt_end_t_hexnumber)
trans_afd_number, strt_end_afd_number, min_number, min_strt_number = subconjuntos(trans_t_number, strt_end_t_number)
trans_afd_signnumber, strt_end_afd_signnumber, min_signnumber, min_strt_signnumber = subconjuntos(trans_t_signnumber, strt_end_t_signnumber)
trans_afd_whitetoken, strt_end_afd_whitetoken, min_whitetoken, min_strt_whitetoken = subconjuntos(trans_t_whitetoken, strt_end_t_whitetoken)

minimo.append([min_ident, min_strt_ident, alfa_ident])
minimo.append([min_hexnumber, min_strt_hexnumber, alfa_hexnumber])
minimo.append([min_number, min_strt_number, alfa_number])
minimo.append([min_signnumber, min_strt_signnumber, alfa_signnumber])
minimo.append([min_whitetoken, min_strt_whitetoken, alfa_whitetoken])
n_f = input('Ingrese el nombre del archivo... ')
scanner(keywords, minimo, n_f)
