def get_news(api_key):
    conn = setup_database()
    headlines = fetch_news(api_key)
    for article in headlines:
        newstitle = article['title']
        if newstitle == '[Removed]' or title_exists_in_db(conn, newstitle):
            continue
        source = article['source']['name']
        date_time = article['publishedAt']
        url = article['url']
        categories = categorize_headline(newstitle)
        news_item = (date_time, newstitle, source, categories, url)
        save_news_to_db(conn, news_item)
    conn.close()
