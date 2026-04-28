import streamlit as st
import pandas as pd
import plotly.express as px

# 🪐 CosmicPulse Project Branding [cite: 1, 2]
st.set_page_config(page_title="CosmicPulse | Solar System Viz", layout="wide")

# Custom Styling for "Attractive" UI
st.markdown("""
    <style>
    .main { background-color: #0b0d11; color: white; }
    h1, h2, h3 { color: #b8f241 !important; font-family: 'sans-serif'; }
    .stMarkdown { font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- Chapter 1: The Data Behind the Planets [cite: 11, 12] ---
data = {
    "Planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Mass": [0.33, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102], # 10^24 kg [cite: 14]
    "Gravity": [3.7, 8.87, 9.8, 3.72, 24.8, 10.4, 8.87, 11.2], # m/s^2 [cite: 36-43]
    "Temp": [167, 464, 15, -65, -110, -140, -195, -200], # Mean Temp °C [cite: 30]
    "Distance": [57.9, 108.2, 149.6, 228.0, 778.5, 1433.5, 2872.5, 4495.1], # 10^6 km [cite: 14]
    "Orbit": [0.24, 0.62, 1.0, 1.88, 11.86, 29.45, 84.02, 164.8] # Earth Years [cite: 33]
}
df = pd.DataFrame(data) [cite: 16]

st.title("🔭 CosmicPulse")
st.subheader("Transforming raw planetary data into stunning, interactive charts.") [cite: 2]

# --- Chapter 2: Comparing Planetary Mass [cite: 19, 20] ---
st.header("Chapter 2: Mass & Scale")
st.write("Jupiter's mass is more than 300 times that of Earth. We use a logarithmic scale to keep rocky planets visible.") [cite: 22, 23]
fig_mass = px.bar(df, x="Mass", y="Planet", orientation='h', log_x=True, 
                  color_discrete_sequence=['#b8f241'], template="plotly_dark")
st.plotly_chart(fig_mass, use_container_width=True)

# --- Chapter 3: Expected Output: Surface Temperature vs. Distance [cite: 25] ---
st.header("Chapter 3: The Non-Linear Heat Story") [cite: 26]
st.write("A clear cooling trend exists, but Venus is a dramatic outlier due to its greenhouse effect.") [cite: 27]
fig_temp = px.scatter(df, x="Distance", y="Temp", size="Mass", color="Planet",
                     hover_name="Planet", template="plotly_dark", 
                     title="Atmospheric Science Across the Solar System") [cite: 28]
st.plotly_chart(fig_temp, use_container_width=True)

# --- Chapter 4: Orbital Periods (Kepler's Law) [cite: 32, 33] ---
st.header("Chapter 4: Physics in Motion")
st.write("Neptune's orbit of 165 Earth years sits in stark contrast to Mercury's 88-day sprint.") [cite: 34]
fig_orbit = px.line(df, x="Planet", y="Orbit", markers=True, 
                    template="plotly_dark", title="Kepler's Third Law in Action") [cite: 33]
st.plotly_chart(fig_orbit, use_container_width=True)

# --- Gravity Insights [cite: 44] ---
st.header("How Heavy Would You Feel?") [cite: 44]
st.write("On Jupiter, you'd weigh nearly 2.5× more. On Mars, you'd feel feather-light at just 38% of Earth's pull.") [cite: 46]
fig_grav = px.bar(df, x="Planet", y="Gravity", color="Planet", template="plotly_dark")
fig_grav.add_hline(y=9.8, line_dash="dash", annotation_text="Earth Reference (9.8 m/s²)") [cite: 45, 47]
st.plotly_chart(fig_grav, use_container_width=True)
