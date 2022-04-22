data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for comment in f:
		data.append(comment)
		count += 1
		if count % 1000 == 0:
			print(len(data))


print(data[0])

		