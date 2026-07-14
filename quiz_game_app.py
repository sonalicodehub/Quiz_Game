"""
🎮 QUIZ AREA — A gamified quiz app built with Streamlit
Run with:  streamlit run quiz_game_app.py
"""

import streamlit as st
import random
import time

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Quiz Area — Test Your Knowledge",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Optional background music file — drop a file named "background.mp3"
# next to this script to enable it. The app works fine without it.
MUSIC_FILE = "background.mp3"

# ----------------------------------------------------------------------
# QUIZ DATA
# ----------------------------------------------------------------------
QUIZ_DATA = {
    "General Knowledge": [
        {"q": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris", "difficulty": "Easy"},
        {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars", "difficulty": "Easy"},
        {"q": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": "7", "difficulty": "Easy"},
        {"q": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific", "difficulty": "Medium"},
        {"q": "Which country gifted the Statue of Liberty to the USA?", "options": ["UK", "France", "Spain", "Italy"], "answer": "France", "difficulty": "Medium"},
        {"q": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino", "Malta"], "answer": "Vatican City", "difficulty": "Hard"},
        {"q": "Who wrote the Indian National Anthem?", "options": ["Mahatma Gandhi", "Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Jawaharlal Nehru"], "answer": "Rabindranath Tagore", "difficulty": "Easy"},
        {"q": "What is national animal of India?", "options": ["Lion", "Bengal Tiger", "Elephant", "Peacock"], "answer": "Bengal Tiger", "difficulty": "Medium"},
        {"q": "Which is longest river in world?", "options": ["Amazon River ", "Nile River", "Yangtze River", "Mississippi River"], "answer": "Nile River", "difficulty": "Medium"},
        {"q": "Which country is Known as the Land of the Rising Sun?", "options": ["China", "Japan", "South Korea", "Thailand"], "answer": "Japan", "difficulty": "Hard"},
    ],
    "Science": [
        {"q": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide", "difficulty": "Easy"},
        {"q": "What is the chemical symbol for Gold?", "options": ["Go", "Gd", "Au", "Ag"], "answer": "Au", "difficulty": "Easy"},
        {"q": "How many bones are in the adult human body?", "options": ["206", "196", "216", "226"], "answer": "206", "difficulty": "Medium"},
        {"q": "What is the powerhouse of the cell?", "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi Body"], "answer": "Mitochondria", "difficulty": "Medium"},
        {"q": "What particle has a negative charge?", "options": ["Proton", "Neutron", "Electron", "Photon"], "answer": "Electron", "difficulty": "Hard"},
        {"q": "What is the speed of light (approx.)?", "options": ["3x10^8 m/s", "3x10^6 m/s", "3x10^5 m/s", "3x10^7 m/s"], "answer": "3x10^8 m/s", "difficulty": "Hard"},
        {"q": "Which organ pumps blood throughout the human body?", "options": ["Lungs", "Brain", "Heart", "Kidney"], "answer": "Heart", "difficulty": "Easy"},
        {"q": "Which vitamin is mainly obtained from sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D", "difficulty": "Easy"},
        {"q": "What is the boiling point of water at sea level?", "options": ["90°C", "95°C", "100°C", "110°C"], "answer": "100°C", "difficulty": "Easy"},
        {"q": "Which is the largest planet in our Solar System?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter", "difficulty": "Easy"},
    ],
    "Movies & Pop Culture": [
        {"q": "Who directed the movie 'Inception'?", "options": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Ridley Scott"], "answer": "Christopher Nolan", "difficulty": "Easy"},
        {"q": "Which movie features the character 'Jack Sparrow'?", "options": ["Titanic", "Pirates of the Caribbean", "The Mask", "Avatar"], "answer": "Pirates of the Caribbean", "difficulty": "Easy"},
        {"q": "Which studio produces the 'Toy Story' films?", "options": ["DreamWorks", "Pixar", "Illumination", "Warner Bros"], "answer": "Pixar", "difficulty": "Medium"},
        {"q": "Who played the Joker in 'The Dark Knight'?", "options": ["Jared Leto", "Joaquin Phoenix", "Heath Ledger", "Jack Nicholson"], "answer": "Heath Ledger", "difficulty": "Medium"},
        {"q": "Which film won the first-ever Academy Award for Best Picture?", "options": ["Wings", "Sunrise", "The Jazz Singer", "Metropolis"], "answer": "Wings", "difficulty": "Hard"},
        {"q": "Which superhero uses the hammer Mjolnir?", "options": ["Hulk", "Thor", "Loki", "Captain America"], "answer": "Thor", "difficulty": "Easy"},
        {"q": "Which movie won the Academy Award for Best Picture in 2024?", "options": ["Barbie", "Oppenheimer", "Poor Things", "Killers of the Flower Moon"], "answer": "Oppenheimer", "difficulty": "Medium"},
        {"q": "Which actor plays Spider-Man in the Marvel Cinematic Universe?", "options": ["Andrew Garfield", "Tobey Maguire", "Tom Holland", "Chris Evans"], "answer": "Tom Holland", "difficulty": "Easy"},
        {"q": "Which Disney movie features Simba as the main character?", "options": ["Aladdin", "The Lion King", "Finding Nemo", "Frozen"], "answer": "The Lion King", "difficulty": "Easy"},
    ],
    "Sports": [
        {"q": "How many players are on a football (soccer) team on the field?", "options": ["9", "10", "11", "12"], "answer": "11", "difficulty": "Easy"},
        {"q": "In which sport would you perform a slam dunk?", "options": ["Volleyball", "Basketball", "Tennis", "Badminton"], "answer": "Basketball", "difficulty": "Easy"},
        {"q": "How often are the Summer Olympic Games held?", "options": ["Every 2 years", "Every 3 years", "Every 4 years", "Every 5 years"], "answer": "Every 4 years", "difficulty": "Medium"},
        {"q": "Which country has won the most FIFA World Cups?", "options": ["Germany", "Argentina", "Brazil", "Italy"], "answer": "Brazil", "difficulty": "Medium"},
        {"q": "In tennis, what is a score of zero called?", "options": ["Nil", "Love", "Zero", "Duck"], "answer": "Love", "difficulty": "Hard"},
        {"q": "Which Grand Slam tournament is played on clay courts?", "options": ["Wimbledon", "US Open", "Australian Open", "French Open"], "answer": "French Open", "difficulty": "Medium"},
        {"q": "Which Indian athlete won a gold medal in javelin throw at the Tokyo Olympics?", "options": ["Neeraj Chopra", "Milkha Singh", "P. T. Usha", "Bajrang Punia"], "answer": "Neeraj Chopra", "difficulty": "Easy"},
        {"q": "What is the highest possible break in snooker?", "options": ["147", "155", "167", "180"], "answer": "147", "difficulty": "Hard"},
        {"q": "Which country is famous for originating the martial art of Taekwondo?", "options": ["China", "Japan", "South Korea", "Thailand"], "answer": "South Korea", "difficulty": "Medium"}
    ],
}

# ----------------------------------------------------------------------
# CUSTOM CSS — GAMING THEME
# ----------------------------------------------------------------------
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Rajdhani', sans-serif;
    }

    /* Animated gaming background */
    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a3d);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Title styling */
    .quiz-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #00f5ff, #ff00e5, #ffea00);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 4s linear infinite;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.3);
        margin-bottom: 0;
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }

    .quiz-subtitle {
        text-align: center;
        color: #b8b8ff;
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin-bottom: 1.5rem;
    }

    /* Glass card */
    .glass-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
        margin-bottom: 1.2rem;
    }

    .question-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.4rem;
        color: #ffffff;
        text-align: center;
        line-height: 1.6;
        text-shadow: 0 0 15px rgba(0, 245, 255, 0.25);
    }

    .badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        margin: 0 4px;
    }
    .badge-easy { background: rgba(0, 230, 118, 0.2); color: #00e676; border: 1px solid #00e676; }
    .badge-medium { background: rgba(255, 193, 7, 0.2); color: #ffc107; border: 1px solid #ffc107; }
    .badge-hard { background: rgba(255, 23, 68, 0.2); color: #ff1744; border: 1px solid #ff1744; }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: 1px;
        padding: 0.9rem 0.5rem;
        border-radius: 14px;
        border: 1px solid rgba(0, 245, 255, 0.4);
        background: rgba(0, 245, 255, 0.08);
        color: #eafcff;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background: rgba(0, 245, 255, 0.25);
        border-color: #00f5ff;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
        transform: translateY(-2px);
        color: #ffffff;
    }
    div.stButton > button:active {
        transform: translateY(0px) scale(0.98);
    }

    /* Score chip row */
    .stat-box {
        text-align: center;
        background: rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 0.8rem 0.4rem;
        border: 1px solid rgba(255,255,255,0.12);
    }
    .stat-num {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.6rem;
        font-weight: 700;
        color: #00f5ff;
    }
    .stat-label {
        font-size: 0.8rem;
        color: #b8b8ff;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Progress bar restyle */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(90deg, #00f5ff, #ff00e5);
    }

    section[data-testid="stSidebar"] {
        background: rgba(10, 8, 30, 0.85);
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    </style>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------------------
# SESSION STATE INIT
# ----------------------------------------------------------------------
def init_state():
    defaults = {
        "stage": "start",       # start -> playing -> finished
        "questions": [],
        "current_index": 0,
        "score": 0,
        "streak": 0,
        "best_streak": 0,
        "answered": False,
        "selected": None,
        "high_score": 0,
        "start_time": None,
        "last_time_taken": 0.0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def badge_html(difficulty):
    cls = {"Easy": "badge-easy", "Medium": "badge-medium", "Hard": "badge-hard"}.get(difficulty, "badge-easy")
    return f'<span class="badge {cls}">{difficulty.upper()}</span>'


def start_quiz(category, num_questions):
    pool = QUIZ_DATA[category][:]
    random.shuffle(pool)
    num_questions = min(num_questions, len(pool))
    st.session_state.questions = pool[:num_questions]
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.stage = "playing"
    st.session_state.start_time = time.time()


def restart():
    st.session_state.stage = "start"
    st.session_state.answered = False
    st.session_state.selected = None


# ----------------------------------------------------------------------
# SCREENS
# ----------------------------------------------------------------------
def render_start_screen():
    st.markdown('<div class="quiz-title">🎮 QUIZ AREA</div>', unsafe_allow_html=True)
    st.markdown('<div class="quiz-subtitle">TEST YOUR KNOWLEDGE · BEAT YOUR HIGH SCORE</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        category = st.selectbox("🗂️ Choose a Category", list(QUIZ_DATA.keys()))
        max_q = len(QUIZ_DATA[category])
        num_questions = st.slider("🔢 Number of Questions", min_value=3, max_value=max_q, value=min(10, max_q))
        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.high_score:
        st.markdown(
            f'<p style="text-align:center;color:#ffea00;">🏆 Current High Score: {st.session_state.high_score}</p>',
            unsafe_allow_html=True,
        )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 START GAME", use_container_width=True):
            start_quiz(category, num_questions)
            st.rerun()


def render_stats_row():
    q_num = st.session_state.current_index + 1
    total = len(st.session_state.questions)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{q_num}/{total}</div><div class="stat-label">Question</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{st.session_state.score}</div><div class="stat-label">Score</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-num">🔥{st.session_state.streak}</div><div class="stat-label">Streak</div></div>', unsafe_allow_html=True)


def select_option(opt):
    st.session_state.selected = opt
    st.session_state.answered = True
    st.session_state.last_time_taken = round(time.time() - st.session_state.start_time, 1)
    correct = st.session_state.questions[st.session_state.current_index]["answer"]
    if opt == correct:
        st.session_state.streak += 1
        st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
        # bonus points for speed + streak
        base = 10
        speed_bonus = 5 if st.session_state.last_time_taken < 5 else 0
        streak_bonus = min(st.session_state.streak - 1, 5) * 2
        st.session_state.score += base + speed_bonus + streak_bonus
    else:
        st.session_state.streak = 0


def next_question():
    st.session_state.current_index += 1
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.start_time = time.time()
    if st.session_state.current_index >= len(st.session_state.questions):
        st.session_state.stage = "finished"
        st.session_state.high_score = max(st.session_state.high_score, st.session_state.score)


def render_playing_screen():
    total = len(st.session_state.questions)
    idx = st.session_state.current_index
    question = st.session_state.questions[idx]

    st.markdown('<div class="quiz-title" style="font-size:2rem;">🎮 QUIZ AREA</div>', unsafe_allow_html=True)
    st.progress(idx / total if not st.session_state.answered else (idx + 1) / total)
    render_stats_row()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(badge_html(question["difficulty"]), unsafe_allow_html=True)
    st.markdown(f'<p class="question-text">{question["q"]}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    options = question["options"]
    correct = question["answer"]

    col_pairs = [options[i:i + 2] for i in range(0, len(options), 2)]
    for row in col_pairs:
        cols = st.columns(len(row))
        for c, opt in zip(cols, row):
            with c:
                if st.session_state.answered:
                    if opt == correct:
                        st.success(f"✅ {opt}")
                    elif opt == st.session_state.selected:
                        st.error(f"❌ {opt}")
                    else:
                        st.button(opt, key=f"disabled_{opt}_{idx}", disabled=True)
                else:
                    if st.button(opt, key=f"opt_{opt}_{idx}"):
                        select_option(opt)
                        st.rerun()

    if st.session_state.answered:
        if st.session_state.selected == correct:
            st.markdown(f'<p style="text-align:center;color:#00e676;font-weight:700;">🎉 Correct! (+{10 + (5 if st.session_state.last_time_taken < 5 else 0) + min(st.session_state.streak-1,5)*2} pts · {st.session_state.last_time_taken}s)</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="text-align:center;color:#ff1744;font-weight:700;">💥 Wrong! Correct answer: {correct}</p>', unsafe_allow_html=True)

        label = "NEXT QUESTION ➡️" if idx + 1 < total else "SEE RESULTS 🏁"
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(label, use_container_width=True):
                next_question()
                st.rerun()


def render_finished_screen():
    total = len(st.session_state.questions)
    score = st.session_state.score
    max_possible = total * 21  # rough max with bonuses
    pct = int((score / max_possible) * 100) if max_possible else 0

    st.markdown('<div class="quiz-title">🏁 GAME OVER</div>', unsafe_allow_html=True)

    if pct >= 80:
        msg, emoji = "LEGENDARY PERFORMANCE!", "🏆"
        st.balloons()
    elif pct >= 60:
        msg, emoji = "GREAT JOB, CHAMPION!", "🥈"
    elif pct >= 40:
        msg, emoji = "NOT BAD, KEEP LEVELING UP!", "🥉"
    else:
        msg, emoji = "PRACTICE MAKES PERFECT!", "🎯"

    st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:3rem;">{emoji}</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="question-text">{msg}</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="stat-num" style="font-size:2.5rem;">{score} pts</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{total}</div><div class="stat-label">Questions</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-num">🔥{st.session_state.best_streak}</div><div class="stat-label">Best Streak</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-num">🏆{st.session_state.high_score}</div><div class="stat-label">High Score</div></div>', unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 PLAY AGAIN", use_container_width=True):
            restart()
            st.rerun()


# ----------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------
def render_background_music():
    """Play looping background music if a background.mp3 file is present.
    Silently skipped (with a one-time hint) if the file doesn't exist, so
    the app never crashes when the audio asset is missing."""
    import os
    if not st.session_state.get("music_on"):
        return
    if os.path.exists(MUSIC_FILE):
        with open(MUSIC_FILE, "rb") as f:
            st.audio(f.read(), format="audio/mp3", autoplay =True, loop=True)
    else:
        st.sidebar.info(f"🎵 Add a '{MUSIC_FILE}' file next to the script to enable music.")


def render_sidebar():
    with st.sidebar:
        st.markdown("### 🎮 Quiz Area")
        st.markdown("Sharpen your mind, one question at a time.")
        st.markdown("---")
        st.markdown("**Scoring:**")
        st.markdown("- ✅ Correct answer: **10 pts**")
        st.markdown("- ⚡ Answer under 5s: **+5 pts**")
        st.markdown("- 🔥 Streak bonus: **+2 pts/streak** (max +10)")
        st.markdown("---")
        st.session_state.music_on = st.toggle("🎵 Background Music", value=st.session_state.get("music_on", False))
        st.markdown("---")
        if st.session_state.stage != "start":
            if st.button("🏠 Return to Home", use_container_width=True):
                restart()
                st.rerun()


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main():
    inject_css()
    init_state()
    render_sidebar()
    render_background_music()

    if st.session_state.stage == "start":
        render_start_screen()
    elif st.session_state.stage == "playing":
        render_playing_screen()
    elif st.session_state.stage == "finished":
        render_finished_screen()


if __name__ == "__main__":
    main()