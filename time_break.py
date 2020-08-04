import time
import webbrowser
import requests

total_breaks = 3
break_counts = 0


print("this start on "+time.ctime())

while(break_counts < total_breaks):
	time.sleep(5)
	controller = webbrowser.get()
	controller.open("https://www.youtube.com/watch?v=JyN-3YpuHn8; autoplay(K)")
	break_counts = break_counts + 1


