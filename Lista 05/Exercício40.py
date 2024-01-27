print("Calcule sua média.")
notA = float(input("Insira sua primeira nota: "))
notB = float(input("Insira sua segunda nota: "))

med = (notA + notB)/2

if med >= 7:
    print("Parabéns! \nVocê foi aprovado." ) 
elif med < 5:
    print("Você ficou em recuperação. \n                    :(")
else:
    print("Infelizmente você foi reprovado. \n                                :(")