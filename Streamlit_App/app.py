import streamlit as st
import numpy as np
import joblib

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="EstateIQ · Bengaluru Price Estimator",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== CSS — real-estate portal look ====================
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
    .stApp { background: #F4F6F8; }
    .block-container { padding-top: 1rem; max-width: 1100px; }

    /* Top nav */
    .navbar {
        background: #FFFFFF; border-radius: 14px; padding: 16px 26px;
        display:flex; align-items:center; justify-content:space-between;
        box-shadow: 0 2px 12px rgba(16,42,67,0.06); margin-bottom: 22px;
    }
    .brand { font-size: 24px; font-weight: 800; color: #0E7C86; letter-spacing:-0.5px; }
    .brand span { color:#F4796B; }
    .navlinks { color:#6B7C93; font-size:14px; font-weight:600; }
    .navlinks a { color:#6B7C93; margin-left:22px; text-decoration:none; }

    /* Hero */
    .hero {
        background: linear-gradient(120deg, #0E7C86 0%, #12A19A 100%);
        border-radius: 18px; padding: 40px 44px; color:#fff; margin-bottom: 26px;
        box-shadow: 0 10px 30px rgba(14,124,134,0.28);
    }
    .hero h1 { font-size: 38px; font-weight: 800; margin:0; }
    .hero p  { font-size: 16px; color:#DFF5F3; margin:8px 0 0 0; }

    /* Section card */
    .card {
        background:#FFFFFF; border-radius:16px; padding:26px 30px;
        box-shadow: 0 2px 14px rgba(16,42,67,0.07); margin-bottom: 20px;
    }
    .card h3 { color:#102A43; margin:0 0 4px 0; font-size:19px; }
    .muted { color:#8494A7; font-size:14px; }

    /* Listing result */
    .listing {
        background:#FFFFFF; border-radius:16px; overflow:hidden;
        box-shadow: 0 6px 26px rgba(16,42,67,0.12); border:1px solid #E4EAF0;
    }
    .listing-banner {
        background: linear-gradient(120deg, #0E7C86 0%, #12A19A 100%);
        padding: 26px 30px; color:#fff;
    }
    .listing-tag { background:rgba(255,255,255,0.2); display:inline-block; padding:4px 12px;
        border-radius:20px; font-size:12px; font-weight:700; letter-spacing:1px; margin-bottom:10px; }
    .listing-price { font-size:46px; font-weight:800; margin:0; }
    .listing-range { color:#DFF5F3; font-size:14px; margin-top:4px; }
    .listing-body { padding: 22px 30px; }

    /* feature pills */
    .pill {
        display:inline-block; background:#EAF6F5; color:#0E7C86; font-weight:700;
        padding:8px 16px; border-radius:24px; font-size:14px; margin:4px 8px 4px 0;
    }
    .stat-row { display:flex; gap:14px; margin-top:16px; }
    .stat {
        flex:1; background:#F7FAFC; border:1px solid #E4EAF0; border-radius:12px;
        padding:14px; text-align:center;
    }
    .stat b { color:#0E7C86; font-size:20px; display:block; }
    .stat small { color:#8494A7; font-size:12px; }

    div.stButton > button {
        background:#F4796B; color:#fff; font-weight:700; font-size:16px;
        border:none; border-radius:12px; padding:12px 0; width:100%; transition:.2s;
    }
    div.stButton > button:hover { background:#e8604f; transform:translateY(-1px); }

    label, .stSelectbox label, .stSlider label, .stNumberInput label { color:#334E68 !important; font-weight:600 !important; }
</style>
""", unsafe_allow_html=True)

# ==================== LOAD MODEL ====================
model = joblib.load('Model/house_price_model.pkl')
columns = joblib.load('Model/model_columns.pkl')
locations = sorted([c for c in columns if c not in ['total_sqft', 'bath', 'balcony', 'bhk']])

# ==================== NAVBAR ====================
st.markdown("""
<div class="navbar">
    <div class="brand">Estate<span>IQ</span></div>
    <div class="navlinks">Buy &nbsp;·&nbsp; Rent &nbsp;·&nbsp; Sell &nbsp;·&nbsp; <b style="color:#0E7C86;">Price Estimator</b></div>
</div>
""", unsafe_allow_html=True)

# ==================== HERO ====================
st.markdown("""
<div class="hero">
    <h1>Find the fair price of any home in Bengaluru</h1>
    <p>Instant AI-powered valuations, trained on 7,532 real property records.</p>
</div>
""", unsafe_allow_html=True)

# ==================== SEARCH / INPUT BAR ====================
st.markdown('<div class="card"><h3>🔎 Property Search</h3><p class="muted">Enter the property details to get an estimated market price.</p></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    location = st.selectbox("📍 Locality", locations)
with c2:
    total_sqft = st.number_input("📐 Built-up Area (sqft)", 300, 10000, 1200, 50)
with c3:
    bhk = st.selectbox("🛏️ Configuration (BHK)", [1, 2, 3, 4, 5, 6], index=1)

c4, c5, c6 = st.columns([1, 1, 1])
with c4:
    bath = st.slider("🛁 Bathrooms", 1, 10, 2)
with c5:
    balcony = st.slider("🌿 Balconies", 0, 5, 1)
with c6:
    st.markdown("<br>", unsafe_allow_html=True)
    predict = st.button("Estimate Price →")

# ==================== RESULT ====================
if predict:
    x = np.zeros(len(columns))
    x[columns.get_loc('total_sqft')] = total_sqft
    x[columns.get_loc('bath')] = bath
    x[columns.get_loc('balcony')] = balcony
    x[columns.get_loc('bhk')] = bhk
    if location in columns:
        x[columns.get_loc(location)] = 1

    price = model.predict([x])[0]
    low, high = price * 0.90, price * 1.10
    pps = (price * 100000) / total_sqft
    # rough EMI: 80% loan, 8.5% annual, 20 yrs
    P = price * 100000 * 0.80
    r = 0.085 / 12
    n = 20 * 12
    emi = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

    st.markdown(f"""
    <div class="listing">
        <div class="listing-banner">
            <div class="listing-tag">ESTIMATED MARKET VALUE</div>
            <p class="listing-price">₹ {price:,.2f} Lakhs</p>
            <p class="listing-range">Fair price range: ₹ {low:,.1f} L — ₹ {high:,.1f} L</p>
        </div>
        <div class="listing-body">
            <span class="pill">🛏️ {bhk} BHK</span>
            <span class="pill">🛁 {bath} Bath</span>
            <span class="pill">🌿 {balcony} Balcony</span>
            <span class="pill">📐 {total_sqft:,} sqft</span>
            <span class="pill">📍 {location}</span>
            <div class="stat-row">
                <div class="stat"><b>₹ {pps:,.0f}</b><small>per sqft</small></div>
                <div class="stat"><b>₹ {price/bhk:,.1f} L</b><small>per bedroom</small></div>
                <div class="stat"><b>₹ {emi:,.0f}</b><small>est. monthly EMI*</small></div>
            </div>
            <p class="muted" style="margin-top:14px;">*Indicative EMI: 80% loan, 8.5% p.a., 20-year tenure. For illustration only.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="card" style="text-align:center; padding:44px;"><div style="font-size:46px;">🏙️</div><p class="muted" style="margin-top:8px;">Fill in the details above and click <b>Estimate Price</b> to see the valuation.</p></div>', unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown('<p class="muted" style="text-align:center; margin-top:24px;">EstateIQ · Powered by a Random Forest model (R² = 0.74) · Built by Khushi Yadav, AIML Internship 2026, MNNIT Allahabad</p>', unsafe_allow_html=True)