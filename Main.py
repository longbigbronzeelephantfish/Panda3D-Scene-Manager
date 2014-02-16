from SceneManager import SceneManager

from MenuScene import MenuScene

class Main():

  def __init__(self):
    sceneManager = SceneManager()

    scene = MenuScene()

    sceneManager.Startup(scene)
    sceneManager.run()

app = Main()

