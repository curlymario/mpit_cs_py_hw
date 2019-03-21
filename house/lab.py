# # подключение библиотеки под синонимом gr
# import graphics as gr

# # Инициализация окна с названием "Russian game" и размером 100х100 пикселей
# window = gr.GraphWin("Russian Game", 100, 100)

# # Инициализация окна с названием "Russian game" и размером 100х100 пикселей
# # window.close()

# # Создание круга с радиусом 10 и координатами центра (50, 50)
# my_circle = gr.Circle(gr.Point(50, 50), 10)

# # Создание отрезка с концами в точках (2, 4) и (4, 8)
# my_line = gr.Line(gr.Point(2, 4), gr.Point(4, 8))

# # Создание прямоугольника у которого диагональ — отрезок с концами в точках (2, 4) и (4, 8)
# my_rect = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))

# # Отрисовка примитивов в окне window
# my_circle.draw(window)
# my_line.draw(window)
# my_rect.draw(window)

# #  Ожидание нажатия кнопки мыши по окну.
# window.getMouse()

# #  После того как мы выполнили все нужные операции, окно следует закрыть.
# window.close()

import graphics as gr

window = gr.GraphWin("Lab_4", 788, 584)

def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(788, 320))
    sky.setFill(gr.color_rgb(66, 139, 216))
    sky.setWidth(0)
    sky.draw(window)


def draw_land():
    land = gr.Rectangle(gr.Point(0, 320), gr.Point(788, 584))
    land.setFill(gr.color_rgb(163, 247, 181))
    land.setWidth(0)
    land.draw(window)


def draw_house():
    house_body = gr.Rectangle(gr.Point(200, 220), gr.Point(400, 420))
    house_body.setFill(gr.color_rgb(200, 180, 140))
    house_body.setOutline(gr.color_rgb(160, 140, 100))
    house_body.setWidth(5)
    house_body.draw(window)

    house_roof = gr.Polygon(gr.Point(190, 220), gr.Point(300, 110), gr.Point(410, 220))
    house_roof.setFill(gr.color_rgb(140, 25, 30))
    house_roof.setOutline(gr.color_rgb(100, 5, 10))
    house_roof.setWidth(5)
    house_roof.draw(window)

    house_window = gr.Rectangle(gr.Point(250, 260), gr.Point(350, 360))
    house_window.setFill(gr.color_rgb(132, 205, 255))
    house_window.setWidth(5)
    house_window.draw(window)

    line1 = gr.Line(gr.Point(300, 260), gr.Point(300, 360))
    line2 = gr.Line(gr.Point(250, 310), gr.Point(350, 310))

    line1.setWidth(5)
    line2.setWidth(5)

    line1.draw(window)
    line2.draw(window)


def draw_cloud():
    pass


def draw_sun():
    sun = gr.Circle(gr.Point(700,100), 40)
    sun.setFill('yellow')
    sun.setOutline('orange')
    sun.setWidth(10)

    sun.draw(window)


def draw_tree():
    tree_1 = gr.Polygon(gr.Point(525, 450), gr.Point(625, 350), gr.Point(725, 450))
    tree_2 = gr.Polygon(gr.Point(525, 400), gr.Point(625, 300), gr.Point(725, 400))
    tree_3 = gr.Polygon(gr.Point(525, 350), gr.Point(625, 250), gr.Point(725, 350))

    tree_1.setFill(gr.color_rgb(60, 200, 160))
    tree_2.setFill(gr.color_rgb(60, 200, 160))
    tree_3.setFill(gr.color_rgb(60, 200, 160))

    tree_1.setOutline(gr.color_rgb(50, 160, 150))
    tree_2.setOutline(gr.color_rgb(50, 160, 150))
    tree_3.setOutline(gr.color_rgb(50, 160, 150))

    tree_1.setWidth(5)
    tree_2.setWidth(5)
    tree_3.setWidth(5)

    tree_leg = gr.Rectangle(gr.Point(600, 450), gr.Point(650, 525))
    tree_leg.setFill(gr.color_rgb(100, 65, 70))
    tree_leg.setOutline(gr.color_rgb(80, 55, 50))
    tree_leg.setWidth(5)

    tree_leg.draw(window)
    tree_1.draw(window)
    tree_2.draw(window)
    tree_3.draw(window)


def draw_picture():
    draw_sky()
    draw_cloud()
    draw_sun()
    draw_land()
    draw_house()
    draw_tree()
    

draw_picture()

window.getMouse()

window.close()
