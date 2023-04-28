def verificar_leite(pH):
    if 6.5 <= pH <= 6.7:
        return "O leite está adequado para consumo."
    else:
        return "O leite não está adequado para consumo."

pH = float(input("Digite o valor do pH do leite: "))
resultado = verificar_leite(pH)
print(resultado)
if resultado != "O leite está adequado para consumo.":
    acidez = (pH - 6.5) * 1000
    dornic = acidez / 0.085
    print(f"A acidez do leite é de {dornic:.2f} graus Dornic.")
