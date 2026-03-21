# 🎯 Number Guessing Game
A simple, beginner-friendly command-line game written in Python where you try to guess a randomly generated number. After each guess, the game tells you whether to go higher or lower.



## 📋 Features
- Random number generation between 1 and 100
- Helpful hints after every guess (`Too high!` / `Too low!` / `Correct!`)
- Tracks the number of attempts per round
- Input validation — handles non-numeric and out-of-range entries gracefully
- Replay option after each round
- Clean, well-documented code with docstrings
- Unit tests included



## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No external libraries required — uses only the Python standard library

### Running the Game
```bash
# Clone the repository
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game

# Run the game
python game.py
```



## 🎮 How to Play
1. The game picks a secret number between **1 and 100**.
2. Enter your guess when prompted.
3. The game will tell you:
   - `Too low!` — guess higher
   - `Too high!` — guess lower
   - `Correct!` — you win! 🎉
4. Your attempt count is shown when you guess correctly.
5. Choose to play again or exit.

### Example Session

```
========================================
   Welcome to the Number Guessing Game!
========================================

🎯 I'm thinking of a number between 1 and 100.
Can you guess what it is?

Enter your guess (1-100): 50
  → Too high!
Enter your guess (1-100): 25
  → Too low!
Enter your guess (1-100): 37
  → Correct!

🎉 You got it in 3 attempts!

Play again? (yes/no): no

Thanks for playing! Goodbye! 👋
```



## 🧪 Running the Tests

```bash
python -m unittest test_game.py -v
```

The test suite covers:
- Random number generation within valid ranges
- Hint logic for all cases (too low, too high, correct)
- Player input validation (invalid types, out-of-range values, boundary values)



## 📁 Project Structure
```
number-guessing-game/
├── game.py          # Main game logic
├── test_game.py     # Unit tests
└── README.md        # Project documentation
```


## 🛠️ Built With

- **Python 3** — core language
- **random** — standard library module for number generation
- **unittest** — standard library module for testing



## 📄 License
This project is open source and available under the [MIT License](LICENSE).
