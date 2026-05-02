import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# Page title and layout
st.set_page_config(page_title="25 Days Puzzle", page_icon="✨")
st.title("🧩 25 Days of Special Puzzles")

# --- CUSTOM HEART RAIN EFFECT ---
def heart_animation():
    # Ye chota sa code screen par dilon ki barish kar dega
    components.html(
        """
        <div id='hearts' style='position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:9999;'></div>
        <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.innerHTML = '❤️';
            heart.style.position = 'fixed';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.top = '-20px';
            heart.style.fontSize = (Math.random() * 20 + 20) + 'px';
            heart.style.animation = 'fall ' + (Math.random() * 3 + 2) + 's linear forwards';
            document.getElementById('hearts').appendChild(heart);
            setTimeout(() => { heart.remove(); }, 5000);
        }
        const style = document.createElement('style');
        style.innerHTML = @keyframes fall { to { transform: translateY(105vh) rotate(360deg); opacity: 0; } };
        document.head.appendChild(style);
        setInterval(createHeart, 150);
        </script>
        """,
        height=0,
    )

# --- SETTINGS ---
START_DATE = date(2026, 5, 1) 
today = date.today()
delta = today - START_DATE
days_passed = delta.days + 1

st.write(f"### Aaj hamara Day {max(0, days_passed)} hai!")

# Custom Styling
st.markdown("""
    <style>
    .promise-card { background-color: #fff0f0; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 10px; color: #333; }
    .tease-card { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border: 2px dashed #ff4b4b; color: #333; }
    .heart-card { background-color: #ffe6eb; padding: 20px; border-radius: 15px; border: 1px solid #ff4b4b; text-align: center; color: #333; font-style: italic; }
    .ask-card { background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #2196f3; color: #333; }
    </style>
    """, unsafe_allow_html=True)

# Grid system
for row in range(5):
    cols = st.columns(5)
    for col in range(5):
        day_num = row * 5 + col + 1
        with cols[col]:
            if day_num <= days_passed:
                if st.button(f"Day {day_num} 🔓", key=f"btn_{day_num}"):
                    st.session_state["active_day"] = day_num
                
                if st.session_state.get("active_day") == day_num:
                    st.markdown("---")
                    
                    # --- DAY 1 ---
                    if day_num == 1:
                        answer = st.text_input("Hamari pehli mulaqat kahan hui thi?", key="q1")
                        if answer.lower() == "homescapes":
                            heart_animation()
                            st.subheader("✨ Day 1 Surprise ✨")
                            st.info("Kyunke ap meri muskurahat ke peechay chuppay insaan ko sab se behtar jantay han...")

                    # --- DAY 2 ---
                    elif day_num == 2:
                        ans2 = st.text_input("Ma ap k Lia kaya hon?", key="q2")
                        if ans2.lower() == "jaanyman":
                            heart_animation()
                            st.video("https://youtu.be/kv_5z2ROptE?si=Yu_8uhoqyAwJfPLe")

                    # --- DAY 3 ---
                    elif day_num == 3:
                        ans3 = st.text_input("Mujay ap ki konsi cheez bohat passand ha?", key="q3")
                        if ans3.lower() == "smile":
                            heart_animation()
                            st.markdown("<div class='promise-card'><b>Waada 1:</b> Ma vada Karti hon...</div>", unsafe_allow_html=True)

                    # --- DAY 4 ---
                    elif day_num == 4:
                        ans4 = st.text_input("Ap ko sab sa ziada kaya passand ha?", key="q4")
                        if ans4.lower() == "biryani":
                            heart_animation()
                            st.markdown("<div class='tease-card'><b>Hahaha! Mujay pata tha... 😒</b></div>", unsafe_allow_html=True)

                    # --- DAY 5 ---
                    elif day_num == 5:
                        ans5 = st.text_input("Mera 1st name kya tha?", key="q5")
                        if ans5.lower() == "mala":
                            heart_animation()
                            st.markdown("<div class='heart-card'>'Mala' sa 'Jaan' tak ka safar bohat mazay ka tha... ❤️</div>", unsafe_allow_html=True)

                    # --- DAY 6 ---
                    elif day_num == 6:
                        st.subheader("😭 Day 6: Mera 'Favourite' Kaam")
                        ans6 = st.text_input("Mera wo konsa 'favourite' kaam hai jo main bohat shauq se karti hoon?", key="q6")
                        if ans6.lower() == "rona":
                            heart_animation()
                            st.markdown(f"""
                                <div class='ask-card'>
                                    <b>Hahaha! Bilkul sahi pehchana! 😂</b><br><br>
                                    <b>Surprise Challenge:</b> Aaj main aapko ek 'Secret Truth' batane ka mauka de rahi hoon...<br>
                                    <b>Aaj wo ek baat aap mujh se WhatsApp par poochenge.</b> ✨
                                </div>
                            """, unsafe_allow_html=True)
                        elif ans6:
                            st.error("Nahi! Socho wo konsi cheez hai jis ka 'nal' hamesha khula rehta hai? 😂")

                    else:
                        st.write(f"Day {day_num} ka surprise abhi raaz hai!")
            else:
                st.button(f"Day {day_num} 🔒", disabled=True, key=f"lock_{day_num}")

st.markdown("---")
st.caption("Custom built with ❤️ for someone special")
