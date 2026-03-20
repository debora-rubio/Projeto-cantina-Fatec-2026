# Acesso Dev (desenvolvedores).
# Iniciando a criação de uma classe Produto. Cada produto da cantina será um objeto dessa classe.
# _init_ é o metodo que executa quando o objeto é criado.
# self representa o proprio objeto, ou seja, o produto que esta sendo criado.
# Incluí a proteção Getters(leitura) e Setters(atributo protegico com permissão de alteração restrita) no codigo,
# para proteção dos dados, assim os atributos (nome, preço, data, vencimento e quantidade)
# ficam privados, podendo ser alterados somente quando autorizado, evitando erros ou alterações indevidas.



class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, vencimento, quantidade):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__data_compra = data_compra
        self.__vencimento = vencimento
        self.__quantidade = quantidade

    # Getters
    def get_nome(self): return self.__nome
    def get_preco_compra(self): return self.__preco_compra
    def get_preco_venda(self): return self.__preco_venda
    def get_data_compra(self): return self.__data_compra
    def get_vencimento(self): return self.__vencimento
    def get_quantidade(self): return self.__quantidade

    # Setters
    def set_preco_compra(self, novo_preco):
        if novo_preco >= 0: self.__preco_compra = novo_preco
    def set_preco_venda(self, novo_preco):
        if novo_preco >= 0: self.__preco_venda = novo_preco
    def set_quantidade(self, nova_qtd):
        if nova_qtd >= 0: self.__quantidade = nova_qtd

    # Baixar estoque
    def consumir(self, qtd):
        if qtd <= self.__quantidade:
            self.__quantidade -= qtd
            return True
        else:
            print("Estoque insuficiente!")
            return False

