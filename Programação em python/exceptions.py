try:
    nome = "Lucas Lima"
    for caractere in nome:
        if "0" <= caractere <= "9":
            raise ValueError("O nome nao pode conter números.")
        print(f"Noem digitado: {nome}")
except ValueError as e:
    print(f"Erro: {e}")
finally:
    print("Exemplo completo de utilizacao \ do tratamento de excecoes.")