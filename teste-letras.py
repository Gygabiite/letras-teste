class Teste:
    def __init__(self, entrada):
        self.entrada = entrada

    def desDuplicar(self):
        #Cria uma string vazia para guardar a resposta.
        resposta = ""
        #Loopa entre todas as palavras da string informada.
        for palavra in self.entrada.split(" "):
            #Variável boolean para verificar se a duplicação foi eliminada.
            confirmaPalavraComDuplicacao = False
            #Verifica se o tamanho da palavra é impar ou par, porque se for impar tem que eliminar a primeira letra, pois a mesma não vai ter duplicação
            if len(palavra) % 2 == 0:
                #Loopa pela metade do tamanho da palavra, verificando se substrings da mesma são iguais
                for i in range(int(len(palavra)/2)):
                    if palavra.removesuffix(palavra[int(len(palavra)/2) + i:])[-int(len(palavra[int(len(palavra)/2) + i:])):] == palavra[int(len(palavra)/2) + i:]:
                        #Se as substrings forem iguais, elimina a duplicação da palavra e confirma que foi eliminada
                        resposta += palavra.removesuffix(palavra[int(len(palavra) / 2) + i:]) + " "
                        confirmaPalavraComDuplicacao = True
                        break
            else:
                #Loopa pela metade do tamanho da palavra, verificando se substrings da mesma são iguais
                for i in range(int(len(palavra[1:])/2)):
                    if palavra[1:].removesuffix(palavra[1:][int(len(palavra[1:])/2) + i:])[-int(len(palavra[1:][int(len(palavra[1:])/2) + i:])):] == palavra[1:][int(len(palavra[1:])/2) + i:]:
                        #Se as substrings forem iguais, elimina a duplicação da palavra e confirma que foi eliminada
                        resposta += palavra.removesuffix(palavra[1:][int(len(palavra[1:])/2) + i:]) + " "
                        confirmaPalavraComDuplicacao = True
                        break
            #Se alguma palavra não houver duplicação, retorna a string como ela entrou.               
            if confirmaPalavraComDuplicacao == False:
                return self.entrada.strip() + "."
        #Se todas as palavras tiverem duplicação, retorna a nova string sem as duplicações com um ponto no final
        return resposta.strip() + "."


#Instanciando a classe com os casos de teste
teste1 = Teste("oo ratoato roeuoeu aa roupaoupa dodo reiei dee romaoma")
teste2 = Teste("banana")
teste3 = Teste("a bananeira tem banana")
teste4 = Teste("saarara temem duas bolass")
teste5 = Teste("araraara")
casoTeste = Teste(str(input("Digite o texto: ")))

#Chamando o método de desduplicação e mostrando o resultado
print(teste1.desDuplicar())
print(teste2.desDuplicar())
print(teste3.desDuplicar())
print(teste4.desDuplicar())
print(teste5.desDuplicar())
print(casoTeste.desDuplicar())
