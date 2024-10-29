#list
scores = [90, 45, 78, 56, 23, 88]


#acess a value
print(scores[0]) #first
print(scores[3]) #third

#add
scores.append(61)
print(scores)

#remove
scores.pop(3)
print(scores)

scores.sort(reverse=True)
print(scores)
