# getNEWS

Create a database of news headlines using the https://newsapi.org/ API key

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-May%2C%207%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```bash
pip install requests textblob
```

or

```bash
pip install -r requirements.txt
```

```python
import requests
import sqlite3
from textblob import TextBlob
```

## How to run

```python
API_KEY = 'Your API key here'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

get_news(API_KEY)
```
