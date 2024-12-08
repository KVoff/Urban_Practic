"""
Модуль для загрузки и обработки данных об акциях.

Содержит функции для извлечения данных из интернета, расчёта скользящего среднего
и вычисления средней цены закрытия акций за период.
"""

import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
        Загружает исторические данные об акциях для указанного тикера и периода.

        Args:
            ticker (str): Тикер акции (например, 'AAPL' для Apple Inc).
            period (str): Период времени для загрузки данных (например, '1mo', '1y').

        Returns:
            pandas.DataFrame: Таблица с историческими данными о ценах акций.
        """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
        Добавляет колонку со скользящим средним в данные о ценах закрытия.

        Args:
            data (pandas.DataFrame): Таблица с историческими данными о ценах акций.
            window_size (int): Размер окна для расчёта скользящего среднего (по умолчанию 5).

        Returns:
            pandas.DataFrame: Таблица с добавленной колонкой 'Moving_Average'.
        """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
        Вычисляет и выводит среднюю цену закрытия акций за заданный период.

        Args:
            data (pandas.DataFrame): Таблица с историческими данными о ценах акций.
        """
    if 'Close' in data:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия за период: {average_price:.2f}")
    else:
        print("Ошибка: В предоставленных данных отсутствует колонка 'Close'.")


def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует данные и уведомляет о сильных колебаниях.

    Args:
        data (pandas.DataFrame): Таблица с историческими данными о ценах акций.
        threshold (float): Пороговое значение колебаний в процентах.

    Returns:
        None
    """
    if 'Close' not in data:
        print("Ошибка: В предоставленных данных отсутствует колонка 'Close'.")
        return

    max_price = data['Close'].max()
    min_price = data['Close'].min()

    fluctuation = ((max_price - min_price) / min_price) * 100

    if fluctuation > threshold:
        print(
            f"⚠️ Внимание! Цена акций колебалась более чем на {threshold}% за период.")
        print(
            f"Максимальная цена: {max_price:.2f}, Минимальная цена: {min_price:.2f}, "
            f"Колебание: {fluctuation:.2f}%")
    else:
        print(
            f"Цена акций оставалась в пределах {threshold}% колебаний за период.")
