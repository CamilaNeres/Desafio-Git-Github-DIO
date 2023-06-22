#O código em questão tem como objetivo calcular o diâmetro, a área e o perímetro de um círculo com base no valor do raio fornecido pelo usuário.


try:
    print("Bem-vindo! Este programa calcula o diâmetro, a área e o perímetro de um círculo.")
    entrada = input("Digite o valor do raio: ")
    raio = float(entrada)

    # Valor de pi
    pi = 3.14159

    # Cálculo do diâmetro
    diametro = 2 * raio

    # Cálculo da área
    area = pi * (raio ** 2)

    # Cálculo do perímetro
    perimetro = 2 * pi * raio

    # Exibição dos resultados com duas casas decimais
    print(f"Diametro: {diametro:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")

except ValueError:
    print("Entrada inválida. Digite um número.")
