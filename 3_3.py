import pandas
import time
start_timer = time.time()
data = pandas.read_csv("77.csv")
print(data)
print("Затрачено: %s секунд" % (time.time()-start_timer ))