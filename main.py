import kivy
#__version__= '1.0'
kivy.require('1.0.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout

class Calculator(StackLayout):

	def backward(self, express):
		if express:
			self.display.text = express[:-1]

	def calculate(self, express):
		if not express: return

		try:
			self.display.text = str( eval(express) )
		except Exception:
			self.display.text = 'error'

class CalculatorApp(App):
	title = 'calculator'

	def build(self):
		return Calculator()

	def on_pause(self):
		return True


if __name__ in ('__main__', '__android__'):
	CalculatorApp().run()