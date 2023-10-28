def somme(T):
    S = 0
    for i in range(10):
        S += T[i]
    return S

def produit(T):
    p = 1
    for i in range(10):
        p *= T[i]
    return p

def moyenne(T):
    m = somme(T) / 10
    return m

def sign(T):
    positive_str = ""
    negative_str = ""

    for i in range(10):
        if T[i] > 0:
            positive_str += str(T[i]) + " "
        elif T[i] < 0:
            negative_str += str(T[i]) + " "

    print("Les éléments positifs sont :")
    print(positive_str)

    print("Les éléments négatifs sont :")
    print(negative_str)

T = []
for i in range(10):
    value = float(input("Entrer un réel : "))
    T.append(value)

print("La somme est", somme(T))
print("Le produit est", produit(T))
print("La moyenne est", moyenne(T))
sign(T)
