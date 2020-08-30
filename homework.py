import datetime as dt


class Calculator:
    def __init__(self,limit):
        self.limit=limit
        self.records=[]
    def add_record(self,r):
        self.records.append(r)
    def get_today_stats(self):
        stats=0
        for rec in self.records:
            if rec.date==dt.date.today():
                stats+=rec.amount
        return stats
    def get_week_stats(self):
        stats=0
        for rec in self.records:
            if dt.date.today()-dt.timedelta(days=7)<rec.date<=dt.date.today():
                stats+=rec.amount
        return stats



class Record:
    def __init__(self,amount,comment,date=dt.date.today().strftime('%d.%m.%Y')):
        self.amount=amount
        self.date=dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment=comment


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats(self)<self.limit:
            N=self.limit-self.get_today_stats(self)
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {N} кКал"
        else:
            return "Хватит есть!"



class CashCalculator(Calculator):
    (USD_RATE,EURO_RATE)=(74.64,88.74)
    currency_translate=[{}]
    def get_today_cash_remained(self,currency):
        if self.get_today_stats(self)<self.limit:
            N=self.limit-self.get_today_stats(self)
            return f"На сегодня осталось {N} {currency}"
        elif self.get_today_stats(self)==self.limit:
            return "Денег нет, держись"
        else:
            N=self.get_today_stats()-self.limit
            return f"Денег нет, держись: твой долг - {N} {currency}"