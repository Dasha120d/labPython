import numpy as np
import time
start_timer = time.time()
data = np.loadtxt("77.csv", dtype=str)
print(data)
print("Затрачено: %s секунд" % (time.time()-start_timer ))