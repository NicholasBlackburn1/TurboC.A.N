"""
Drivetrain Data Grabbing
"""


import binascii



# gets data from Steering System and retunds the rounding info
def steeringWheelDataGeneral(data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[2:4]))

# gets smaller wheel rotations for finer control of wheel
def steeringWheelDataFine(data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[:2]))

