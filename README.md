# Rock-Paper-Scissor Game

This is a simple Rock-Paper-Scissor game implemented in Python. The computer randomly selects one of the three options (Rock, Paper, or Scissor), and the user is prompted to make their choice. The game then determines the winner based on the rules of Rock-Paper-Scissor.

## How to Play

1. Run the Python script.
2. Enter your choice when prompted (`Rock`, `Paper`, or `Scissor`).
3. The computer will also make a choice.
4. The game will then display whether you won, lost, or if the match is a tie.

## Rules

- **Rock vs Scissor**: Rock wins.
- **Paper vs Rock**: Paper wins.
- **Scissor vs Paper**: Scissor wins.
- If both choices are the same, the match is a tie.

## Code Explanation

- The `random` module is used to allow the computer to make a random choice from the list `['Rock', 'Paper', 'Scissor']`.
- The user's choice is taken as input and compared with the computer's choice.
- Based on the comparison, the game will determine the outcome (Win, Lose, or Tie).

## Example Usage

```bash
Enter your choice [Rock/Paper/Scissor] = Rock
You won! Rock smashes scissor!
