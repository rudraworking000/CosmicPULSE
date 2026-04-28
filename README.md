# 🔭 CosmicPulse: Solar System Data Visualization

[cite_start]**CosmicPulse** is a Python-powered data science project that transforms raw planetary data into stunning, interactive charts—making the scale and structure of our Solar System tangible and accessible[cite: 1, 2].

---

## 🚀 Project Overview
[cite_start]This project is an open-data science initiative that pulls publicly available planetary data from sources like **NASA** and transforms it into clear, comparative visualizations[cite: 4]. [cite_start]It is designed as a modular pipeline to help students, educators, and amateur astronomers connect with astronomical data through code[cite: 54, 56, 58].

### Core Parameters Analyzed:
* [cite_start]**Mass**: Visualizing the sheer scale of planets[cite: 6].
* [cite_start]**Gravity**: Understanding surface pull (m/s²)[cite: 7].
* [cite_start]**Temperature**: Mapping the non-linear heat story of the Solar System[cite: 8].
* [cite_start]**Distance**: Measuring orbital spacing from the Sun[cite: 9].
* [cite_start]**Orbit**: Comparing planetary "years" in Earth years[cite: 10].

---

## 🛠️ Built With
* [cite_start]**Python**: Core logic and data processing[cite: 65].
* [cite_start]**Pandas**: Used for loading, structuring, and cleaning raw datasets[cite: 15, 16].
* [cite_start]**Matplotlib & Seaborn**: Used for foundational plots and aesthetic layering[cite: 18].
* **Streamlit**: Used to create the interactive web dashboard interface.

---

## 📈 Key Insights & "Expected Outputs"

### 1. Planetary Mass (Chapter 2)
[cite_start]Using a **logarithmic scale**, the project reveals Jupiter's overwhelming mass—more than 300 times that of Earth—without causing the smaller rocky planets to disappear from the chart[cite: 22, 23].

### 2. Surface Temperature vs. Distance
[cite_start]A scatter plot reveals the cooling trend of the planets but highlights **Venus as a dramatic outlier** due to its runaway greenhouse effect[cite: 27].

### 3. Kepler’s Third Law (Orbital Periods)
[cite_start]A line chart illustrates that the further a planet is, the dramatically longer its year is, contrasting Mercury's 88-day sprint with Neptune's 165-year orbit[cite: 33, 34].

### 4. Gravity Comparison
A vertical bar chart with an **Earth reference line (9.8 m/s²)** makes gravitational differences intuitive. [cite_start]It highlights that on Jupiter, you would weigh nearly 2.5× more[cite: 45, 46].

---

## 🏗️ The Pipeline
The project follows a modular 4-step workflow:
1. [cite_start]**Collect Data**: Gathering raw NASA datasets[cite: 53].
2. [cite_start]**Clean & Structure**: Processing data with Pandas[cite: 52].
3. [cite_start]**Visualize**: Rendering charts with Seaborn and Plotly[cite: 51].
4. [cite_start]**Interpret**: Adding scientific context and annotations[cite: 50].

---

## 📡 Open Science
[cite_start]Built entirely on publicly available NASA datasets, CosmicPulse is reproducible, verifiable, and ready to be extended to exoplanets or real-time space APIs[cite: 68, 70].
