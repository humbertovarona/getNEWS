def fetch_news(api_key, page_size=100, country='us', language='en'):
    headlines = []
    total_results = None
    page = 1

    while total_results is None or len(headlines) < total_results:
        params = {
            'apiKey': api_key,
            'pageSize': page_size,
            'page': page,
            'country': country,
            'language': language
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            headlines.extend(data.get('articles', []))
            if total_results is None:
                total_results = data.get('totalResults', 0)
            page += 1
        else:
            print(f'Error fetching page {page}:', response.status_code)
            print(response.text)
            break
        if len(headlines) >= total_results or len(data.get('articles', [])) < page_size:
            break
    return headlines
