import tkinter as tk

WIDTH = 800
HEIGHT = 500
SHIP_SPEED = 5
BULLET_SPEED = 10
BULLET_WIDTH = 15
BULLET_HEIGHT = 4
SHIP_WIDTH = 50
SHIP_HEIGHT = 30

class SideShooter:
    def __init__(self, root):
        self.root = root
        self.root.title("侧面射击游戏")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.ship_y = HEIGHT // 2
        self.ship_x = 30
        self.bullets = []
        self.keys = set()

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)

        self.draw_ship()
        self.game_loop()

    def draw_ship(self):
        self.canvas.delete("ship")
        x, y = self.ship_x, self.ship_y
        self.canvas.create_polygon(
            x, y,
            x + SHIP_WIDTH, y - SHIP_HEIGHT // 2,
            x + SHIP_WIDTH, y + SHIP_HEIGHT // 2,
            fill="cyan", outline="white", tags="ship"
        )
        self.canvas.create_rectangle(
            x - 10, y - 8, x, y + 8,
            fill="orange", tags="ship"
        )

    def on_key_press(self, event):
        self.keys.add(event.keysym)
        if event.keysym == "space":
            self.shoot()

    def on_key_release(self, event):
        self.keys.discard(event.keysym)

    def shoot(self):
        bullet_id = self.canvas.create_rectangle(
            self.ship_x + SHIP_WIDTH,
            self.ship_y - BULLET_HEIGHT // 2,
            self.ship_x + SHIP_WIDTH + BULLET_WIDTH,
            self.ship_y + BULLET_HEIGHT // 2,
            fill="yellow", outline="red"
        )
        self.bullets.append({"id": bullet_id, "x": self.ship_x + SHIP_WIDTH})

    def update_ship(self):
        if "Up" in self.keys or "w" in self.keys or "W" in self.keys:
            if self.ship_y - SHIP_HEIGHT // 2 > 0:
                self.ship_y -= SHIP_SPEED
        if "Down" in self.keys or "s" in self.keys or "S" in self.keys:
            if self.ship_y + SHIP_HEIGHT // 2 < HEIGHT:
                self.ship_y += SHIP_SPEED
        self.draw_ship()

    def update_bullets(self):
        new_bullets = []
        for bullet in self.bullets:
            bullet["x"] += BULLET_SPEED
            self.canvas.move(bullet["id"], BULLET_SPEED, 0)
            if bullet["x"] < WIDTH:
                new_bullets.append(bullet)
            else:
                self.canvas.delete(bullet["id"])
        self.bullets = new_bullets

    def game_loop(self):
        self.update_ship()
        self.update_bullets()
        self.root.after(16, self.game_loop)

def main():
    root = tk.Tk()
    game = SideShooter(root)
    root.mainloop()

if __name__ == "__main__":
    main()