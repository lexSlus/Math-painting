
from canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input('What do you like to draw?, Enter quit to quit: ')
    if shape_type == 'rectangle':
        rec_x = int(input('Enter x of the rectangle: '))
        rec_y = int(input('Enter y of the rectangle: '))
        rec_width = int(input('Enter width of the rectangle: '))
        rec_height = int(input('Enter height of the rectangle: '))
        red = int(input("Enter how much red do you want: "))
        green = int(input("Enter how much green do you want: "))
        blue = int(input("Enter how much blue do you want: "))

        # Creating the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)
    if shape_type == 'square':
        sqr_x = int(input('Enter x of square: '))
        sqr_y = int(input('Enter y of square: '))
        sqr_side = int(input("Enter the side length of the square: "))
        red = int(input("Enter how much red do you want: "))
        green = int(input("Enter how much green do you want: "))
        blue = int(input("Enter how much blue do you want: "))
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == 'quit':
        break


canvas.make('canvas.png')
