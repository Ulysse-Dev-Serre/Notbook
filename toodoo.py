# Importation des bibliothèques nécessaires
# - tkinter : une bibliothèque standard en Python pour créer des interfaces graphiques.
# - os : une bibliothèque standard pour interagir avec le système d'exploitation (par exemple, pour vérifier l'existence d'un fichier).
import tkinter as tk
import os

# Chemin du fichier pour sauvegarder le contenu
# Ce fichier sera utilisé pour stocker le texte de la zone de saisie.
fichier_sauvegarde = "todo_sauvegarde.txt"

# Fonction pour charger le contenu du fichier
# Cette fonction vérifie si un fichier de sauvegarde existe. Si oui, elle ouvre le fichier, lit son contenu,
# puis insère ce contenu dans la zone de texte.
def charger_contenu():
    # Vérifie si le fichier de sauvegarde existe
    if os.path.exists(fichier_sauvegarde):
        # Ouvre le fichier en mode lecture avec encodage UTF-8
        with open(fichier_sauvegarde, "r", encoding="utf-8") as file:
            # Lit tout le contenu du fichier
            contenu = file.read()
            # Insère le contenu dans le widget texte à partir de la position "1.0" (ligne 1, colonne 0)
            texte.insert("1.0", contenu)

# Fonction pour sauvegarder le contenu du texte
# Elle récupère tout le texte du widget principal et l'enregistre dans un fichier.
def sauvegarder_contenu(event=None):
    # Ouvre le fichier en mode écriture, ce qui écrase le contenu existant
    with open(fichier_sauvegarde, "w", encoding="utf-8") as file:
        # Récupère le texte du widget (de la première position "1.0" jusqu'à la fin)
        contenu = texte.get("1.0", tk.END).strip()  # .strip() pour supprimer les espaces inutiles
        # Écrit le contenu dans le fichier
        file.write(contenu)

# Fonction pour supprimer les parties de texte sélectionnées
# Si l'utilisateur a sélectionné une portion de texte, elle sera supprimée. Sinon, rien ne se passe.
def supprimer_selection(event=None):
    try:
        # Supprime le texte entre le début et la fin de la sélection actuelle
        texte.delete(tk.SEL_FIRST, tk.SEL_LAST)
    except tk.TclError:
        # En cas d'absence de sélection, une erreur Tcl est ignorée
        pass

# Fonction pour commencer le déplacement de la fenêtre
# Cette fonction vérifie si le clic a été effectué hors du widget texte
def commencer_deplacement(event):
    # Si le clic est à l'extérieur de la zone de texte, enregistrer la position pour le déplacement
    if event.widget != texte:  # Vérifie que l'élément cliqué n'est pas la zone de texte
        fenetre.x = event.x
        fenetre.y = event.y


# Fonction pour déplacer la fenêtre
# Elle met à jour la position de la fenêtre en fonction du mouvement du curseur.
def deplacer_fenetre(event):
    # Calcule la nouvelle position x et y en fonction du mouvement du curseur
    x = fenetre.winfo_pointerx() - fenetre.x
    y = fenetre.winfo_pointery() - fenetre.y
    # Applique les nouvelles coordonnées à la fenêtre
    fenetre.geometry(f"+{x}+{y}")

# Fonction pour fermer la fenêtre
# Cette fonction détruit l'objet fenêtre, ce qui termine l'application.
def fermer_fenetre():
    fenetre.destroy()

# Création de la fenêtre principale de l'application
fenetre = tk.Tk()  # Instanciation d'un objet Tkinter pour la fenêtre principale
fenetre.title("To-Do List")  # Définition du titre de la fenêtre
fenetre.attributes('-topmost', True)  # S'assure que la fenêtre reste toujours au-dessus des autres fenêtres

# Définition des dimensions initiales de la fenêtre
largeur = 600
hauteur = 400
fenetre.geometry(f"{largeur}x{hauteur}")  # Définit la largeur et la hauteur de la fenêtre

# Permet de redimensionner la fenêtre (horizontalement et verticalement)
fenetre.resizable(True, True)

# Personnalisation de l'apparence de la fenêtre
fenetre.configure(bg="#8b5e3c")  # Définition de la couleur d'arrière-plan de la fenêtre
fenetre.wm_attributes("-alpha", 0.9)  # Rend la fenêtre légèrement transparente (90% d'opacité)

# Création d'un canvas pour simuler une bordure autour du contenu
canvas = tk.Canvas(fenetre, bg="#8b5e3c", highlightthickness=0)
canvas.pack(padx=5, pady=5, fill="both", expand=True)  # Ajuste le canvas pour remplir tout l'espace

# Création de la zone principale de saisie de texte (Text Widget)
texte = tk.Text(
    canvas,  # Associé au canvas
    wrap="none",  # Désactive le retour automatique à la ligne
    bg="#1b3618",  # Couleur de fond (vert foncé)
    fg="#f8f1e5",  # Couleur du texte (blanc cassé)
    insertbackground="#f8f1e5",  # Couleur du curseur
    highlightthickness=2,  # Épaisseur des bordures
    highlightbackground="#8b5e3c",  # Couleur des bordures
    highlightcolor="#8b5e3c"  # Couleur des bordures lorsqu'elles sont en surbrillance
)
texte.pack(padx=10, pady=10, fill="both", expand=True)  # Ajuste le widget texte pour remplir tout l'espace

# Chargement du contenu précédemment sauvegardé (si disponible)
charger_contenu()

# Sauvegarde automatique du texte chaque fois qu'une touche est relâchée
texte.bind("<KeyRelease>", sauvegarder_contenu)

# Ajout d'un bouton pour fermer l'application
bouton_fermer = tk.Button(
    fenetre,
    text="Fermer",  # Texte du bouton
    command=fermer_fenetre,  # Action associée : fermeture de la fenêtre
    bg="#8b5e3c",  # Couleur de fond du bouton
    fg="#f8f1e5"  # Couleur du texte du bouton
)
bouton_fermer.pack(pady=5)  # Positionne le bouton avec un espacement vertical

# Liaison des touches "Backspace" et "Delete" pour supprimer une sélection
texte.bind("<BackSpace>", lambda event: supprimer_selection())
texte.bind("<Delete>", lambda event: supprimer_selection())

# Permet de déplacer la fenêtre en cliquant et glissant avec le bouton gauche
fenetre.bind("<Button-1>", commencer_deplacement)  # Enregistre la position initiale du clic
fenetre.bind("<B1-Motion>", deplacer_fenetre)  # Met à jour la position lors du déplacement

# Lancement de la boucle principale de l'application (affichage de la fenêtre)
fenetre.mainloop()
















