'''

	Modified: 21.06.2015 by Mehmet Efe Tiryaki (m.efetiryaki@gmail.com)
	Created : 19.06.2015 by Mehmet Efe Tiryaki (m.efetiryaki@gmail.com)


'''
#! usr/bin/env python
# -*- coding: utf-8 -*-
# system imports

import random
import numpy
import sys
import cv2
import time
# ros package imports

from without.srv import *
from without.msg import *
import rospy


if __name__ == '__main__':
	rospy.wait_for_service('MasterControlService')
	Hub_Service= rospy.ServiceProxy('MasterControlService',\
						 MasterControl)
	# Initiliaze One robot
	request=MasterControlRequest()
	request.ID="Sadetra"
	request.CMD="Init"
	# Player 1 is initiated
	request.players=[Player()]
	request.players[0].Sticker=3
	request.players[0].playable="yes"
	request.players[0].speedCoefficient=1

	Hubresponse=Hub_Service(request)
	print("Master : Robot is initiliazed")
	# Ask Hub for is players ready ?
	waiting=True
	while waiting:
		request= MasterControlRequest()
		request.ID="Sadetra"
		request.CMD="IsReady"
		Hubresponse=Hub_Service(request)
		if Hubresponse.Status=="Ready":
			waiting=False
		else:
			time.sleep(0.5)
	print("Master : Players are ready, Game is starting")
	# Then send start Message
	request= MasterControlRequest()
	request.ID="Sadetra"
	request.CMD="Start"
	Hubresponse=Hub_Service(request)
	'''
	while "q"!=input("Press q to end the game\n"):
		pass
	request= MasterControlRequest()
	request.ID="Sadetra"
	request.CMD="End"
	Hubresponse=Hub_Service(request)
	
	print("Master : Game over\n")
	'''




