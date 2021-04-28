"""
Drivetrain Data Grabbing
"""


import binascii


# gets data from Steering System and retunds the rounding info
def steeringWheelData(id,data):
    #Data to Ints UwU
    return (int(binascii.hexlify(data[:1]),16)+ int(binascii.hexlify(data[:2]),16)*255/26)


def gassPeddleData(id,data):
     #Data to Ints UwU
    return  int(binascii.hexlify(data[:3]),16)