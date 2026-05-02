import streamlit as st
from datetime import date

# Page title and layout
st.set_page_config(page_title="25 Days Puzzle", page_icon="✨")
st.title("🧩 25 Days of Special Puzzles")

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
    </style>
    """, unsafe_allow_html=True)

# Grid system for 25 days
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
                    
                    if day_num == 1:
                        answer = st.text_input("Hamari pehli mulaqat kahan hui thi?", key="q1")
                        if answer.lower() == "homescapes":
                            st.subheader("✨ Day 1 Surprise ✨")
                            st.info("1. Kyunke ap meri muskurahat ke peechay chuppay insaan ko sab se behtar jantay han...")
                            # (Baqi reasons wese hi rahenge)

                    elif day_num == 2:
                        ans2 = st.text_input("Ma ap k Lia kaya hon?", key="q2")
                        if ans2.lower() == "jaanyman":
                            st.balloons()
                            st.video("https://youtu.be/kv_5z2ROptE?si=Yu_8uhoqyAwJfPLe")

                    elif day_num == 3:
                        ans3 = st.text_input("Mujay ap ki konsi cheez bohat passand ha?", key="q3")
                        if ans3.lower() == "smile":
                            st.balloons()
                            st.markdown("<div class='promise-card'><b>Waada 1:</b> Ma vada Karti hon zindagi k har mushkil vakat ma ap ka sath don gi.</div>", unsafe_allow_html=True)
                            st.markdown("<div class='promise-card'><b>Waada 2:</b> Ma vada Karti hon... ap ka sakoon bano.</div>", unsafe_allow_html=True)
                            st.markdown("<div class='promise-card'><b>Waada 3:</b> Ma vada Karti hon k hum mil kar apni zindagi Islam k asolon k mutabik guzarain gay.</div>", unsafe_allow_html=True)

                    elif day_num == 4:
                        ans4 = st.text_input("Ap ko sab sa ziada kaya passand ha?", key="q4")
                        if ans4.lower() == "biryani":
                            st.balloons()
                            st.markdown("<div class='tease-card'><b>Hahaha! Mujay pata tha ap ko muj sa ziada biryani hi passand ha... Ma to 2nd number par hon! 😒</b><br><br>Balkay sach to ye hai ke shayad main 3rd number par hon... Kyunke:<br>1️⃣ Biryani 🍗<br>2️⃣ Apka dost Ahmad 👬<br>3️⃣ Shayad Main... 🥺</div>", unsafe_allow_html=True)

                    elif day_num == 5:
                        st.subheader("🕰️ Day 5: Purani Yaadein")
                        ans5 = st.text_input("Mera 1st name kya tha?", key="q5")
                        if ans5.lower() == "mala":
                            st.balloons()
                            st.markdown(f"""
                                <div class='heart-card'>
                                    <b>Wao! Aap ko to abhi tak yaad hai! ✨</b><br><br>
                                    'Mala' sa 'Jaan' tak ka safar bohat mazay ka tha... <br>
                                    Shukria zindagi ma anay ka aur maray Lia sab sa bahtreen insan banany ka. <br>
                                    Bas hamesha aise hi muskurate raha karein! ❤️
                                </div>
                            """, unsafe_allow_html=True)
                        elif ans5:
                            st.error("Nahi... Thora aur peechay jayein! 🤫")

                    else:
                        st.write(f"Day {day_num} ka surprise abhi raaz hai!")
            else:
                st.button(f"Day {day_num} 🔒", disabled=True, key=f"lock_{day_num}")

st.markdown("---")
st.caption("Custom built with ❤️ for someone special")
