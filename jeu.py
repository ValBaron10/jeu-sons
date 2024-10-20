import streamlit as st
from PIL import Image

# Dossier contenant les sons et les images
SONS_DIR = "./sons"
IMAGES_DIR = "./images"

# Liste des sons et des images (avec .wav)
sons = ["son1.wav", "son2.wav", "son3.wav"]
images = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Dictionnaire pour associer les sons aux images
associations = {
    "son1.wav": "image1.jpg",
    "son2.wav": "image2.jpg",
    "son3.wav": "image3.jpg"
}

# Fonction pour afficher le mini-jeu
def mini_jeu():
    st.title("Mini-Jeu : Associe le son à la photo")

    # Initialise l'état du jeu
    if 'son_index' not in st.session_state:
        st.session_state.son_index = 0
        st.session_state.correct_answers = 0

    # Affiche le son actuel
    son = sons[st.session_state.son_index]
    son_path = SONS_DIR + "/" + son
    st.audio("./sons/son1.wav")

    # Affiche les images
    st.write("Choisissez l'image correspondante :")
    image_cols = st.columns(len(images))

    for col, image in zip(image_cols, images):
        img_path = IMAGES_DIR + "/" + image
        # img = Image.open(img_path)
        # col.image(img, caption=image, use_column_width=True)

    # Sélection de l'image associée
    choix_image = st.selectbox("Sélectionnez l'image associée :", images)
    
    # Vérification de l'association
    if st.button("Vérifier"):
        if associations[son] == choix_image:
            st.success("Bravo ! Vous avez fait la bonne association.")
            st.session_state.correct_answers += 1
        else:
            st.error("Dommage ! Ce n'est pas la bonne association.")

    # Bouton pour le son suivant
    if st.button("Son suivant"):
        st.session_state.son_index += 1

        # Réinitialiser l'index si tous les sons ont été joués
        if st.session_state.son_index >= len(sons):
            st.session_state.son_index = 0
            st.session_state.correct_answers = 0
            st.success("Tous les sons ont été joués. Recommençons !")

    # Barre de progression
    st.progress((st.session_state.son_index + 1) / len(sons))

# Exécution de l'application
if __name__ == "__main__":
    mini_jeu()