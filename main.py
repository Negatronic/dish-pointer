import numpy as np

earth_station_long = float(input("Enter Earth Station Longitude "))* -1 *np.pi/180
earth_station_lat = 37.6872*np.pi/180
earth_radius = 6371
sat_subpoint_long = -123*np.pi/180
a_gso = 42164


# Calculate look angle
angle_B = earth_station_long - sat_subpoint_long
print(angle_B)

angle_b = np.arccos(np.cos(angle_B) * np.cos(earth_station_lat))
print(angle_b * 180 / np.pi)

angle_A = np.arcsin(np.sin(abs(angle_B)) / np.sin(angle_b))
print(angle_A * 180 / np.pi)

antenna_distance = np.sqrt(earth_radius * earth_radius + a_gso * a_gso - 2 * a_gso * 6371 * np.cos(angle_b))
print(antenna_distance)

antenna_elevation = np.arccos(a_gso/antenna_distance*np.sin(angle_b))
print(antenna_elevation * 180 /np.pi)
