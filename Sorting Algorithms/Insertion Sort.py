# add an insertion sort function for lists of numbers (increasing order)
def insertion_sort(l):
	N = len(l)
	if(N < 2):
		return l
	for i in range(N):
		insertion_value = l[i]
		inserted = False
		for j in range(i-1, -1, -1):
			if(l[j] > insertion_value):
				l[j+1] = l[j]
			else:
				l[j+1] = insertion_value
				inserted = True
				break
		if(not inserted):
			l[0] = insertion_value
	return l


if __name__ == "__main__":
	numbers = [3,4,2,1]
	print(insertion_sort(numbers))