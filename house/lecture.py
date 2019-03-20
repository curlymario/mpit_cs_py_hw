import graphics as gr

def calculate_height():
    """Функция, которая находит высоту из ширины"""
    pass

def build_house(window, upper_left_corner, width):    
    """Функция, которая рисует дом"""
    # height = calculate_height(width)

window = gr.GraphWin("Russian game", 300, 300)
build_house(window, gr.Point(100, 100), 100)

print("Ура, дом построен!")