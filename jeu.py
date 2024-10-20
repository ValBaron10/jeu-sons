import streamlit as st
from PIL import Image

# Dossier contenant les sons et les images
SONS_DIR = "./sons"
IMAGES_DIR = "./images"

# Liste des sons et des images (avec .wav)
sons = ["son1.wav", "son2.wav", "son3.wav", "son4.wav", "son5.wav"]
images = ["boton-de-oro.jpg", "chisco.jpg", "tordo-matorral.jpg", "tortolita.jpg", "colibri.jpg"]

# Dictionnaire pour associer les sons aux images
associations = {
    "son1.wav": "tortolita.jpg",
    "son2.wav": "boton-de-oro.jpg",
    "son3.wav": "colibri.jpg",
    "son4.wav": "tordo-matorral.jpg",
    "son5.wav": "chisco.jpg"
}

# Fonction pour afficher le mini-jeu
def mini_jeu():
    st.title("A vous de jouer ! Associez le son à la photo !")

    # Initialise l'état du jeu
    if 'son_index' not in st.session_state:
        st.session_state.son_index = 0
        st.session_state.correct_answers = 0

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

    # Affiche le son actuel
    son = sons[st.session_state.son_index]
    print(st.session_state.son_index)
    son_path = SONS_DIR + "/" + son
    st.audio(son_path)

    # Affiche les images
    st.write("Regardez bien les images suivantes (vous pouvez les agrandir !) :")
    image_cols = st.columns(len(images))

    for col, image in zip(image_cols, images):
        img_path = IMAGES_DIR + "/" + image
        img = Image.open(img_path)
        img = img.rotate(-90, expand=True)
        col.image(img, caption=image, use_column_width=True)

    # Sélection de l'image associée
    choix_image = st.selectbox("Sélectionnez le nom de l'image que vous pensez associée au son :", images)
    
    # Vérification de l'association
    if st.button("Vérifier"):
        if associations[son] == choix_image:
            st.success("Bravo ! Vous avez fait la bonne association.")
            st.session_state.correct_answers += 1

            # Lien vers plus d'informations sur le chisco
            if associations[son] == "chisco.jpg":
                st.write("Si vous voulez en savoir plus sur le chisco, allez voir ce lien : [Chisco](https://ebird.org/species/lotmoc1)")

            # Lien vers plus d'informations sur le boton de oro
            if associations[son] == "boton-de-oro.jpg":
                st.write("Si vous voulez en savoir plus sur le boton de oro, allez voir ce lien : [Boton de oro](https://ebird.org/species/saffin)")

            # Lien vers plus d'informations sur le tordo de matorral
            if associations[son] == "tordo-matorral.jpg":
                st.write("Si vous voulez en savoir plus sur le Tordo de Matorral, allez voir ce lien : [Tordo de Matorral](https://ebird.org/species/scrbla1)")

            # Lien vers plus d'informations sur le colibri
            if associations[son] == "colibri.jpg":
                st.write("Si vous voulez en savoir plus sur le colibri de vientre rufo, allez voir ce lien : [Colibri](https://ebird.org/species/amahum1)")

            # Lien vers plus d'informations sur la tortolita
            if associations[son] == "tortolita.jpg":
                st.write("Si vous voulez en savoir plus sur la Tortolita Peruana, allez voir ce lien : [Tortolita](https://ebird.org/species/crgdov1)")
        else:
            st.error("Dommage ! Ce n'est pas la bonne association.")


# Exécution de l'application
if __name__ == "__main__":
    mini_jeu()