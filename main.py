# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys

import pyttsx3
speaker=pyttsx3.init()

class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting window title
		self.setWindowTitle("Python ")
		self.setGeometry(100, 100, 320, 350)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

		# defining random words
		self.words = ['accessible','attentive','azure','beneficial','chum','compassionate','fascinated','generous','jittery','jovial',
		              'keen','onomatopoeia','optimistic','pragmatic','quiescent','receptive','tactful','whizbang','zeitgeist']

		# default current word
		self.current_text = ""

	# method for components of GUI
	def UiComponents(self):

		# creating head label
		head = QLabel("Scramble Words", self)
		head.setGeometry(20, 10, 280, 60)

		font = QFont('Times', 15)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)
		head.setFont(font)

		head.setAlignment(Qt.AlignCenter)

		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.red)
		head.setGraphicsEffect(color)
		
		# creating label to show the scramble word
		self.j_word = QLabel(self)
		self.j_word.setGeometry(30, 80, 260, 50)
		self.j_word.setStyleSheet("border : 2px solid black; background : white;")
		self.j_word.setFont(QFont('Times', 12))
		self.j_word.setAlignment(Qt.AlignCenter)

		# creating a line edit widget for input text
		self.input = QLineEdit(self)
		self.input.setGeometry(20, 150, 200, 40)
		self.input.setAlignment(Qt.AlignCenter)

		# creating push button to check the input
		self.check = QPushButton("Check", self)
		self.check.setGeometry(230, 155, 80, 30)
		# adding action to the check button
		self.check.clicked.connect(self.check_action)

		# result label
		self.result = QLabel(self)
		self.result.setGeometry(40, 210, 240, 50)
		self.result.setFont(QFont('Times', 13))
		self.result.setAlignment(Qt.AlignCenter)
		self.result.setStyleSheet("border : 2px solid black; background : blue;")

		# creating push buttons to start and reset
		start = QPushButton("Start", self)
		reset = QPushButton("Reset", self)
		start.setGeometry(15, 290, 140, 40)
		reset.setGeometry(165, 290, 140, 40)
		# adding action to both the buttons
		start.clicked.connect(self.start_action)
		reset.clicked.connect(self.reset_action)

	def start_action(self):

		# selecting random word
		self.current_text = random.choice(self.words)

		# sample() method shuffles the characters of the word
		random_word = random.sample(self.current_text, len(self.current_text))

		# join() method join the elements of the list with particular character 
		jumbled = ''.join(random_word)

		# setting text to the jumbled word
		self.j_word.setText(jumbled)

		# setting default result text to blank
		self.result.setText("")

		self.result.setStyleSheet("border : 2px solid black; background : blue;")

		# setting default input text to blank
		self.input.setText("")

	def check_action(self):

		# getting input text from the line edit widget
		text = self.input.text()

		# checking input text is similar to the current text
		if text == self.current_text:
			self.result.setText("Correct Answer")
			self.result.setStyleSheet("background : lightgreen;")

			# text-to-speech conversion
			speaker.say(self.current_text)

			# setting rate
			rate=speaker.getProperty("rate")
			speaker.setProperty("rate",100)
			
			# setting volume
			volume=speaker.getProperty("volume")
			speaker.setProperty("volume",1.0)
			
			speaker.runAndWait()

		else:
			self.result.setText("Wrong Answer")
			self.result.setStyleSheet("background : red;")

			# text-to-speech conversion
			speaker.say("Wrong Answer")

			# setting rate
			rate=speaker.getProperty("rate")
			speaker.setProperty("rate",125)
			
			# setting volume
			volume=speaker.getProperty("volume")
			speaker.setProperty("volume",1.0)
			
			speaker.runAndWait()

	def reset_action(self):

		# setting current text blank
		self.current_text = ""

		# setting input to blank
		self.input.setText("")

		# clear the text of all the labels
		self.j_word.setText("")

		self.result.setText("")
		self.result.setStyleSheet("border : 2px solid black; background : blue;")

# creating pyqt5 gui app
App = QApplication(sys.argv)

# creating the instance of our Window
window = Window()

# starting the app
sys.exit(App.exec())
