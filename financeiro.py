from datetime import datetime
from produtos import ItemConsumo 


class Carrinho:
    def __init__(self):
        self.__itens = []  # encapsulamento privado

    def adicionar_item(self, item_consumo):
        self.__itens.append(item_consumo)

    def remover_item(self, indice):
        if 0 <= indice < len(self.__itens):
            removido = self.__itens.pop(indice)
            print(f"Item removido: {removido.produto.nome}")
        else:
            print("Índice inválido!")

    def alterar_item(self, indice, nova_quantidade):
        if 0 <= indice < len(self.__itens):
            
            self.__itens[indice].quantidade = nova_quantidade   # Usando o setter da classe ItemConsumo.
            print(f"Quantidade alterada para {nova_quantidade}")
        else:
            print("Índice inválido!")

    @property
    def itens(self):
        return self.__itens

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.__itens)




class Pagamento:
    def __init__(self, nome, categoria, curso, data_hora, carrinho):
        self.__nome = nome
        self.__categoria = categoria
        self.__curso = curso
        self.__data_hora = data_hora
        self.__carrinho = carrinho

        if self.__categoria in ["aluno", "professor"]:
            if self.__curso not in ["IA", "ESG"]:
                raise ValueError("Curso inválido! Escolha apenas IA ou ESG.")
        elif self.__categoria == "colaborador":
            if self.__curso != "Sem Curso":
                raise ValueError("Colaborador deve estar como 'Sem Curso'.")

    
    def resumo_pagamento(self):
        print(f"Nome: {self.__nome}")
        print(f"Categoria: {self.__categoria}")
        print(f"Curso: {self.__curso}")
        print(f"Data/Hora: {self.__data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("Itens consumidos:")

        for item in self.__carrinho.itens:
            produto = item.produto
            qtd = item.quantidade
            subtotal = item.calcular_subtotal()

            print(f"- {produto.nome} | R$ {produto.preco_venda:.2f} x {qtd} = R$ {subtotal:.2f}")

        print(f"Total: R$ {self.__carrinho.calcular_total():.2f}")

    
    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def curso(self):
        return self.__curso

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def carrinho(self):
        return self.__carrinho