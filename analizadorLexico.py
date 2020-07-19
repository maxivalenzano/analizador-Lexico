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
		'SINO', 'REPETIR', 'HASTA_QUE', 'PARA', 'HASTA', 'REAL'
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
	cad1 = str(t.value[0].encode('ascii', 'ignore').decode('ascii')) + ''
	cad2 = 'Error lexico: " ' + ' " en la linea: ' + str(t.lineno) + cad1 
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
    cad1 = str(t.value[0])
    cad2 = 'Error lexico: " ' + cad1 + ' " en la linea: ' + str(t.lineno)
    print (cad2)
    t.lexer.skip(1)

def t_foo_comentario(t):
	r'[a-zA-Z0-9\!\@\$\%\^\&\*\(\)\-\_\=\+\[\]\{\}\;\:\'\"\?\,\.\<\>\t\r\f]+'
	pass

def t_foo_end(t):
     r'\# '
     t.lexer.begin('INITIAL') 

def buscarFicheros(directorio):
 	ficheros = []
 	numArchivo = ''
 	respuesta = False
 	cont = 1

	for base, dirs, files in os.walk(directorio):
 		ficheros.append(files)

 	for file in files:
 		print str(cont)+". "+file
 		cont = cont+1

 	while respuesta == False:
 		numArchivo = raw_input('\nNumero del test: ')
 		for file in files:
 			if file == files[int(numArchivo)-1]:
 				respuesta = True
 				break

 	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

 	return files[int(numArchivo)-1]


print ("Hola este es el analizador Lexico")
print ("Desea ingresar manualmente el codigo o desde un archivo?")
op = raw_input('\n(1)manual \t(2)archivo \n')
if int(op) == 1:
	print ("Escogio entrada manual")
	print ("Ingrese el codigo a analizar \n")
	cadena = ''
	while True:
		try:
			cad = raw_input('> ')
			cadena = cadena+cad+ '\n'
		except EOFError:
			break
		if not cadena: continue
	print ('\n')
else:
	print ("Escogio por archivo")
	print ("Seleccione el archivo a analizar")
	directorio = (str(os.getcwd())+ '/test/')
	archivo = buscarFicheros(directorio)
	test = directorio+archivo
	fp = codecs.open(test,'r','utf-8')
	cadena = fp.read()
	fp.close()

analizador = lex.lex()

analizador.input(cadena)
print("Lista de tokens")
while True:
 	tok = analizador.token()
 	if not tok : break
 	print (tok)