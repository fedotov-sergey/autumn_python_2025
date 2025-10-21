# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.
from selectors import SelectSelector

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99", "18.99", "N/A", "¥5000"]
curses = {
    "₽": 1,
    "€": 110,
    "$": 70,
    "¥": 1 / 2,
}
result = [
    (
        float(p.replace("₽", "")) * curses["₽"]
        if "₽" in p
        else (
            float(p.replace("USD", "").replace("$", "")) * curses["$"]
            if "USD" in p or "$" in p
            else (
                float(p.replace("€", "")) * curses["€"]
                if "€" in p
                else (
                    float(p.replace("¥", "")) * curses["¥"]
                    if "¥" in p
                    else float(p) * curses["₽"] if p.replace(".", "", 1).isdigit() else None
                )
            )
        )
    )
    for p in prices
]
print(result)
