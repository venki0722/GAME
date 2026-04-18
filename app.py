import streamlit as st
from game_logic import init_board, move, is_solved

st.set_page_config(page_title="Brain Puzzle Game", layout="centered")

st.title("🧠 Sliding Puzzle Game")

# Initialize game
if "board" not in st.session_state:
    st.session_state.board = init_board()
    st.session_state.moves = 0

# Display grid
for i in range(4):
    cols = st.columns(4)
    for j in range(4):
        val = st.session_state.board[i][j]

        if val == " ":
            cols[j].button(" ", disabled=True)
        else:
            if cols[j].button(str(val), key=f"{i}-{j}"):
                move(st.session_state.board, i, j)
                st.session_state.moves += 1

# Show moves
st.write(f"Moves: {st.session_state.moves}")

# Win check
if is_solved(st.session_state.board):
    st.success("🎉 You solved it!")

# Restart
if st.button("🔄 Restart"):
    st.session_state.board = init_board()
    st.session_state.moves = 0
