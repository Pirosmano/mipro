temp = input ("introduce la temperatura ")
grados = float(temp[:-1])
letra = temp [-1]
if letra == "c":
	CtoF = grados * 1.8 + 32
	print ("la temperatura en Celsius es = ", CtoF)
if letra == "f":
	CtoF = grados - 32 / 1.8
	print ("la temperatura en Farenheit es = ", CtoF)