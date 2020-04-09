from datetime import timedelta, datetime
from random import randint


class Week:
    def __init__(self, start=datetime.now()) -> None:
        self.start = start.strftime('%d-%m-%y')
        self.end = (start + timedelta(days=7)).strftime('%d-%m-%y')
        self.week_days = self.get_weekdays(start)

    def get_weekdays(self, start):
        weekdays = []
        for i in range(8):
            weekdays.append((start + timedelta(days=i)).strftime('%d-%m-%y'))
        return weekdays


def get_weather_for_date(day):
    return randint(5, 15)
