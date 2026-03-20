# Iniciando a criação de uma classe Produto. Cada produto da cantina será um objeto dessa classe.
# _init_ é o metodo que executa quando o objeto é criado.
# self representa o proprio objeto, ou seja, o produto que esta sendo criado.
class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.vencimento = vencimento
        self.quantidade = quantidade

    def atualizar_quantidade(self, nova_qtd):
        self.quantidade = nova_qtd

# testando:
# if __name__ == "__main__": serve para separar código de teste do código principal.
# Assim o arquivo pode ser usado tanto para rodar sozinho quanto para ser importado em outros projetos.        
if __name__ == "__main__":
    produto1 = Produto("salgadinho_torcida", 3.00, 5.00, "19/03/2026", "21/03/2026", 10)
    print(f"{produto1.nome} - Estoque: {produto1.quantidade}")
    produto1.atualizar_quantidade(8)
    print(f"Depois da venda: {produto1.quantidade}")

