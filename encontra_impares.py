'''
    Função que recebe como parâmetro uma lista de números inteiros e 
devolve uma outra lista apenas com os números ímpares da lista dada
(o algoritmo utiliza recursão).
'''

class Recursao:
    def encontra_impares(self,lista):

        terminou = True

        if len(lista) == 0:
            return lista

        for elemento in lista:

            if elemento % 2 == 0:
                terminou = False

        if not terminou:

            if (lista[0] % 2) != 0:    #verifica se o primeiro elemento da lista recebeida é ímpar,
                lista.append(lista[0])  #se for, o adiciona ao fim da lista

            return self.encontra_impares(lista[1:])

        else:
            return lista



