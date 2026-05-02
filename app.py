import streamlit as st
from datetime import date

# Page title and layout
st.set_page_config(page_title="25 Days Puzzle", page_icon="✨")
st.title("🧩 25 Days of Special Puzzles")

# --- SETTINGS ---
# 1 May se start taake Day 4 (May 4) ko khulay
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
                    
                    # --- DAY 1 ---
                    if day_num == 1:
                        st.balloons()
                        answer = st.text_input("Hamari pehli mulaqat kahan hui thi?", key="q1")
                        if answer.lower() == "homescapes":
                            st.subheader("✨ Day 1 Surprise ✨")
                            st.write("### 5 reasons Why are you number 1 for me")
                            st.info("1. Kyunke ap meri muskurahat ke peechay chuppay insaan ko sab se behtar jantay han.")
                            st.info("2. Kyunke ap un duwaon ka jawab han jo maine abhi tak maangi bhi nahi theen.")
                            st.info("3. Kyunke ap aam se lamhon ko bhi jadu jaisa bana detay han.")
                            st.info("4. Kyunke mere dil ne ap ko chuna hai...")
                            st.info("5. Kyunke ap k saath har cheez mukammal lagti hai.")

                    # --- DAY 2 ---
                    elif day_num == 2:
                        st.subheader("🎵 Day 2: Ek Khaas Sawal")
                        ans2 = st.text_input("Ma ap k Lia kaya hon?", key="q2")
                        if ans2.lower() == "jaanyman":
                            st.balloons()
                            st.success("Sahi jawab! ❤️")
                            st.video("https://youtu.be/kv_5z2ROptE?si=Yu_8uhoqyAwJfPLe")

                    # --- DAY 3 ---
                    elif day_num == 3:
                        st.subheader("💍 Day 3: Dil ki Baat")
                        ans3 = st.text_input("Mujay ap ki konsi cheez bohat passand ha?", key="q3")
                        if ans3.lower() == "smile":
                            st.balloons()
                            st.markdown("### ❤️ Aaj ke 3 Promises")
                            st.markdown("<div class='promise-card'><b>Waada 1:</b> Ma vada Karti hon zindagi k har mushkil vakat ma ap ka sath don gi.</div>", unsafe_allow_html=True)
                            st.markdown("<div class='promise-card'><b>Waada 2:</b> Ma vada Karti hon ab jab b thak kar Ghar vapis ain to ma ap k muskranay ki vaja bano, ap ka sakoon bano.</div>", unsafe_allow_html=True)
                            st.markdown("<div class='promise-card'><b>Waada 3:</b> Ma vada Karti hon k hum mil kar apni zindagi Islam k asolon k mutabik guzarain gay aur mil kar apnay Rab sa duain mangay gain.</div>", unsafe_allow_html=True)

                    # --- DAY 4 (NEW ADDED) ---
                    elif day_num == 4:
                        st.subheader(" Day 4: Reality Check")
                        ans4 = st.text_input("Ap ko sab sa ziada kaya passand ha?", key="q4")
                        if ans4.lower() == "biryani":
                            st.balloons()
                            st.markdown(f"""
                                <div class='tease-card'>
                                    <b>Hahaha! Mujay pata tha ap ko muj sa ziada biryani hi passand ha... Ma to 2nd number par hon! 😒</b><br><br>
                                    Balkay sach to ye hai ke shayad main 3rd number par hon... Kyunke:<br>
                                    1️⃣ <b>Biryani</b> 🍗<br>
                                    2️⃣ <b>Apka dost Ahmad</b> (jis k sath sara sara din ghomtay rahtaya han) 👬<br>
                                    3️⃣ <b>Shayad Main...</b> 🥺<br><br>
                                    Chalo, kam az kam aaj ye sach samne to aaya! Ab sara din Ahmad ke sath hi ghoomein aur Biryani hi khayein!
                                </div>
                            """, unsafe_allow_html=True)
                        elif ans4:
                            st.error("Nahi... Kuch khanay wali cheez sochein jo aapko mujh se bhi zyada pyari hai! 🙄")

                    else:
                        st.write(f"Day {day_num} ka surprise abhi raaz hai!")
            else:
                st.button(f"Day {day_num} 🔒", disabled=True, key=f"lock_{day_num}")

st.markdown("---")
st.caption("Custom built with ❤️ for someone special")
