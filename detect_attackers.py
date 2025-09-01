import streamlit as st
import pandas as pd
import plotly.express as px
import os
import platform
import subprocess

# ✅ Function to block IP using netsh (Windows only)
import subprocess
import streamlit as st


import subprocess


st.set_page_config(page_title="Live DDoS Suspect Analyzer", layout="wide")
st.title("🚨 Real-Time DDoS Suspect Analyzer")
st.markdown("Upload your captured PCAP CSV log file to detect suspicious IPs involved in potential DDoS attacks.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload PCAP CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Source' in df.columns and 'Destination' in df.columns:
        # Count how many times each IP appears as source
        ip_summary = df['Source'].value_counts().reset_index()
        ip_summary.columns = ['IP Address', 'Request Count']

        st.subheader("📊 Top Suspicious IPs (by frequency)")
        fig = px.bar(ip_summary.head(10), x='IP Address', y='Request Count', color='Request Count',
                     color_continuous_scale='reds')
        st.plotly_chart(fig, use_container_width=True)

        # Mark IPs by count
        def flag_ip(count):
            if count > 1000:
                return '🔴 High'
            elif count > 200:
                return '🟡 Medium'
            else:
                return '🟢 Low'

        ip_summary['Risk Level'] = ip_summary['Request Count'].apply(flag_ip)
        st.write("### 🔍 IP Risk Table")
        st.dataframe(ip_summary.head(20))
       
        # Save report
        st.download_button("📥 Download IP Risk Report", data=ip_summary.to_csv(index=False),
                           file_name="ddos_ip_report.csv", mime="text/csv")
    else:
        st.error("CSV must contain 'Source' and 'Destination' columns!")
