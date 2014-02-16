from Scene import Scene

import sys

from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import DirectLabel
from direct.gui.OnscreenText import OnscreenText

class MenuScene(Scene):

	def Enter(self):

		# Set background colour
		self.GetSceneManager().setBackgroundColor(0.25,0.5,1.0,1)

		self.startButton = DirectButton(text="Start",scale=0.1,command=self.HandleClick,
								extraArgs=[1],pos=(0,0,0.3))

		self.exitButton = DirectButton(text="Exit",scale=0.1,command=self.HandleClick,
								extraArgs=[2],pos=(0,0,0.1))
		
		self.menuTitle = DirectLabel(text="Angry Pacman",frameColor=(0.25,0.5,1.0,1),scale=0.25,pos=(0,0,0.5))

	def HandleClick(self,n):
		# If the Start button is clicked
		if (n==1):
			# Change the active scene to the GameScene
			from GameScene import GameScene
			scene = GameScene()
			self.GetSceneManager().ChangeScene(scene)
		# If the Exit button is clicked
		else:
			# We exit
			sys.exit(1)

	def Update(self):
		# Nothing to update
		pass

	def Leave(self):
		# Clean up
		self.startButton.remove()
		self.exitButton.remove()
		self.menuTitle.remove()