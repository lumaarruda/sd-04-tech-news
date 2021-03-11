import datetime
from pymongo import MongoClient
client = MongoClient()


def find_news():
    db = client.tech_news
    data = db.news.find({}, {"_id": 0})
    return data


def search_by_title(title):
    data = find_news()
    results = []
    for new in data:
        if title.lower() in new["title"].lower():
            results.append((new["title"], new["url"]))

    return results


def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    data = find_news()
    results = []
    for new in data:
        if date in new["timestamp"]:
            results.append((new["title"], new["url"]))

    return results


def search_by_source(source):
    data = find_news()
    results = []
    for new in data:
        new["sources"] = map(lambda x: x.lower(), new["sources"])
        if source.lower() in new["sources"]:
            results.append((new["title"], new["url"]))

    return results


def search_by_category(category):
    data = find_news()
    results = []

    for new in data:
        new["categories"] = map(lambda x: x.lower(), new["categories"])
        if category.lower() in new["categories"]:
            results.append((new["title"], new["url"]))

    return results
