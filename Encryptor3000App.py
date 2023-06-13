import Encrypt
import kivy

from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.clipboard import Clipboard
#from kivy.graphics import RoundedRectangle
from kivy.core.window import Window
from kivy.properties import ObjectProperty


class FullGrid(GridLayout):
    def reset(self):
        self.ids.bottom_grid.reset()
        
    def copyTxt(self):
        self.ids.bottom_grid.copyTxt()

class BottomGrid(GridLayout):
    # Function to copy an encoded password to clipboard
    def copyTxt(self):
        name = ObjectProperty()
        encrypted = Encrypt.do_encrypt(name.text)
        Clipboard.copy(encrypted)
        self.password.text = 'Your password: \n'+encrypted
        name.text = 'Copied to Clipboard!'
    
    # Function to reset text and states to the default state
    def reset(self):
        name = ObjectProperty()
        self.toCopy.text = 'Copy and Convert to Password'
        self.prompt.text=''
        name.text=''

class Encryptor3000App(App):
    def build(self):
        return FullGrid()
        
    
if __name__ == "__main__":
    Encryptor3000App().run()
