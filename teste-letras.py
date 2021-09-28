entrada = str(input())

entradaSplit = entrada.split(" ")
resposta = ""
for palavra in entradaSplit:
    temp = ""
    temp2 = ""
    for letra in palavra:
        if letra in temp and letra not in temp2:
            temp2 += letra
        else:
            temp += letra
    
    if len(temp2) == 0:
        resposta = entrada.strip() + "."
        break
    else:
        palavra = palavra[:-len(temp2)]
        resposta += palavra + " "

print(resposta)