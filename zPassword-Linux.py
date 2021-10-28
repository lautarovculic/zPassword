from random import sample
def password_generator(longitud):
	abc_minusculas = "abcdefghijkmnlopqrstuvwxyz"
	abc_mayusculas = abc_minusculas.upper()
	numeros = "0123456789"
	simbolos = "@#$_&-+()/*'|={}\:;][><!?"
	combinacion = abc_minusculas + abc_mayusculas + numeros + simbolos
	password_union = sample(combinacion, longitud)
	password_result = "".join(password_union)
	return password_result
password = password_generator(12)
print("zPassword - Lautaro Villarreal Culic'")
print("Contraseña: ", password)
print("https://lautarovculic.com")
