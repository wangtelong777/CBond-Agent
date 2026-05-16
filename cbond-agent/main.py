import time

from app.data.collector import get_cbond_data
from app.strategies.premium_strategy import PremiumStrategy
from app.trader.trader import Trader
from app.risk.risk_manager import RiskManager
from app.notifier.telegram_bot import send_message
from app.agents.sentiment_agent import analyze_market

strategy = PremiumStrategy()
trader = Trader()
risk_manager = RiskManager()

def run():

    while True:

        try:

            df = get_cbond_data()

            for _, row in df.iterrows():

                signal = strategy.generate_signal(row)

                code = row['代码']

                if signal == 'BUY':

                    if risk_manager.check(0.03, 0.2):

                        trader.buy(code, 100)

                        send_message(f"BUY {code}")

                elif signal == 'SELL':

                    trader.sell(code, 100)

                    send_message(f"SELL {code}")

            news = "今日可转债市场情绪较强"

            ai_result = analyze_market(news)

            print(ai_result)

            time.sleep(60)

        except Exception as e:

            print(e)

            time.sleep(10)

if __name__ == '__main__':
    run()
