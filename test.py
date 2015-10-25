import time

from core.mony import Mony

m = Mony()

while True:
    m.sendData()
    time.sleep(30)
