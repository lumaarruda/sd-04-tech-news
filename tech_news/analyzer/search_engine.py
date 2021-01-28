from tech_news import database


def search_by_title(title):
    db_result = database.search_news({"title": {"$regex": title, "$options": "i"}})
    search_result = []
    for news in db_result:
        search_result.append((news["title"], news["url"]))
    return search_result

def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""

search_by_title("vamos")