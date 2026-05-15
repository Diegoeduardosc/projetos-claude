"""Calculadora CLI simples."""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def main():
    print("=== Calculadora CLI ===")
    print("Operações: + - * /")
    print("Digite 'sair' para encerrar\n")

    while True:
        entrada = input("Expressão (ex: 10 + 5): ").strip()
        if entrada.lower() == "sair":
            print("Até mais!")
            break

        try:
            partes = entrada.split()
            if len(partes) != 3:
                print("Formato inválido. Use: número operador número\n")
                continue

            a = float(partes[0])
            op = partes[1]
            b = float(partes[2])

            if op == "+":
                resultado = somar(a, b)
            elif op == "-":
                resultado = subtrair(a, b)
            elif op == "*":
                resultado = multiplicar(a, b)
            elif op == "/":
                resultado = dividir(a, b)
            else:
                print(f"Operador '{op}' não reconhecido.\n")
                continue

            print(f"Resultado: {resultado}\n")
        except ValueError as e:
            print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()
