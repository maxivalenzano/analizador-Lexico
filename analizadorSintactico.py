import ply.yacc as yacc
import logging
import os
import codecs
import re
from lex import tokens
from sys import stdin

precedence = (
	('right','ID','PROCESO','SI','MIENTRAS', 'REPETIR'),
	('right','ASIGNACION'),
	('right','IGUALQUE'),
	('left','DISTINTO'),
	('left','MENORQUE','MENOROIGUAL','MAYORQUE','MAYOROIGUAL'),
	('left','SUMA','RESTA'),
	('left','PRODUCTO','DIVISION'),
	('left','PARENTIZQ','PARENTDER'),
	)

def p_sigma(p):
	'''sigma : programa'''
	print "sigma"
	print "\nFelicidades"
	print "Su codigo es sintacticamente correcto"

def p_programa(p):
	'''programa : titulo bloque final'''
	print "programa"

#def p_programa_error(p):
#	'''programa : error '''
#	print "Syntax error in print statement. Bad expression"

def p_titulo(p):
	'''titulo : ACCION ID ES
				| ACCION ILEGAL ES'''
	print "titulo"

def p_final(p):
	'''final : FIN_ACCION'''
	print "pie final"

def p_bloque1(p):
	'''bloque : ambient procesos'''
	print "bloque 1"

def p_bloque2(p):
	'''bloque : procesos'''
	print "bloque 2"

def p_ambient(p):
	'''ambient : AMBIENTE declaraciones'''
	print "ambient"

def p_declaraciones1(p):
	'''declaraciones : ID DOSPUNTOS tipodato'''
	print "declaraciones 1"

def p_declaraciones2(p):
	'''declaraciones : ID DOSPUNTOS tipodato declaraciones'''
	print "declaraciones 2"

def p_tipodato(p):
	'''tipodato : CADENA 
				| ENTERO
				| NUMERO
				| NUM
				| FLOAT
				| REAL'''
	print "tipodato"

def p_procesos(p):
	'''procesos : PROCESO listasentencias'''
	print "procesos"

def p_listasentencias1(p):
	'''listasentencias : sentencia PUNTOYCOMA listasentencias'''
	print "listasentencias 1 "

def p_listasentencias2(p):
	'''listasentencias : sentencia'''
	print "listasentencias 2"

def p_listasentencias3(p):
	'''listasentencias : sentencia PUNTOYCOMA'''
	print "listasentencias 3"

def p_sentencia1(p):
	'''sentencia : ID ASIGNACION expresion'''
	print "sentencia 1"

def p_sentencia2(p):
	'''sentencia : LEER PARENTIZQ ID PARENTDER'''
	print "sentencia 2"

def p_sentencia3(p):
	'''sentencia : ESCRIBIR PARENTIZQ listext PARENTDER'''
	print "sentencia 3"

def p_text1(p):
	'''text : TEXTO'''
	print "text 1"

def p_text2(p):
	'''text : ID
			| NUM
			| FLOAT'''
	print "text 2"

def p_listext1(p):
	'''listext : text COMA listext'''
	print "listext 1"

def p_listext2(p):
	'''listext : text'''
	print "listext 2"

def p_sentencia4(p):
	'''sentencia : REPETIR listasentencias HASTA_QUE cond '''
	print "sentencia 4"

def p_sentencia5(p):
	'''sentencia : SI cond ENTONCES PUNTOYCOMA listasentencias FIN_SI '''
	print "sentencia 5"

def p_sentencia6(p):
	'''sentencia : SI cond ENTONCES PUNTOYCOMA listasentencias SINO PUNTOYCOMA listasentencias FIN_SI'''
	print "sentencia 6"

def p_sentencia7(p):
	'''sentencia : MIENTRAS cond HACER PUNTOYCOMA listasentencias FIN_MIENTRAS'''
	print "sentencia 7"

def p_vinicial1(p):
	'''vinicial : PARENTIZQ ID ASIGNACION NUM PARENTDER'''
	print "vinicial 1"

def p_vinicial2(p):
	'''vinicial : PARENTIZQ ID ASIGNACION ID PARENTDER'''
	print "vinicial 2"

