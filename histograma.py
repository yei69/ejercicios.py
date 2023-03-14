from collections import Counter

arr = [2, 5, 3, 2, 5, 2, 1, 2, 3, 2, 1]

mapa_arr = Counter(arr)

for valor in sorted(mapa_arr):
	print(f'{valor}: {"*" * mapa_arr[valor]}')