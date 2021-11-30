import ursina
from ursina.vec3 import Vec3 
#test

class TestCube(ursina.Entity):
    def __init__(self) -> None:
        super().__init__(
            model = "cube", 
            color = ursina.color.white, 
            texture = "white_cube",
            rotation = ursina.Vec3(45,45,45)
            )

class TestButton(ursina.Button):
    def __init__(self):
        super().__init__(
            parent = ursina.scene,
            model = "cube",
            texture = "brick",
            color = ursina.color.blue,
            highlight_color = ursina.color.red,
            pressed_color = ursina.color.lime,
            )
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                print("button_pressed")


def update():
    if ursina.held_keys["a"]:
        mc_ride.x -= 4 * ursina.time.dt
    if ursina.held_keys["w"]:
        mc_ride.y += 4 * ursina.time.dt
    if ursina.held_keys["d"]:
        mc_ride.x += 4 * ursina.time.dt
    if ursina.held_keys["s"]:
        mc_ride.y -= 4 * ursina.time.dt

app = ursina.Ursina()

square = ursina.Entity(model = "quad", color = ursina.color.red, scale = (1,4), position = (3,4))

test_cube = TestCube()
test_button = TestButton()


app.run()