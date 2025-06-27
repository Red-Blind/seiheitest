import streamlit as st

st.title("性癖YES/NO診断アプリ")

questions = [
    "年上女性に魅力を感じますか？",
    "お尻のほうが好きですか？",
    "癒されたい願望が強いですか？",
    "年下の女性にもドキドキしますか？",
    "現実逃避したくなることが多いですか？"
]

answers = []

for q in questions:
    ans = st.radio(q, ["YES", "NO"], key=q)
    answers.append(ans)

if st.button("診断結果を見る"):
    if answers[0] == "YES" and answers[1] == "YES":
        st.success("あなたは『年上尻派』です。母性と包容力に飢えた癒し系フェチ！")
    elif answers[3] == "YES":
        st.success("あなたは『年下好きロマン派』。危ない橋は渡らないでね！")
    else:
        st.success("あなたは『こだわり派』。独自の性癖を極めましょう。")
