import pandas as pd

# Question: What does the raw Federal Register AI dataset look like, and are the fields usable for policy analysis?
# Governance insight: Viewing the first rows and schema confirms whether core governance metadata (agency, date, type) is present and structured for accountability tracking.
df = pd.read_csv("week5_federal_register.csv")
print("First 5 rows:")
print(df.head())
print("\nDataFrame info:")
print(df.info())

# Question: Which kinds of AI-related federal actions (rules, notices, proposed rules, etc.) are most common?
# Governance insight: Document type frequency reveals whether U.S. AI governance is currently more proposal-oriented, informational, or enforcement/regulatory in nature.
print("\nDocument type counts:")
print(df["type"].value_counts())

# Question: How much of this AI policy activity is recent (post-2022) versus older?
# Governance insight: Filtering by publication date highlights the acceleration of federal AI governance in the current policy era.
df["publication_date"] = pd.to_datetime(df["publication_date"], errors="coerce")
recent_docs = df[df["publication_date"].dt.year > 2022]
print("\nDocuments published after 2022:")
print(recent_docs)

# Question: Which federal agencies are contributing the most AI-related documents?
# Governance insight: Grouping by agency identifies where governance leadership and administrative attention to AI are concentrated across the federal system.
agency_counts = (
    df.assign(agency_names=df["agency_names"].fillna("Unknown"))
    .groupby("agency_names")
    .size()
    .sort_values(ascending=False)
)
print("\nDocument counts by agency:")
print(agency_counts)

# Question: Are there data quality gaps that could bias conclusions about AI governance?
# Governance insight: Missing-value counts show where records are incomplete, helping assess confidence in agency activity and document-type trends.
print("\nMissing values by column:")
print(df.isnull().sum())
