"""Build three Plotly charts from week5_federal_register.csv and save as PNG."""

import subprocess
import sys

subprocess.check_call(
    [sys.executable, "-m", "pip", "install", "kaleido", "plotly", "pandas", "-q"]
)

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "week5_federal_register.csv"

TYPE_ORDER = ["Notice", "Rule", "Proposed Rule", "Presidential Document"]


def load_df() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["publication_date"] = pd.to_datetime(df["publication_date"], errors="coerce")
    return df


def agency_rows(df: pd.DataFrame) -> pd.Series:
    """One row per (document, agency) after splitting semicolon-separated names."""
    names = df["agency_names"].fillna("Unknown").astype(str)

    def split_agencies(cell: str) -> list[str]:
        parts = [p.strip() for p in cell.split(";")]
        return [p for p in parts if p]

    exploded = []
    for cell in names:
        agencies = split_agencies(cell)
        exploded.extend(agencies if agencies else ["Unknown"])
    return pd.Series(exploded)


def main() -> None:
    df = load_df()

    # 1 — Top 10 agencies (horizontal bar)
    agency_counts = agency_rows(df).value_counts().head(10).sort_values(ascending=True)
    fig1 = px.bar(
        x=agency_counts.values,
        y=agency_counts.index.astype(str),
        orientation="h",
        labels={"x": "Number of documents", "y": "Agency"},
    )
    fig1.update_layout(
        title="Top 10 Federal Agencies by AI-Related Documents",
        showlegend=False,
        yaxis={"categoryorder": "total ascending"},
    )
    fig1.write_image(str(BASE / "chart1_agencies.png"), scale=2)

    # 2 — Document types
    type_counts = df["type"].fillna("Unknown").value_counts()
    counts_ordered = pd.Series(
        {t: int(type_counts.get(t, 0)) for t in TYPE_ORDER},
        index=TYPE_ORDER,
    )
    fig2 = px.bar(
        x=counts_ordered.index.astype(str),
        y=counts_ordered.values,
        labels={"x": "Document type", "y": "Count"},
    )
    fig2.update_layout(
        title="AI-Related Federal Documents by Type",
        showlegend=False,
    )
    fig2.write_image(str(BASE / "chart2_types.png"), scale=2)

    # 3 — Documents per year
    years = df["publication_date"].dt.year.dropna().astype(int)
    per_year = years.value_counts().sort_index()
    fig3 = go.Figure(
        data=go.Scatter(
            x=per_year.index.astype(int),
            y=per_year.values,
            mode="lines+markers",
        )
    )
    fig3.update_layout(
        title="AI-Related Federal Documents Published Per Year",
        xaxis_title="Year",
        yaxis_title="Number of documents",
    )
    fig3.update_xaxes(tickmode='linear', tick0=2023, dtick=1)
    fig3.write_image(str(BASE / "chart3_timeline.png"), scale=2)

    print("Wrote:", BASE / "chart1_agencies.png")
    print("Wrote:", BASE / "chart2_types.png")
    print("Wrote:", BASE / "chart3_timeline.png")


if __name__ == "__main__":
    main()
