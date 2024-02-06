import graphics
import app
import inputs

class Main_app:
    def __init__(self):
        self.category = app.Category()
        self.product = app.Product()
        
        self.display = graphics.Display(self)
        self.is_running = True
        self.input = inputs.Input(self, self.display)
        
    def run(self):
        while self.is_running:
            self.input.handle_inputs()
            self.display.draw_main()
        
    def quit(self):
        self.is_running = False
        self.display.quit()