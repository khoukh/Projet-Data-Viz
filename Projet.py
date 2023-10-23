
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import seaborn as sns
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot

st.title('Projet Data Visualisation')

# URL de l'ensemble de données brutes GitHub
github_url = "https://github.com/tidyverse/ggplot2/raw/main/data-raw/diamonds.csv"

# Charger l'ensemble de données directement à partir de l'URL
@st.cache_data
def load_data():
    return pd.read_csv(github_url)

# Chargement des données
df = load_data()

# Affichaer les cinq premières lignes du DataFrame 'df' pour obtenir un aperçu initial des données
st.write("Aperçu des 5 premières lignes du dataset :")
st.write(df.head())


# Définir le style du graphique sur "white" et la palette de couleurs sur "plasma"
sns.set(style="white")
sns.set_palette("plasma")

# Titre et description
st.title("Prix du diamant par carat avec filtre de qualité de taille")
st.write("Explorer la relation entre le prix du diamant, le carat et la qualité de taille.")

# Options de filtrage
cut_options = st.multiselect("Select one or more cut types:", df['cut'].unique())

# Filtrer la DataFrame sur la base des coupes sélectionnées
filtered_df = df[df['cut'].isin(cut_options)]

# Créer un nuage de points
fig = px.scatter(filtered_df, x="carat", y="price", color="cut", title="Price vs Carat by Cut",color_discrete_sequence=px.colors.sequential.Plasma)

# Personnaliser la mise en page
fig.update_layout(xaxis_title="Carat", yaxis_title="Price")

# Afficher le nuage de points
st.plotly_chart(fig)

# Titre et description
st.title("Nuage de points 3D des diamants")
st.write("Explorez la relation entre les dimensions des diamants (x, y, z) avec un filtre de qualité de taille.")

# Options de filtrage
cut_options = st.multiselect("Select one or more cut types:", df['cut'].unique(), key="cut_filter")

# Filtrer le DataFrame sur la base des coupes sélectionnées
filtered_df = df[df['cut'].isin(cut_options)]

# Créer un nuage de points en 3D
fig = px.scatter_3d(filtered_df, x="x", y="y", z="z", color="cut", title="3D Scatter Plot of Diamonds",color_discrete_sequence=px.colors.sequential.Plasma)

# Personnaliser la mise en page
fig.update_layout(scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z"))

# Afficher le nuage de points en 3D
st.plotly_chart(fig)


st.title("Diagramme à barres empilées : Qualité de taille par Clarté avec filtre sur les carats")

# Filtre Carat
carat_min = st.slider("Minimum Carat", min_value=df["carat"].min(), max_value=df["carat"].max(), value=df["carat"].min())
carat_max = st.slider("Maximum Carat", min_value=df["carat"].min(), max_value=df["carat"].max(), value=df["carat"].max())

# Filtrer le DataFrame sur la base de la gamme de carats sélectionnée
filtered_df = df[(df["carat"] >= carat_min) & (df["carat"] <= carat_max)]

# Créer un diagramme à barres empilées
fig = px.bar(
    filtered_df,
    x="cut",
    color="clarity",
    labels={"cut": "Cut"},
    color_discrete_sequence=px.colors.sequential.Plasma,
)


# Personnaliser la mise en page
fig.update_xaxes(title_text="Cut")
fig.update_yaxes(title_text="Count")
fig.update_layout(barmode="stack")

# Afficher le diagramme à barres empilées
st.plotly_chart(fig)


