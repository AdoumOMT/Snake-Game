import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Serpent")
        
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()
        
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.snake_direction = "Right"
        self.food_position = self.place_food()
        self.score = 0
        
        self.master.bind("<Key>", self.change_direction)
        self.game_over = False
        
        self.update_game()
    
    def place_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)
    
    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.snake_direction = event.keysym
    
    def update_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_collisions()
            self.draw_elements()
            self.master.after(100, self.update_game)
    
    def move_snake(self):
        head_x, head_y = self.snake[0]
        
        if self.snake_direction == "Up":
            head_y -= 10
        elif self.snake_direction == "Down":
            head_y += 10
        elif self.snake_direction == "Left":
            head_x -= 10
        elif self.snake_direction == "Right":
            head_x += 10
        
        new_head = (head_x, head_y)
        print(f"Moving to: {new_head}")
        self.snake.insert(0, new_head)
        
        if new_head == self.food_position:
            self.score += 1
            self.food_position = self.place_food()
        else:
            self.snake.pop()
    
    def check_collisions(self):
        head_x, head_y = self.snake[0]
        
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over = True
        
        if len(self.snake) != len(set(self.snake)):
            self.game_over = True
    
    def draw_elements(self):
        self.canvas.delete(tk.ALL)
        
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green")
        
        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill="red")
        
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white")

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()