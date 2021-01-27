import datetime
from tech_news.database import search_news, find_news


def search_by_title(title):
    tuples_list = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in data:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        tuples_list = []
        data = search_news({"timestamp": {"$regex": date}})
        for new in data:
            tuples_list.append((new["title"], new["url"]))
        return tuples_list


def search_by_source(source):
    tuples_list = []
    print(find_news())
    data = search_news({"sources": {"$regex": source, "$options": "i"}})
    for new in data:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list


def search_by_category(category):
    """Seu código deve vir aqui"""
