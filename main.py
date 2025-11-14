import streamlit as st
import matplotlib.pyplot as plt
import os

st.title("Construis ta pyramide !")

# --- Inputs utilisateur ---
volume_pierre = st.slider(
    f"Quel volume de pierre pour construire l'extérieur de ta pyramide ? (en milliers de m3)\n(min: 10, max: 100)",
    min_value=10,
    max_value=100,
    value=40
)

type_roche = st.selectbox(
    "Choisis le type de roche pour construire l'extérieur de ta pyramide",
    ["Granite", "Calcaire", "Grès"]
)

methode_extrac = st.selectbox(
    "Choisis la méthode d'extraction",
    ["Levage", "Dragage", "Explosifs"]
)

# --- Bouton centré et rouge ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit = st.button("Soumettre données", key="submit", help="Clique pour afficher les résultats")
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: red;
            color: white;
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

# --- Affichage des résultats ---
if submit:
    st.markdown("## Résultats de ta pyramide")

    # Logique du choix d'image
    if volume_pierre < 60:
        image = "no_pyramide.jpg"
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

    # Affichage centré avec texte en gras
    st.markdown(f"<p style='text-align:center;'>Votre volume de pierre : <b>{volume_pierre}</b> milliers de m3</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'>Type de roche choisi : <b>{type_roche}</b></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'>Méthode d'extraction : <b>{methode_extrac}</b></p>", unsafe_allow_html=True)

    # Affichage image centrée
    img_path = os.path.join("model", image)
    if os.path.exists(img_path):
        fig, ax = plt.subplots()
        img = plt.imread(img_path)
        ax.imshow(img)
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning(f"Image {image} introuvable dans le dossier 'model/'.")
