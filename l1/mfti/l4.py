def paint_hause (x,y,width,height):
    paint_walls(x,y,width,height//2)
    paint_roof(x,y,width,height//2)
    w_height=height//6
    w_width=widht//3
    paint_window(x+w_width,y+w_height,w_width,w_height)

