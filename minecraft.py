import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.texture_importer import load_texture

app = ursina.Ursina()

grass_texture = load_texture("grass_block.png")  # textury nefunguji tak jak bych si prestavoval 

class Voxel(ursina.Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = ursina.scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = grass_texture ,
            color = ursina.color.white,
            highlight_color = ursina.color.orange
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position = self.position + ursina.mouse.normal)
            if key == "right mouse down":
                ursina.destroy(self)

for z in range(10):
    for x in range(20):
        voxel = Voxel((x,0,z))

player = FirstPersonController()

app.run()