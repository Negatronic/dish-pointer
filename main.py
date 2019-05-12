import numpy as np

earth_station_long = float(input("Enter Earth Station Longitude, for West use '-': ")) * np.pi / 180
earth_station_lat = float(input("Enter Earth Station Latitude, for South use '-': ")) * np.pi / 180
sat_subpoint_long = float(input("Enter Satellite subpoint Longtitude, for West use '-': ")) * np.pi / 180

a_gso = 42164
earth_radius = 6371

# Calculate look angles
angle_B = earth_station_long - sat_subpoint_long
angle_b = np.arccos(np.cos(angle_B) * np.cos(earth_station_lat))
angle_A = np.arcsin(np.sin(abs(angle_B)) / np.sin(angle_b))

# True Az look angle
if earth_station_lat < 0 and angle_B < 0:
    antenna_azimuth = (angle_A * 180 / np.pi)
elif earth_station_lat < 0 and angle_B > 0:
    antenna_azimuth = 360 - (angle_A * 180 / np.pi)
elif earth_station_lat > 0 and angle_B < 0:
    antenna_azimuth = 180 - (angle_A * 180 / np.pi)
elif earth_station_lat > 0 and angle_B > 0:
    antenna_azimuth = 180 + (angle_A * 180 / np.pi)

print("\nAntenna azimuth is " + str(round(antenna_azimuth, 1)) + "°")

# Dish El look angle
antenna_distance = np.sqrt(earth_radius * earth_radius + a_gso * a_gso - 2 * a_gso * 6371 * np.cos(angle_b))
antenna_elevation = np.arccos(a_gso/antenna_distance*np.sin(angle_b))
print("\nAntenna look angle " + str(round(antenna_elevation * 180 / np.pi, 1)) + "°")

# Limit of Visibility, this is what satellites the dish can look at
angle_S_lov = np.arcsin(earth_radius/a_gso * np.sin(95 * np.pi / 180)) #rad
angle_b_lov = ((180 - 95) * np.pi / 180) - angle_S_lov #rad
angle_B_lov = np.arccos(np.cos(angle_b_lov)/np.cos(earth_station_lat))
angle_lov_east = (earth_station_long * 180 / np.pi) + (angle_B_lov * 180 / np.pi)
angle_lov_west = (earth_station_long * 180 / np.pi) - (angle_B_lov * 180 / np.pi)

if angle_lov_west <= (sat_subpoint_long * 180 / np.pi) <= angle_lov_east:
    print("Satellite is within arc of visibility of dish.")
else:
    print("Satellite is outside of arc of visibility of dish")

# Polarization angle

