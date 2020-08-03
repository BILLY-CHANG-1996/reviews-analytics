data = []
count = 0
percent = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count%10000 == 0:
            percent += 1
            print(percent, '%')
print('檔案讀取完了總共有', len(data),'筆資料')

print(data[0])

sum_len = 0
for d in data:
    sum_len += len(d)
print('每筆留言的平均長度是', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆資料長度小於100')
print(new[0].strip())
print(new[1].strip())

# good = [d for d in data if 'good' in d]
wd = []
w = input('請輸入要搜尋的留言關鍵字: ')
for d in data:
    if w == 'N':
        continue   
    if w in d:
        wd.append(d)
print('一共有', len(wd), '筆留言提到', w)
print(wd[0])

#文字計數
wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增字進字典
#如果在字典中出現過的次數大於100
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print(len(wc))
#文字查詢功能
while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])

    else:
        print('留言中沒有你要找的詞')
        print('感謝使用本查詢功能')

