# Identificador de palíndromo

import re # Importa a biblioteca re para usar expressões regulares

def analisar(entrada):
    if entrada is None: # Verifica se a entrada é None
        return False # Retorna False se a entrada for None
    
    limpa = re.sub(r'[^a-zA-Z0-9]', '', entrada).lower() # Remove tudo que não for letra ou número e converte para minúsculas
    
    invertida = limpa[::-1] # Inverte a string usando fatiamento (slicing)
    
    return limpa == invertida # Retorna True se a string limpa for igual à string invertida

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    texto1 = "A sacada da casa de cadasa" # Define o primeiro texto a ser analisado
    texto2 = "Socorram-me, subi no ônibus em Marrocos" # Define o segundo texto a ser analisado

    print(f"Teste 1: {analisar(texto1)}") # Imprime o resultado da análise do primeiro texto
    print(f"Teste 2: {analisar(texto2)}") # Imprime o resultado da análise do segundo texto
