class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return "Deuce" if self.m_score1 >= 3 else f"{self.m_score_names[self.m_score1]}-All"
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self.m_score2
            if minus_result == 1:
                return f"Advantage {self.player1_name}"
            elif minus_result == -1:
                return f"Advantage {self.player2_name}"
            elif minus_result >= 2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"
        else:
            return f"{self.m_score_names[self.m_score1]}-{self.m_score_names[self.m_score2]}"

