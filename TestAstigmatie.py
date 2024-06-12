import streamlit as st
import random
import matplotlib.pyplot as plt

# Fonction pour générer une couleur aléatoire
def generate_random_color():
    return [random.random() for _ in range(3)]

# Fonction pour afficher le graphique de couleurs
def show_color_graph():
    fig, ax = plt.subplots()
    color = generate_random_color()
    ax.plot([0, 1], [0, 1], color=color, linewidth=15)
    ax.axis('off')
    st.pyplot(fig)
    return color

# Fonction pour convertir une couleur RGB en hexadécimal
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(int(x*255) for x in rgb)

# Fonction pour évaluer la perception des couleurs
def evaluate_color_perception(displayed_color, selected_color):
    selected_rgb = tuple(int(selected_color.lstrip('#')[i:i+2], 16) / 255 for i in (0, 2, 4))
    score = 100 - sum(abs(d - s) for d, s in zip(displayed_color, selected_rgb)) * 100 / 3
    st.write(f"Votre score de perception des couleurs est : {score:.2f}/100")
    if score < 50:
        st.warning("Il se peut que vous ayez des difficultés avec la perception des couleurs. Veuillez consulter un spécialiste.")
    else:
        st.success("Votre perception des couleurs semble bonne.")

# Interface principale
def main():
    st.title("Test de Perception des Couleurs")
    st.write("Cliquez sur le bouton ci-dessous pour commencer le test.")
    if 'displayed_color' not in st.session_state:
        st.session_state['displayed_color'] = None
    
    if st.button("Commencer le Test"):
        st.session_state['displayed_color'] = show_color_graph()
    
    if st.session_state['displayed_color'] is not None:
        selected_color = st.color_picker("Choisissez la couleur affichée", "#000000")
        if st.button("Valider le choix"):
            evaluate_color_perception(st.session_state['displayed_color'], selected_color)

if __name__ == "__main__":
    main()