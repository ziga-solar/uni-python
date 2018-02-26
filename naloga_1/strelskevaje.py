from math import *

velocity = float(input("Vpiši hitrost izstrelka(v m/s): "))
angle = float(input("Vpiši kot topa (v stopinjah): "))

print("Krogla bo letla", (pow(velocity, 2) * sin(2 * (radians(angle)))) / 10, "metrov")