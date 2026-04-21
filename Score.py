class SCORE:
    def __init__(self):
        try:
            with open('score.txt', 'r') as f:
                self.high_score = int(f.readline())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

        self.current_score = 0  # live score this run

    def add(self, points):
        self.current_score += points

    def deduct(self, points):
        self.current_score -= points

    def save(self):
        self.high_score = max(self.high_score, self.current_score)
        with open('score.txt', 'w') as f:
            f.write(str(self.high_score))