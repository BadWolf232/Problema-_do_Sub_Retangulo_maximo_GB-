import numpy as np
import time 


inicio = time.time()# Inicio do tempo de execução

def matriz_genarator(arquivo_dado):
    try: 
        with open(arquivo_dado, 'r') as f: # leitura do arquivo
            conteudo = f.read()
            linhas = conteudo.splitlines()
            try:
                n = int(linhas[0].strip()) # Analisa o tamanho da matriz
            except (ValueError, IndexError):
                print(f"ERRO: o arquivo {arquivo_dado} não foi processado") # Informar erro caso o arquivo não seja processado
    
        dados = ' '.join(linhas[1:]).split()

        if len(dados) != n * n:
            print(f"ERRO: o elemento {n*n} não corresponde ao tamanho do arquivo")# Informar erro caso o tamanho do arquivo não corresponda ao esperado
            return None
        
        matriz = np.array(dados, dtype=np.int32).reshape(n,n) # Formatação da matriz
        print(f"Matriz lida do arquivo ({n}x{n}):")
        #print("\n",matriz, "\n")
        return matriz # Retornar a matriz lida
        
    except FileNotFoundError:
        print(f"ERRO: o arquivo {arquivo_dado} não foi encontrado")  # Informar erro caso o arquivo não seja encontrado
        exit(1)

   
# Função para encontrar o sub-retângulo de soma máxima
def maximo_subretangulo(matriz):
    n = matriz.shape[0] # Obtém o tamanho da matriz
    
    max_soma = float("-inf") # Infinito negativo para garantir que qualquer soma será maior
    
    # Itera sobre todas as combinações possíveis de linhas e colunas
    for linha1 in range(n):
        for linha2 in range(linha1, n):
            for coluna1 in range(n):
                for coluna2 in range(coluna1, n):
                    soma_momento = 0 
                    # Calcula a soma do sub-retângulo definido pelas linhas e  colunas atuais 
                    for i in range(linha1, linha2 + 1):
                        for j in range(coluna1, coluna2 + 1):
                            soma_momento += matriz[i][j] # Adiciona o valor do elemento atual à soma momentânea
                    max_soma = max(max_soma, soma_momento) # Atualiza a soma máxima se a soma momentânea for maior
    return max_soma # Retorna a soma máxima encontrada


# Função de execução do programa
if __name__ == "__main__":
    arquivo_matriz = ["\\GB - subretangulo maximo\\in_out\\in5"]# Caminho do arquivo de entrada
    
    # Loop para ler o arquivo e processar a matriz
    for nome in arquivo_matriz:
        matriz_lida = matriz_genarator(nome) # Variavel que irá ler a matriz do arquivo
        
        
        if matriz_lida is not None: # Verifica se a matriz foi lida corretamente
            resultado = maximo_subretangulo(matriz_lida)
            fim = time.time() # Fim do tempo de execução
            
            print("\nTempo de execução: {:.6f} segundos\n".format(fim - inicio)) # Imprime o tempo de execução  
            print("Resultado do subretângulo de soma máxima:", resultado, "\n")  # Imprime o resultado do subretângulo de soma máxima
            