import streamlit as st
import os
from crew_logic import UsineOda
import base64

# --- FONCTION MAGIQUE DE CONVERSION BASE64 (ÉLIMINE LES BUGS D'URL) ---
def extraire_image_locale(chemin_relatif):
    chemin_absolu = os.path.join(os.path.dirname(__file__), chemin_relatif)
    if os.path.exists(chemin_absolu):
        with open(chemin_absolu, "rb") as fichier_image:
            encodage = base64.b64encode(fichier_image.read()).decode()
            return f"data:image/jpeg;base64,{encodage}"
    # Image de secours si le fichier est introuvable
    return "https://unsplash.com"

# --- CONVERSION DES COMPOSANTS EN BASE64 ---
FOND_GLOBAL = extraire_image_locale("images/a.jpg")
IMG_NOBUNAGA = extraire_image_locale("images/nobunaga.jpeg")
IMG_HIDEYOSHI = extraire_image_locale("images/hideyoshi.jpeg")
IMG_SHIBATA = extraire_image_locale("images/shibata.jpeg")
IMG_AKECHI = extraire_image_locale("images/akechi.jpeg")

st.set_page_config(page_title="Le Clan d'IA Oda", layout="wide")

# --- 2. LE CORE CSS COMPATIBLE VERCEL & STYLE GAMING EASYTECH ---
css_style = f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(10, 15, 30, 0.92), rgba(5, 5, 15, 0.98)), url('{FOND_GLOBAL}');
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Cinzel', 'Georgia', serif;
        color: #f0f4f8;
    }}
    .epic-title {{
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        color: #f39c12;
        text-shadow: 0px 0px 20px rgba(243, 156, 18, 0.6), 3px 3px 0px #000000;
        letter-spacing: 5px;
        margin-top: -30px;
    }}
    .gold-tier-card {{
        /* Le dégradé protège le texte à gauche (foncé) et s'efface totalement à droite (transparent) */
        background: linear-gradient(to right, rgba(15, 23, 42, 0.98) 0%, rgba(15, 23, 42, 0.9) 25%, rgba(15, 23, 42, 0) 40%), url('{IMG_NOBUNAGA}');
        background-size: cover;
        background-position: center right; /* Aligne l'illustration de Nobunaga vers la droite */
        border: 3px solid #f39c12; /* Bordure OR EasyTech */
        border-radius: 12px;
        padding: 35px;
        box-shadow: 0px 0px 30px rgba(243, 156, 18, 0.4);
        transition: all 0.3s ease;
        max-width: 650px;
        margin: 0 auto 40px auto;
    }}
    .gold-tier-card:hover {{
         transform: translateY(-5px);
        box-shadow: 0px 0px 45px rgba(243, 156, 18, 0.7);
        border-color: #f1c40f;
    }}
    /* 🛡️ CARTES PURPLE TIER (Généraux - Version Éclatante) */
    .purple-tier-card {{
        background-size: cover;
        background-position: center top;
        border: 2px solid #8e44ad; /* Bordure VIOLETTE EasyTech */
        border-radius: 10px;
        padding: 25px 15px;
        text-align: center;
        min-height: 280px;
        box-shadow: 0px 0px 20px rgba(142, 68, 173, 0.3);
        transition: all 0.3s ease;
    }}
    .purple-tier-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0px 0px 35px rgba(155, 89, 182, 0.7);
        border-color: #9b59b6;
    }}
    
    /* 
       L'astuce EasyTech : transparent en haut (0%) pour laisser les visages et armures 100% éclatants, 
       et fondu violet/sombre en bas (100%) uniquement sous le texte pour garder une lisibilité maximale.
    */
    .hideyoshi-bg {{ 
        background-image: linear-gradient(to bottom, rgba(15, 5, 25, 0) 0%, rgba(15, 5, 25, 0) 70%, rgba(35, 15, 50, 0.98) 100%), url('{IMG_HIDEYOSHI}'); 
    }}
    .shibata-bg   {{ 
        background-image: linear-gradient(to bottom, rgba(15, 5, 25, 0) 0%, rgba(15, 5, 25, 0) 70%, rgba(35, 15, 50, 0.98) 100%), url('{IMG_SHIBATA}'); 
    }}
    .akechi-bg    {{ 
        background-image: linear-gradient(to bottom, rgba(15, 5, 25, 0) 0%, rgba(15, 5, 25, 0) 70%, rgba(35, 15, 50, 0.98) 100%), url('{IMG_AKECHI}'); 
    }}

    .tier-label-gold {{ font-size: 0.8rem; letter-spacing: 2px; color: #f1c40f; font-weight: bold; }}
    .tier-label-purple {{ font-size: 0.8rem; letter-spacing: 2px; color: #bb8fce; font-weight: bold; }}
    .general-name {{ font-size: 1.8rem; margin: 5px 0 15px 0; font-weight: bold; text-shadow: 2px 2px 4px #000000; }}

    .stButton>button {{
        background: linear-gradient(90deg, #c0392b 0%, #e74c3c 50%, #c0392b 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: 2px solid #f39c12 !important;
        box-shadow: 0px 0px 15px rgba(231, 76, 60, 0.4) !important;
    }}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown("<h1 class='epic-title'>🏯 CONSEIL DE GUERRE ODA</h1>", unsafe_allow_html=True)

# 1. Affichage de Nobunaga Oda (Gold Tier)
st.markdown(f"""
<div class='gold-tier-card'>
    <div class='tier-label-gold'>★ ★ ★ GOLD TIER GENERAL</div>
    <div class='general-name'>NOBUNAGA ODA</div>
    <p style='color:#bdc3c7; font-size:0.95rem; line-height:1.5;'>
        Orchestrateur Suprême & Second Cerveau du système. Il analyse votre décret en langage naturel pour assigner l'ordre de bataille idéal.
    </p>
</div>
""", unsafe_allow_html=True)

# 2. Affichage des 3 lieutenants (Purple Tier)
col1, col2, col3 = st.columns(3)

with col1:
    hideyoshi_on = st.checkbox("Déployer Hideyoshi", value=True)
    if hideyoshi_on:
        st.markdown(f"""
        <div class='purple-tier-card hideyoshi-bg'>
            <div class='tier-label-purple'>PURPLE TIER</div>
            <div class='general-name'>HIDEYOSHI</div>
            <p style='font-size:0.85rem; color:#ccc;'>
                Division Frontend (React / Flutter). Conçoit et assemble les structures visuelles de vos interfaces utilisateur.
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    shibata_on = st.checkbox("Déployer Shibata", value=True)
    if shibata_on:
        st.markdown(f"""
        <div class='purple-tier-card shibata-bg'>
            <div class='tier-label-purple'>PURPLE TIER</div>
            <div class='general-name'>SHIBATA</div>
            <p style='font-size:0.85rem; color:#ccc;'>
                Division Backend & Bases de Données. Gère la force algorithmique (Python, Scikit-Learn) et architecture l'infrastructure de données (SQL/NoSQL).
            </p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    akechi_on = st.checkbox("Déployer Akechi", value=True)
    if akechi_on:
        st.markdown(f"""
        <div class='purple-tier-card akechi-bg'>
            <div class='tier-label-purple'>PURPLE TIER</div>
            <div class='general-name'>AKECHI</div>
            <p style='font-size:0.85rem; color:#ccc;'>
                Division Embarquée & IoT. Soumet et manipule le matériel physique à l'aide de MicroPython et de scripts Arduino.
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- CONFIGURATION API & DÉPLOYEMENT ---
st.markdown("<br>", unsafe_allow_html=True)
with st.sidebar:
    st.markdown("### 🎛️ ACCÈS TACTIQUE")
    cle_api = st.text_input("Sceau Clé API OpenRouter", type="password")
    modele = st.selectbox("Modèle Tactique", ["openrouter/openrouter/free", "openrouter/anthropic/claude-3.5-sonnet"])

ordre = st.text_area("📜 Écrivez votre décret impérial :",
                     placeholder="Ex: Crée une API et une table SQL pour suivre le niveau d'eau de ma bonbonne...")

if st.button("🪓 DÉPLOYER LES ARMÉES"):
    if not cle_api:
        st.error("Seigneur, le sceau API manque à l'appel !")
    elif not ordre:
        st.warning("Le décret est vide.")
    else:
        with st.spinner("⚔️ Les généraux tracent les plans de code..."):
            usine = UsineOda(cle_api, modele)
            rapport = usine.executer_strategie(ordre, hideyoshi_on, shibata_on, akechi_on)
            st.success("💥 Victoire ! Le parchemin stratégique est livré.")
            st.markdown(rapport)
