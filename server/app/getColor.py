def get_color(type_edge, weight):
    # Задаем цвета в RGB формате для разных типов отношений
    colors = {
        'друзья': (0, 255, 0),  # Зеленый
        'партнеры': (10, 186, 181),  # Тиффани
        'романтик': (255, 0, 0),  # Красный
        'негатив': (0, 0, 255)  # Синий
    }

    if type_edge in colors:
        rgb = colors[type_edge]
        rgb = tuple(int((1 - weight) * 255 + weight * i) for i in rgb)
        hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
        return hex_color
    else:
        return '#000000' # цвет если не указали тип


print(get_color('романтик', 0.9))
