# Acesso Dev (desenvolvedores).

# Iniciando a criação de uma classe Produto. Cada produto da cantina será um objeto dessa classe.

# Os Atributos (variáveis) da classe Produto são: nome, preço de compra, preço de venda, data de compra, vencimento e quantidade.

# Os métodos (ações/funções) da classe Produto.

# _init_ é o metodo que executa quando o objeto é criado.

# self representa o objeto atual que está chamando o método.

# Incluí a proteção Getters(leitura) e Setters(atributo protegico com permissão de alteração restrita) no codigo,
# para proteção dos dados, assim os atributos (nome, preço, data, vencimento e quantidade)
# ficam privados, podendo ser alterados somente quando autorizado, evitando erros ou alterações indevidas.

# Para melhoria do código, substitui o getters e setters por @property e @setter, deixando o codigo mais limpo.


class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, vencimento, quantidade):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__data_compra = data_compra
        self.__vencimento = vencimento
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @property
    def preco_compra(self):
        return self.__preco_compra

    @preco_compra.setter
    def preco_compra(self, novo_preco):
        if novo_preco >= 0:
            self.__preco_compra = novo_preco
        else:
            print("Preço de compra inválido!")

    @property
    def preco_venda(self):
        return self.__preco_venda

    @preco_venda.setter
    def preco_venda(self, novo_preco):
        if novo_preco >= 0:
            self.__preco_venda = novo_preco
        else:
            print("Preço de venda inválido!")

    @property
    def data_compra(self):
        return self.__data_compra

    @property
    def vencimento(self):
        return self.__vencimento

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd
        else:
            print("Quantidade inválida!")

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

class Carrinho:
    def __init__(self):
        self.__itens = []

    def adicionar_item(self, item_consumo):
        self.__itens.append(item_consumo)

    @property
    def itens(self):
        return self.__itens

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.__itens)