import matplotlib.pyplot as plt                                                                                 #bibliotheque pr graph mathematiques

cm=float(input("Quelle est la concentration initiale "))                                                        #float : 
vm=float(input("Quel est le volume initial "))

def graph(cm,vm):

    while(True):
        try:
            i=int(input("Combien de valeurs voulez-vous tracer "))
            if (i>0):
                break
        except(ValueError):
            pass
        print("Valeur incorrecte, veuillez choisir une valeur positive")

    lv=[vm+va for va in range(0,i)] #si = 2, on veut lv'2 = [vm,vm+1,vm+2]

    lc=[cm*vm/vphi for vphi in lv] #si 2e boucle : on veut lc'2 = [cm*vm/vm,cm*vm/(vm+1),cm*vm/(vm+2)]

    plt.title("Concentration fille en fonction d'un volume fille ")
    plt.xlabel("Volume fille ")
    plt.ylabel("Concentration fille ")
    plt.grid(True)
    plt.plot(lv,lc)
    plt.show()

graph(cm,vm)

#def calculconcentration(cm,vm):
#    vphi=input("Quel est le volume final ")
#    if vphi=="":
#        cphi=input("Quel est la concentration finale ")
#        if cphi=="":
#            print("Valeur incorrecte, veuillez choisir une valeur positive")
#        else:
#            cphi=float(cphi) 
#            vphi=(cm*vm/cphi)   
#            print("Le volume final est ",vphi)
#            print("Le volume de solution ajoute est ")
#    else: 
#        vphi=float(vphi)
#        cphi=(cm*vm/vphi)
#        print("La concentration finale est ",cphi)
#
## fonction qui marche mais tu dois imput au moins 3 trucs sinon print : calculconcentration(cm,vm)

