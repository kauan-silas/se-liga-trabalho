#include <stdio.h>
#include <stdlib.h> // Para system("cls") ou system("clear") se necessário

// Função para calcular a idade
void calcular_idade() {
    int ano_nascimento, ano_atual = 2024, idade;
    printf("\nDigite o ano de nascimento (ex: 1990): ");
    if (scanf("%d", &ano_nascimento) != 1) {
        printf("\n❌ Entrada inválida. Por favor, digite um numero inteiro.\n");
        // Limpar o buffer de entrada apos um erro
        while (getchar() != '\n'); 
        return;
    }
    idade = ano_atual - ano_nascimento;
    printf("\n✅ A sua idade e: %d anos.\n", idade);
}

// Função para calcular o preço da compra
void calcular_compra() {
    int quantidade;
    float preco_unitario, total;
    
    printf("\nDigite a quantidade de itens comprados: ");
    if (scanf("%d", &quantidade) != 1) {
        printf("\n❌ Entrada invalida. Por favor, digite um numero inteiro para a quantidade.\n");
        while (getchar() != '\n');
        return;
    }
    
    printf("Digite o preco unitario do item (ex: 15.50): ");
    if (scanf("%f", &preco_unitario) != 1) {
        printf("\n❌ Entrada invalida. Por favor, digite um numero valido para o preco.\n");
        while (getchar() != '\n');
        return;
    }
    
    total = quantidade * preco_unitario;
    printf("\n✅ O preco total da compra e: R$ %.2f\n", total);
}

// Função principal do menu
int main() {
    int escolha;
    
    do {
        printf("\n");
        printf("==============================\n");
        printf("         MENU DE PROGRAMAS\n");
        printf("==============================\n");
        printf("1 - Calcular idade\n");
        printf("2 - Calcular preco da compra\n");
        printf("3 - Sair\n");
        printf("------------------------------\n");
        printf("Escolha uma opcao (1, 2 ou 3): ");
        
        // Limpar o buffer de entrada antes de ler a nova escolha
        while (getchar() != '\n');

        // Tentativa de ler a escolha
        if (scanf("%d", &escolha) != 1) {
            printf("\n⚠️ Opcao invalida. Por favor, escolha 1, 2 ou 3.\n");
            escolha = 0; // Força uma opção inválida para continuar o loop
            continue;
        }

        switch (escolha) {
            case 1:
                calcular_idade();
                break;
            case 2:
                calcular_compra();
                break;
            case 3:
                printf("\n👋 Programa encerrado. Obrigado!\n");
                break;
            default:
                printf("\n⚠️ Opcao invalida. Por favor, escolha 1, 2 ou 3.\n");
        }
    } while (escolha != 3);
    
    return 0;
}