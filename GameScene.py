from Scene import Scene

class GameScene(Scene):

	def Enter(self):

		# Get the ShowBase
		sceneManager = self.GetSceneManager()

		# Set the Background to a nice SkyBlue
		sceneManager.setBackgroundColor(0.25,0.5,1.0,1)

		# Setup the Camera
		sceneManager.cam.setPos(0, -50, 50)
		sceneManager.cam.lookAt(0, 0, 0)

		# Prevent user from changing the Camera view
		sceneManager.disableMouse()

		# Add a Ground
		self.groundNP = render.attachNewNode("Ground")
		model = sceneManager.loader.loadModel("models/floor.egg")
		model.reparentTo(self.groundNP)
		texture = sceneManager.loader.loadTexture("models/floor.bmp")
		self.groundNP.setTexture(texture)

		# Add a Player
		self.playerNP = render.attachNewNode("Ground")
		model = sceneManager.loader.loadModel("smiley")
		model.reparentTo(self.playerNP)

		# Press "escape" to go back to menu
		sceneManager.accept('escape',	self.LeaveGame)

	def LeaveGame(self):
		# Change the current scene to the Menu
		from MenuScene import MenuScene
		scene = MenuScene()
		self.GetSceneManager().ChangeScene(scene)

	def Update(self):
		# Move the Player
		self.playerNP.setPos(self.playerNP, 0,0,0.01)

	def Leave(self):
		# CLeanup
		self.groundNP.removeNode()
		self.playerNP.removeNode()