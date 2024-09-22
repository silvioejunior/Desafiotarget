#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;
texto = input("Digite uma string: ")
texto_invertido = ""
tamanho = len(texto)
i = tamanho - 1
while i >= 0:
    texto_invertido += texto[i]  
    i -= 1  
print("String invertida:", texto_invertido)