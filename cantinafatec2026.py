# Acesso Dev (desenvolvedores).

# Iniciando a criação de uma classe Produto. Cada produto da cantina será um objeto dessa classe.

# Os Atributos (variáveis) da classe Produto são: nome, preço de compra, preço de venda, data de compra, vencimento e quantidade.

# Os métodos (ações/funções) da classe Produto.

# _init_ é o metodo que executa quando o objeto é criado.

# self representa o objeto atual que está chamando o método.

# Incluí a proteção Getters(leitura) e Setters(atributo protegico com permissão de alteração restrita) no codigo,
# para proteção dos dados, assim os atributos (nome, preço, data, vencimento e quantidade)
# ficam privados, podendo ser alterados somente quando autorizado, evitando erros ou alterações indevidas.

# Para melhoria do código, ocultei getters e setters com @property e @setter, deixando o codigo mais limpo e elegante.

from datetime import datetime

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
    def vencimento(self):
        return self.__vencimento

    def dias_para_vencer(self):
        """Calcula quantos dias faltam para o vencimento"""
        vencimento_dt = datetime.strptime(self.__vencimento, "%d/%m/%Y")
        dias_restantes = (vencimento_dt - datetime.now()).days
        return dias_restantes

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



class Pagamento:
    def __init__(self, nome, categoria, curso, data_hora, carrinho):
        self.__nome = nome
        self.__categoria = categoria
        self.__data_hora = data_hora
        if curso in ["IA", "ESG"]:
            self.__curso = curso
        else:
            raise ValueError("Curso inválido! Escolha apenas IA ou ESG.")
        self.__carrinho = carrinho

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


    def resumo_pagamento(self):
        print(f"Nome: {self.__nome}")
        print(f"Categoria: {self.__categoria}")
        print(f"Curso: {self.__curso}")
        print(f"Data/Hora: {self.__data_hora}")
        print("Itens consumidos:")
        for item in self.__carrinho.itens:
            produto = item.produto
            qtd = item.quantidade
            subtotal = item.calcular_subtotal()
            print(f"- {produto.nome} | R$ {produto.preco_venda:.2f} x {qtd} = R$ {subtotal:.2f}")
        print(f"Total: R$ {self.__carrinho.calcular_total():.2f}")
        print("Pagamento via PIX disponível!")


#Testando o código com um exemplo de compra:

from datetime import datetime


if __name__ == "__main__":
    p1 = Produto("salgadinho", 3.00, 5.00, "19/03/2026", "25/03/2026", 10)

    print(f"O produto {p1.nome} vence em {p1.dias_para_vencer()} dias.")
    p2 = Produto("refrigerante", 4.50, 7.00, "19/03/2026", "30/03/2026", 20)

    carrinho = Carrinho()
    carrinho.adicionar_item(ItemConsumo(p1, 2))
    carrinho.adicionar_item(ItemConsumo(p2, 1))

    # Gerar data/hora automática no momento da compra
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    pagamento = Pagamento("João Silva", "aluno", "IA", data_hora, carrinho)
    pagamento.resumo_pagamento()

    # Alterando quantidade com setter
    p1.quantidade = 8
    print(f"Nova quantidade de {p1.nome}: {p1.quantidade}")




