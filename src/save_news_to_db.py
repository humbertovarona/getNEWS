def save_news_to_db(conn, news_item):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO news (date_time, title, source, category, url)
        VALUES (?, ?, ?, ?, ?)
    ''', news_item)
    conn.commit()
