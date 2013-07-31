# Flower excercise (4.2) from Week 0

# Name: Michael Krieger


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob


world.clear()
bob = Turtle()
import math
bob.delay = 0.01

def petal(t,r,angle):
    """create a petal using r as radius and angle as the given angle"""
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def flower(t,p,r,angle):
	"""create flower; p is the number of petals and r is radius"""
	for i in range(p):
		petal(t, r, angle)
		lt(t, 360/p)

def final(t,n,length,angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def arc(t,r,angle):
	arc_length = 2 * math.pi * angle/360 * r
	n = int(arc_length/4) + 1
	segment_length = arc_length / n
	segment_angle = float(angle) / n
	lt(t, segment_angle/2)
	final(t, n, segment_length, segment_angle)
	rt(t, segment_angle/2)

def space(t,distance):
	"""spaces out flowers"""
	pu(t)
	fd(t, distance)
	pd(t)

flower(bob, 7, 60, 50)
space(bob, 150)
flower(bob, 10, 50, 100)
space(bob, 200)
flower(bob, 20, 140, 20)
space(bob,150)

die(bob)

wait_for_user()

