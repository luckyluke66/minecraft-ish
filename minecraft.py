import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.texture_importer import load_texture
from ursina.vec2 import Vec2
from ursina.vec3 import Vec3


app = ursina.Ursina()
block_pick = 1

grass_texture = load_texture("textures/grass_block.png")
stone_texture = load_texture("textures/stone_block.png")
brick_texture = load_texture("textures/brick_block.png")
dirt_texture = load_texture("textures/dirt_block.png")
sky_texture = load_texture("textures/skybox.png")
arm_texture = load_texture("textures/arm_texture.png")
hotbar_texture = load_texture("textures/hotbar.png")
target_texture = load_texture("textures/target.png")
hotbar_grass = load_texture("textures/hotbar_grass.png")
hotbar_dirt = load_texture("textures/hotbar_dirt.png")
hotbar_stone = load_texture("textures/hotbar_stone.png")
hotbar_brick = load_texture("textures/hotbar_brick.png")

def update():
    global block_pick
    if ursina.held_keys["1"]:
        block_pick = 1
    if ursina.held_keys["2"]:
        block_pick = 2
    if ursina.held_keys["3"]:
        block_pick = 3
    if ursina.held_keys["4"]:
        block_pick = 4
    if ursina.held_keys["5"]:
        block_pick = 5
    if ursina.held_keys["6"]:
        block_pick = 6
        
    if ursina.held_keys["left mouse"] or ursina.held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()
    
    pointer.change()

class Voxel(ursina.Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = ursina.scene,
            position = position,
            model = "assets/block",
            origin_y = 0.5,
            texture = texture,
            color = ursina.color.color(0,0,ursina.random.uniform(0.9,1)),
            scale = 0.5
        )
    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                if block_pick == 1:
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = dirt_texture)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = stone_texture)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = brick_texture)

                # TODO: pridat dalsi blocky 
            if key == "left mouse down":
                ursina.destroy(self)

class Sky(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.scene,
            model = "sphere", 
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

class Hand(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "assets/arm",
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.7)
        )
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.7)

class Hotbar(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "quad",
            texture = hotbar_texture,
            scale = (0.9,0.15),
            position = Vec2(-0.44, -0.4)
        )
class Grass(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "quad",
            texture = hotbar_grass,
            scale = (0.10,0.10),
            position = Vec2(-0.820, -0.4)
        )    
            
class Dirt(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "quad",
            texture = hotbar_dirt,
            scale = (0.10,0.10),
            position = Vec2(-0.675, -0.4)
        )    

class Stone(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "quad",
            texture = hotbar_stone,
            scale = (0.10,0.10),
            position = Vec2(-0.53, -0.4)
        )

class Brick(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "quad",
            texture = hotbar_brick,
            scale = (0.10,0.10),
            position = Vec2(-0.385, -0.4)
        )
            

class Pointer(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent = ursina.camera.ui,
            model = "quad",
            texture = target_texture,
            scale = (0.15, 0.15),
            position = Vec2(-0.820, -0.4)
        )
    
    def change(self):
        if block_pick == 1:
            self.position = Vec2(-0.820, -0.4)
        if block_pick == 2:
            self.position = Vec2(-0.675, -0.4)
        if block_pick == 3:
            self.position = Vec2(-0.53, -0.4) 
        if block_pick == 4:
            self.position = Vec2(-0.385, -0.4)
        if block_pick == 5:
            self.position = Vec2(-0.24, -0.4)
    


for z in range(10):
    for x in range(10):
        for y in range(3):
            voxel = Voxel((x,y,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()
hotbar = Hotbar()
pointer = Pointer()
grass = Grass()
dirt = Dirt()
stone = Stone()
brick = Brick()

app.run()