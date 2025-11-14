import streamlit as st
import matplotlib.pyplot as plt
import os

st.title("Construis ta pyramide !")

# --- Inputs utilisateur ---
volume_pierre = st.slider(
    "Quel volume de pierre pour construire l'extérieur de ta pyramide ? (en milliers de m3)",
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

# --- Logique du choix d'image ---
if volume_pierre < 60:
    image = "no_pyramide.jpeg"
elif volume_pierre > 80:
    image = "no_money.jpeg"
else:
    if type_roche == "Granite":
        image = "marteau_casse.jpeg"
    elif type_roche == "Grès":
        image = "tas_de_sable.jpg"
    else:
        if methode_extrac == "Explosifs":
            image = "carr_dest.jpeg"
        elif methode_extrac == "Dragage":
            image = "pas_eau.jpeg"
        else:
            image = "bravo.jpeg"

# --- Affichage des résultats ---
st.write(f"Votre volume de pierre : {volume_pierre} milliers de m3")
st.write(f"Type de roche choisi : {type_roche}")
st.write(f"Méthode d'extraction : {methode_extrac}")

# Vérifier que l'image existe
img_path = os.path.join("model", image)
if os.path.exists(img_path):
    img = plt.imread(img_path)
    plt.imshow(img)
    plt.axis("off")
    st.pyplot(plt)
else:
    st.warning(f"Image {image} introuvable dans le dossier 'model/'.")
