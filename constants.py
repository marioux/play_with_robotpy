#
# The constants module is a convenience place for teams to hold robot-wide
# numerical or boolean constants. Don't use this for any other purpose!
#

import math

import wpilib

# Motors

# pneumatic control module (pcm) 30
# power distribution panel (pdp) 21
# sparkmax right 1, 2
# sparkmax right 3, 4

kLeftMotor1Port = 0
kLeftMotor1Inverted = False
kLeftMotor2Port = 1
kLeftMotor2Inverted = False
kRightMotor1Port = 2
kRightMotor1Inverted = False
kRightMotor2Port = 3
kRightMotor2Inverted = False

# PID
kP = 5e-5
kI = 1e-6
kD = 0
kIz = 0
kFF = 0.000156
kMaxOutput = 1
kMinOutput = -1
max_rpm = 5700

# Smart Motion coefficients
max_vel = 2000  # rpm
max_acc = 1500
min_vel = 0
allowed_err = 0

# Encoders
# kLeftEncoderPorts = (0, 1)
# kRightEncoderPorts = (2, 3)
# kLeftEncoderReversed = False
# kRightEncoderReversed = True
#
# kEncoderCPR = 1024
# kWheelDiameterInches = 6
# # Assumes the encoders are directly mounted on the wheel shafts
# kEncoderDistancePerPulse = (kWheelDiameterInches * math.pi) / kEncoderCPR
#
# # Hatch
# kHatchSolenoidModuleType = wpilib.PneumaticsModuleType.CTREPCM
# kHatchSolenoidModule = 0
# kHatchSolenoidPorts = (0, 1)
#
# # Autonomous
# kAutoDriveDistanceInches = 60
# kAutoBackupDistanceInches = 20
# kAutoDriveSpeed = 0.5
#
# # Operator Interface
# kDriverControllerPort = 0
#
# Physical parameters
kDriveTrainMotorCount = 2
kTrackWidth = 0.381 * 2
kGearingRatio = 8
kWheelRadius = 0.0508

# kEncoderResolution = -
