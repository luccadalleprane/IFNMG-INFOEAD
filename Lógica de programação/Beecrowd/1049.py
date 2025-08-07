# Entrada de Dados
animal1 = input().strip()
animal2 = input().strip()
animal3 = input().strip()

# Verifica o tipo de animal
if animal1 == "vertebrado":
    if animal2 == "ave":
        if animal3 == "carnivoro":
            print("aguia")
        elif animal3 == "onivoro":
            print("pomba")
    elif animal2 == "mamifero":
        if animal3 == "onivoro":
            print("homem")
        elif animal3 == "herbivoro":
            print("vaca")
elif animal1 == "invertebrado":
    if animal2 == "inseto":
        if animal3 == "hematofago":
            print("pulga")
        elif animal3 == "herbivoro":
            print("lagarta")
    elif animal2 == "anelideo":
        if animal3 == "hematofago":
            print("sanguessuga")
        elif animal3 == "onivoro":
            print("minhoca")
