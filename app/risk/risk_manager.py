class RiskManager:

    def __init__(self):
        self.max_drawdown = 0.08
        self.max_position = 0.3

    def check(self, drawdown, position_ratio):

        if drawdown > self.max_drawdown:
            return False

        if position_ratio > self.max_position:
            return False

        return True
