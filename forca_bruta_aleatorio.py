import numpy as np
import time

inicio = time.time() # Inicio do tempo de execução

# Função para gerar a matriz aleatória
def matriz_genarator():
    try: 
        n = int(input("Digite o tamanho da matriz quadrada (n x n): ")) # Solicitar ao usuário o tamanho da matriz
    except ValueError:
        print("Por favor, insira um número inteiro válido.") # Informar erro caso o valor inserido não seja um inteiro
        exit(1)

    p = np.random.randint(-127, 128, size=(n, n), dtype=np.int64) # Gerar matriz aleatória com valores entre -127 e 127
    print(f"Matriz lida do arquivo ({n}x{n}):") 
    print(p) # Exibir a matriz gerada
    return p # Retornar a matriz gerada

# Função para encontrar o subretângulo de soma máxima usando força bruta
def maximo_subretangulo(p):
    m = p.shape[0] # Obtém o tamanho da matriz
    
    max_soma = float('-inf') # Infinito negativo para garantir que qualquer soma será maior
    
    # Itera sobre todas as combinações possíveis de linhas e colunas
    for linha1 in range(m):
        for linha2 in range(linha1, m):
            for coluna1 in range(m):
                for coluna2 in range(coluna1, m):
                    soma_momento = 0 
                    # Calcula a soma do sub-retângulo definido pelas linhas e  colunas atuais 
                    for i in range(linha1, linha2 + 1):
                        for j in range(coluna1, coluna2 + 1):
                            soma_momento += p[i][j]
                    max_soma = max(max_soma, soma_momento)
    return max_soma

# Função de execução do programa
def main():
    matriz = matriz_genarator()
    resultado = maximo_subretangulo(matriz)
    fim = time.time()
    print("Tempo de execução: {:.6f} segundos".format(fim - inicio)) 
    print("Resultado do subretângulo de soma máxima:", resultado)

if __name__ == "__main__":
    main()

