import time
import webbrowser
import requests

total_breaks = 3
break_counts = 0

# play youtube video
print("this start on "+time.ctime())

while(break_counts < total_breaks):
	time.sleep(5)
	r = requests.get()
    r = requests.put("https://www.youtube.com/watch?v=JyN-3YpuHn8; autoplay")
		break_counts = break_counts + 1

	# it returns youtube video
