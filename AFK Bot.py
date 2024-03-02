import pyautogui as pag
import tkinter as tk
import random
import time
import threading

class AFKBOT:
    def __init__(self, root, afk):
        self.root = root
        self.root.title('AFKBOT')
        self.root.geometry('500x300')
        self.afk_mouse_on = False
        self.afk_keyboard_on = False
        self.afk_moukey_on = False
        self.afk_instance = afk
        self.afk_thread = None

        self.start_mouse_button = tk.Button(root, text="Mouse Only AFK", command=self.toggle_afk_mouse)
        self.start_keyboard_button = tk.Button(root, text="Keyboard Only AFK", command=self.toggle_afk_keyboard)
        self.start_moukey_button = tk.Button(root, text="Keyboard + Mouse AFK", command=self.toggle_afk_moukey)

        self.stop_button = tk.Button(root, text="Stop AFK", command=self.stop_afk, state=tk.DISABLED)

        self.start_mouse_button.pack()
        self.start_keyboard_button.pack()
        self.start_moukey_button.pack()
        self.stop_button.pack()

        root.bind("<F6>", lambda event: self.toggle_afk_mouse())
        root.bind("<F7>", lambda event: self.toggle_afk_keyboard())
        root.bind("<F8>", lambda event: self.toggle_afk_moukey())
        root.bind("<F9>", lambda event: self.stop_afk())

    def toggle_afk_mouse(self):
        self.afk_mouse_on = not self.afk_mouse_on
        self.toggle_afk()

    def toggle_afk_keyboard(self):
        self.afk_keyboard_on = not self.afk_keyboard_on
        self.toggle_afk()

    def toggle_afk_moukey(self):
        self.afk_moukey_on = not self.afk_moukey_on
        self.toggle_afk()

    def toggle_afk(self):
        if self.afk_mouse_on or self.afk_keyboard_on or self.afk_moukey_on:
            self.start_afk()
        else:
            self.stop_afk()

    def start_afk(self):
        if not self.afk_thread or not self.afk_thread.is_alive():
            self.afk_thread = threading.Thread(target=self.run_afk)
            self.afk_thread.start()
            self.stop_button.config(state=tk.NORMAL)

    def stop_afk(self):
        self.afk_mouse_on = False
        self.afk_keyboard_on = False
        self.afk_moukey_on = False
        self.stop_button.config(state=tk.DISABLED)
        if self.afk_thread and self.afk_thread.is_alive():
            self.afk_thread.join()
        exit()

    def run_afk(self):
        while self.afk_mouse_on or self.afk_keyboard_on or self.afk_moukey_on:
            if self.afk_mouse_on:
                self.afk_instance.perform_mouse()
            if self.afk_keyboard_on:
                self.afk_instance.perform_keyboard()
            if self.afk_moukey_on:
                self.afk_instance.perform_moukey()
            time.sleep(1)

class MouseAFK:
    def perform_mouse(self):
        x = random.randint(200, 1200)
        y = random.randint(300, 800)
        pag.dragTo(x, y, 2, button='left')
        time.sleep(random.randint(1, 2))

    def perform_keyboard(self):
        pass

    def perform_moukey(self):
        pass 

class KeyboardAFK:
    def perform_mouse(self):
        pass

    def perform_keyboard(self):
        for _ in range(random.randint(3, 7)):
            trig = random.randint(1, 4)
            if trig == 1:
                pag.press('w')
            elif trig == 2:
                pag.press('a')
            elif trig == 3:
                pag.press('s')
            elif trig == 4:
                pag.press('d')

    def perform_moukey(self):
        pass

class KeyboardMouseAFK:
    def perform_mouse(self):
        x = random.randint(200, 1200)
        y = random.randint(300, 800)
        pag.dragTo(x, y, 2, button='right')
        time.sleep(random.randint(1, 5))

    def perform_keyboard(self):
        for _ in range(random.randint(3, 7)):
            trig = random.randint(1, 4)
            if trig == 1:
                pag.press('w')
            elif trig == 2:
                pag.press('a')
            elif trig == 3:
                pag.press('s')
            elif trig == 4:
                pag.press('d')

    def perform_moukey(self):
        x = random.randint(200, 1200)
        y = random.randint(300, 800)
        pag.dragTo(x, y, 2, button='left')
        time.sleep(random.randint(1, 2))
        for _ in range(random.randint(3, 7)):
            trig = random.randint(1, 4)
            if trig == 1:
                pag.press('w')
            elif trig == 2:
                pag.press('a')
            elif trig == 3:
                pag.press('s')
            elif trig == 4:
                pag.press('d')

if __name__ == "__main__":
    root = tk.Tk()
    afk_bot = AFKBOT(root, KeyboardMouseAFK())
    root.mainloop()
