import csv

# ── 1. LOAD DATA ──────────────────────────────────────────────────────────────
# Read the CSV file and extract each row's ID and response text.
# The CSV is expected to have a header row with at least an `id` and `response`
# column. If no `id` column exists, a 1-based row number is used instead.

INPUT_FILE = "responses.csv"

rows = []
with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        row_id = row.get("id", i)          # fall back to row number if no id
        response = row.get("response", "")
        rows.append({"id": row_id, "response": response})

# ── 2. COUNT WORDS ────────────────────────────────────────────────────────────
# Split each response on whitespace to count words, then attach the result
# back to the row dictionary for easy access later.

for row in rows:
    row["word_count"] = len(row["response"].split())

# ── 3. PRINT PER-ROW DETAILS ─────────────────────────────────────────────────
# Show one line per response: its ID, word count, and a 60-character preview
# of the text (truncated with "…" if it runs longer).

print(f"{'ID':<6} {'Words':>5}  Preview")
print("-" * 60)

for row in rows:
    preview = row["response"][:60]
    if len(row["response"]) > 60:
        preview += "…"
    print(f"{str(row['id']):<6} {row['word_count']:>5}  {preview}")

# ── 4. COMPUTE SUMMARY STATISTICS ────────────────────────────────────────────
# Find the shortest and longest response by word count, and compute the
# average across all responses (rounded to one decimal place).

word_counts = [row["word_count"] for row in rows]

total      = len(word_counts)
shortest   = min(word_counts)
longest    = max(word_counts)
average    = round(sum(word_counts) / total, 1) if total else 0

# ── 5. PRINT SUMMARY BLOCK ───────────────────────────────────────────────────
# Display a clean summary so the key metrics are easy to spot at a glance.

print()
print("=" * 40)
print("         RESPONSE LENGTH SUMMARY")
print("=" * 40)
print(f"  Total responses : {total}")
print(f"  Shortest        : {shortest} words")
print(f"  Longest         : {longest} words")
print(f"  Average         : {average} words")
print("=" * 40)