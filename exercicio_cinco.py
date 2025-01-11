def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida  
    return invertida


string = input("Digite uma string para inverter: ")
resultado = inverter_string(string)

print(f"String invertida: {resultado}")
