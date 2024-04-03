import random
import tkinter as tk

# Global variables to track game results
won = 0
Lost = 0
Tie = 0

def Game(rules_window):
    global won, Lost, Tie
    
    rules_window.destroy()  # Destroy the rules window

    # Create the game window
    game_window = tk.Toplevel(start)
    game_window.title("Game")
    game_window.geometry("600x500")

    def winner(player, computer):
        global won, Lost, Tie
        
        if player == computer:
            Tie += 1
            return "It is a Tie 1"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            won += 1
            return "Hooray you won this round!"
        else:
            Lost += 1
            return "Computer won this round"
    
    def play_again():
        play_again_window = tk.messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again_window:
            game_window.destroy()
            Game(start)
        else:
            start.deiconify()  

    # Labels
    instruction_label = tk.Label(game_window, text="Remember the Rules: You move first:")
    instruction_label.grid(row=0, column=0, columnspan=3)

    result_label = tk.Label(game_window, text="")
    result_label.grid(row=2, column=0, columnspan=3)

    # Buttons
    def play_game(choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = winner(choice, computer_choice)
        result_label.config(text=f"Computer chose: {computer_choice}\nResult: {result}\n\n"
                                  f"Results:\nWins: {won}\nLosses: {Lost}\nTies: {Tie}")
        play_again()

    rock_button = tk.Button(game_window, text="Rock", width=10, command=lambda: play_game("Rock"))
    rock_button.grid(row=1, column=0)

    paper_button = tk.Button(game_window, text="Paper", width=10, command=lambda: play_game("Paper"))
    paper_button.grid(row=1, column=1)

    scissors_button = tk.Button(game_window, text="Scissors", width=10, command=lambda: play_game("Scissors"))
    scissors_button.grid(row=1, column=2)

def rules(root):
    root.withdraw()

    # Rules window
    rule_window = tk.Toplevel(root)
    rule_window.title("Rules")
    rule_window.geometry("600x500")

    # Labels
    label = tk.Label(rule_window, text="Here are the game RULEs\n\nROCK WINS OVER SCISSOR\nPAPER WINS OVER ROCK\nSCISSOR WINS OVER PAPER\nAND VICE VERSA They LOOSE")
    label.pack()

    # Proceed button to start the game
    proceed_button = tk.Button(rule_window, text="Proceed", command=lambda: Game(rule_window))
    proceed_button.pack()

def start():
    start.destroy()

# Main window
start = tk.Tk()
start.title("Rock, Paper, Scissors Game")
start.configure(bg='purple')
start.resizable(True,True)
start.geometry("600x500")

# Labels
welcome_label = tk.Label(start, text="Welcome to my app. Let's play a game!", font=("Helvetica", 20), bg="purple", fg="white")
welcome_label.pack(pady=20)

# Buttons
PlayttButton = tk.Button(start, text="Play", command=lambda: rules(start))
PlayttButton.pack()

Exit = tk.Button(start, text="Quit", command=start.destroy)
Exit.pack()

# Centering content
start.update_idletasks()
width = start.winfo_width()
height = start.winfo_height()
x = (start.winfo_screenwidth() // 2) - (width // 2)
y = (start.winfo_screenheight() // 2) - (height // 2)
start.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Run the Tkinter event loop
start.mainloop()
