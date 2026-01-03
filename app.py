import streamlit as st
from backend.utils.ocr import extract_text_from_image
from backend.utils.audio import speech_to_text
from backend.agents.parser_agent import parse_problem
from backend.rag.rag_engine import retrieve_context
from backend.agents.intent_router import route_intent
from backend.agents.solver_agent import solve_problem
from backend.agents.verifier_agent import verify_solution
from backend.agents.explainer_agent import explain_solution
from backend.memory.memory_store import save_to_memory

st.write("🚀 Math Mentor AI Loaded")


st.set_page_config(page_title="Math Mentor AI")

st.title("📘 AI Math Mentor")

mode = st.selectbox("Choose input type:", ["Text", "Image", "Audio"])

user_text = ""

if mode == "Text":
    user_text = st.text_area("Enter your math question")

elif mode == "Image":
    img = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
    if img:
        with open("temp.png", "wb") as f:
            f.write(img.read())
        user_text = extract_text_from_image("temp.png")
        user_text = st.text_area("Extracted Text (edit if needed)", user_text)

elif mode == "Audio":
    audio = st.file_uploader("Upload audio", type=["wav", "mp3"])
    if audio:
        with open("temp.wav", "wb") as f:
            f.write(audio.read())
        user_text = speech_to_text("temp.wav")
        user_text = st.text_area("Transcribed Text (edit if needed)", user_text)

if st.button("Solve"):
    parsed = parse_problem(user_text)
    context = retrieve_context(user_text)
    flow = route_intent(parsed)
    result = solve_problem(parsed, context)
    verification = verify_solution(parsed, result)
    explanation = explain_solution(parsed, result)

    st.subheader("📌 Solution")
    st.write(result)

    st.subheader("🧠 Explanation")
    st.text(explanation)

    st.subheader("🧪 Verification")
    st.write(verification)

    feedback = st.radio("Is this correct?", ["Yes", "No"])
    if st.button("Submit Feedback"):
        record = {
            "input": user_text,
            "parsed": parsed,
            "context": context,
            "solution": result,
            "verification": verification,
            "explanation": explanation,
            "feedback": feedback
        }
        save_to_memory(record)
        st.success("Saved to memory!")
