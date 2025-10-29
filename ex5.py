usuarios = ["ana", "marcos", "julia123", "marco@3", "gabrielly 123"]

for usuario in usuarios:
    if not usuario:
        continue

    if any(letra.isspace() for letra in usuario):
        print(f"Ignorando '{usuario}', (contém espaços vazios)")
    else:
        print(f"Cadastrando usuário : {usuario}")