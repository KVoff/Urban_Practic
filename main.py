"""
Точка входа в программу для анализа и визуализации данных об акциях.

Запрашивает у пользователя тикер и период, а так же процент колебания,
загружает данные, обрабатывает их и отображает результаты в виде графика.
"""

import data_download as dd
import data_plotting as dplt


def main():
    """
    Основная функция программы. Управляет процессом загрузки, обработки данных,
    проверки колебаний и визуализации.
    """

    print(
        "Добро пожаловать в инструмент получения и построения графиков "
        "биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: "
        "AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), "
        "AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, "
        "6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input(
        "Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input(
        "Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(
        input("Введите порог колебаний (в процентах, например, 5): "))

    # Загрузка данных об акциях
    stock_data = dd.fetch_stock_data(ticker, period)

    # Вывод средней цены закрытия
    dd.calculate_and_display_average_price(stock_data)

    # Уведомление о сильных колебаниях
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Добавление скользящего среднего
    stock_data = dd.add_moving_average(stock_data)

    # Построение графика
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
