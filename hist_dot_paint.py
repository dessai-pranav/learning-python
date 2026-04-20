# import colorgram
# rgb_colors  = []
# colors = colorgram.extract('static.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as turtle_module
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
color_list = [(238, 232, 222), (224, 236, 227), (241, 224, 230), (177, 165, 151), (226, 231, 237), (111, 98, 88), (154, 169, 160), (177, 154, 161), (113, 87, 95), (88, 104, 95), (202, 196, 171), (158, 166, 172), (88, 99, 106), (54, 47, 38), (210, 181, 190), (208, 184, 180), (41, 54, 45), (182, 198, 188), (61, 40, 48), (147, 115, 124), (137, 131, 110), (117, 135, 126), (82, 53, 61), (45, 51, 57), (145, 120, 115), (53, 71, 59), (79, 55, 53), (189, 190, 195), (114, 135, 138), (70, 64, 53)]
for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()