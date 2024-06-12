import tkinter as tk
from tkinter import messagebox, colorchooser
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fonction pour générer une couleur aléatoire
def generate_random_color():
    return [random.random() for _ in range(3)]

# Fonction pour afficher le graphique de couleurs
def show_color_graph():
    global displayed_color
    displayed_color = generate_random_color()
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], color=displayed_color, linewidth=15)
    ax.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Fonction pour convertir une couleur RGB en hexadécimal
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(int(x*255) for x in rgb)

# Fonction pour évaluer la perception des couleurs
def evaluate_color_perception():
    selected_color = colorchooser.askcolor()[0]
    if selected_color is None:
        return

    selected_color = [x/255 for x in selected_color]
    score = 100 - sum(abs(d - s) for d, s in zip(displayed_color, selected_color)) * 100 / 3
    message = f"Votre score de perception des couleurs est : {score:.2f}/100.\n"
    if score < 50:
        message += "Il se peut que vous ayez des difficultés avec la perception des couleurs. Veuillez consulter un spécialiste."
    else:
        message += "Votre perception des couleurs semble bonne."
    messagebox.showinfo("Résultat du test", message)

# Création de la fenêtre principale
window = tk.Tk()
window.title("Test de perception des couleurs")

# Ajouter des instructions
instructions = tk.Label(window, text="Cliquez sur le bouton ci-dessous pour générer des couleurs et tester votre perception.")
instructions.pack(pady=10)

# Ajouter un bouton pour afficher le graphique de couleurs
color_button = tk.Button(window, text="Afficher les couleurs", command=show_color_graph)
color_button.pack(pady=10)

# Ajouter un bouton pour évaluer la perception des couleurs
evaluate_button = tk.Button(window, text="Évaluer la perception", command=evaluate_color_perception)
evaluate_button.pack(pady=10)

# Lancer l'application
window.mainloop()