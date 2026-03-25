from datetime import datetime
from faker import Faker

# Importações atualizadas com os novos nomes de arquivos
from produtos import Produto, ItemConsumo
from financeiro import Carrinho, Pagamento
from gerenciamento import SistemaCantina

faker = Faker("pt_BR")

if __name__ == "__main__":
    sistema = SistemaCantina()

    # Seus produtos reais
    salgadinho_torcida = Produto("salgadinho_torcida", 2.00, 3.00, "23/03/2026", "25/09/2027", 50)
    refrigerante = Produto("refrigerante", 1.50, 3.00, "23/03/2026", "15/01/2027", 100)
    bombom = Produto("bombom", 1.00, 2.50, "23/03/2026", "10/10/2026", 80)
    drops_freegels = Produto("drops_freegels", 2.00, 3.00, "23/03/2026", "11/01/2027", 60)
    bolinho_recheado = Produto("bolinho_recheado", 2.50, 5.00, "23/03/2026", "15/07/2026", 40)
    todinho = Produto("todinho", 3.50, 5.50, "23/03/2026", "08/09/2026", 70)
    agua_com_gas = Produto("agua_com_gas", 1.50, 4.00, "23/03/2026", "20/11/2026", 90)

    sistema.adicionar_produto(salgadinho_torcida)
    sistema.adicionar_produto(refrigerante)
    sistema.adicionar_produto(bombom)
    sistema.adicionar_produto(drops_freegels)
    sistema.adicionar_produto(bolinho_recheado)
    sistema.adicionar_produto(todinho)
    sistema.adicionar_produto(agua_com_gas)

    print("Produtos cadastrados com sucesso!")

    nomes_fixos = ["Neia", "Dan", "Chateus", "Felipe", "Sara", "Paulo", "Aneci"]

    for i in range(15):
        nome = nomes_fixos[i] if i < len(nomes_fixos) else faker.name()
        categoria = faker.random_element(["aluno", "professor", "colaborador"])
        curso = "Sem Curso" if categoria == "colaborador" else faker.random_element(["IA", "ESG"])
        data_hora = faker.date_time_this_year()  

        carrinho = Carrinho()
        carrinho.adicionar_item(ItemConsumo(faker.random_element(sistema.estoque), faker.random_int(min=1, max=3)))
        carrinho.adicionar_item(ItemConsumo(faker.random_element(sistema.estoque), faker.random_int(min=1, max=2)))

        pagamento = Pagamento(nome, categoria, curso, data_hora, carrinho)
        sistema.registrar_pagamento(pagamento)
        pagamento.resumo_pagamento()

    sistema.salvar_dados("dados_cantina.pkl")
    print("\nPagamentos salvos em dados_cantina.pkl")

    sistema.carregar_dados("dados_cantina.pkl")
    print("Pagamentos carregados com sucesso!\n")

    sistema.relatorio_vendas()
    sistema.relatorio_consumo()