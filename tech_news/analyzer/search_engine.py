from tech_news.database import search_news

def search_by_title(title):
    """Seu código deve vir aqui"""
    result = []
    db_result = search_news({"title": {"$regex": title, "$options": "i"}})

    if len(db_result) == 1:
        result.append((db_result[0]["title"], db_result[0]["url"]))

    return result


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
