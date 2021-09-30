class Teste:
    def __init__(self, entrada):
        self.entrada = entrada

    def desDuplicar(self):
        entradaSplit = self.entrada.split(" ")
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
                resposta = self.entrada
                return resposta.strip() + "."
            else:
                palavra = palavra[:-len(temp2)]
                resposta += palavra + " "

        return resposta.strip() + "."


teste1 = Teste("oo ratoato roeuoeu aa roupaoupa dodo reiei dee romaoma")
teste2 = Teste("banana")
teste3 = Teste("a bananeira tem banana")
teste4 = Teste("saarara temem duas bolass")
teste5 = Teste(str(input("Frase: ")))

print(teste1.desDuplicar())
print(teste2.desDuplicar())
print(teste3.desDuplicar())
print(teste4.desDuplicar())
print(teste5.desDuplicar())