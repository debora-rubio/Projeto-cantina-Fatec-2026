import pickle

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