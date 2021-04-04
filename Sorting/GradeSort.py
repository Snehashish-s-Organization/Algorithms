
dict1 = {"armaan":"B", "Snehashish" : "A+", "Ishan" : "A+", "Shiv":"A", "Yajnesh" : "B", ""}
allgrades = {}

for i,j in dict1.items():
	try:
		allgrades[j].append(i)

	except KeyError:
		allgrades[j] = [i]

for i,j in allgrades.items():
	print(f"{len(j)} ppl got {i}")



