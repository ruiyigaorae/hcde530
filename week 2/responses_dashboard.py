import re
from collections import Counter

import pandas as pd
import streamlit as st
import altair as alt


st.set_page_config(page_title="Responses Dashboard", layout="wide")
st.title("Responses Dashboard")
st.caption("Interactive dashboard for `demo_responses.csv`.")


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["word_count"] = df["response"].fillna("").str.split().str.len()
    return df


def tokenize(text_series: pd.Series) -> list[str]:
    stop_words = {
        "the",
        "and",
        "to",
        "of",
        "a",
        "in",
        "is",
        "it",
        "for",
        "that",
        "we",
        "i",
        "on",
        "with",
        "as",
        "have",
        "be",
        "but",
        "they",
        "this",
        "are",
        "my",
        "at",
        "so",
        "do",
        "by",
        "from",
        "or",
        "not",
        "our",
        "was",
        "had",
        "has",
        "their",
        "all",
        "when",
        "into",
        "than",
        "them",
        "me",
        "you",
        "your",
    }

    tokens = []
    for text in text_series.fillna(""):
        words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
        tokens.extend([w for w in words if len(w) > 2 and w not in stop_words])
    return tokens


data_path = "demo_responses.csv"
df = load_data(data_path)

st.sidebar.header("Filters")
roles = sorted(df["role"].dropna().unique().tolist())
selected_roles = st.sidebar.multiselect("Role", roles, default=roles)

min_words = int(df["word_count"].min())
max_words = int(df["word_count"].max())
word_range = st.sidebar.slider("Word count range", min_words, max_words, (min_words, max_words))

search_text = st.sidebar.text_input("Find text in response", "")

filtered = df[df["role"].isin(selected_roles)].copy()
filtered = filtered[
    (filtered["word_count"] >= word_range[0]) & (filtered["word_count"] <= word_range[1])
]
if search_text.strip():
    filtered = filtered[
        filtered["response"].str.contains(search_text, case=False, na=False)
    ]

col1, col2, col3 = st.columns(3)
col1.metric("Responses", len(filtered))
col2.metric("Avg words", f"{filtered['word_count'].mean():.1f}" if len(filtered) else "0.0")
col3.metric("Unique roles", filtered["role"].nunique())

st.subheader("Role Distribution")
role_counts = filtered.groupby("role", as_index=False).size().rename(columns={"size": "count"})
if len(role_counts):
    role_chart = (
        alt.Chart(role_counts)
        .mark_bar()
        .encode(
            x=alt.X("role:N", sort="-y", title="Role"),
            y=alt.Y("count:Q", title="Responses"),
            tooltip=["role", "count"],
        )
        .properties(height=300)
    )
    st.altair_chart(role_chart, use_container_width=True)
else:
    st.info("No rows match current filters.")

st.subheader("Response Length by Participant")
if len(filtered):
    length_chart = (
        alt.Chart(filtered)
        .mark_circle(size=110)
        .encode(
            x=alt.X("participant_id:N", title="Participant"),
            y=alt.Y("word_count:Q", title="Word Count"),
            color="role:N",
            tooltip=["participant_id", "role", "word_count"],
        )
        .properties(height=320)
    )
    st.altair_chart(length_chart, use_container_width=True)

st.subheader("Top Terms")
tokens = tokenize(filtered["response"])
if tokens:
    top_terms = Counter(tokens).most_common(15)
    term_df = pd.DataFrame(top_terms, columns=["term", "count"])
    term_chart = (
        alt.Chart(term_df)
        .mark_bar()
        .encode(
            x=alt.X("count:Q", title="Frequency"),
            y=alt.Y("term:N", sort="-x", title="Term"),
            tooltip=["term", "count"],
        )
        .properties(height=380)
    )
    st.altair_chart(term_chart, use_container_width=True)
else:
    st.info("No terms available for current filters.")

st.subheader("Filtered Responses")
st.dataframe(
    filtered[["participant_id", "role", "word_count", "response"]],
    use_container_width=True,
    hide_index=True,
)

st.caption("Run with: `streamlit run responses_dashboard.py` from the `week 2` folder.")
