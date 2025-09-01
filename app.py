import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="DDoS Classifier", layout="centered")

st.title("🚨 DDoS Attack Detection App")
st.markdown("Upload a network traffic CSV file to classify it as **Benign** or **DDoS Attack**.")

# File uploader
uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

# Show working directory and files
st.write("📂 Current working directory:", os.getcwd())
st.write("📄 Files in this folder:", os.listdir())

if uploaded_file is not None:
    try:
        # ✅ Force-safe model path (works no matter where you run)
        model_path = os.path.join(os.path.dirname(__file__), "ddos_xgb_model.pkl")

        if not os.path.exists(model_path):
            st.error(f"❌ Model file not found at: `{model_path}`")
        else:
            model = joblib.load(model_path)

            # ✅ Load uploaded CSV and preprocess
            df = pd.read_csv(uploaded_file)
            # 🧼 Strip leading/trailing spaces in column names
            df.columns = df.columns.str.strip()


            # 🧼 Remove unwanted extra columns that aren't in training data
            columns_to_drop = ['Flow Bytes/s', 'Flow Packets/s', 'SimillarHTTP']
            for col in columns_to_drop:
               if col in df.columns:
                    df.drop(col, axis=1, inplace=True)

            original_df = df.copy()
            df = df.select_dtypes(include=['number'])  # Keep only numeric

            # ✅ Predict
            predictions = model.predict(df)
            result_df = original_df.copy()
            result_df['Prediction'] = predictions
            result_df['Prediction Label'] = result_df['Prediction'].map({0: "🟢 Benign", 1: "🔴 DDoS Attack"})

            # ✅ Display results
            st.success("✅ Prediction completed successfully!")
            st.write("### 🧾 Prediction Results:")
            st.dataframe(result_df[['Prediction Label']])

            # ✅ Download CSV
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Prediction Results", csv, "ddos_predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error loading model or processing data:\n\n{e}")
