from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    data = search_news(query)
    if not len(data):
        return []
    news_list = []
    for obj in data:
        news_list.append((obj["title"], obj["url"]))
    return news_list


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
