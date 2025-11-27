import numpy as np
import time 

inicio = time.time() # Inicio do tempo de execução

def matriz_genarator(arquivo_dado):
    
    try: 
        with open(arquivo_dado, 'r') as f:# leitura do arquivo
            conteudo = f.read()
            linhas = conteudo.splitlines()
            try:
                n = int(linhas[0].strip()) #  Analisa o tamanho da matriz
            except (ValueError, IndexError):
                print(f"ERRO: o arquivo {arquivo_dado} não foi processado") # Informar erro caso o arquivo não seja processado
    
        dados = ' '.join(linhas[1:]).split()

        if len(dados) != n * n:
            print(f"ERRO: o elemento {n*n} não corresponde ao tamanho do arquivo") # Informar erro caso o tamanho do arquivo não corresponda ao esperado
            return None
        
        matriz = np.array(dados, dtype=np.int32).reshape(n,n)# Formatação da matriz
        print(f"Matriz lida do arquivo ({n}x{n}):") 
        #print("\n",matriz, "\n")
        return matriz # Retornar a matriz lida
        
    except FileNotFoundError:
        print(f"ERRO: o arquivo {arquivo_dado} não foi encontrado")# Informar erro caso o arquivo não seja encontrado
        exit(1)

# Função para calcular a soma máxima cruzada
def soma_cruzada(matriz, l1, l2, c1,c2, coluna_media, linha_media):  
   
    soma_max_e = float('-inf') #infinito negativo para garantir que qualquer soma será maior
    soma_momento_e = 0 #soma momentânea zerada
    # Soma para a esquerda da coluna média
    for i in range(coluna_media, c1 - 1, -1):
        soma_momento_e += matriz[linha_media][i]
        soma_max_e = max(soma_max_e, soma_momento_e)
    
    soma_max_d = float('-inf')
    soma_momento_d = 0
    # Soma para a direita da coluna média
    for j in range(coluna_media,  c2 + 1):
        soma_momento_d += matriz[linha_media][j]
        soma_max_d = max(soma_max_d, soma_momento_d)

    
    soma_max_c = float('-inf')
    soma_momento_c = 0
    
    # Soma para cima da linha média
    for k in range(linha_media, l1 - 1, -1):
        soma_momento_c += matriz[k][coluna_media]
        soma_max_c = max(soma_max_c, soma_momento_c)
    
    soma_max_b = float('-inf')  
    soma_momento_b = 0

    # Soma para baixo da linha média
    for m in range(linha_media, l2 + 1):
        soma_momento_b += matriz[m][coluna_media]
        soma_max_b = max(soma_max_b, soma_momento_b)
    
    # Retorna o máximo entre as somas cruzadas
    return max(soma_max_e + soma_max_d - matriz[linha_media][coluna_media],soma_max_c + soma_max_b - matriz[linha_media][coluna_media]) 
       

# Função principal de divisão e conquista
def soma_divisao_conquista(matriz, l1, l2, c1,c2):
    # Caso a submatriz seja inválida
    if l1 > l2 or c1 > c2:
        return float('-inf') 
     
    #Submatriz de tamanho 1x1
    if l1 == l2 and c1 == c2: 
        return matriz[l1][c1] 
    
    linha_media = l1 +  (l2 - l1) // 2 # Cálcula a linha média
    coluna_media = c1 + (c2 - c1) // 2 # Cálcula a coluna média
    

    r1 = soma_divisao_conquista(matriz, l1, linha_media, c1, coluna_media) # Quadrante superior esquerdo
    r2 = soma_divisao_conquista(matriz, l1, linha_media, coluna_media + 1, c2) # Quadrante superior direito
    r3 = soma_divisao_conquista(matriz, linha_media + 1, l2, c1, coluna_media) # Quadrante inferior esquerdo
    r4 = soma_divisao_conquista(matriz, linha_media + 1, l2, coluna_media + 1, c2) # Quadrante inferior direito
    r5 = soma_cruzada(matriz, l1, l2, c1, c2, coluna_media, linha_media) # Soma cruzada

    return max(r1, r2, r3, r4, r5) # Retorna o máximo entre os cinco resultados 


# Função de execução do programa
if __name__ == "__main__":
    arquivo_matriz = ["\\GB - subretangulo maximo\\in_out\\in5"] # Caminho do arquivo de entrada

    # Loop para ler o arquivo e processar a matriz
    for nome in arquivo_matriz:
        matriz_lida = matriz_genarator(nome) # Variavel que irá ler a matriz do arquivo
        
        if matriz_lida is not None:# Verifica se a matriz foi lida corretamente
            resultado = soma_divisao_conquista(matriz_lida, 0, matriz_lida.shape[0]-1, 0, matriz_lida.shape[1]-1) # Chama a função de divisão e conquista
            fim = time.time() # Fim do tempo de execução

            print("\nTempo de execução: {:.6f} segundos\n".format(fim - inicio)) # Imprime o tempo de execução
            print("Resultado do subretângulo de soma máxima:", resultado, "\n") # Imprime o resultado do subretângulo de soma máxima