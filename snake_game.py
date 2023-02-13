import tkinter as tk
from PIL import Image, ImageTk
MOVES_PER_SPEED = 25
GAME_SPEED = 1000//MOVES_PER_SPEED


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)
        self.score = 0
        self.load_assets()
        self.create_objects()
        self.after(GAME_SPEED, self.perform_actions)

    def create_objects(self):
        self.create_text(
            45, 12, text=f"Score {self.score}", tag="score", fill="white", font=("TkDefaultFont", 14))

        self.create_rectangle(7, 27, 593, 613, outline="#525d69")
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position,
                              image=self.snake_body, tag="snake")
        self.create_image(*self.food_position, image=self.food, tag="food")

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)

        except IOError as err:
            print("IOERROR")
            root.destroy()

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        new_head_position = (head_x_position + 20, head_y_position)
        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):

            self.coords(segment, position)

    def perform_actions(self):
        self.move_snake()
        self.after(GAME_SPEED, self.perform_actions)

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]
        # todo


root = tk.Tk()
root.title('snake')
root.resizable(False, False)
board = Snake()
board.pack()

root.mainloop()
