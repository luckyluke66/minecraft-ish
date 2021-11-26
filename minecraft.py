import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.texture_importer import load_texture

app = ursina.Ursina()

grass_texture = load_texture("grass_block.png")
stone_texture = load_texture("stone_block.png")
brick_texture = load_texture("brick_block.png")
dirt_texture = load_texture("dirt_block.png")


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
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = stone_texture)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = brick_texture)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + ursina.mouse.normal, texture = dirt_texture)
            if key == "left mouse down":
                ursina.destroy(self)

for z in range(10):
    for x in range(20):
        voxel = Voxel((x,0,z))

player = FirstPersonController()


app.run()