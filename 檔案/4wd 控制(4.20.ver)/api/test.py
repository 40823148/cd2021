import sim as vrep
import sys
# child threaded script: 
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
 
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode,joint=vrep.simxGetObjectHandle(clientID,'input',vrep.simx_opmode_oneshot_wait)
 

 
if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
 
errorCode=vrep.simxSetJointTargetVelocity(clientID,joint,-270, vrep.simx_opmode_oneshot_wait)

