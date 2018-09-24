from datetime import datetime

from flask import Flask, abort, request

from req import get_weather
from news_list import all_news

city = 'Moscow'
units = 'metric'
apikey = 'e751b4fd7076834880632dfd3c73b996'

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units={}'.format(
        city, apikey, units)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    result = '<p><b>Температура:</b> {}</p>'.format(weather['main']['temp'])
    result += '<p><b>Город:</b> {}</p>'.format(weather['name'])
    result += '<p><b>Дата:</b> {}</[>'.format(cur_date)
    return result


@app.route('/news')
def all_the_news():
    colors = ['green', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color', 'black') if request.args.get(
        'color') in colors else 'black'
    return '<h1 style="color: {}">News: <small>{}</small></h1>'.format(color, limit)


@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p><i>%(text)s</i></p>'
        result = result % news_to_show[0]
        return result
    else:
        return abort(404)


if __name__ == '__main__':
    app.run()
