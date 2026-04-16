import csv
from collections import Counter
from pathlib import Path


def normalize_role(role: str) -> list[str]:
    """Split a role cell into separate roles and normalize spacing."""
    separators = ["/", ";", "|"]
    cleaned = role.strip()
    for separator in separators:
        cleaned = cleaned.replace(separator, ",")
    return [part.strip() for part in cleaned.split(",") if part.strip()]


def count_roles(csv_path: Path) -> Counter:
    counts: Counter = Counter()

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        if "role" not in (reader.fieldnames or []):
            raise ValueError("CSV must contain a 'role' column.")

        for row in reader:
            role_value = (row.get("role") or "").strip()
            if not role_value:
                continue
            counts.update(normalize_role(role_value))

    return counts


def main() -> None:
    csv_path = Path(__file__).with_name("demo_responses.csv")
    role_counts = count_roles(csv_path)

    print(f"Role counts for {csv_path.name}:")
    for role, count in role_counts.most_common():
        print(f"{role}: {count}")


if __name__ == "__main__":
    main()
