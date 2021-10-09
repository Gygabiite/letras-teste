class Teste:
    def __init__(self, entrada):
        self.entrada = entrada

    def desDuplicar(self):
        #Cria uma variável para resposta
        resposta = ""
        #Loopa entre todas as palavras da string informada
        for palavra in self.entrada.split(" "):
            temp = ""
            temp2 = ""
            #Loopa por cada letra na palavra ao contrário
            for letra in reversed(palavra):
                #Verifica se a letra atual já ocorreu antes, se sim, adiciona ela na string temporária 2, se não adiciona na string temporária 1
                #Se a letra já ocorreu antes em ambas as strings temporárias, adiciona ela na 1
                if letra in temp and letra not in temp2:
                    temp2 += letra
                    if temp2 == temp:
                        break
                else:
                    temp += letra
            
            #Verificando se ouve alguma duplicação, se não apenas retorna a string dada no começo.
            if len(temp2) == 0:
                return self.entrada.strip() + "."
            #Adiciona a palavra sem a duplicação no final
            resposta += palavra.removesuffix(temp2[::-1]) + " "
        #Retorna a string completa sem a duplicaçõe no final de cada palavra
        return resposta.strip() + "."

#Instanciando a classe com os casos de teste
teste1 = Teste("oo ratoato roeuoeu aa roupaoupa dodo reiei dee romaoma")
teste2 = Teste("banana")
teste3 = Teste("a bananeira tem banana")
teste4 = Teste("saarara temem duas bolass")
teste5 = Teste("araraa")
teste6 = Teste(str(input("Frase: ")))

#Outputs
print(teste1.desDuplicar())
print(teste2.desDuplicar())
print(teste3.desDuplicar())
print(teste4.desDuplicar())
print(teste5.desDuplicar())
print(teste6.desDuplicar())