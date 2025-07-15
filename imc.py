def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Baixo peso"
    elif imc <= 24.9:
        return f"IMC: {imc:.2f} - Peso adequado"
    elif imc <= 29.9:
        return f"IMC: {imc:.2f} - Sobrepeso"
    elif imc <= 34.9:
        return f"IMC: {imc:.2f} - Obesidade grau I"
    elif imc <= 39.9:
        return f"IMC: {imc:.2f} - Obesidade grau II"
    else:
        return f"IMC: {imc:.2f} - Obesidade grau III"

while True:
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser maiores que zero. Tente novamente.")
            continue

        break
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")

resultado = calcular_imc(peso, altura)
print(resultado)