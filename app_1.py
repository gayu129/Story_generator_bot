import streamlit as st
import random
import time

# --- Set up page and background image ---
st.set_page_config(page_title="Story Prompt Generator", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .prompt-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }
    .vibrate-button {
        animation: vibrate 0.5s linear infinite;
    }

    @keyframes vibrate {
        0% { transform: translate(0); }
        25% { transform: translate(-2px, 2px); }
        50% { transform: translate(2px, -2px); }
        75% { transform: translate(-2px, 2px); }
        100% { transform: translate(2px, -2px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Confetti function ---
def trigger_confetti():
    confetti_script = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
    <script>
    setTimeout(function(){
        confetti({
            particleCount: 300,
            spread: 180,
            origin: { y: 0.6 }
        });
    }, 100);
    </script>
    """
    st.markdown(confetti_script, unsafe_allow_html=True)

# --- Play sound function ---
def play_sound():
    sound_html = """
    <audio autoplay>
    <source src="https://www.myinstants.com/media/sounds/success-fanfare-trumpets.mp3" type="audio/mpeg">
    </audio>
    """
    st.markdown(sound_html, unsafe_allow_html=True)

# --- Genre, Theme, Character Options ---
genres = [
    "Fantasy", "Romance", "Thriller", 
    "Science Fiction", "Mystery", "Horror", 
    "Historical Fiction", "Adventure"
]

themes = [
    "Redemption", "Identity", "Betrayal",
    "Love", "Courage", "Friendship", 
    "Survival", "Power"
]

character_types = [
    "The Anti-Hero", "The Mentor", "The Outsider", 
    "The Prodigy", "The Rebel", "The Innocent", 
    "The Trickster"
]

# --- Prompt generator ---
def generate_prompt(genre, character_type):
    prompts = {
        "Fantasy": [
            f"In a world where dreams can be harvested, {character_type.lower()} discovers a plot to steal them.",
            f"A {character_type.lower()} embarks on a quest to retrieve a stolen artifact to save the kingdom."
        ],
        "Romance": [
            f"Two rival bakers must team up and find unexpected love.",
            f"A {character_type.lower()} finds love while escaping a troubled past."
        ],
        "Thriller": [
            f"A {character_type.lower()} races to uncover a conspiracy endangering millions.",
            f"A detective with a dark past is drawn into a secret cult investigation."
        ],
        "Science Fiction": [
            f"In a dystopian future, a {character_type.lower()} must lead a rebellion against AI overlords.",
            f"A {character_type.lower()} discovers a portal to alternate Earths with shocking secrets."
        ],
        "Mystery": [
            f"A {character_type.lower()} investigates a series of impossible disappearances in a cursed town.",
            f"A cryptic letter forces the {character_type.lower()} into a deadly treasure hunt."
        ],
        "Horror": [
            f"A {character_type.lower()} must survive a night in a haunted asylum to break an ancient curse.",
            f"Strange noises and vanishing townspeople lead the {character_type.lower()} to a horrifying truth."
        ],
        "Historical Fiction": [
            f"During a medieval war, a {character_type.lower()} uncovers a plot that could change history.",
            f"In the ancient Roman Empire, a {character_type.lower()} struggles to protect a dangerous secret."
        ],
        "Adventure": [
            f"A {character_type.lower()} must cross the deadly forests of Zynthar to retrieve a sacred gem.",
            f"A lost map leads the {character_type.lower()} to an uncharted island full of danger and wonder."
        ]
    }

    if genre in prompts:
        return random.choice(prompts[genre])
    else:
        return "Sorry, that genre is not available."

# --- App Title ---
st.title("🎨✨ Story Idea Generator ✨🎨")

# --- User Selections ---
genre = st.selectbox("Choose a Genre:", genres)
theme = st.selectbox("Choose a Theme:", themes)
character_type = st.selectbox("Choose a Character Type:", character_types)

# --- Vibrating Button HTML ---
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        font-size:20px;
        font-weight:bold;
        color:white;
        background-color:#ff4b4b;
        border-radius:12px;
        padding:10px 24px;
        animation: vibrate 0.7s infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Generate Button ---
if st.button("🎲 Generate Prompt"):
    prompt = generate_prompt(genre, character_type)

    # Typing animation
    typing_area = st.empty()
    typed_text = ""
    for char in prompt:
        typed_text += char
        typing_area.markdown(f"<div class='prompt-box'><b>Theme:</b> {theme}<br><br> {typed_text}</div>", unsafe_allow_html=True)
        time.sleep(0.03)

    # Confetti and Sound
    trigger_confetti()
    play_sound()
