import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Agri-Systems Dynamics Engine", layout="wide")

st.title("Serverless System Dynamics Pipeline")
st.caption("Real-Time Agri-Systems Management & Environmental Conflict Simulation")

st.sidebar.header("System Dynamics Configuration")
selected_chain = st.sidebar.selectbox("Target Agri-System", ["Cross-Border Maize Logistics (Africa)", "Trans-Tasman Dairy Export", "Global Soybean Supply Chain"])
conflict_severity = st.sidebar.slider("Simulate Environmental Conflict Severity", 1.0, 5.0, 2.5)
run_simulation = st.sidebar.button("Initialize Causal Loop Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: AWS Telemetry -> Stock & Flow Vectorization -> Friction Index")

if run_simulation:
    st.subheader(f"Active System Dynamics Monitor: {selected_chain}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_throughput = col1.empty()
    metric_emissions = col2.empty()
    metric_friction = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(1717)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    throughput_flow = []
    friction_index = []
    
    base_throughput = 10000 
    
    for i in range(100):
        if i < 35:
            current_throughput = base_throughput + int(np.random.uniform(-100, 500))
            current_emissions = np.random.uniform(50.0, 60.0)
            current_friction = np.random.uniform(10.0, 25.0)
            status = "STABLE EQUILIBRIUM"
        elif i >= 35 and i < 65:
            current_throughput = base_throughput - int((i - 35) * (150 * conflict_severity)) + int(np.random.uniform(-500, 500))
            current_emissions = np.random.uniform(80.0, 100.0) + (conflict_severity * 5.0)
            current_friction = np.random.uniform(60.0, 85.0) + (conflict_severity * 2.0)
            status = "ENVIRONMENTAL CONFLICT"
        else:
            current_throughput = current_throughput + int(np.random.uniform(-200, 200))
            current_emissions = current_emissions - np.random.uniform(1.0, 5.0)
            current_friction = np.random.uniform(85.0, 99.0)
            status = "SYSTEM BOTTLENECK"
            
        throughput_flow.append(current_throughput)
        friction_index.append(current_friction)
        
        metric_throughput.metric("Supply Chain Throughput (Flow)", f"{current_throughput:,} Units", f"{(current_throughput - base_throughput):,} variance")
        metric_emissions.metric("Environmental Impact (Stock Accumulation)", f"{current_emissions:.1f} Index", "Rising")
        metric_friction.metric("Stakeholder Friction Index", f"{current_friction:.1f}%")
        
        if status == "ENVIRONMENTAL CONFLICT" or status == "SYSTEM BOTTLENECK":
            metric_status.metric("Causal Loop Status", status, "Negative Feedback Dominant")
        else:
            metric_status.metric("Causal Loop Status", status, "Balanced Flows")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=throughput_flow, mode='lines', name='Operational Throughput (Flow)', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=friction_index, mode='lines', name='Stakeholder Friction Index', yaxis='y2', line=dict(color='red', dash='dot')))
        
        fig.update_layout(
            title="Dynamic Agri-Systems Management: Supply Chain Flow vs Stakeholder Friction",
            xaxis=dict(title="High-Frequency Telemetry Timestamp"),
            yaxis=dict(title="Throughput Volume"),
            yaxis2=dict(title="Friction Index (%)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "ENVIRONMENTAL CONFLICT" and i == 35:
            log_placeholder.error(f"STAKEHOLDER ALERT: Environmental thresholds breached at {time_steps[i].strftime('%H:%M:%S')}. Cloud middleware mapping negative feedback loop. Causal parameters updating to reflect extreme friction.")
        elif status == "STABLE EQUILIBRIUM" and i % 5 == 0:
            log_placeholder.success(f"Log: Telemetry tick {i} ingested via serverless API. Stock and flow variables operating within harmonious systemic bounds.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless cloud pipeline successfully translated real-time telemetry into dynamic System Dynamics parameters, exposing environmental friction.")
else:
    st.info("Click 'Initialize Causal Loop Engine' in the sidebar to simulate high-frequency agri-systems data ingestion.")