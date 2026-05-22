# FAQ - Number Guessing Game

## 1. What is the Number Guessing Game?
It is a simple interactive game where the player tries to guess a randomly generated number within a limited number of attempts.

---

## 2. Which technologies are used in this project?
This project uses:
- HTML
- CSS
- JavaScript

---

## 3. How does the game work?
The game generates a random number. The player enters guesses, and the system provides hints such as:
- Too High
- Too Low
- Correct Guess

---

## 4. Is this project beginner-friendly?
Yes. It is ideal for beginners learning:
- DOM manipulation
- JavaScript events
- Conditional logic
- Random number generation

---

## 5. Does the game generate a new number every time?
Yes. A new random number is generated whenever the game restarts.

---

## 6. Can I change the guessing range?
Yes. Modify the random number generation logic inside the JavaScript file.

Example:
```javascript
Math.floor(Math.random() * 100) + 1
