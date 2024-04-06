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
        try:
            prev_number = self.ids.cal_input.text
            result = eval(prev_number)
            self.ids.cal_input.text = str(result)
        except Exception as e:
            print("Error:", e)
            self.ids.cal_input.text = "Error"

       
        
    
class spyder_calculator(App):
    def build(self):
        return grid()
       
   #for excute program
if __name__ == "__main__":                
    spyder_calculator().run()
