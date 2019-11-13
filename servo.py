window = 15


def move_laser(obj_x, obj_y, x, y):
    if (x + window) < obj_x:
        print("Move servo right.")
    elif (x - window) > obj_x:
        print("Move servo left.")
    else:
        print("x OK")

    if (y + window) < obj_y:
        print("Move servo down.")
    elif (y - window) > obj_y:
        print("Move servo up.")
    else:
        print("Y OK")
