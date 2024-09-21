# le module pr les graphe
import matplotlib.pyplot as plt

# en gros ici tu demande a prendre les parametre
C_mere = float(input("Entrez la concentration mere : "))
V_mere = float(input("Entrez le volume mere : "))

def concentration_fille(C_mere, V_mere):
    # ici tu gere les deux axes tu graphe
    V_fille = [V_mere + v_ajouté for v_ajouté in range(0, 10)]
    C_fille = [(C_mere * V_mere) / v_fille for v_fille in V_fille]
    
    # ca c les petit truc tu peux mettre sur le graphe
    #plt.title("C fille en fonction de V fille")
    #plt.xlabel("Volume fille")
    #plt.ylabel("Concentration fille")
    #plt.grid(True)

    # ici ploit ca dessine et show ca affiche le graphe
    plt.plot(V_fille, C_fille)
    plt.show()

# juste appel a la fonction
concentration_fille(C_mere, V_mere)