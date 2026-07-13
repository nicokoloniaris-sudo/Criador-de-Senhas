import random
sf = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

caracter = int(input("Insira o comprimento da senha: "))
senha = ""

for i in range(caracter):
    senha += random.choice(sf)
print(senha)