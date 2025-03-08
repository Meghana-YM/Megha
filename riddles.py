import streamlit as st
st.title("RIDDLES:-)")
v,a,k=0,0,0
score=0
qs1=st.radio("What has keys but can't open locks?",[" A piano","  A map","A calculator"] ,index=None)
if qs1==" A piano ":
    v+=1
    score+=1
elif qs1=="  A map":
    a+=1
elif qs1=="A calculator":
    k+=1
st.success(f"Your choice:{qs1} ")

# Question 2
qs2 = st.radio("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I", [
    "An cloud",
    "A shadow",
    "An echo"
], index=None)

if qs2 == "A cloud":
    v += 1
elif qs2 == "A shadow":
    a += 1
elif qs2 == "An echo":
    k += 1
    score+=1

st.success(f"Your choice: {qs2}")
# st.write(f"Choices so far: \nCommunicate with animals: {st.session_state.q2_v} \nSpeak every language: {st.session_state.q2_a} \nNone: {st.session_state.q2_k}")

# Question 3
qs3 = st.radio("What can travel around the world while staying in the corner?", [
    "A stamp",
    "A letter",
    "A coin"
], index=None)

if qs3 == "A stamp":
    v += 1
    score+=1
elif qs3 == "A letter":
    a += 1
elif qs3 == "A coin":
    k += 1

st.success(f"Your choice: {qs3}")
# st.write(f"Choices so far: \nNo Technology: {st.session_state.q3_v} \nOnly Technology: {st.session_state.q3_a} \nNone: {st.session_state.q3_k}")

# Question 4
qs4 = st.radio("The more of this there is, the less you see. What is it?", [
    "Light",
    "Fog",
    "Darkness"
], index=None)

if qs4 == "Light":
    v += 1
elif qs4 == "Fog":
    a += 1
elif qs4 == "Darkness":
    k += 1
    score+=1

st.success(f"Your choice: {qs4}")
# st.write(f"Choices so far: \nFly: {st.session_state.q4_v} \nRead Minds: {st.session_state.q4_a} \nNone: {st.session_state.q4_k}")

# Question 5
qs5 = st.radio("*What comes once in a minute, twice in a moment, but never in a thousand years?", [
    "The letter M",
    " The letter E",
    "The letter O"
], index=None)

if qs5 == "The letter M ":
    v += 1
    score+=1
elif qs5 == " The letter E":
    a += 1
elif qs5 == "The letter O":
    k += 1

st.success(f"Your choice: {qs5}")
# st.write(f"Choices so far: \nInvisible: {st.session_state.q5_v} \nTeleport: {st.session_state.q5_a} \nNone: {st.session_state.q5_k}")

# Question 6
qs6 = st.radio("What gets wetter as it dries?", [
    " A towel",
    " A sponge",
    "A cloud"
], index=None)

if qs6 == " A towel":
    v += 1
    score+=1
elif qs6 == "A sponge":
    a += 1
elif qs6 == "A cloud":
    k += 1

st.success(f"Your choice: {qs6}")
# st.write(f"Choices so far: \nTime: {st.session_state.q6_v} \nDate: {st.session_state.q6_a} \nNone: {st.session_state.q6_k}")

# Question 7
qs7 = st.radio("What has a head, a tail, but no body?", [
    "A snake",
    "A coin",
    "A pencil"
], index=None)

if qs7 == "A snake":
    v += 1
elif qs7 == "A coin":
    a += 1
    score+=1
elif qs7 == "A pencil":
    k += 1

st.success(f"Your choice: {qs7}")
# st.write(f"Choices so far: \nPast: {st.session_state.q7_v} \nFuture: {st.session_state.q7_a} \nNone: {st.session_state.q7_k}")

# Question 8
qs8 = st.radio("What can be cracked, made, told, and played?", [
    " A promise",
    "A song",
    " A joke"
], index=None)

if qs8 == " A promise":
    v += 1
elif qs8 == "A song":
    a += 1
elif qs8 == " A joke":
    k += 1
    score+=1

st.success(f"Your choice: {qs8}")
# st.write(f"Choices so far: \nHappy: {st.session_state.q8_v} \nSuccessful: {st.session_state.q8_a} \nNone: {st.session_state.q8_k}")

# Question 9
qs9 = st.radio(" am always hungry, I must always be fed. The finger I touch, Will soon turn red. What am I?", [
    "Fire",
    "A flame",
    "A candle"
], index=None)

if qs9 == "Fire":
    v += 1
    score+=1
elif qs9 == "A flame":
    a += 1
elif qs9 == "A candle":
    k += 1

st.success(f"Your choice: {qs9}")
# st.write(f"Choices so far: \nSpace: {st.session_state.q9_v} \nSea: {st.session_state.q9_a} \nNone: {st.session_state.q9_k}")

# Question 10
qs10 = st.radio("The more you take, the more you leave behind. What am I?", [
    "Time",
    "Footsteps",
    "Water"
], index=None)

if qs10 == "Time":
    v += 1
elif qs10 == "Footsteps":
    a += 1
    score+=1
elif qs10 == "Water":
    k += 1

st.subheader("Final Score")
st.write(f"Your total score: {score}")