import math
def trigonometric_functions():
    angle_deg = 180
    angle_rad = math.radians(angle_deg)

    print(f"\nSine of {angle_deg}°: {math.sin(angle_rad)}")
    print(f"Cosine of {angle_deg}°: {math.cos(angle_rad)}")
    print(f"Tangent of {angle_deg}°: {math.tan(angle_rad)}")
    print(f"Arcsine of 5 (in degrees): {math.degrees(math.asin(0.5))}")
    print(f"Arccosine of 5 (in degrees): {math.degrees(math.acos(0.5))}")
    print(f"Arctangent of 8 (in degrees): {math.degrees(math.atan(1))}")

def constants():
    
    print(f"\nPi (π): {math.pi}")
    print(f"Euler's Number (e): {math.e}")
    print(f"Golden Ratio (φ): {math.tau / 2}")

if __name__ == "__main__":

 trigonometric_functions()
 constants()
