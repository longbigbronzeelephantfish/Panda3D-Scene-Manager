from direct.showbase.ShowBase import ShowBase

from direct.task import Task

class SceneManager(ShowBase):

	def __init__(self):
		ShowBase.__init__(self)
		
	def Startup(self, scene):
		self.currentScene = scene
		self.currentScene.SetSceneManager(self)
		self.currentScene.Enter()
		taskMgr.add(self.Update, 'Update')

	def Update(self, task):
		self.currentScene.Update()
		return Task.cont

	def Shutdown(self):
		self.currentScene.Leave()
		self.cleanup()
		sys.exit(1)

	def ChangeScene(self, scene):
		self.currentScene.Leave()
		self.currentScene = scene
		self.currentScene.SetSceneManager(self)
		self.currentScene.Enter()