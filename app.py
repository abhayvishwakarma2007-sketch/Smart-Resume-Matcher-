import streamlit as st
import pandas as pd
from matcher import match_candidates

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Skill Matcher",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("AI Resume Skill Matcher")
st.caption("Skill-based candidate matching system")

st.divider()

# -----------------------------
# Input Form
# -----------------------------
with st.form("matcher_form"):
    skills_input = st.text_input(
        "Enter Skill(s)",
        placeholder="Example: Python or Data Science or SQL Python"
    )

    job_role = st.text_input(
        "Job Role (Optional)",
        placeholder="Data Scientist"
    )

    submit = st.form_submit_button("Find Matching Candidates")

# -----------------------------
# Processing
# -----------------------------
if submit:
    if skills_input.strip() == "":
        st.warning("Please enter at least one skill.")
    else:
        try:
            df = pd.read_excel("candidates.xlsx")
        except Exception:
            st.error("Dataset could not be loaded.")
            st.stop()

        results = match_candidates(df, skills_input, job_role)

        st.divider()

        if not results:
            st.info("No matching candidates found.")
        else:
            st.subheader("Top Matching Candidates")
            st.dataframe(
                pd.DataFrame(results),
                use_container_width=True,
                hide_index=True
            )
