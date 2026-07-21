# ANUMANA 🎯

ANUMANA is a minimal number-deduction web game built using Django. The objective is simple but mentally challenging: guess a hidden 4-digit number with **zero hints**, relying purely on logic and deduction.
---
## 🧠 How It Works
* The system generates a random 4-digit number.
* It is displayed as: `XXXX`
* Players enter their guesses through the UI.
* After each guess:
  * Correct digits in the correct position are revealed.
  * Incorrect digits remain hidden as `X`.

### Example:
```
Hidden Number: 5673
Your Guess:    1234
Result:        XX3X
```

* Only the **3rd digit is correct and correctly placed**.
* The rest are incorrect or misplaced.
## ⚙️ Project Structure

* `index.html`
  Contains the frontend UI for user interaction (input field, buttons, display of results and attempts).

* `views.py`
  Handles the game logic, session management, and request-response cycle.
---
## 🔍 Core Logic Overview

### `checker(ognum, gnum)`

* Compares original number with guessed number.
* Returns:

  * Count of correctly placed digits
  * A masked string (e.g., `XX3X`)

### `home(request)`

* Initializes session with:

  * Random number (`num`)
  * Attempt history (`attempts`)
* Handles:

  * User input validation
  * Guess processing
  * Result display
  * Game reset functionality

---

## 🔄 Features

* Session-based gameplay (state persists per user)
* Attempt tracking
* Instant feedback after each guess
* Reset option to start a new game
* Clean and simple UI

---

## 🚀 How to Run

1. Clone the repository
2. Install Django

   ```
   pip install django
   ```
3. Run the server

   ```
   python manage.py runserver
   ```
4. Open in browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## 🎮 Gameplay Goal

Use logical deduction to narrow down possibilities and correctly identify the hidden number in the fewest attempts possible.

Thanks for readingggg :)))
