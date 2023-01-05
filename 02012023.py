#AUFGABE1




liste = {"Birne","Annanas","Apfel","Clementine","Aprikose"}

print(type{liste})
print(liste{3})















#AUFGABE2





# import the time module
import time

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))








#AUFGABE3


liste = {1,4,7,9,2,18}

print(sum{liste})
