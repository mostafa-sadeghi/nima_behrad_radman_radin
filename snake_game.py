import tkinter as tk
from PIL import Image, ImageTk


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.load_assets()
        self.create_objects()

    def create_objects(self):
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position,
                              image=self.snake_body, tag="snake")

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)

        except IOError as err:
            print("IOERROR")
            root.destroy()


root = tk.Tk()
root.title('snake')
root.resizable(False, False)
board = Snake()
board.pack()

root.mainloop()
