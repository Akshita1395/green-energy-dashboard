import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Green Future Analytics Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -------------------------------
# Load Data (Cached)
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_energy.csv")

    # Remove aggregated data
    exclude = [
        'World','Asia','Europe','Africa','North America','South America','Oceania',
        'High-income countries','Upper-middle-income countries',
        'Lower-middle-income countries','Low-income countries',
        'European Union'
    ]
    df = df[~df['country'].isin(exclude)]

    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🔎 Filters")
countries = sorted(df['country'].unique())
selected_country = st.sidebar.selectbox("Select Country", countries)

filtered_df = df[df['country'] == selected_country].sort_values("year")

# -------------------------------
# Title Section
# -------------------------------
st.markdown("<h1 style='text-align:center;'>🌍 Green Future Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>Data-driven insights for <b>{selected_country}</b></p>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# KPI Cards
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🌱 Avg Renewable (%)", round(filtered_df['renewables_share_energy'].mean(), 2))
col2.metric("🔥 Avg CO₂", round(filtered_df['greenhouse_gas_emissions'].mean(), 2))
col3.metric("📅 Years", f"{int(filtered_df['year'].min())}-{int(filtered_df['year'].max())}")

st.markdown("---")

# -------------------------------
# Charts Section
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 CO₂ Emissions Trend")
    fig1 = px.line(
        filtered_df,
        x='year',
        y='greenhouse_gas_emissions',
        color_discrete_sequence=['#ff4b4b']
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("⚡ Renewable Energy Growth")
    fig2 = px.line(
        filtered_df,
        x='year',
        y='renewables_share_energy',
        color_discrete_sequence=['#00cc96']
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# -------------------------------
# Advanced Scatter Plot
# -------------------------------
st.subheader("📊 Renewable vs CO₂ Relationship")

fig3 = px.scatter(
    filtered_df,
    x="renewables_share_energy",
    y="greenhouse_gas_emissions",
    color="year",
    size="renewables_share_energy",
    hover_name="year",
    title=f"Impact of Renewable Energy on Emissions ({selected_country})",
    template="plotly_white"
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# -------------------------------
# Insights Section
# -------------------------------
st.subheader("💡 Key Insights")

avg_renewable = df.groupby("country")["renewables_share_energy"].mean()
top_country = avg_renewable.idxmax()
top_value = avg_renewable.max()

highest_emission = df.groupby("country")["greenhouse_gas_emissions"].mean().idxmax()

col1, col2 = st.columns(2)

with col1:
    st.success(f"🌱 {top_country} has the highest renewable adoption ({top_value:.2f}%).")

with col2:
    st.error(f"🔥 {highest_emission} has the highest carbon emissions.")

st.markdown("---")

# -------------------------------
# ML Prediction
# -------------------------------
st.subheader("🔮 CO₂ Emission Prediction")

ml_df = filtered_df[['renewables_share_energy', 'year', 'greenhouse_gas_emissions']].dropna()

if len(ml_df) > 5:
    X = ml_df[['renewables_share_energy', 'year']]
    y = ml_df['greenhouse_gas_emissions']

    model = LinearRegression()
    model.fit(X, y)

    col1, col2 = st.columns(2)

    with col1:
        renew = st.slider(
            "Renewable Energy (%)",
            0.0, 100.0,
            float(ml_df['renewables_share_energy'].iloc[-1])
        )

    with col2:
        year = st.number_input("Year", 2000, 2050, value=2030)

    prediction = model.predict([[renew, year]])[0]

    st.success(f"Predicted CO₂ Emissions: {prediction:.2f}")

else:
    st.warning("Not enough data for prediction.")

st.markdown("---")

# -------------------------------
# Footer
# -------------------------------
st.caption("Built with Streamlit | Data Analytics Project")