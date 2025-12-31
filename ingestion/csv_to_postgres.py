import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="kara",
    user="kara",
    password="kara"
)

cur = conn.cursor()

insert_query = """
    INSERT INTO reviews (cid, review_str)
    VALUES (%s, %s)
    ON CONFLICT (cid) DO NOTHING
"""

with open("../data/movie_review.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute(
            insert_query,
            (int(row["cid"]), row["review_str"])
        )

conn.commit()
cur.close()
conn.close()

print("Ingestion completed safely")
