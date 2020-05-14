from roku import Roku
import time
roku = Roku("192.168.0.13")

while True:
    time.sleep(10)
    roku.home()
