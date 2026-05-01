import streamlit as st
from datetime import date

# Page title and layout
st.set_page_config(page_title="25 Days Puzzle", page_icon="✨")
st.title("🧩 25 Days of Special Puzzles")

# --- SETTINGS ---
# Jis date se game shuru karni hai
START_DATE = date(2026, 4, 30) 

today = date.today()
delta = today - START_DATE
days_passed = delta.days + 1

st.write(f"### Aaj hamara *Day {max(0, days_passed)}* hai!")

# Grid system for 25 days
for row in range(5):
    cols = st.columns(5)
    for col in range(5):
        day_num = row * 5 + col + 1
        with cols[col]:
            if day_num <= days_passed:
                if st.button(f"Day {day_num} 🔓", key=f"btn_{day_num}"):
                    st.session_state["active_day"] = day_num
                
                # Jab Button click ho jaye
                if st.session_state.get("active_day") == day_num:
                    # --- DAY 1 ---
                    if day_num == 1:
                        st.balloons()
                        answer = st.text_input("Hamari pehli mulaqat kahan hui thi?", key="q1")
                        
                        if answer.lower() == "homescapes":
                            st.markdown("---")
                            st.subheader("✨ Day 1 Surprise ✨")
                            st.write("Aj day one ha to is Lia aj ka surprise ya ha:")
                            st.write("### 5 reasons Why are you number 1 for me")
                            st.info("1. Kyunke ap meri muskurahat ke peechay chuppay insaan ko sab se behtar jantay han.")
                            st.info("2. Kyunke ap un duwaon ka jawab han jo maine abhi tak maangi bhi nahi theen.")
                            st.info("3. Kyunke ap aam se lamhon ko bhi jadu jaisa bana detay han.")
                            st.info("4. Kyunke mere dil ne ap ko chuna hai, jo kabhi kisi cheez ke liye itna sure nahi tha jitna ap k lia ha.")
                            st.info("5. Kyunke ap k saath har cheez mukammal lagti hai.")
                        elif answer:
                            st.error("Galat jawab! Thora aur sochein... 😉")

                    # --- DAY 2 (NEW ADDED) ---
                    elif day_num == 2:
                        st.subheader("🎵 Day 2: Ek Khaas Sawal")
                        ans2 = st.text_input("Ma ap k Lia kaya hon?", key="q2")
                        
                        if ans2.lower() == "jaanyman":
                            st.balloons()
                            st.success("Sahi jawab! ❤️ Ye song ap k liye:")
                            # YouTube link directly embed kar diya hai
                            st.video("https://youtu.be/kv_5z2ROptE?si=Yu_8uhoqyAwJfPLe")
                            st.write("Isay sun kar batana kaisa laga! ✨")
                        elif ans2:
                            st.error("Nahi... Kuch aur kehti hain ap mujhe! 😉")

                    else:
                        st.write(f"Day {day_num} ka surprise abhi raaz hai!")
            else:
                st.button(f"Day {day_num} 🔒", disabled=True, key=f"lock_{day_num}")

st.markdown("---")
st.caption("Custom built with ❤️ for someone special")
