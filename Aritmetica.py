from thomson import *
from subconjuntos import *
from libs import *
#KEYWORDS
keywords = ['while', 'do', 'if', 'switch']
#CHARACTERS
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter  = or_ing(letter )

digit = "0123456789" 
tab = ","
eol = ";"

#TOKENS
digit = or_ing(digit)
ident = "("+letter+")_("+letter+"|"+digit+")*"
number = "("+digit+")_("+digit+")*"

#PRODUCTIONS


def Expr(): 
	while(True):
		Stat ("")
	get(".")
	
	return result


def Stat (): 
	value = 0  
	value = input()
	value = Factor(value)
	
	return value


def Expression( result): 
	result1 = 0
	result2 = 0
	Term(  result1)
	while follow() == '+' or follow() == '-':
		if follow() == '+':
			result2=Term(result2)
			result1+=result2
		if follow() == '-':
			result2=Term(result2)
			result1-=result2
	
	result=result1
	
	return result


def Term( result):
	result1 = 0
	result2 = 0
	result1 = Factor(result1)
	while follow() == '*' or follow() == '/':
		if follow() == '*':
			result2=Factor(result2)
			result1*=result2
		if follow() == '/':
			result2=Factor(result2)
			result1/=result2
	
	result=result1
	
	return result


def Factor( result): 
	signo=1
	if follow() == "-":
		signo = -1

	 
	result*=signo
	
	return result



minimo = [] 

pos_fx_ident, alfa_ident = postfix(ident) 
pos_fx_number, alfa_number = postfix(number) 

#Iniciando los AFN 
print("Iniciando los AFN")
trans_t_ident, strt_end_t_ident = thomson(pos_fx_ident, alfa_ident)
trans_t_number, strt_end_t_number = thomson(pos_fx_number, alfa_number)
#Iniciando los AFD
print("Iniciando los AFD")
trans_afd_ident, strt_end_afd_ident, min_ident, min_strt_ident = subconjuntos(trans_t_ident, strt_end_t_ident)
trans_afd_number, strt_end_afd_number, min_number, min_strt_number = subconjuntos(trans_t_number, strt_end_t_number)

minimo.append([min_ident, min_strt_ident, alfa_ident])
minimo.append([min_number, min_strt_number, alfa_number])
n_f = input('Ingrese el nombre del archivo... ')
scanner(keywords, minimo, n_f)


