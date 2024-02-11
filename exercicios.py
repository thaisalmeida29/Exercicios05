# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números      

def encontrarPares():
    for num in range(1,21):
        if num % 2 == 0:
         print(num)
encontrarPares()
    

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def string(str):
    print(str)
minha_string = "Olá mundo".upper()
string(minha_string)

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def lista(parametro1, parametro2, parametro3, parametro4):
    lis.append(5)
    lis.append(6)
    print(lis)
lis = [1,2,3,4]
lista(1,2,3,4)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def minha_funcao(arg1, *lista_de_elementos):
    print("Argumento formal:", arg1)
    print("Lista de elementos:", lista_de_elementos)

minha_funcao("Chamada 1")
minha_funcao("Chamada 2", 2, 4, 6, 8)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

soma = lambda x, y: x + y
resultado = soma(3, 5)
print("Resultado da soma:", resultado)

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
celsius_para_fahrenheit = lambda c: (c * 9/5) + 32
Fahrenheit = map(celsius_para_fahrenheit, Celsius)
print (list(Fahrenheit))

# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
minha_lista = [x**2 for x in range(1,11) if x % 2 == 0]
print(minha_lista)

# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
palavras_com_a = [palavra for palavra in palavras if 'a' in palavra.lower()]
print(palavras_com_a)


# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10
lista_numeros = [lista_numero for lista_numero in range(1,11) if lista_numero < 5]
print(lista_numeros)


