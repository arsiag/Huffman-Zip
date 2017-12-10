__author__ = 'arsia'

from ZipTextFile.HuffmanTree import HuffmanTree



myHtree = HuffmanTree("ABACA")

print("zipDict:   " + str(myHtree.zipDict))
print("unzipDict: " + str(myHtree.unzipDict))
print("txt: " + "ABACA")
binzipme = ''.join(format(ord(x), 'b') for x in "ABACA")
print("bin: " + binzipme)
zipzipme = ''.join(myHtree.zipDict[x] for x in "ABACA")
print("zip: " + zipzipme)
print("Display:   ")
myHtree.displayHuffmanTree()

mystr="1001011"
mystr1="0100110"

myHtree.decodeHuff2(zipzipme)
myHtree.decodeHuff1(zipzipme)
print("fintxt: " + myHtree.fintxt)
'''
zipme1 = "this is a test"
zipme2 = "this is a much longer test with many different chars like xyz or other signs like @#$"
zipme3 = "aaaa bbb cccc dd eeeeeeeee fffffffffffffffff ghkuhvpuycwejhqvdocvq7feruhqvcdkhgc 13ugdc @#$&pihvfogc$%    &%$DIDIYTD HHHHHHHHfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ljhfvqhvcg;jhva;dhvdshv;ajhv;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"

HTree1 = HuffmanTree(zipme1)

print("zipDict:   " + str(HTree1.zipDict))
print("unzipDict: " + str(HTree1.unzipDict))
print("txt: " + zipme1)
binzipme = ''.join(format(ord(x), 'b') for x in zipme1)
print("bin: " + binzipme)
zipzipme = ''.join(HTree1.zipDict[x] for x in zipme1)
print("zip: " + zipzipme)
#print("Display:   ")
#HTree1.displayHuffmanTree()

HTree2 = HuffmanTree(zipme2)

print("zipDict:   " + str(HTree2.zipDict))
print("unzipDict: " + str(HTree2.unzipDict))
print("txt: " + zipme2)
binzipme = ''.join(format(ord(x), 'b') for x in zipme2)
print("bin: " + binzipme)
zipzipme = ''.join(HTree2.zipDict[x] for x in zipme2)
print("zip: " + zipzipme)
#print("Display:   ")
#HTree2.displayHuffmanTree()

HTree3 = HuffmanTree(zipme3)

print("zipDict:   " + str(HTree3.zipDict))
print("unzipDict: " + str(HTree3.unzipDict))
print("txt: " + zipme3)
binzipme = ''.join(format(ord(x), 'b') for x in zipme3)
print("bin: " + binzipme)
zipzipme = ''.join(HTree3.zipDict[x] for x in zipme3)
print("zip: " + zipzipme)
#print("Display:   ")
#HTree3.displayHuffmanTree()



#step 1, figure out how many of each letter are in the phrase

#step 2, figure out a way to grab which 2 have the smallest frequencies & remove from the list

#step 3, figure out how to create a node, where the left & right are the 2 smallest, & put the node back to the list



* 14 (eahsit_)

a  0010 (1)
e  000  (1)
h  0011 (1)
i  100  (2)
s  01   (3)
t  101  (3)
_  11   (3)

                 * 14
             /              \
         * 6                  * 8
      /       \              /     \
      *3       s 3        * 5     _ 3
   /     \               /  \
 e 1      * 2          i 2   t 3
      /       \
    a 1       h 1


t 10
a 00
e 010
s 011
f 11

teasf - 01010101 01010101 01010101 01010101 01010101
teasf - 10010000 1111


teasf

          *
       /      \
      *        e
    /   \
   a     *
        / \
       *   s
      / \
     t   f

'''

