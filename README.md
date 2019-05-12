# dish-pointer
the dish-pointer project a rough protoype of the equations required for Parabolic Dish Pointing software for GEO satellites.

## Getting Started
the dish-pointer should work on all OS that support Python 3.6

### Requirements
main.py was written in Python 3.6, and has the following dependecies:

|Package|Description|Version|Install|
|-----|-----|-----|-----|
|matplotlib|Graphing and math Library| 3.03| pip install matplotlib|

### Installing
Included in the project is a pip freeze of the needed libraries.
To install requirements using pip freeze
`````
1. Open Command Line
2. cd to where dish-pointer project is cloned
3. Enter "pip install -r dish-pointer_pip_freeze.txt
`````

## Exectuion
To run main.py
`````
1. Open Command Line
2. cd to where dish-pointer project is cloned
3. python main.py
`````

### Example Operation
`````
Enter Earth Station Longitude, for West use '-': -97.33
Enter Earth Station Latitude, for South use '-': 37.68
Enter Satellite subpoint Longitude, for West use '-': -123
Antenna azimuth is 218.2°
Antenna look angle 38.7°
Satellite is within arc of visibility of dish.
angle of polarization 29.46°
`````
