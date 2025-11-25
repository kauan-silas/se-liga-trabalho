def calcular_idade():
    """Calcula a idade a partir do ano de nascimento."""
    try:
        ano_nascimento = int(input("Digite o ano de nascimento (ex: 1990): "))
        ano_atual = 2024  # Supondo o ano atual como 2024
        idade = ano_atual - ano_nascimento
        print(f"\n✅ A sua idade é: {idade} anos.")
    except ValueError:
        print("\n❌ Entrada inválida. Por favor, digite um número inteiro.")

def calcular_compra():
    """Calcula o preço total de uma compra com base na quantidade e preço unitário."""
    try:
        quantidade = int(input("Digite a quantidade de itens comprados: "))
        preco_unitario = float(input("Digite o preço unitário do item (ex: 15.50): "))
        total = quantidade * preco_unitario
        print(f"\n✅ O preço total da compra é: R$ {total:.2f}")
    except ValueError:
        print("\n❌ Entrada inválida. Certifique-se de digitar números válidos.")

def menu():
    """Exibe o menu e gerencia as opções do usuário."""
    while True:
        print("\n" + "="*30)
        print("         MENU DE PROGRAMAS")
        print("="*30)
        print("1 - Calcular idade")
        print("2 - Calcular preço da compra")
        print("3 - Sair")
        print("-"*30)
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        
        if escolha == '1':
            calcular_idade()
        elif escolha == '2':
            calcular_compra()
        elif escolha == '3':
            print("\n👋 Programa encerrado. Obrigado!")
            break
        else:
            print("\n⚠️ Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Chama a função principal do menu
if __name__ == "__main__":
    menu()


    // Importa a biblioteca para ler a entrada do usuário de forma síncrona
const readline = require('readline-sync');

function calcularIdade() {
    /** Calcula a idade a partir do ano de nascimento. */
    const anoNascimentoStr = readline.question("Digite o ano de nascimento (ex: 1990): ");
    const anoNascimento = parseInt(anoNascimentoStr);
    const anoAtual = 2024;
    
    if (isNaN(anoNascimento)) {
        console.log("\n❌ Entrada inválida. Por favor, digite um número inteiro.");
        return;
    }
    
    const idade = anoAtual - anoNascimento;
    console.log(`\n✅ A sua idade é: ${idade} anos.`);
}

function calcularCompra() {
    /** Calcula o preço total de uma compra com base na quantidade e preço unitário. */
    const quantidadeStr = readline.question("Digite a quantidade de itens comprados: ");
    const precoUnitarioStr = readline.question("Digite o preco unitario do item (ex: 15.50): ");
    
    const quantidade = parseInt(quantidadeStr);
    const precoUnitario = parseFloat(precoUnitarioStr);
    
    if (isNaN(quantidade) || isNaN(precoUnitario)) {
        console.log("\n❌ Entrada inválida. Certifique-se de digitar números válidos.");
        return;
    }
    
    const total = quantidade * precoUnitario;
    console.log(`\n✅ O preco total da compra é: R$ ${total.toFixed(2)}`);
}

function menu() {
    /** Exibe o menu e gerencia as opções do usuário. */
    let escolha = '';
    
    while (escolha !== '3') {
        console.log("\n" + "=".repeat(30));
        console.log("         MENU DE PROGRAMAS");
        console.log("=".repeat(30));
        console.log("1 - Calcular idade");
        console.log("2 - Calcular preco da compra");
        console.log("3 - Sair");
        console.log("-".repeat(30));
        
        escolha = readline.question("Escolha uma opcao (1, 2 ou 3): ");
        
        switch (escolha) {
            case '1':
                calcularIdade();
                break;
            case '2':
                calcularCompra();
                break;
            case '3':
                console.log("\n👋 Programa encerrado. Obrigado!");
                break;
            default:
                console.log("\n⚠️ Opcao invalida. Por favor, escolha 1, 2 ou 3.");
        }
    }
}

// Chama a função principal do menu
menu();