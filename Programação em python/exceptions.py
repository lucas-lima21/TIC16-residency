try:
    nome = "123"
    for caractere in nome:
        if "0" <= caractere <= "9":
            raise ValueError("O nome nao pode conter números.")
    print(f"Nome digitado: {nome}")
finally:
    print("Exemplo completo de utilizacao do tratamento de excecoes.")