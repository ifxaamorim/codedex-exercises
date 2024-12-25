# D2- Criar um sistema de ensino médio de quatro anos usando uma instrução if/ elif/ :else
grade = int (input("Insira sua nota: "))

if grade == 9:
    print("Freshman")
elif grade == 10:
    print ("Sophomore")
elif grade == 11:
    print("Junior")
elif grade == 12:
    print("Senior")
else:
    print("TBD")