print("--------------------------------")
print("      CALCULADORA DO IMC        ")
print("--------------------------------")

Peso = float(input("Digite seu peso em kilos: "))

print("--------------------------------")

Altura = float(input("Digite sua altura em metros: "))

print("--------------------------------")

Imc = Peso/(Altura * Altura)

if Imc < 18.5:
    print("Seu iMC (", Imc,  ") está classificado como: MAGREZA")
    print("----------------------------")
    print("     FIM DA VERIFICAÇÃO     ")
    print("----------------------------")

elif Imc > 18.5  and Imc < 24.9:
    print("Seu iMC (", Imc,  ") está classificado como: NORMAL")
    print("----------------------------")
    print("     FIM DA VERIFICAÇÃO     ")
    print("----------------------------")

elif Imc > 25 and Imc < 29.9:
    print("Seu iMC (", Imc,  ") está classificado como: SOBRREPESO")
    print("----------------------------")
    print("     FIM DA VERIFICAÇÃO     ")
    print("----------------------------")

elif Imc > 30 and Imc < 39.9:
    print("Seu iMC (", Imc,  ") está classificado como: OBESIDADE 1")
    print("----------------------------")
    print("     FIM DA VERIFICAÇÃO     ")
    print("----------------------------")

else:
    print("Seu iMC (", Imc,  ") está classificado como: OBESIDADE 2")
    print("----------------------------")
    print("     FIM DA VERIFICAÇÃO     ")
    print("----------------------------")

