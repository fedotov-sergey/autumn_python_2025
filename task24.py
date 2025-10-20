# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов
from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>Document</title>

</head>
<body>
    <h1>Cat</h1>
    <p> Some shit on html document</p>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZPidQfIOQJ91KT-cboTNmWvjRUYuVIeUfXmDKG5O3Dc47hiC3x4GOj9jNI6wQHtUVZ3UDt5vh4w7CyYl0sBAV0etkMUfEg20z0CJTn2KjWQ">
    <ul>
        <li> Котенок маленький </li>
        <li> Котенок по больше </li>
        <li> Котенок большой </li
    </ul>
    <a href="https://en.wikipedia.org/wiki/Kitten">Kitten</a>
    <div id="321123312312312">
    <table>
        <tr>
            <td> String 1 </td>
            <td> String 2 </td>
        </tr>
        <tr>
            <td> String 1 </td>
            <td> String 2 </td>
        </tr>
    </table>
    </div>
</body>
</html>
"""


@app.route("/about_company")
def about_company():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>О компании</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.1/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-50 text-gray-800">
        <div class="max-w-4xl mx-auto py-20 px-6">
            <h1 class="text-4xl font-bold text-blue-700 mb-6">О компании</h1>
            <p class="text-lg leading-relaxed">
                Наша компания занимается [Пишет код] и успешно работает на рынке уже более [двух недель].
                Мы ценим инновации, честность и результат.
            </p>
            <p class="mt-4">
                Наша миссия — [Писать код].
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/contact")
def contact():
    return """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Контакты</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.1/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-blue-50 text-gray-900">
    <div class="max-w-4xl mx-auto py-20 px-6">
        <h1 class="text-4xl font-bold text-blue-700 mb-6">Контакты</h1>
        <p><strong>Адрес:</strong> [ул. Плюшкина, дом Колотушкина]</p>
        <p><strong>Телефон:</strong> <a href="tel:[Хороший номер]" class="text-blue-700">[Mobile phone]</a></p>
        <p><strong>Email:</strong> <a href="mailto:[person@email.ru]" class="text-blue-700">[frederico@gmail.com]</a></p>
        <p><strong>Сайт:</strong> <a href="http://127.0.0.1:5000/" class="text-blue-700">[http]</a></p>

        <div class="mt-6">
            <h2 class="text-2xl font-semibold mb-2">Соцсети:</h2>
            <ul class="list-disc pl-5">
                <li><a href="[Instagram]" class="text-blue-700">Instagram</a></li>
                <li><a href="[Telegram]" class="text-blue-700">Telegram</a></li>
                <li><a href="[LinkedIn]" class="text-blue-700">LinkedIn</a></li>
            </ul>
        </div>
    </div>
</body>
</html>
"""


@app.route("/posts")
def posts():
    return """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Посты</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.1/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 text-gray-900">
    <div class="max-w-5xl mx-auto py-20 px-6">
        <h1 class="text-4xl font-bold text-blue-700 mb-8">Последние посты</h1>

        <div class="grid md:grid-cols-3 gap-6">
            <article class="bg-white shadow rounded-2xl p-6 hover:shadow-lg transition">
                <h2 class="text-xl font-semibold text-blue-700 mb-2">[Пост о контактах компании]</h2>
                <p class="text-gray-600 mb-4">[Ссылочка на контакты компании]</p>
                <a href="http://127.0.0.1:5000/contact" class="text-blue-700 hover:underline">Читать далее →</a>
            </article>

            <article class="bg-white shadow rounded-2xl p-6 hover:shadow-lg transition">
                <h2 class="text-xl font-semibold text-blue-700 mb-2">[Пост о компании]</h2>
                <p class="text-gray-600 mb-4">[ссылочка на страницу о компании]</p>
                <a href="http://127.0.0.1:5000/about_company" class="text-blue-700 hover:underline">Читать далее →</a>
            </article>

            <article class="bg-white shadow rounded-2xl p-6 hover:shadow-lg transition">
                <h2 class="text-xl font-semibold text-blue-700 mb-2">[ЗРИШЬ В КОРЕНЬ]</h2>
                <p class="text-gray-600 mb-4">[Переход на корневую страницу с котенком]</p>
                <a href="http://127.0.0.1:5000/" class="text-blue-700 hover:underline">Читать далее →</a>
            </article>
        </div>
    </div>
</body>
</html>
"""
