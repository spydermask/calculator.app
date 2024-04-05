import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(10, 10)
Builder.load_file('my.kv')

class grid(Widget):
    def clear(self):
        self.ids.cal_input.text = '0'

   
    def button_value(self, number):
        prev_number = self.ids.cal_input.text
        if prev_number == '0':
            self.ids.cal_input.text =''
            self.ids.cal_input.text =f'{number}'
            
        else:
            self.ids.cal_input.text = f'{prev_number}{number}'

    def sign (self,sign):
        prev_number = self.ids.cal_input.text
        self.ids.cal_input.text =f'{prev_number}{sign}'

    def remove (self):
        prev_number = self.ids.cal_input.text
        prev_number = prev_number[:-1]
        self.ids.cal_input.text = prev_number
        
    def result(self):
        prev_number = self.ids.cal_input.text
        
        
        results = eval(prev_number)
        self.ids.cal_input.text = str(results)
        
    
       # self.ids.cal_input.text ="ERROR" 

       
        
    
class spyder_calculator(App):
    def build(self):
        return grid()
       
   #for excute program
if __name__ == "__main__":                
    spyder_calculator().run()