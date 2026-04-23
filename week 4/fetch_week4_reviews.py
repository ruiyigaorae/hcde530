import csv
import json
import ssl
from collections import Counter
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

# define the API URL and the total number of reviews to fetch
API_URL = "https://hcde530-week4-api.onrender.com/reviews"
TOTAL_REVIEWS = 500
PAGE_SIZE = 100
OUTPUT_FILE = "week4_results.csv"

# fetch a single page of reviews from the API
def fetch_page(offset: int, limit: int) -> list[dict]:
    """Fetch a single page of reviews from the API."""
    query = urlencode({"offset": offset, "limit": limit})
    url = f"{API_URL}?{query}"
    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
    except URLError as error:
        if "CERTIFICATE_VERIFY_FAILED" not in str(error):
            raise
        # Fallback for local environments missing root certificates.
        insecure_context = ssl._create_unverified_context()
        with urlopen(url, context=insecure_context) as response:
            data = json.loads(response.read().decode("utf-8"))

    # Support either a raw list response or a wrapped object response.
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "reviews" in data and isinstance(data["reviews"], list):
        return data["reviews"]
    return []


def main() -> None:
    rows: list[tuple[str, int]] = []
    category_counts: Counter[str] = Counter()
    top_review: dict | None = None

# loop through the reviews and count the number of reviews in each category
    for offset in range(0, TOTAL_REVIEWS, PAGE_SIZE):
        reviews = fetch_page(offset=offset, limit=PAGE_SIZE)
        if not reviews:
            break

        for review in reviews:
            category = str(review.get("category", "unknown"))
            helpful_votes = int(review.get("helpful_votes", 0))
            rows.append((category, helpful_votes))
            category_counts[category] += 1

# find the review with the most helpful votes
            if top_review is None or helpful_votes > int(top_review.get("helpful_votes", 0)):
                top_review = review

# save the results to a CSV file
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["category", "helpful_votes"])
        writer.writerows(rows)

# print the results
    print(f"Saved {len(rows)} rows to {OUTPUT_FILE}\n")
    print("Category counts:")
    for category, count in sorted(category_counts.items()):
        print(f"- {category}: {count}")

    if top_review is not None:
        top_category = top_review.get("category", "unknown")
        top_votes = top_review.get("helpful_votes", 0)
        print("\nTop-voted review:")
        print(f"- category: {top_category}")
        print(f"- helpful_votes: {top_votes}")
    else:
        print("\nTop-voted review: none found")

# run the main function
if __name__ == "__main__":
    main()
