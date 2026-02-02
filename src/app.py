# dashboard/app.py
"""
10 Academy Week 10 – Task 5: Interactive Dashboard
Forecasting Financial Inclusion in Ethiopia

Run with:
    streamlit run dashboard/app.py

Features:
- Overview: key metrics & current status
- Trends: historical time series + event markers
- Forecasts: baseline vs intervention scenarios with uncertainty
- Progress: toward NFIS-II / 60% target
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ────────────────────────────────────────────────
# Page config
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    page_icon="🇪🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ────────────────────────────────────────────────
# Simulated / hard-coded data (replace with real files later)
# ────────────────────────────────────────────────

# Historical account ownership (from enriched dataset + Findex)
historical_data = pd.DataFrame({
    'Year': [2014, 2017, 2021, 2024],
    'Ownership (%)': [22, 35, 46, 49],
    'Source': ['Findex 2014', 'Findex 2017', 'Findex 2021', 'Findex 2025']
})

# Forecast data (from Task 4 style output)
forecast_data = pd.DataFrame({
    'Year': [2025, 2026, 2027],
    'Baseline': [50.8, 52.1, 53.4],
    'Optimistic': [53.5, 56.8, 59.2],
    'Pessimistic': [49.0, 49.5, 50.0],
    'With Events (mid)': [52.6, 55.3, 57.9]
})

# Key metrics (latest known + short commentary)
metrics = {
    "Account Ownership (2024)": "49%",
    "Registered Digital Accounts (2025)": "~222 million",
    "Telebirr Users (Dec 2025)": "58.61 million",
    "Gender Gap (2024)": "15 pp (Men 57% – Women 42%)",
    "P2P vs ATM": "P2P transfers surpassed ATM withdrawals"
}

# Simple event timeline (for annotation)
events = [
    {"year": 2021, "event": "Telebirr launch", "impact": "Mobile money surge"},
    {"year": 2023, "event": "M-Pesa entry", "impact": "Competition begins"},
    {"year": 2024, "event": "Fayda rollout acceleration", "impact": "Digital ID push"},
    {"year": 2025, "event": "Interoperability milestone", "impact": "P2P dominance"}
]

# ────────────────────────────────────────────────
# Sidebar – Controls
# ────────────────────────────────────────────────
st.sidebar.title("Controls & Scenarios")

show_events = st.sidebar.checkbox("Show key events on charts", value=True)
scenario = st.sidebar.radio(
    "Forecast Scenario",
    ["Baseline (trend only)", "With Events (intervention)", "Optimistic", "Pessimistic"],
    index=1
)

target_2030 = st.sidebar.slider("NFIS-II aspirational target (%)", 50, 80, 60, step=5)

st.sidebar.markdown("---")
st.sidebar.info("Data last enriched: Jan 31, 2026\n\nForecasts are illustrative due to sparse historical points.")

# ────────────────────────────────────────────────
# Main Page – Tabs
# ────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Trends", "🔮 Forecasts", "🎯 Progress"])

# ────────────────────────────────────────────────
# Tab 1: Overview
# ────────────────────────────────────────────────
with tab1:
    st.header("Financial Inclusion Overview – Ethiopia 2026")

    cols = st.columns(4)
    for i, (title, value) in enumerate(metrics.items()):
        with cols[i % 4]:
            st.metric(title, value)

    st.markdown("""
    ### Current Situation (early 2026)
    - Account ownership grew only **+3 pp** (46% → 49%) between 2021–2024 despite explosive registration numbers.
    - **>220 million** digital accounts registered, but active usage remains shallow (mostly P2P).
    - Persistent **15 pp gender gap** and low merchant/wage/bill-pay adoption.
    - Key opportunity: convert registrations into active usage via infrastructure (Fayda, agents, interoperability).
    """)

    st.caption("Sources: Global Findex 2025, Ethio Telecom H1 2025/26, NBE / Shega reports")

# ────────────────────────────────────────────────
# Tab 2: Trends
# ────────────────────────────────────────────────
with tab2:
    st.header("Historical Trends & Events")

    # Line chart – Account Ownership
    fig_trend = px.line(
        historical_data,
        x='Year',
        y='Ownership (%)',
        markers=True,
        title="Account Ownership Rate (Findex waves)",
        labels={'Ownership (%)': 'Account Ownership (%)'}
    )

    fig_trend.update_traces(line=dict(width=2.8), marker=dict(size=10))

    # Add event annotations
    if show_events:
        for ev in events:
            fig_trend.add_vline(x=ev['year'], line_dash="dot", line_color="red", opacity=0.5)
            fig_trend.add_annotation(
                x=ev['year'], y=48,
                text=ev['event'],
                showarrow=True,
                arrowhead=1,
                ax=20,
                ay=-30,
                font=dict(size=11)
            )

    fig_trend.update_layout(
        height=500,
        xaxis_title="Year",
        yaxis_title="Account Ownership (%)",
        yaxis_range=[15, 55],
        hovermode="x unified"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

    st.markdown("""
    **Key observation**: Growth slowed dramatically after 2021 despite major product launches (Telebirr 2021, M-Pesa 2023).  
    Infrastructure and activation efforts appear more promising drivers.
    """)

# ────────────────────────────────────────────────
# Tab 3: Forecasts
# ────────────────────────────────────────────────
with tab3:
    st.header("Forecasts 2025–2027")

    # Select which scenario line to emphasize
    if scenario == "Baseline (trend only)":
        main_line = 'Baseline'
        color_main = 'gray'
    elif scenario == "With Events (intervention)":
        main_line = 'With Events (mid)'
        color_main = 'darkgreen'
    elif scenario == "Optimistic":
        main_line = 'Optimistic'
        color_main = 'teal'
    else:
        main_line = 'Pessimistic'
        color_main = 'darkred'

    fig_forecast = go.Figure()

    # Historical
    fig_forecast.add_trace(go.Scatter(
        x=historical_data['Year'],
        y=historical_data['Ownership (%)'],
        mode='lines+markers',
        name='Observed',
        line=dict(color='navy', width=2.8),
        marker=dict(size=10)
    ))

    # Forecast lines
    for col, col_color, dash in [
        ('Baseline', 'gray', 'dash'),
        ('With Events (mid)', 'darkgreen', 'solid'),
        ('Optimistic', 'teal', 'dashdot'),
        ('Pessimistic', 'darkred', 'dot')
    ]:
        fig_forecast.add_trace(go.Scatter(
            x=forecast_data['Year'],
            y=forecast_data[col],
            mode='lines+markers',
            name=col,
            line=dict(color=col_color, dash=dash, width=2.2 if col != main_line else 3.5),
            marker=dict(size=9 if col != main_line else 11)
        ))

    # NFIS target line
    fig_forecast.add_hline(
        y=target_2030,
        line_dash="dot",
        line_color="red",
        annotation_text=f"NFIS-II target ({target_2030}%)",
        annotation_position="top right",
        annotation_font_size=12
    )

    fig_forecast.update_layout(
        title=f"Account Ownership Forecast – {scenario} scenario emphasized",
        xaxis_title="Year",
        yaxis_title="Account Ownership (%)",
        height=580,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis_range=[40, max(70, target_2030 + 5)]
    )

    st.plotly_chart(fig_forecast, use_container_width=True)

    st.markdown(f"""
    **Selected scenario**: **{scenario}**  
    Projected range by 2027: **{forecast_data[main_line].iloc[-1]:.1f}%** (mid-point)
    """)

# ────────────────────────────────────────────────
# Tab 4: Progress toward target
# ────────────────────────────────────────────────
with tab4:
    st.header("Progress Toward Inclusion Targets")

    latest = historical_data['Ownership (%)'].iloc[-1]
    gap_to_target = target_2030 - latest

    cols = st.columns([1, 2])
    with cols[0]:
        st.metric(
            "Current Ownership (2024)",
            f"{latest}%",
            delta=None
        )
        st.metric(
            f"Gap to {target_2030}% target",
            f"+{gap_to_target:.1f} pp needed",
            delta=None,
            delta_color="off"
        )

    with cols[1]:
        fig_progress = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=latest,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"Account Ownership vs {target_2030}% Target"},
            delta={'reference': target_2030, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
            gauge={
                'axis': {'range': [0, 80]},
                'bar': {'color': "navy"},
                'steps': [
                    {'range': [0, 40], 'color': "lightgray"},
                    {'range': [40, target_2030], 'color': "lightblue"},
                    {'range': [target_2030, 80], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': target_2030
                }
            }
        ))

        fig_progress.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_progress, use_container_width=True)

    st.markdown("""
    **Interpretation**  
    Reaching **60%** would require an average **~3.7 pp/year** increase from 2025–2030 — significantly faster than the recent +1 pp/year trend.  
    Optimistic event-driven scenarios could make this feasible; baseline trend alone is not sufficient.
    """)

# ────────────────────────────────────────────────
# Footer
# ────────────────────────────────────────────────
st.markdown("---")
st.caption("Dashboard built for 10 Academy Week 10 Challenge – February 2026 | Data last updated Jan 31, 2026")