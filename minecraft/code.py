from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from tqdm.auto import tqdm



global texture
block = 'dirt'
texture = 'dirt'
app = Ursina()



player = FirstPersonController()




#window settings
window.fullscreen = True
window.fps_counter.enabled = False
window.exit_button.visible = False
window.title = 'Minecraft-Asaf'









#block placer/breaker
class Block(Button):
    met = ['wood','stone']
    def __init__(self, position=(0,0,0),texture='stone'):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .01,
            texture =texture,
            color = color.color(0, 0, .9),
            highlight_color = color.lime,
        )


    def input(self, key):
        global texture
        texture = {
            "1": "dirt",
            "2": "wood",
            "3": "stone",
            "4": "stone_bricks",
            "5": "oak_log",
            "6": "wool",
            "7": "obsidian",
            "8": "granite",
            "9": "bedrock",
        }.get(str(key), texture)


        if self.hovered:
            if key == 'right mouse down':
                try:
                    block = Block(position=self.position + mouse.normal,texture=texture)
                except NameError:
                    texture = 'dirt'
                    block = Block(position=self.position + mouse.normal, texture=texture)

            if key == 'left mouse down':
                destroy(self)

#Inventory
class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (.9, .1),
            origin = (-.5, .5),
            position = (-0.45,-0.4),
            texture = 'widgets',
            texture_scale = (9,1),
            color = color.dark_gray
            )





class Items(Entity):
    def __init__(self,texture,position):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.1, .1),
            origin=(-.5, .5),
            position=(-position, -0.4),
            texture=texture,
            texture_scale=(1, 1),
            color= color.white


        )


blocks_List = ['dirt','wood','stone','stone_bricks','oak_log','wool','obsidian','granite','bedrock']
startPos = 0.45
for i in range(9):
    items = Items(blocks_List[i],startPos)
    startPos -= 0.1


inventory = Inventory()
inventory.texture


#movind up/down
def update():
    player.y += held_keys['space'] * time.dt * 10
    player.y -= held_keys['shift'] * time.dt * 10




#making platform
#chaning range to bigger x size platform
for z in tqdm(range(15)):
    #chaning range to bigger x size platform
    for x in range(15):
        i = 0
        block = Block(position=(x, 0, z), texture='bedrock')
        # chaning range to bigger y size platform
        for k in range(4):
            i += 1
            block = Block(position=(x, i, z), texture='dirt')





app.run()
