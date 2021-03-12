
dict1 = {"armaan":"B", "Snehashish" : "A+", "Ishan" : "A+", "Shiv":"A", "Yajnesh" : "B", ""}
allgrades = {}

for i,j in dict1.items():
	try:
		allgrades[j].append(i)

	except KeyError:
		allgrades[j] = [i]

for i,j in allgrades.items():
	print(f"{len(j)} ppl got {i}")


# A2 = []
# A = []
# B2 = []
# B =[]
# C2 = []
# C = []
# for i in dict1:
# 	if dict1[i] == "A":
# 		A.append(i)
# 	elif dict1[i] == "A+":
# 		A2.append(i)
# 	elif dict1[i] == "B+":
# 		B2.append(i)
# 	elif dict1[i] == "B":
# 		B.append(i)
# 	elif dict1[i] == "C+":
# 		C2.append(i)
# 	elif dict1[i] == "C":
# 		C.append(i)
# print(f"{len(A2)} ppl got A+")
# print(f"{len(A)} ppl fot A")
