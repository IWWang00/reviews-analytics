data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for comment in f:
		data.append(comment)
		count += 1
		if count % 1000 == 0:
			print(len(data))
	
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc: #排列出來 不是清單
	if wc[word] > 100: #次數超過100次才印出來
		print(word, wc[word]) #印出word 和出現次數
print(len(wc))
print(wc['Allen'])

#讓使用者查想查的字
while True:
	word = input('請輸入查詢的字: ')
	
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')
		
print('感謝使用查詢功能')




# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# print('留言平均長度是', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')
# print(new[0])



# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good),'筆留言提到good')
# print(good[0])