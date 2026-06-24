import streamlit as st
import random

#Bu kod sekmenin ikonu ve adini olusturur
if "page_icon" not in st.session_state:
    st.session_state.page_icon = "🤠"

st.set_page_config(page_title="A RPS Game",page_icon=st.session_state.page_icon)

st.title("🧱-📄-✂️-🦎-🖖🏻 Rock Paper Scissors Lizard Spock Gameeee")
st.markdown("Play to Dalin🐥")

#Her key(Anahtar yani : onceki yazi) yendigi degerleri liste olarak tutar

rules = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Rock", "Scissors"]
}

opinions = list(rules.keys())

#session state tanimlamalari

if "total_rounds" not in st.session_state:
    st.session_state.total_rounds = 0
if "draw_rounds" not in st.session_state:
    st.session_state.draw_rounds = 0
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "dalin_score" not in st.session_state:
    st.session_state.dalin_score = 0

#game main functions: def play_game vb

def play_game(player_choose):
    dalin_choose = random.choice(opinions)
    st.info(f"Player Choose:{player_choose}")
    st.warning(f"Dalin Choose:{dalin_choose}")
    st.session_state.total_rounds += 1
    #Skor belirleme
    if player_choose == dalin_choose:
        result = "DRAWWWWWWWW🤝"
        st.session_state.draw_rounds += 1
        st.write(result)
    elif dalin_choose in rules[player_choose]:
        result = "Winner Winner Chicken Dinner😎😎"
        st.session_state.player_score += 1
        st.balloons()
        st.success(result)
    else:
        result = "Loser Loser Dalin Is Winner😖😖"
        st.session_state.dalin_score += 1
        st.error(result)
#choose buttons

st.subheader("Do your choice!")
cols = st.columns(5)
display_names = {
    "Rock" : "**Rock-🧱**",
    "Paper" : "**Paper-📄**",
    "Scissors" : "**Scissors-✂️**",
    "Lizard" : "**Lizard-🦎**",
    "Spock" : "**Spock-🖖🏻**"
}
for i,(key,name) in enumerate(display_names.items()):
    with cols[i]:
        if st.button(name,use_container_width=True):
            play_game(key)
st.divider()


#score table
st.subheader("📈Score Table📉")
tr,dr,ps,ds = st.columns(4)
tr.metric("**Total Round**",st.session_state.total_rounds)
dr.metric("**Draw Rounds**",st.session_state.draw_rounds)
ps.metric("**Player Score**",st.session_state.player_score)
ds.metric("**Dalin Score**",st.session_state.dalin_score)


#rerun button

if st.button("ReStart"):
    st.session_state.total_rounds = 0
    st.session_state.draw_rounds = 0
    st.session_state.player_score = 0
    st.session_state.dalin_score = 0
    st.session_state.page_icon = "😎"
    st.rerun()

