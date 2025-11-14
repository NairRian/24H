import streamlit as st
import matplotlib.pyplot as plt
import os

# ----------------------- CONFIG PAGE -----------------------
apptitle = "Construis ta pyramide !"
st.set_page_config(page_title=apptitle, page_icon="🔺")
st.title("Construis ta pyramide 🔺 !")

# ----------------------- STYLE GLOBAL -----------------------
st.markdown("""
    <style>
        /* Augmenter la police des labels */
        label, .stSlider, .stSelectbox div {
            font-size: 18px !important;
            color: black !important;
        }
        /* Agrandir la police du lien */
        .big-link a {
            font-size: 26px !important;
            font-weight: bold;
            color: #1E90FF !important;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------- INPUTS -----------------------
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
    ["Explosifs", "Levage", "Dragage"]
)

# ----------------------- BOUTON CENTRÉ -----------------------
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    submit = st.button("Soumettre données", key="submit")

# ----------------------- SCRIPT AUTO-SCROLL -----------------------
if submit:
    st.markdown(
        """
        <script>
            document.getElementById('resultats').scrollIntoView({behavior: 'smooth'});
        </script>
        """,
        unsafe_allow_html=True
    )

# ----------------------- RÉSULTATS -----------------------
if submit:

    # Ancre pour le scroll
    st.markdown("<div id='resultats'></div>", unsafe_allow_html=True)

    # Titre des résultats
    st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Résultats de ta pyramide 🔺</h2>",
                unsafe_allow_html=True)

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

    # ----------------------- IMAGE -----------------------
    img_path = os.path.join("model", image)
    if os.path.exists(img_path):
        fig, ax = plt.subplots()
        img = plt.imread(img_path)
        ax.imshow(img)
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning(f"Image {image} introuvable dans le dossier 'model/'.")

    # ----------------------- FEEDBACK & LIEN -----------------------
    if image != "bravo.jpg":
        st.markdown(
            "<h2 style='text-align: center; color:red;'>-10 points : Recommence !</h2>",
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
