
def move_laser(obj_x, obj_y, x, y):
    if x < obj_x:
        print("Move servo right.")
    elif x > obj_x:
        print("Move servo left.")

    if y < obj_y:
        print("Move servo down.")
    elif y > obj_y:
        print("Move servo up.")
