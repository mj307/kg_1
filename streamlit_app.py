import streamlit as st
from PIL import Image
import json
from datetime import datetime
import os
#from streamlit_extras.let_it_rain import rain
import plotly.express as px
import pandas as pd

message_file = "messages.json"

if "message_input" not in st.session_state:
    st.session_state.message_input = ""

if os.path.exists(message_file):
    with open(message_file, "r") as file:
        messages = json.load(file)
else:
    messages = []

st.set_page_config(page_title="With Love, Med and Kaju", layout="wide")


st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Indie+Flower&family=Patrick+Hand&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #f0f8ff; /* soft blue */
        }

        .photo-box {
            background-color: #fff8dc; /* light yellow */
            border: 3px dashed #fcd34d;
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 4px 4px 10px rgba(0,0,0,0.05);
            text-align: center;
            margin-top: 1rem;
        }
 
        .caption {
            margin-top: 0.8rem;
            font-size: 16px;
            font-style: italic;
            color: #444;
        }
        .post-it {
            font-family: 'Indie Flower';
            font-size: 18px;
            padding: 1.2rem;
            margin: 1rem 0;
            border-radius: 10px;
            box-shadow: 4px 4px 8px rgba(0,0,0,0.15);
            min-height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .note1 { background-color: #ffd1dc; font-family: 'Indie Flower';}  /* soft pink */
        .note2 { background-color: #ffe5b4; font-family: 'Patrick Hand';}  /* peach */
        .note3 { background-color: #ffc1cc; font-family: 'Indie Flower';}  /* cotton candy pink */
        .note4 { background-color: #ffcab1; font-family: 'Patrick Hand';}  /* apricot */
        .note5 { background-color: #ffb6b9; font-family: 'Indie Flower';}  /* warm blush pink */
        .note6 { background-color: #ffd6a5; font-family: 'Patrick Hand';}  /* soft orange */

        .note-text {
            color: #333;
            padding: 0.5rem;
        }
        
        textarea {
            background-color: #d8f3ff !important;
            color: #5a3e36 !important;
            font-family: 'Patrick Hand', cursive;
            font-size: 18px !important;
        }
        .message-box {
            background-color: #fdf6f0;
            border-left: 5px solid #d7ccc8;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)


st.title("With Love, Med and Kaju")
st.subheader("Starring Med. Featuring Kaju 😉")


col1, col2, col3 = st.columns(3)

with col1:
    lil_kaju = Image.open("kaju_lil.png").resize((500, 500))
    st.image(lil_kaju,use_container_width=True)
    st.markdown('<div class="caption"> Kaju doing the 😮 (2021)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    mouth = Image.open("mouth.png").resize((500, 500))
    st.image(mouth, use_container_width=True)
    st.markdown('<div class="caption"> Us doing the 😮 Together (2024)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    lil_med = Image.open("med_lil.png").resize((500, 500))
    st.image(lil_med, use_container_width=True)
    st.markdown('<div class="caption"> Med doing the 😮 (2019)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


st.subheader("Love letters 🧸💛")

row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown('<div class="post-it note1"><div class="note-text">"so uh funny story someone asked to see who u were and they liked the photo but despite that. hello! "<br><br>– Kaju</div></div>', unsafe_allow_html=True)

with row1_col2:
    st.markdown('<div class="post-it note2"><div class="note-text">"what\'s krishna\'s coffee order? a GRANDHE matcha latte HAHAHAHA"<br><br>– Med</div></div>', unsafe_allow_html=True)

with row1_col3:
    st.markdown('<div class="post-it note3"><div class="note-text">"second first one [kiss] i wasn\'t even thinking about the kissing that much the only thing that was in my mind was you and how lucky i was that i was w u in that moment"<br><br>– Kaju</div></div>', unsafe_allow_html=True)

# Second row of 3 post-its
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown('<div class="post-it note4"><div class="note-text">"but like you have an amazing body and an even more amazing personality??? hella smart hella funny hella respectful hella caring. like u listen to me, u do things for me without me asking, ur literally the dream boyfriend. i am not joking when i tell you i have hit the jackpot in terms of boyfriend "<br><br>– Med</div></div>', unsafe_allow_html=True)

with row2_col2:
    st.markdown('<div class="post-it note5"><div class="note-text">"when i pick u up from the airport i\'m gonna have a guinness representative with me bc imma give u the worlds biggest hug"<br><br>– Kaju</div></div>', unsafe_allow_html=True)

with row2_col3:
    st.markdown('<div class="post-it note6"><div class="note-text">"i hate you"<br><br>– Med</div></div>', unsafe_allow_html=True)


st.markdown("""
    <div style="background-color: #e1e1e1; padding: 2rem; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1); text-align: center;">
        <h2 style="color: #333;">🎶 Songs that remind us of each other  💿</h2>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/CD_icon_2.svg/768px-CD_icon_2.svg.png" style="width: 150px; margin: 1rem auto;" />
        <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3tb2MNGJcoBSgW6JcsMapG?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture" loading="lazy"></iframe>
    </div>
""", unsafe_allow_html=True)

st.write()
st.write()
timeline_events = [
    ("2024-02-01", "med stalks kaju on insta"),
    ("2024-03-05", "med and kaju meet in JCL wrap line"),
    ("2024-04-06", "start talking"),
    ("2024-04-19", "first kiss:D"),
    ("2024-04-20", "official!!"),
    ("2024-05-04", "med leaves for cali 💔"),
    ("2024-08-24", "long distance over :D"),
    ("2024-08-30", "first date after LD"),
    ("2024-09-20", "first in-person anniversary"),
    ("2024-10-20", "6 months YAY"),
    ("2024-11-08", "movie date (med's fav date🥰)"),
    ("2025-02-14", "valentine's day 💘"),
    ("2025-03-01", "first holiiiii"),
    ("2025-04-20", "one year 💞")
]

df_timeline = pd.DataFrame(timeline_events, columns=["Date", "Event"])
df_timeline["Date"] = pd.to_datetime(df_timeline["Date"])

import plotly.graph_objects as go

fig = go.Figure()


fig.add_trace(go.Scatter(
    x=[df_timeline["Date"].min(), df_timeline["Date"].max()],
    y=[0, 0],
    mode="lines",
    line=dict(color="#a47148", width=3),
    hoverinfo="skip",
    showlegend=False
))


fig.add_trace(go.Scatter(
    x=df_timeline["Date"],
    y=[0] * len(df_timeline),
    mode="markers",
    marker=dict(size=14, color="#d7a86e", line=dict(width=2, color="#a47148")),
    hovertext=df_timeline["Event"],
    hovertemplate="<b>%{hovertext}</b><br>%{x|%B %d, %Y}<extra></extra>",
    showlegend=False
))


fig.update_layout(
    height=220,
    xaxis=dict(
        title="",
        showgrid=False,
        tickformat="%b %Y", 
        tickfont=dict(color="#5a3e36", size=12)
    ),
    yaxis=dict(
        visible=False
    ),
    plot_bgcolor="#f5e6d3", 
    paper_bgcolor="#f5e6d3",
    margin=dict(t=20, b=40, l=20, r=20),
)

st.subheader("📅 Our Timeline")
st.plotly_chart(fig, use_container_width=True)






st.markdown("<h2 style='text-align: center;'>💌 Leave a Message</h2>", unsafe_allow_html=True)

# Text area input
st.session_state.message_input = st.text_area(
    "Write your message below:",
    value=st.session_state.message_input,
    key="message_box"
)

# Button to submit
if st.button("Send"):
    message = st.session_state.message_input.strip()
    if message:
        timestamp = datetime.now().strftime("%m/%d/%Y")
        messages.append({"date": timestamp, "text": message})

        # Save updated messages
        with open(message_file, "w") as file:
            json.dump(messages, file, indent=4)

        st.success("Message sent!")
        #rain(emoji="🤎",font_size=20,falling_speed=5,animation_length=2,)

        st.session_state.message_input = ""

if messages:
    st.markdown("<h4 style='margin-top:2rem;'>💬 Messages:</h4>", unsafe_allow_html=True)
    for msg in reversed(messages):  
        st.markdown(f"""
            <div class="message-box">
                <strong style="color:#5a3e36;">{msg['date']}</strong><br>
                <span style="color:#5a3e36;">{msg['text']}</span>
            </div>
        """, unsafe_allow_html=True)