class PremiumStrategy:

    def __init__(self):
        self.buy_premium = 10
        self.sell_premium = 25

    def generate_signal(self, row):

        premium = row['转股溢价率']

        if premium < self.buy_premium:
            return "BUY"

        elif premium > self.sell_premium:
            return "SELL"

        return "HOLD"
