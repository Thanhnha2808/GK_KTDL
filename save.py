import psycopg2

def save_to_db(articles):
    conn = psycopg2.connect(
        dbname="airflow", user="airflow", password="airflow", host="postgres"
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id SERIAL PRIMARY KEY,
        title TEXT,
        url TEXT,
        summary TEXT,
        time TEXT,
        author TEXT
    )
    """)

    for article in articles:
        cursor.execute(
            "INSERT INTO articles (title, url, summary, time, author) VALUES (%s, %s, %s, %s, %s)",
            (article["title"], article["url"], article["summary"], article["time"], article["author"]),
        )

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    from transform import clean_articles
    from crawl import crawl_articles

    articles = crawl_articles()
    cleaned_articles = clean_articles(articles)
    save_to_db(cleaned_articles)
