def title_exists_in_db(conn, title):
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM news WHERE title = ?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    return result[0] > 0
