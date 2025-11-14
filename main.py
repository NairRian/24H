import streamlit as st
import matplotlib.pyplot as plt
import os

# configurer la page
apptitle = "Construis ta pyramide !"
st.set_page_config(page_title=apptitle, page_icon="🔺")
st.title("Construis ta pyramide 🔺 !")

# --- Inputs utilisateur ---

# LABEL PERSONNALISÉ POUR LE SLIDER
st.markdown("<p style='font-size:18px; font-weight:bold; text-align:center;'>"
            "Quel volume de pierre pour construire l'extérieur de ta pyramide ? (en milliers de m3)"
            "</p>", 
            unsafe_allow_html=True)

volume_pierre = st.slider(
    "",  # label retiré
    min_value=10,
    max_value=100,
    value=40
)


# LABEL PERSONNALISÉ POUR LA ROCHE
st.markdown("<p style='font-size:18px; font-weight:bold; text-align:center;'>"
            "Choisis le type de roche pour construire l'extérieur de ta pyramide"
            "</p>", 
            unsafe_allow_html=True)

type_roche = st.selectbox(
    "",
    ["Granite", "Calcaire", "Grès"]
)


# LABEL PERSONNALISÉ POUR LA MÉTHODE D'EXTRACTION
st.markdown("<p style='font-size:18px; font-weight:bold; text-align:center;'>"
            "Choisis la méthode d'extraction"
            "</p>", 
            unsafe_allow_html=True)

methode_extrac = st.selectbox(
    "",
    ["Explosifs", "Levage", "Dragage"]
)

# Créer trois colonnes pour centrer le bouton
col1, col2, col3 = st.columns([2, 2, 1])
with col2:
    submit = st.button("Soumettre données", key="submit")

# --- Affichage des résultats ---
if submit:
    # Expander pour afficher les résultats dans une mini-fenêtre
    with st.expander("Résultats de ta pyramide 🔺", expanded=True):

        # Logique du choix d'image
        if volume_pierre < 60:
            image = "no_pyramid.jpg"
        elif volume_pierre > 80:
            image = "no_money.jpg"
        else:
            if type_roche == "Granite":
                image = "marteau_casse.jpg"
            elif type_roche == "Grès":
                image = "tas_de_sable.jpg"
            else:
                if methode_extrac == "Explosifs":
                    image = "carr_dest.jpg"
                elif methode_extrac == "Dragage":
                    image = "pas_eau.jpg"
                else:
                    image = "bravo.jpg"

        # Affichage image
        img_path = os.path.join("model", image)
        if os.path.exists(img_path):
            fig, ax = plt.subplots()
            img = plt.imread(img_path)
            ax.imshow(img)
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning(f"Image {image} introuvable dans le dossier 'model/'.")

        # Texte de fin et lien
        if image != "bravo.jpg":
            st.markdown(
                "<h3 style='text-align:center; color:red;'>-10 points : Recommence !</h3>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<p class="big-link" style="text-align:center; margin-top: 20px;">'
                '<a href="https://nairrian.github.io/24H/" target="_blank">'
                'Clique ici pour accéder à ta carte de compétences !'
                '</a></p>',
                unsafe_allow_html=True
            )
