import tkinter as tk
import random

# Set up the game window
WIDTH = 800
HEIGHT = 600
root = tk.Tk()
root.title("Ping Pong Game")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Set up the game elements
player_score = 0
opponent_score = 0

# Create the player paddle
player_paddle = canvas.create_rectangle(50, 250, 70, 350, fill="blue")

# Create the opponent paddle
opponent_paddle = canvas.create_rectangle(730, 250, 750, 350, fill="red")

# Create the ball
ball = canvas.create_oval(395, 295, 405, 305, fill="black")

# Set the initial ball speed
dx = 50
dy = 50

# Move the ball
def move_ball():
    global dx, dy, player_score, opponent_score
    canvas.move(ball, dx, dy)
    ball_pos = canvas.coords(ball)
    if ball_pos[0] <= 0:
        dx = 5
        opponent_score += 1
        canvas.itemconfigure(opponent_score_label, text="Opponent Score: {}".format(opponent_score))
    if ball_pos[1] <= 0:
        dy = 5
    if ball_pos[2] >= WIDTH:
        dx = -5
        player_score += 1
        canvas.itemconfigure(player_score_label, text="Player Score: {}".format(player_score))
    if ball_pos[3] >= HEIGHT:
        dy = -5
    if canvas.coords(ball)[0] <= canvas.coords(player_paddle)[2] and canvas.coords(ball)[3] >= canvas.coords(player_paddle)[1] and canvas.coords(ball)[1] <= canvas.coords(player_paddle)[3]:
        dx = 5
    if canvas.coords(ball)[2] >= canvas.coords(opponent_paddle)[0] and canvas.coords(ball)[3] >= canvas.coords(opponent_paddle)[1] and canvas.coords(ball)[1] <= canvas.coords(opponent_paddle)[3]:
        dx = -5
    root.after(25, move_ball)

# Move the player paddle
def move_player_paddle(event):
    if event.keysym == "Up":
        canvas.move(player_paddle, 0, -60)
    elif event.keysym == "Down":
        canvas.move(player_paddle, 0, 60)

# Move the opponent paddle
def move_opponent_paddle():
    ball_center = canvas.coords(ball)[1] + 10
    paddle_center = canvas.coords(opponent_paddle)[1] + 50
    if ball_center > paddle_center:
        canvas.move(opponent_paddle, 0, 2)
    elif ball_center < paddle_center:
        canvas.move(opponent_paddle, 0, -4)
    root.after(25, move_opponent_paddle)

# Create the score labels
player_score_label = canvas.create_text(100, 50, text="Player Score: 0", font=("Helvetica", 16))
opponent_score_label = canvas.create_text(700, 50, text="Opponent Score: 0", font=("Helvetica", 16))

# Bind the player paddle movement to the arrow keys
canvas.bind_all("<Up>", move_player_paddle)
canvas.bind_all("<Down>", move_player_paddle)

# Start the game loop
move_ball()
move_opponent_paddle()

root.mainloop()
