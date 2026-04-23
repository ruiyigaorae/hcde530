import csv
import json
import ssl
from collections import Counter
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen


API_URL = "https://www.federalregister.gov/api/v1/documents.json"
OUTPUT_FILE = "week4_federal_register.csv"
MIN_RECORDS = 50
PER_PAGE = 20


def fetch_page(page: int) -> dict:
    """
    The endpoint returns JSON with metadata (like total count and pages)
    and a `results` list of document objects for the requested page.
    """
    # Query parameters used:
    # - conditions[term]: full-text search term across Federal Register documents.
    # - page: which pagination page to request.
    # - per_page: number of records returned per page.
    params = {
        "conditions[term]": "artificial intelligence",
        "page": page,
        "per_page": PER_PAGE,
    }
    url = f"{API_URL}?{urlencode(params)}"

    try:
        with urlopen(url) as response:
            return json.loads(response.read().decode("utf-8"))
    except URLError as error:
        if "CERTIFICATE_VERIFY_FAILED" not in str(error):
            raise
        # Fallback for local environments missing root certificates.
        insecure_context = ssl._create_unverified_context()
        with urlopen(url, context=insecure_context) as response:
            return json.loads(response.read().decode("utf-8"))


def main() -> None:
    rows: list[dict] = []
    type_counts: Counter[str] = Counter()
    page = 1
    api_total_count: int | None = None

    while len(rows) < MIN_RECORDS:
        payload = fetch_page(page)
        if api_total_count is None:
            api_total_count = payload.get("count")

        documents = payload.get("results", [])
        if not documents:
            break

        for doc in documents:
            # title: the headline/title of the Federal Register document.
            title = doc.get("title", "")
            # publication_date: date the document was published (YYYY-MM-DD).
            publication_date = doc.get("publication_date", "")
            # agency_names: agencies responsible for issuing the document.
            agency_names = doc.get("agency_names", [])
            # document_number: unique Federal Register document identifier.
            document_number = doc.get("document_number", "")
            # type: document class (for example RULE, PROPOSED RULE, NOTICE).
            doc_type = doc.get("type", "UNKNOWN")

            if isinstance(agency_names, list):
                agency_names_text = "; ".join(agency_names)
            else:
                agency_names_text = str(agency_names)

            rows.append(
                {
                    "title": title,
                    "publication_date": publication_date,
                    "agency_names": agency_names_text,
                    "document_number": document_number,
                    "type": doc_type,
                }
            )
            type_counts[doc_type] += 1

        page += 1

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "title",
                "publication_date",
                "agency_names",
                "document_number",
                "type",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} records to {OUTPUT_FILE}")
    if api_total_count is not None:
        print(f"Total documents matching search term in API: {api_total_count}")

    print("Document types found in downloaded records:")
    for doc_type, count in sorted(type_counts.items()):
        print(f"- {doc_type}: {count}")


if __name__ == "__main__":
    main()
