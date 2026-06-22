# Import the core Streamlit library for rendering the UI
import streamlit as st

# Configure the web application window properties
st.set_page_config(
    page_title="MATHlover - GCSE Mastery",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Define custom CSS styling to create a dopamine-driven, gamified dark theme environment
# This overrides default fonts, sets pulsing button graphics, and highlights reward tracks
st.markdown("""
    <style>
    /* Main app container styling with a premium deep purple space background */
    .stApp {
        background-color: #1A0B2E;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }
    
    /* Top global navigation bar configuration */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #2D124D;
        padding: 15px 30px;
        border-radius: 12px;
        margin-bottom: 25px;
        border-bottom: 3px solid #00F0FF;
    }
    
    /* App branding title styling */
    .brand-title {
        font-size: 24px;
        font-weight: 900;
        color: #CCFF00;
        letter-spacing: 1.5px;
    }
    
    /* Active and passive navigation links container */
    .nav-links {
        display: flex;
        gap: 20px;
    }
    .nav-item {
        color: #E0D5FA;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        padding: 5px 10px;
        transition: 0.2s;
    }
    .nav-item-active {
        color: #00F0FF;
        border-bottom: 2px solid #00F0FF;
        font-weight: 700;
    }
    
    /* Top header gamified streak display container */
    .streak-badge {
        background: linear-gradient(45deg, #FF4500, #FF8C00);
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        box-shadow: 0 0 10px rgba(255, 69, 0, 0.5);
    }
    
    /* Hero header text layout */
    .hero-title {
        font-size: 46px;
        font-weight: 800;
        text-align: center;
        margin-top: 20px;
        line-height: 1.2;
    }
    .hero-highlight {
        color: #CCFF00;
        background: linear-gradient(to right, #CCFF00, #00F0FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Main body copy descriptions */
    .hero-subtitle {
        font-size: 18px;
        text-align: center;
        color: #BDB2FF;
        max-width: 800px;
        margin: 15px auto 35px auto;
        line-height: 1.6;
    }
    
    /* Dopamine conversion component container for standardising user actions */
    .reward-box {
        background: linear-gradient(135deg, #2D124D 0%, #120621 100%);
        border: 2px solid #00F0FF;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.15);
        margin-bottom: 40px;
    }
    
    /* Text layout for standard section content headings */
    .section-header {
        font-size: 28px;
        font-weight: 700;
        color: #FFFFFF;
        border-left: 5px solid #CCFF00;
        padding-left: 15px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    
    /* Individual feature list layout boxes */
    .feature-card {
        background-color: #250F3E;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #00F0FF;
        margin-bottom: 15px;
    }
    .feature-card h4 {
        margin: 0 0 8px 0;
        color: #00F0FF;
    }
    .feature-card p {
        margin: 0;
        color: #E0D5FA;
        font-size: 15px;
    }
    
    /* Feature comparison layout matrix table structural configurations */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        background-color: #250F3E;
        border-radius: 12px;
        overflow: hidden;
    }
    th, td {
        padding: 15px;
        text-align: left;
        border-bottom: 1px solid #3D1B66;
    }
    th {
        background-color: #35165A;
        color: #CCFF00;
        font-weight: 700;
    }
    tr:hover {
        background-color: #2D124D;
    }
    .mathlover-row {
        color: #00F0FF;
        font-weight: bold;
    }
    
    /* Interactive lock state styling for premium access warnings */
    .lesson-teaser-box {
        background: linear-gradient(135deg, #3D1B66 0%, #1A0B2E 100%);
        border: 2px dashed #CCFF00;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin-top: 40px;
    }
    .timer-text {
        color: #FF8C00;
        font-weight: bold;
        font-family: monospace;
        font-size: 16px;
    }
    
    /* Global styles forcing Streamlit native buttons to conform to Neon Lime theme */
    div.stButton > button {
        background-color: #CCFF00 !important;
        color: #1A0B2E !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        padding: 12px 30px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(204, 255, 0, 0.4) !important;
        transition: transform 0.1s ease, box-shadow 0.1s ease !important;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 20px rgba(204, 255, 0, 0.6) !important;
        background-color: #D8FF33 !important;
    }
    div.stButton > button:active {
        transform: scale(0.98);
    }
    
    /* Custom secondary alternative cyan buttons style specification */
    .cyan-btn-container div.stButton > button {
        background-color: #00F0FF !important;
        color: #1A0B2E !important;
        box-shadow: 0 4px 15px rgba(0, 240, 255, 0.4) !important;
    }
    .cyan-btn-container div.stButton > button:hover {
        background-color: #33F3FF !important;
        box-shadow: 0 6px 20px rgba(0, 240, 255, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. TOP NAVIGATION BAR (STICKY HEADER) ---
# Custom raw HTML header to cleanly present navigation tabs without layout shifting
st.markdown("""
    <div class="nav-container">
        <div class="brand-title">MATHlover</div>
        <div class="nav-links">
            <a class="nav-item nav-item-active" href="#">Home</a>
            <a class="nav-item" href="#">Lessons</a>
            <a class="nav-item" href="#">Questions</a>
            <a class="nav-item" href="#">Notes</a>
        </div>
        <div class="streak-badge">5 Day Streak</div>
    </div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION (ABOVE THE FOLD) ---
# Displays primary brand messaging instantly when loading the homepage layout
st.markdown(
    '<h1 class="hero-title">Master GCSE Maths Without the Boredom. <br>'
    '<span class="hero-highlight">Powered by AI.</span></h1>', 
    unsafe_allow_html=True
)

st.markdown(
    '<p class="hero-subtitle">MATHlover turns painful algebra and geometry into an interactive game. '
    'Get step-by-step guidance, track your mistakes in real-time, and smash your target GCSE grades '
    'with a patient, personal AI tutor built directly into your dashboard.</p>', 
    unsafe_allow_html=True
)

# Dopamine Trigger Action Box: Instant claiming of daily reward multiplier
st.markdown("""
    <div class="reward-box">
        <h3 style="color: #00F0FF; margin-top:0;">Daily Reward Ready to Claim</h3>
        <p style="color: #E0D5FA; margin-bottom: 20px;">Claim your daily free lesson and secure plus 10 Experience Points to protect your streak status.</p>
    </div>
""", unsafe_allow_html=True)

# Columns structure to keep the main primary activation button centered cleanly
hero_left, hero_center, hero_right = st.columns([1, 2, 1])
with hero_center:
    if st.button("Claim Free Daily Lesson"):
        st.balloons()  # Visual screen celebration interaction loop triggering a dopamine micro-reward

# --- 3. CORE FEATURE DESCRIPTION BLOCKS ---
# Explains the specific application value propositions for GCSE students and teachers
st.markdown('<div class="section-header">How We Help You Conquer GCSE Maths</div>', unsafe_allow_html=True)

# Symmetrical multi-column card layout to outline product details cleanly
feat_col1, feat_col2 = st.columns(2)

with feat_col1:
    st.markdown("""
        <div class="feature-card">
            <h4>Syllabus Aligned Material</h4>
            <p>Our curriculum matches current Edexcel, AQA, and OCR exam specification boards down to the exact sub-topic module.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-card">
            <h4>Interactive Equation Scratchpad</h4>
            <p>Write out your formulas directly inside your interface windows. Our engine analyses exact step-by-step lines rather than scoring only your final answers.</p>
        </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown("""
        <div class="feature-card">
            <h4>Infinite Explanatory Patience</h4>
            <p>If an equation does not make sense, your AI companion instantly rewrites its approach using alternative graphics, real-world analogies, or simpler steps.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-card">
            <h4>Dynamic Workspace Generation</h4>
            <p>Practice modules update based entirely on automated logs monitoring your historic problem-solving mistakes and weak mathematical targets.</p>
        </div>
    """, unsafe_allow_html=True)

# Secondary clear call-to-action utilizing an alternative bright container theme color
st.markdown('<div class="cyan-btn-container">', unsafe_html=True)
demo_left, demo_center, demo_right = st.columns([1, 1.5, 1])
with demo_center:
    if st.button("Try An AI Lesson Demo Now"):
        st.toast("Loading sample lesson module workspace...", icon=None)
st.markdown('</div>', unsafe_html=True)

# --- 4. WHY MATHLOVER BEATS EVERYONE ELSE ---

