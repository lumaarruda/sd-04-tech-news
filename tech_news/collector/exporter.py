import csv

# from ..database import find_news


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    print(filepath)
    if not filepath.endswith(".csv"):
        raise ValueError("Formato Invalido")
    try:
        with open(filepath) as file:
            print(file)

    except FileNotFoundError:
        raise ValueError("Arquivo inexistente")
