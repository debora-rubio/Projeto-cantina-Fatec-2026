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
import pickle

# ---------------- CLASSES ----------------

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

    def dias_para_vencer(self):
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


class SistemaCantina:
    def __init__(self):
        self.__estoque = []
        self.__pagamentos = []

    @property
    def estoque(self):
        return self.__estoque

    def adicionar_produto(self, produto):
        self.__estoque.append(produto)

    @property
    def pagamentos(self):
        return self.__pagamentos

    def registrar_pagamento(self, pagamento):
        for item in pagamento.carrinho.itens:
            item.produto.consumir(item.quantidade)
        self.__pagamentos.append(pagamento)

    def salvar_dados(self, arquivo="dados.pkl"):
        with open(arquivo, "wb") as f:
            pickle.dump(self.__pagamentos, f)

    def carregar_dados(self, arquivo="dados.pkl"):
        with open(arquivo, "rb") as f:
            self.__pagamentos = pickle.load(f)

    def relatorio_vendas(self):
        total = sum(p.carrinho.calcular_total() for p in self.__pagamentos)
        print(f"Relatório de Vendas: Total arrecadado R$ {total:.2f}")

    def relatorio_consumo(self):
        print("Relatório de Consumo:")
        for pagamento in self.__pagamentos:
            print(f"{pagamento.nome} ({pagamento.categoria}, {pagamento.curso}) comprou R$ {pagamento.carrinho.calcular_total():.2f}")
            for item in pagamento.carrinho.itens:
                produto = item.produto
                dias = produto.dias_para_vencer()
                if dias < 0:
                    aviso = "Produto vencido!"
                elif dias <= 3:
                    aviso = f"Vence em {dias} dias"
                else:
                    aviso = f"vence em {dias} dias"
                print(f"   - {produto.nome}: {aviso}")


# ---------------- BLOCO PRINCIPAL ----------------

if __name__ == "__main__":
    sistema = SistemaCantina()

    # Produtos reais da cantina
    salgadinho_torcida = Produto("salgadinho_torcida", 2.00, 3.00, "23/03/2026", "25/09/2027", 50)
    refrigerante = Produto("refrigerante", 1.50, 3.00, "23/03/2026", "15/01/2027", 100)
    bombom = Produto("bombom", 1.00, 2.50, "23/03/2026", "10/10/2026", 80)
    drops_freegels = Produto("drops_freegels", 2.00, 3.00, "23/03/2026", "11/01/2027", 60)
    bolinho_recheado = Produto("bolinho_recheado", 2.50, 5.00, "23/03/2026", "15/07/2026", 40)
    todinho = Produto("todinho", 3.50, 5.50, "23/03/2026", "08/09/2026", 70)
    copo_cafe = Produto("copo_cafe", 2.50, 4.00, "23/03/2026", "23/03/2026", 200)
    agua_com_gas = Produto("agua_com_gas", 1.50, 4.00, "23/03/2026", "20/11/2026", 90)

    # Adicionando ao sistema
    sistema.adicionar_produto(salgadinho_torcida)
    sistema.adicionar_produto(refrigerante)
    sistema.adicionar_produto(bombom)
    sistema.adicionar_produto(drops_freegels)
    sistema.adicionar_produto(bolinho_recheado)
    sistema.adicionar_produto(todinho)
    sistema.adicionar_produto(copo_cafe)
    sistema.adicionar_produto(agua_com_gas)

    print("Produtos cadastrados com sucesso!")

    # Compra de teste
    carrinho = Carrinho()
    carrinho.adicionar_item(ItemConsumo(salgadinho_torcida, 2))
    carrinho.adicionar_item(ItemConsumo(refrigerante, 1))
    carrinho.adicionar_item(ItemConsumo(bombom, 3))

    pagamento = Pagamento("João Silva", "aluno", "IA", datetime.now().strftime("%d/%m/%Y %H:%M"), carrinho)
    sistema.registrar_pagamento(pagamento)

    pagamento.resumo_pagamento()
    sistema.relatorio_vendas()
    sistema.relatorio_consumo()