def p_vfinal1(p):
	'''vfinal : NUM'''
	print "vfinal 1"

def p_vfinal2(p):
	'''vfinal : ID'''
	print "vfinal 2"

def p_sentencia8(p):
	'''sentencia : PARA vinicial HASTA vfinal COMA NUM HACER PUNTOYCOMA listasentencias FIN_PARA '''
	print "sentencia 8"

def p_expresion1(p):
	'''expresion : term'''
	print "expresion 1"

def p_expresion2(p):
	'''expresion : agregarOperador term'''
	print "expresion 2"

def p_expresion3(p):
	'''expresion : expresion agregarOperador term'''
	print "expresion 3"

def p_agregarOperador1(p):
	'''agregarOperador : SUMA'''
	print "agregarOperador 1"

def p_agregarOperador2(p):
	'''agregarOperador : RESTA'''
	print "agregarOperador 1"

def p_term1(p):
	'''term : factor'''
	print "term 1"

def p_term2(p):
	'''term : term multiplicarOperador factor'''
	print "term 1"

def p_multiplicarOperador1(p):
	'''multiplicarOperador : PRODUCTO'''
	print "multiplicarOperador 1"

def p_multiplicarOperador2(p):
	'''multiplicarOperador : DIVISION'''
	print "multiplicarOperador 2"

def p_multiplicarOperador3(p):
	'''multiplicarOperador : DIV'''
	print "multiplicarOperador 3"

def p_multiplicarOperador4(p):
	'''multiplicarOperador : MOD'''
	print "multiplicarOperador 4"

def p_multiplicarOperador5(p):
	'''multiplicarOperador : POTENCIA'''
	print "multiplicarOperador 5"

def p_factor1(p):
	'''factor : ID'''
	print "factor 1"

def p_factor2(p):
	'''factor : NUM
			| FLOAT'''
	print "factor 1"

def p_factor3(p):
	'''factor : PARENTIZQ expresion PARENTDER'''
	print "factor 1"

def p_cond(p):
	''' cond : PARENTIZQ listacondicion PARENTDER'''
	print "cond"

def p_listacondicion1(p):
	'''listacondicion : condicion'''
	print "listacondicion 1"

def p_listacondicion2(p):
	'''listacondicion : condicion CONJUNCION listacondicion
						| condicion DISYUNCION listacondicion'''
	print "listacondicion 2"

def p_condicion1(p):
	'''condicion : NEGACION expresion'''
	print "condicion 1"

def p_condicion2(p):
	'''condicion : expresion relacion expresion'''
	print "condicion 2"

def p_relacion1(p):
	'''relacion : IGUALQUE'''
	print "relacion 1"

def p_relacion2(p):
	'''relacion : DISTINTO'''
	print "relacion 2"

def p_relacion3(p):
	'''relacion : MENORQUE'''
	print "relacion 3"

def p_relacion4(p):
	'''relacion : MAYORQUE'''
	print "relacion 4"

def p_relacion5(p):
	'''relacion : MENOROIGUAL'''
	print "relacion 5"

def p_relacion6(p):
	'''relacion : MAYOROIGUAL'''
	print "relacion 6"

def p_relacion7(p):
	'''relacion : DISYUNCION'''
	print "relacion 7"

def p_relacion8(p):
	'''relacion : CONJUNCION'''
	print "relacion 8"

def p_error(p):

	print "Error de sintaxis con el: ", p
	

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

print ("Hola este es el analizador sintactico")
print ("Desea ingresar manualmente el codigo o desde un archivo?")
op = raw_input('\nmanual(1) \tarchivo(2) \n')
if int(op) == 1:
	print ("Escogio entrada manual")
	print ("Ingrese el codigo a analizar")
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
	fp = codecs.open(test,"r","utf-8")
	cadena = fp.read()
	fp.close()
	


parser = yacc.yacc()
#log = logging.getLogger () 
#Debug en tiempo de ejecucion, cambiar result
#result = parser.parse(cadena, debug = log)
result = parser.parse(cadena, tracking=True)
