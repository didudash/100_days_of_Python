import turtle
from PIL import Image

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
width, height = Image.open(image).size
print(width, height)

screen.addshape(image)
screen.setup(width, height)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


# event listen
turtle.onscreenclick(get_mouse_click_coor)

# keep screen open
turtle.mainloop()
