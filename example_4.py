class ScoreLimitExceededError(Exception):
    def __init__(self, message="Score limit exceeded. Maximum score is 1000."):
        super().__init__(message)

class GameScore:
    def __init__(self):
        self.score = 0

    def add_score(self, points):
        if self.score + points > 1000:
            raise ScoreLimitExceededError()
        self.score += points

    def subtract_score(self, points):
        if self.score - points < 0:
            raise ValueError("Score cannot be negative.")
        self.score -= points

    def get_score(self):
        return self.score

def main():
    game_score = GameScore()

    while True:
        print(f"Current score: {game_score.get_score()}")
        action = input("Choose an action (add/subtract/exit): ").strip().lower()

        if action == 'add':
            try:
                points = int(input("Enter points to add: "))
                game_score.add_score(points)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except ScoreLimitExceededError as e:
                print(e)

        elif action == 'subtract':
            try:
                points = int(input("Enter points to subtract: "))
                game_score.subtract_score(points)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except ValueError as e:
                print(e)

        elif action == 'exit':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid action. Please choose 'add', 'subtract', or 'exit'.")

if __name__ == "__main__":
    main()
