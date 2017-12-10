__author__ = 'arsia'



def get_parent(i):
    return(int(i - 1 )// 2)

def get_leftchild(i):
    return(2 * i + 1)

def get_rightchild(i):
    return(2 * i + 2)

# insert puts new item at the end, then repeatedly compares it to its parent, swapping if it is smaller
# stops when it hits index 0, or when parent is smaller
def insert(x, heap):
    heap.append(x)
    indx = len(heap) - 1
    pindx = get_parent(indx)
    while indx > 0 and heap[indx] < heap[pindx]:
        tmpval = heap[indx]
        heap[indx] =  heap[pindx]
        heap[pindx] = tmpval
        indx = pindx
        pindx = get_parent(indx)

def remove(heap):
    res = heap[0]
    print("Heap: " + str(heap))
    heap[0] = heap[len(heap) - 1]
    del heap[-1]
    print("Popped: " + str(heap))
    indx = 0
    lcindx = get_leftchild(indx)
    rcindx = get_rightchild(indx)
    while (indx < len(heap) and lcindx < len(heap) and rcindx < len(heap) ) and \
            (heap[indx] > heap[lcindx] or heap[indx] > heap[rcindx]):
        print("Now: " + str(heap))
        if heap[lcindx] < heap[rcindx]:
            tmpval = heap[indx]
            heap[indx] =  heap[lcindx]
            heap[lcindx] = tmpval
            indx = lcindx
            lcindx = get_leftchild(indx)
        else:
            tmpval = heap[indx]
            heap[indx] =  heap[rcindx]
            heap[rcindx] = tmpval
            indx = rcindx
            rcindx = get_rightchild(indx)
    return res






heap = [1,5,3]
print(heap)
insert(2, heap)
print(heap)
insert(7, heap)
print(heap)
insert(4, heap)
print(heap)
remove(heap)
print(heap)
remove(heap)
print(heap)


# 96 total characters - 95 comparisons
# including chinese & russian, 65,000  - 64,999 -> 17

# a g C # r A t y e x a h t u B i o p % s q w ! r g c s
#
'''
c = 2 * p + 1
c = 2 * p + 2

p = (c - 1) / 2
p = (c - 2) / 2
index 1, children are 2*1+1 and 2*1+2
index 3, children are 2*3+1 and 2*3+2
11  17 28 29 93 44  31
0
         11
    17         28
29    93     44   31



'''