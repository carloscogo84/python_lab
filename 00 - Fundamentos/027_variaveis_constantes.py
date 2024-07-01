car_vel = 61  # velocidade do carro
car_loc = 100  # local do carro

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

distance1 = LOCAL_1 - RADAR_RANGE
distance2 = LOCAL_1 + RADAR_RANGE

car_radar = car_loc >= (distance1) and car_loc <= (distance2)
car_vel_up = car_vel > RADAR_1

car_radar_vel_up = car_radar and car_vel_up

if car_radar_vel_up:
    print(f'MULTADO! Acima de {RADAR_1} Km/h.')

if car_loc >= (LOCAL_1 - RADAR_RANGE) and \
    car_loc <= (LOCAL_1 + RADAR_RANGE) and \
        car_vel > RADAR_1:
    print(f'MULTADO! Acima de {RADAR_1} Km/h.')
