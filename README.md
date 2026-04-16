# Quiz-Game
# 🧠 Ultimate Python Quiz Challenge

A dynamic, terminal-based Quiz Game built with Python. This project uses Object-Oriented Programming (OOP) to deliver a randomized, interactive trivia experience.

## ✨ Features
*   **Object-Oriented Design:** Built using a `QuizGame` class for clean, scalable code.
*   **Randomized Questions:** Questions are shuffled every time you play so no two games are the same.
*   **Real-time Feedback:** Instant scoring and emoji-based feedback after every answer.
*   **Formatted UI:** Includes a "Big Text" ASCII art logo and clear separators for a better user experience.

## 🚀 Getting Started

### Prerequisites
*   **Python 3.x** installed on your machine.

### Installation & Running
1.  Clone the repository:
    ```bash
    git clone https://github.com
    ```
2.  Navigate to the project folder:
    ```bash
    cd quiz-game-python
    ```
3.  Run the game:
    ```bash
    python quiz.py
    ```

## 📂 Project Structure
*   `quiz.py`: The main engine of the game containing the logic and class structure.
*   `quizques.py`: The data module containing the `Question_bank` and `options` lists.
*   `art.py`: (Optional) Stores the ASCII art logos.

## 🎮 How to Play
1.  The game will present a question and 4 options (A, B, C, D).
2.  Type your choice and press **Enter**.
3.  The game will tell you if you are correct and display your current score.
4.  At the end, you'll see your final percentage and success rate!

## 📸 Preview
```text
  ___  _   _ ___ ________   _____   _   __  __ _____ 
 / _ \| | | |_ _|_  /  _ \ / _ \ \ / / |  \/  |  ___|

| | | | | | || |  / /| |_) | | | \ V /  | |\/| | |__  
| |_| | |_| || | / / |  _ <| |_| || |   | |  | |  __| 
 \__\_\\___/|___/___||_| \_\\___/ |_|   |_|  |_|_____|

Q.1: What is the capital city of France?
  A. Paris
  B. London
  C. France
  D. Europe
Enter your answer (A/B/C/D): A
✅ Correct!
