def func(input):
	elementos = input.split('+')
	n1 = elementos[0].strip()
	num = len(elementos)
	for i in range(1,num):
		n2 = elementos[i].strip()
		n1 = suma(n1,n2)
	print n1

def suma(n1, n2):
	nivel1 = nivel(n1)
	nivel2 = nivel(n2)
	res = ''
	if nivel1 > nivel2:
		for i in range(0, len(n1)-1):
			res = res + n1[i]
		res = res + n2 + n1[len(n1)-1]
	if nivel2 > nivel1:
		res = n2[0]+n1
		for i in range(1, len(n2)):
			res = res + n2[i]
	if nivel1 == nivel2:
		res = n1 + n2
	return res
	

def nivel(n):
	nivel = 0
	nivelT = 0
	for a in n:
		if a == '(':
			nivelT = nivelT +1
		else:
			if nivelT > nivel:
				nivel = nivelT
			nivelT = nivelT -1
	return nivel

