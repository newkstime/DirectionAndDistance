import math

def main():
    print("Enter x and y coordinates of two points:")
    print("Point 1: (x1, y1)")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    print("Point 2: (x1, y1)")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x1, y1, x2, y2 = transform_points(x1, y1, x2, y2)
    quadrant = find_quadrant(x1, y1, x2, y2)
    if quadrant == 1 or quadrant == 3:
        x3 = x2
        y3 = y1
    else:
        x3 = x1
        y3 = y2
    sideA_len = distance(x2, y2, x3, y3)
    sideB_len = distance(x1, y1, x3, y3)
    sideC_len = distance(x1, y1, x2, y2)
    angle = float(format(compute_angle(sideA_len, sideB_len, sideC_len), '.2f'))
    direction = compute_direction(angle, quadrant)
    print("The distance between these points: " + format(sideC_len, '.2f'))
    print("The direction traveled from the first point to the second: " + direction)

def transform_points(x1, y1, x2, y2):
    x2_transformed = x2 - x1
    y2_transformed = y2 - y1
    x1_transformed = 0.0
    y1_transformed = 0.0
    return x1_transformed, y1_transformed, x2_transformed, y2_transformed

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def compute_angle(sideA_len, sideB_len, sideC_len):
    return math.degrees(math.acos((sideB_len**2 + sideC_len**2 - sideA_len**2)
                        / (2 * (sideB_len) * (sideC_len))))

def compute_direction(angle, quadrant):
    q1_dict = {(00.00, 11.25) : 'E', (11.26, 33.75) : 'ENE', (33.76, 56.25) : 'NE',
               (56.26, 78.75) : 'NNE', (78.76, 90.00) : 'N'}
    q2_dict = {(00.00, 11.25) : 'N', (11.26, 33.75) : 'NNW', (33.76, 56.25) : 'NW',
               (56.26, 78.75) : 'WNW', (78.76, 90.00) : 'W'}
    q3_dict = {(00.00, 11.25) : 'W', (11.26, 33.75) : 'WSW', (33.76, 56.25) : 'SW',
               (56.26, 78.75) : 'SSW', (78.76, 90.00) : 'S'}
    q4_dict = {(00.00, 11.25) : 'S', (11.26, 33.75) : 'SSE', (33.76, 56.25) : 'SE',
               (56.26, 78.75) : 'ESE', (78.76, 90.00) : 'E'}
    if quadrant == 1:
        for degrees, direction in q1_dict.items():
            if angle >= degrees[0] and angle <= degrees[1]:
                return q1_dict[degrees]
    elif quadrant == 2:
        for degrees, direction in q2_dict.items():
            if angle >= degrees[0] and angle <= degrees[1]:
                return q2_dict[degrees]
    elif quadrant == 3:
        for degrees, direction in q3_dict.items():
            if angle >= degrees[0] and angle <= degrees[1]:
                return q3_dict[degrees]
    elif quadrant == 4:
        for degrees, direction in q4_dict.items():
            if angle >= degrees[0] and angle <= degrees[1]:
                return q4_dict[degrees]

def find_quadrant(x1_transformed, y1_transformed, x2_transformed, y2_transformed):
    print(x1_transformed, y1_transformed, x2_transformed, y2_transformed)
    if x2_transformed > x1_transformed and y2_transformed >= y1_transformed:
        return 1
    elif x2_transformed <= x1_transformed and y2_transformed > y1_transformed:
        return 2
    elif x2_transformed < x1_transformed and y2_transformed <= y1_transformed:
        return 3
    elif x2_transformed >= x1_transformed and y2_transformed < y1_transformed:
        return 4

main()
