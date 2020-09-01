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
        if self.get_today_stats()<self.limit:
            N=self.limit-self.get_today_stats()
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {N} кКал"
        else:
            return "Хватит есть!"



class CashCalculator(Calculator):
    USD_RATE,EURO_RATE=74.64,88.74
    def get_today_cash_remained(self,currency):
        currency_translate={"rub":[1,"руб"], "usd":[self.USD_RATE,"USD"], "eur":[self.EURO_RATE,"Euro"]}
        if self.get_today_stats()<self.limit:
            N=round((self.limit-self.get_today_stats())/currency_translate[currency][0],2)
            return f"На сегодня осталось {N} {currency_translate[currency][1]}"
        elif self.get_today_stats()==self.limit:
            return "Денег нет, держись"
        else:
            N=round((self.get_today_stats()-self.limit)/currency_translate[currency][0],2)
            return f"Денег нет, держись: твой долг - {N} {currency_translate[currency][1]}"