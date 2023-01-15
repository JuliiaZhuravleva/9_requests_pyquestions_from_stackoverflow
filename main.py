import requests
import datetime


def date_days_ago(days):
    today = datetime.datetime.today()
    today2 = today.replace(hour=0, minute=0, second=0, microsecond=0)
    difference = datetime.timedelta(days=days)
    required_date = today2 - difference
    return required_date


def get_last_py_questions():
    url = 'https://api.stackexchange.com/2.3/questions'
    datefrom = int(date_days_ago(2).timestamp())
    params = {'fromdate': datefrom, 'tagged': 'Python', 'site': 'stackoverflow', 'order': 'desc', 'sort': 'creation'}
    py_questions = requests.get(url, params=params).json()
    for question in py_questions['items']:
        print(question['title'])


if __name__ == '__main__':
    get_last_py_questions()



