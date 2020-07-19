import ply.lex as lex
import re
import codecs
import os
import sys

states = (
    ('foo', 'exclusive'),
)

reservadas = ['ACCION', 'AMBIENTE', 'PROCESO', 'FIN_ACCION', 'SI',
		'FIN_SI', 'ENTONCES', 'MIENTRAS', 'FIN_MIENTRAS', 'HACER', 
		'SINO', 'REPETIR', 'HASTA_QUE', 'PARA', 'HASTA', 'REAL',
		'FIN_PARA', 'ESCRIBIR', 'LEER', 'CADENA', 'ENTERO', 'NUMERO', 
		
		]

tokens = reservadas+['ID','FLOAT','NUM','SUMA','RESTA','PRODUCTO','DIVISION',
		'IGUALQUE','DISTINTO','MENORQUE','MENOROIGUAL','MAYORQUE','MAYOROIGUAL',
		'PARENTIZQ', 'PARENTDER','COMA','PUNTOYCOMA', 'ES',
		'ASIGNACION', 'DOSPUNTOS', 'TEXTO', 'ILEGAL', 'POTENCIA',
		'DISYUNCION', 'CONJUNCION', 'NEGACION', 'MOD', 'DIV'
		]


t_ignore = '\t '
t_foo_ignore = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_IGUALQUE = r'='
t_DISTINTO = r'<>'
t_MENORQUE = r'<'
t_MENOROIGUAL = r'<='
t_MAYORQUE = r'>'
t_MAYOROIGUAL = r'>='
t_PARENTIZQ = r'\('
t_PARENTDER = r'\)'
t_COMA = r','
t_PUNTOYCOMA = r';'
t_POTENCIA = r'[*][*]'
t_ASIGNACION = r':='
t_DOSPUNTOS = r':'

def t_TEXTO(t):
	r'[\'\"].*[\'\"]'
	return t

def t_DISYUNCION(t):
	r'[_][oO]'
	return t

def t_CONJUNCION(t):
	r'[_][yY]'
	return t

def t_NEGACION(t):
	r'[_][nN][oO]'
	return t

def t_MOD(t):
	r'[_][mM][oO][dD]'
	return(t)

def t_DIV(t):
	r'[_][dD][iI][vV]'
	return(t)

def t_ES(t):
	r'[_][eE][sS]'
	return(t)

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9]*(_[a-zA-Z0-9]+)*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\@ .*'
	pass

def t_FLOAT(t):
	r'\d+ \. \d+'
	t.value = float(t.value)
	return t

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_ILEGAL(t):
	r'[_][_]*'
	return (t)

def t_error(t):
	cad1 = str(t.value[0].encode('ascii', 'ignore').decode('ascii')) + 'hola'
	cad2 = 'Error lexico: " ' + cad1 + ' " en la linea: ' + str(t.lineno)
	print (cad1)
	print (cad2)
	t.lexer.skip(1)

def t_begin_foo(t): 
     r' \# '
     t.lexer.begin('foo') # Inicia el estado' foo '

def t_foo_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_foo_error(t):
    cad1 = str(t.value[0].encode('ascii', 'ignore').decode('ascii'))
    print ( 'Error lexico: " ' + cad1 + ' " en la linea: ' + str(t.lineno))
    t.lexer.skip(1)

def t_foo_comentario(t):
	r'[a-zA-Z0-9\!\@\$\%\^\&\*\(\)\-\_\=\+\[\]\{\}\;\:\'\"\?\,\.\<\>\t\r\f]+'
	pass

def t_foo_end(t):
     r'\# '
     t.lexer.begin('INITIAL') 

analizador = lex.lex()