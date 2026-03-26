from datetime import datetime

#O construtor __init__ é o método que executa quando o objeto é criado.
class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, vencimento, quantidade):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda

    #try: execute o codigo, se der erro, execute o except. 
        try:
            self.__data_compra = datetime.strptime(data_compra, "%d/%m/%Y")
            self.__vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Formato de data inválido! Use dd/mm/aaaa")   #o raise mostrará a mensagem de erro de forma clara.

        self.__quantidade = quantidade
  

    @property               # GETTERS (com @property)
    def nome(self):
        return self.__nome

    @property
    def preco_compra(self):
        return self.__preco_compra

    @property
    def preco_venda(self):
        return self.__preco_venda

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def data_compra(self):
        return self.__data_compra.strftime("%d/%m/%Y")

    @property
    def vencimento(self):
        return self.__vencimento.strftime("%d/%m/%Y")


    @preco_compra.setter                       # @setter (alteração com validação, ou seja, não permite dar negativo).
    def preco_compra(self, novo_preco):
        if novo_preco >= 0:
            self.__preco_compra = novo_preco
        else:
            print("Preço de compra inválido!")

    @preco_venda.setter
    def preco_venda(self, novo_preco):
        if novo_preco >= 0:
            self.__preco_venda = novo_preco
        else:
            print("Preço de venda inválido!")

    @quantidade.setter
    def quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd
        else:
            print("Quantidade inválida!")

    @data_compra.setter
    def data_compra(self, nova_data):
        try:                                     #try: execute o codigo, se der erro, execute o except. 
            self.__data_compra = datetime.strptime(nova_data, "%d/%m/%Y")
        except ValueError:
            print("Data de compra inválida!")

    @vencimento.setter
    def vencimento(self, nova_data):
        try:
            self.__vencimento = datetime.strptime(nova_data, "%d/%m/%Y")
        except ValueError:
            print("Data de vencimento inválida!")

    

    def dias_para_vencer(self):
        return (self.__vencimento - datetime.now()).days

    def consumir(self, qtd):
        if qtd <= self.__quantidade:
            self.__quantidade -= qtd
            return True
        else:
            print("Estoque insuficiente!")
            return False

class ItemConsumo:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    def calcular_subtotal(self):
        return self.__produto.preco_venda * self.__quantidade