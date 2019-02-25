import random
#this is a dictionary
d={8:37,11:2,20:34,28:4,38:9,40:68,65:46,52:81,89:70,93:64,76:97}

p=random.choice([2,8,11,34,38,89,93,52])

print("you got",p)

if p in d:
	if p>d[p]:
		print("snake")
	else:
		print("lader")

		print("you can go to",d[p])
