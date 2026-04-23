import csv
import json
import ssl
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen


API_URL = "https://hcde530-week4-api.onrender.com/reviews"
TOTAL_REVIEWS = 500
PAGE_SIZE = 100
OUTPUT_FILE = "week4_results.csv"


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

    for offset in range(0, TOTAL_REVIEWS, PAGE_SIZE):
        reviews = fetch_page(offset=offset, limit=PAGE_SIZE)
        if not reviews:
            break

        for review in reviews:
            category = review.get("category", "")
            helpful_votes = review.get("helpful_votes", 0)
            print(f"category: {category}, helpful_votes: {helpful_votes}")
            rows.append((category, helpful_votes))

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["category", "helpful_votes"])
        writer.writerows(rows)

    print(f"\nSaved {len(rows)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
