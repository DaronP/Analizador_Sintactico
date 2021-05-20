from thomson import *
from subconjuntos import *
from libs import *

#CHARACTERS
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letters  = or_ing(letters )

digits = "0123456789"
digits  = or_ing(digits )

indent = chr(9)
indent  = or_ing(indent )
space = chr(32)
space  = or_ing(space )
eol = chr(10)
eol  = or_ing(eol )

#KEYWORDS
keywords =[' while', ' for', ' if', ' switch', ' case']
#TOKENS
ident = letters+")_("+letters+"|"+digits+")*"
number = digits+")_("+digits+")*"

letter_kw = ident 


pos_fx_tkn, alfa_tkn = postfix(letter_kw) 
pos_fx_num, alfa_num = postfix(num_kw) 

#Iniciando los AFN 
trans_t_tkn, strt_end_t_tkn = thomson(pos_fx_tkn, alfa_tkn)
trans_t_num, strt_end_t_num = thomson(pos_fx_num, alfa_num)
#Iniciando los AFD
trans_afd_tkn, strt_end_afd_tkn, minimo_tkn, minimo_strt_end_tkn = subconjuntos(trans_t_tkn, strt_end_t_tkn)
trans_afd_num, strt_end_afd_num, minimo_num, minimo_strt_end_num = subconjuntos(trans_t_num, strt_end_t_num)
minimo = [minimo_tkn, minimo_strt_end_tkn, alfa_tkn], [minimo_num, minimo_strt_end_num, alfa_num]

n_f = input('Ingrese el nombre del archivo... ')
scanner(keywords, minimo, n_f)
