
def traffic_light_choice(car, light):
    car_movement = ""
    if car == "moving":
        if light == "red":
            car_command = "stop"
        elif light == "yellow":
            car_command = "stop"
        elif light == "green":
            car_command = "go"
    elif car == "stopped":
        if light == "red":
            car_command = "stop"
        elif light == "yellow":
            car_command = "stop"
        elif light == "green":
            car_command = "go"
    return car_command

print(traffic_light_choice)





