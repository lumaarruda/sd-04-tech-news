import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def collector_menu():
    """Seu código deve vir aqui"""
    menu_collector = input("Selecione uma das opções a seguir:\n"
                           " 1 - Importar notícias a partir de um arquivo CSV;\n"
                           " 2 - Exportar notícias para CSV;\n"
                           " 3 - Raspar notícias online;\n"
                           " 4 - Sair.\n"
                           )

    if menu_collector == "1":
        import_csv = input("Digite o nome do arquivo CSV a ser importado: ")
        importer = csv_importer(import_csv)
        return create_news(importer)
    elif menu_collector == "2":
        export_csv = input("Digite o nome do arquivo CSV a ser exportado: ")
        return csv_exporter(export_csv)
    elif menu_collector == "3":
        qtd_pages = input("Digite a quantidade de páginas a serem raspadas: ")
        news = scrape(fetcher=fetch_content, pages=int(qtd_pages))
        return create_news(news)
    elif collector_menu == "4":
        return print('Encerrando script\n')
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    """Seu código deve vir aqui"""
    menu_analyzer = input("Selecione uma das opções a seguir:\n"
                          " 1 - Buscar notícias por título;\n"
                          " 2 - Buscar notícias por data;\n"
                          " 3 - Buscar notícias por fonte;\n"
                          " 4 - Buscar notícias por categoria;\n"
                          " 5 - Listar top 5 notícias;\n"
                          " 6 - Listar top 5 categorias;\n"
                          " 7 - Sair."
                          )

    if menu_analyzer == "1":
        return search_by_title(input("Digite o titulo:"))
    elif menu_analyzer == "2":
        return search_by_date(input("Digite a data no formato aaaa-mm-dd:"))
    elif menu_analyzer == "3":
        return search_by_source(input("Digite a fonte:"))
    elif menu_analyzer == "4":
        return search_by_category(input("Digite a categoria:"))
    elif menu_analyzer == "5":
        return top_5_news()
    elif menu_analyzer == "6":
        return top_5_categories()
    elif menu_analyzer == "7":
        return print("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")
