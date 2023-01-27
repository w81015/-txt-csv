#讀取txt檔，再轉成csv檔

products = []
with open('food.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		p = line.strip().split(',')
		products.append(p)


with open('food.csv', 'w', encoding = 'utf-8-sig') as f:
	f.write('時間,項目,價錢' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] +  ',' + p[2] + '\n')