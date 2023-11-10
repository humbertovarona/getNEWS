def setup_database():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            date_time TEXT,
            title TEXT,
            source TEXT,
            category TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    return conn
