def _max_heapify(vals:list, i:int = 0):
	"""
	modifies a given list of ints into a max heap representation
	ex. [4,7,8,3,2,6,5] --> [8,7,6,3,2,4,5]
	"""
	# find the children of the i'th element in vals
	l = 2*i + 1
	r = l + 1
	# figure out if the parent and children satisfy the heap property
	# ie. parent > both of its children
	# ie. find the index of the largest val
	larger = i
	if l < len(vals) and (vals[l] > vals[i]):
		larger = l
	if r < len(vals) and (vals[r] > vals[larger]):
		larger = r
	if larger != i:
		tmp = vals[i]
		vals[i] = vals[larger]
		vals[larger] = tmp
		_max_heapify(vals, larger)

def _min_heapify(vals:list, i:int = 0):
	l = 2*i + 1
	r = l + 1
	smaller = i
	if l < len(vals) and (vals[l] < vals[i]):
		smaller = l
	if r < len(vals) and (vals[r] < vals[smaller]):
		smaller = r
	if smaller != i:
		tmp = vals[i]
		vals[i] = vals[smaller]
		vals[smaller] = tmp
		_min_heapify(vals, smaller)

def build_heap(vals:list, property_fn):
	# _max_heapify starting from the leaves
	for i in range(len(vals)//2, -1, -1):
		property_fn(vals, i)


ex = [4,7,8,9,2,6,5]
build_heap(ex)
print(ex)