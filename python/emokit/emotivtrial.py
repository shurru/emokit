import sys
import emotiv 
import gevent 

#adds the path to all systems
if "C:\\Python27" not in sys.path:
	sys.path.append("C:\\Python27")

if __name__== "main":
	headset= emotiv.Emotiv()
	gevent.spawn(headset.setup)
	gevent.sleep(1)

	try:
		while True: 
			packet= headset.dequeue
			print packet.value, packet.quality
			gevent.sleep(0)
	except KeyboardInterrupt: 
		headset.close()
		
	finally:
		headset.close()