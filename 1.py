# 1. Crie três variáveis e atribua os valores a seguir: a=1, b=5.9 e c=‘teste’. A partir disso, retorne o tipo de cada uma das variáveis. 
a = 1 
b = 5.9
c = "teste"

print(type(a))
print(type(b))
print(type(c))

# 2. Calcular a quantidade de litros de combustível gasta numa viagem, utilizando-se um automóvel que faz 12Km por litro. 
# Para obter o cálculo, o usuário deverá fornecer o tempo gasto na viagem e a velocidade média durante a mesma. 
# Assim, será possível calcular a distância percorrida com a 
# fórmula: DISTÂNCIA <- TEMPO * VELOCIDADE. Tendo o valor da distância, calcule a quantidade de litros de combustível usada na viagem com a fórmula: 
# LITROS_USADOS <- DISTÂNCIA / 12. O programa deverá exibir os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros usada na viagem.

tempogasto = int(input("Digite o tempo gasto na viagem em horas: "))
velocidade = int(input("Digite a velocidade em km/h: "))
distancia = tempogasto*velocidade;

litros_usados = distancia/12

print("\nvelocidade Média:", velocidade, "km/h", "\nTempo Gasto:", tempogasto,"horas", "\nDistância Percorrida:", distancia, "km/h" "\nQuantidade de Litros usados:", litros_usados, "litros")

# 3. Receber uma temperatura em graus Fahrenheit (valor direto na variável) e 
# exibi-la convertida em graus Centígrados, com a fórmula: C <- (((F-32) * 5) / 9), onde F é a temperatura em Fahrenheit e C em Centígrados.

tempf = float(input("Digite o valor da temperatura em Fahreinheit: "))
tempc = ((tempf-32) * 5) /9
print("A temperatura convertida em graus centígrados é:", str(tempc) + "°C") # Descobri que não pode concatenar string com número então tive que transformar a temperatura em String

# 4. Calcular e exibir o valor do volume de uma lata de óleo, usando a fórmula: VOLUME <- 3.14159 * R * R * ALTURA.
altura = float(input("Digite o valor da altura da lata de óleo em cm: "))
r = float(input("Digite o valor do raio da lata de óleo em cm: "))
volume = 3.14159 * r * r * altura
print("O volume da lata de óleo é:", str(volume) + " cm^3")

# 5. Transformar dois valores A e B, efetuar a troca dos mesmos de forma que a variável A passe a ter o valor da variável B e vice-versa. Exibir os valores trocados.

a = input("Digite o valor da variável A: ") 
b = input("Digite o valor da variável B: ")
aa = a
bb = b
a = bb
b = aa

print("Valor de A:", a, "\nValor de B:", b) # Fiz variáveis "temporarias" que eu armazeno o valor delas e depois só atribuo os valores

# 6. Calcular o valor de uma prestação em atraso, usando a fórmula: PRESTAÇÃO <- VALOR + (VALOR * (TAXA / 100) * TEMPO).

valor = float(input("Digite o valor original da prestação em reais: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = int(input("Digite o tempo em meses: "))
prestacao = valor + (valor * (taxa/100) * tempo)
print("O valor da prestação em atraso é:", prestacao)

# 7. Uma loja petshop precisa de um programa para calcular os custos de criação de coelhos. O custo é calculado com a fórmula: CUSTO <- (NR_COELHOS * 0.70)
#/18 + 10. O programa deve atribuir o valor para a variável NR_COELHOS e exibir o valor da variável CUSTO.

nr_coelhos = int(input("Digite o número de coelhos: "))
custo = (nr_coelhos * 0.70) / 18 + 10
print("Os custos da criação de coelhos é R$:", custo)

# 8. Um funcionário recebe R$800,00 de salário e receberá um aumento de 15,8%. Implemente um algoritmo que calcule o novo salário do funcionário.
salario = 800.00
salario = salario + (salario*0.158)
print("O salário com o aumento de 15,8% é R$:", salario)