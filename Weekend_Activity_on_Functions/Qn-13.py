# Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567

from functools import reduce
l = [[1,2,3],[4,5],[6,7,8]]
flat_l = list(reduce(lambda x,y : x+y, l))
flat = str(reduce(lambda x,y : str(x) + str(y), flat_l))
print("flatten list of original list : ", flat_l)
print("flatten string of list : ", flat, type(flat))
