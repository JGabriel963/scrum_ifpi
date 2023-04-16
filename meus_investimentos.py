class Investimento:
    def __init__(self, codigo, data, quantidade, valor_unitario, compra_venda, taxa_corretora):
        self.codigo = codigo
        self.data = data
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.compra_venda = compra_venda
        self.taxa_corretora = taxa_corretora

    def calcular_valor_operacional(self):
        return self.quantidade * self.valor_unitario

    def calcular_imposto(self):
        valor_operacional = self.calcular_valor_operacional()
        return (valor_operacional * 0.03) / 100

    def calcular_valor_final(self):
        valor_operacional = self.calcular_valor_operacional()
        imposto = self.calcular_imposto()
        taxa_corretora = self.taxa_corretora
        if self.compra_venda == "VENDA":
            valor_final = valor_operacional - taxa_corretora - imposto
        elif self.compra_venda == 'COMPRA':
            valor_final = valor_operacional + taxa_corretora + imposto
        else:
            print('Opção inválida! Digite novamente.')
        return valor_final


class ControleInvestimentos:
    def __init__(self):
        self.investimentos = []

    def adicionar_investimento(self):
        print('Digite o valor abaixo considerando QUATRO LETRAS com UM ou DOIS NÚMEROS:')
        codigo = input("Digite o código do investimento: ").upper()
        data = input("Digite a data do investimento (no formato dd/mm/aaaa): ")
        quantidade = int(input("Digite a quantidade do investimento: "))
        print('Digite o valor abaixo com duas casas decimais:')
        valor_unitario = float(
            input("Digite o valor unitário do investimento: "))
        compra_venda = input("Operação de compra ou venda? ").upper()
        print('Digite o valor abaixo com duas casas decimais:')
        taxa_corretora = float(input("Digite a taxa de corretagem: "))

        investimento = Investimento(codigo, data, quantidade, valor_unitario, compra_venda, taxa_corretora)
        self.investimentos.append(investimento)
        print("Investimento adicionado com sucesso!")

    def remover_investimento(self):
        codigo = input("Digite o código do investimento que deseja remover: ").upper()
        for investimento in self.investimentos:
            if investimento.codigo == codigo:
                self.investimentos.remove(investimento)
                print("Investimento removido com sucesso!")
                return
        print("Investimento não encontrado.")

    def visualizar_todos_investimentos(self):
        for investimento in self.investimentos:
            print("Lista de investimentos:")
            print(f'''
            Código: {investimento.codigo}
            Data: {investimento.data}
            Quantidade: {investimento.quantidade}
            Valor unitário: R$ {investimento.valor_unitario:.2f}
            Compra ou venda: {investimento.compra_venda}
            Taxa de corretagem: R$ {investimento.taxa_corretora:.2f}
            Valor final: R$ {investimento.calcular_valor_final():.2f}
            ''')  
            return
        print('Não há nenhum investimento registrado!')

    def visualizar_investimento_especifico(self):
        codigo = input(
            "Digite o código do investimento que deseja visualizar: ").upper()
        for investimento in self.investimentos:
            if investimento.codigo == codigo:
                print(f"Código: {investimento.codigo}")
                print(f"Data: {investimento.data}")
                print(f"Quantidade: {investimento.quantidade}")
                print(f"Valor unitário: R$ {investimento.valor_unitario:.2f}")


controle = ControleInvestimentos()

while True:
    print('''

    --------------MENU---------------
    1. Adicionar novo investimento
    2. Remover investimento
    3. Visualizar todos os investimentos
    4. Visualizar investimento específico
    0. Sair
    ---------------------------------
    
    ''')

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        controle.adicionar_investimento()
    elif opcao == "2":
        controle.remover_investimento()
    elif opcao == "3":
        controle.visualizar_todos_investimentos()
    elif opcao == "4":
        controle.visualizar_investimento_especifico()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")
