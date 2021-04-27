"""
Drivetrain Data Grabbing
"""


import binascii


# gets data from Steering System and retunds the rounding info
def steeringWheelData(msg):
    #Data to Ints UwU
    steering = int(binascii.hexlify(msg.data[:1]),16)+ int(binascii.hexlify(msg.data[:2]),16)*255/26 
    return round(steering*255/26)