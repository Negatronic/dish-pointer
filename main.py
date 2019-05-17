import numpy as np

earth_station_long = float(input("Enter Earth Station Longitude, for West use '-': ")) * np.pi / 180
earth_station_lat = float(input("Enter Earth Station Latitude, for South use '-': ")) * np.pi / 180
sat_subpoint_long = float(input("Enter Satellite subpoint Longitude, for West use '-': ")) * np.pi / 180
# earth_station_long = -73 * np.pi / 180
# earth_station_lat = 18 * np.pi / 180
# sat_subpoint_long = -105 * np.pi / 180

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

print("Antenna azimuth is " + str(round(antenna_azimuth, 1)) + "°")

# Dish El look angle
antenna_distance = np.sqrt(earth_radius * earth_radius + a_gso * a_gso - 2 * a_gso * 6371 * np.cos(angle_b))
antenna_elevation = np.arccos(a_gso/antenna_distance*np.sin(angle_b))
print("Antenna look angle " + str(round(antenna_elevation * 180 / np.pi, 1)) + "°")

# Limit of Visibility, this is what satellites the dish can look at
angle_S_lim_of_view = np.arcsin(earth_radius / a_gso * np.sin(95 * np.pi / 180))
angle_b_lim_of_view = ((180 - 95) * np.pi / 180) - angle_S_lim_of_view
angle_B_lim_of_view = np.arccos(np.cos(angle_b_lim_of_view) / np.cos(earth_station_lat))
angle_lim_of_view_east = (earth_station_long * 180 / np.pi) + (angle_B_lim_of_view * 180 / np.pi)
angle_lim_of_view_west = (earth_station_long * 180 / np.pi) - (angle_B_lim_of_view * 180 / np.pi)

if angle_lim_of_view_west <= (sat_subpoint_long * 180 / np.pi) <= angle_lim_of_view_east:
    print("Satellite is within arc of visibility of dish.")
else:
    print("Satellite is outside of arc of visibility of dish")

# Polarization angle

# R
earth_radius_R_vec = []

earth_radius_R_vec.append(earth_radius * np.cos(earth_station_lat) * np.cos(angle_B))
earth_radius_R_vec.append(earth_radius * np.cos(earth_station_lat) * np.sin(angle_B))
earth_radius_R_vec.append(earth_radius * np.sin(earth_station_lat))
#print("R " + str(earth_radius_R_vec))

# r = -R
earth_radius_r_vec = [-1*earth_radius_R_vec[0], -1*earth_radius_R_vec[1], -1*earth_radius_R_vec[2]]
#print("r " + str(earth_radius_r_vec))

# k = [Rx- agso, Ry, Rz]
earth_propagation_vec = []
earth_propagation_vec.append(earth_radius_R_vec[0] - a_gso)
earth_propagation_vec.append(earth_radius_R_vec[1])
earth_propagation_vec.append(earth_radius_R_vec[2])
#print("k " + str(earth_propagation_vec))

# e = [0, 0, 1]
earth_pol_vec = [0, 0, 1]
#print("e " + str(earth_pol_vec))

# f = k x r
normal_propagation_vec = -1 * np.cross(earth_radius_r_vec, earth_propagation_vec)
#print("f " + str(normal_propagation_vec))

# g = k x e
normal_earth_pol_propagation_vec = np.cross(earth_propagation_vec, earth_pol_vec)
#print("g " + str(normal_earth_pol_propagation_vec))

# h = g x k
normal_propagation_earth_pol_earth_prop_vec = np.cross(normal_earth_pol_propagation_vec, earth_propagation_vec)
#print("h " + str(normal_propagation_earth_pol_earth_prop_vec))

# magnitude of h = (h[0]^2 + h[1]^2 + h[2]^2)^1/2
magnitude_normal_propagation_earth_pol_earth_prop_vec = np.sqrt(np.square(normal_propagation_earth_pol_earth_prop_vec[0]) + np.square(normal_propagation_earth_pol_earth_prop_vec[1]) + np.square(normal_propagation_earth_pol_earth_prop_vec[2]))
#print("|h| " + str(magnitude_normal_propagation_earth_pol_earth_prop_vec))

unit_polarization_vector = normal_propagation_earth_pol_earth_prop_vec / magnitude_normal_propagation_earth_pol_earth_prop_vec
#print("p " + str(unit_polarization_vector))

# p dot f
normal_propagation_vec_unit_polarization_vector = np.dot(unit_polarization_vector, normal_propagation_vec)
#print("p . f " + str(normal_propagation_vec_unit_polarization_vector))

# magnitude of f = (f[0]^2 + f[1]^2 + f[2]^2)^1/2
magnitude_normal_propagation_vec = np.sqrt(np.square(normal_propagation_vec[0])
+ np.square(normal_propagation_vec[1]) + np.square(normal_propagation_vec[2]))
#print("|f| " + str(magnitude_normal_propagation_vec))

# epsilon = arccsin(p dot f/|f|)
angle_polarization = np.arcsin(normal_propagation_vec_unit_polarization_vector / magnitude_normal_propagation_vec)
print("angle of polarization " + str(round(angle_polarization * 180 / np.pi, 2)) + "°")
