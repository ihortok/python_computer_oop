import processor
import ram
import storage
import display
import keyboard
import mouse
import computer

processor = processor.Processor('3.4 GHz', 2)
ram =  ram.Ram(500)
storage =  storage.Storage(5000)
display =  display.Display('LG', '1920x1080')
keyboard =  keyboard.Keyboard('Samsung')
mouse =  mouse.Mouse('Apple')

class ComputerBuilder:
    def build(self):
        return computer.Computer(
            processor,
            ram,
            storage,
            display,
            keyboard,
            mouse
        )
