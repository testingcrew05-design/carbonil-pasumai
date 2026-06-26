import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Carbonil Pasumai 2.0",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/leaf.png", width=70)
    st.title("Carbonil Pasumai 2.0")
    st.caption("AI Driven Carbon Registry & MRV Platform")

    st.divider()

    st.success("✅ Hackathon MVP")

    st.markdown("### Navigation")
    st.info("""
Use the **Pages** menu above to navigate.

📊 Dashboard

🧮 Carbon Calculator

🌿 Blue Carbon Registry

📈 Industry Benchmark

🤖 AI Advisor

🔍 MRV Verification

⛓ Blockchain

💰 Carbon Credits

🛒 Marketplace

📜 Certificates
""")

# -----------------------------
# Main Page
# -----------------------------

st.title("🌱 Carbonil Pasumai 2.0")

st.subheader(
    "AI Driven Carbon Calculator Integrated with Blockchain for Blue Carbon Registry & MRV System"
)

st.write("---")

col1, col2 = st.columns([2,1])

with col1:

    st.markdown("""
## 🌍 Vision

Carbonil Pasumai 2.0 is an AI-powered sustainability platform that helps:

- 🏭 Industries
- 🌿 NGOs
- 🏫 Educational Institutions
- 🌊 Coastal Communities
- 🏛 Government Agencies

monitor emissions, generate carbon credits, verify projects through blockchain, and support India's Net Zero 2070 mission.
""")

with col2:

    st.metric("Registered Projects", "18")
    st.metric("Carbon Credits", "2,450")
    st.metric("Blockchain Verified", "18")
    st.metric("AI Accuracy", "97.8%")

st.write("---")

st.header("🚀 Platform Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### 🌿 Blue Carbon

✔ Mangrove Registry

✔ Wetland Registry

✔ Seagrass Registry
""")

with c2:
    st.info("""
### 🤖 Artificial Intelligence

✔ Carbon Calculator

✔ AI Advisor

✔ Industry Benchmark

✔ Emission Prediction
""")

with c3:
    st.warning("""
### ⛓ Blockchain

✔ Smart Verification

✔ Carbon Credits

✔ Marketplace

✔ Certificates
""")

st.write("---")

st.header("📈 Carbon Credit Workflow")

st.markdown("""
1️⃣ Register Project

⬇

2️⃣ Upload Carbon Data

⬇

3️⃣ AI Carbon Calculation

⬇

4️⃣ Industry Benchmark Comparison

⬇

5️⃣ MRV Verification

⬇

6️⃣ Blockchain Validation

⬇

7️⃣ Carbon Credit Generation

⬇

8️⃣ Marketplace Trading

⬇

9️⃣ Certificate Generation
""")

st.write("---")

st.header("🌎 Our Mission")

st.success("""
Empowering organizations with AI and Blockchain to create a transparent,
trustworthy, and scalable Blue Carbon ecosystem supporting India's Net Zero 2070 vision.
""")

st.write("---")

st.caption("Carbonil Pasumai 2.0 | Nimirndhu Nil Hackathon 2026")
