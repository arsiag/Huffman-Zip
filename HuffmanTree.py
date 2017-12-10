__author__ = 'arsia'


from ZipTextFile.HuffmanNode import HuffmanNode

class HuffmanTree:
    fintxt = ''
    level = 0
    def __init__(self, txt):
        self.root = None
        self.txt = txt

        self.freqDict = {}
        self.zipDict = {}
        self.unzipDict = {}
        self.huffman_nodes = []

        self.makeFreq()
        self.makeNodes()
        self.makeHuffmanTree()
        self.makeZipDict()
        self.makeunZipDict()

    def makeFreq(self):
        for i in range(len(self.txt)):
            if self.txt[i] in self.freqDict:
                self.freqDict[self.txt[i]] += 1
            else:
                self.freqDict[self.txt[i]] = 1

    def makeNodes(self):
        for k,v in self.freqDict.items():
            #print("Key " + str(k) + " VAL " + str(v) )
            self.heapInsert(HuffmanNode(k, v))
            #self.huffman_nodes.append(HuffmanNode(k, v))
        #print("HuffmanNodes: ")
        #for i in range(len(self.huffman_nodes)):
        #    print(str(self.huffman_nodes[i].val) , end=" ")
        #print()

    def get_parent(self, i):
        return(int(i - 1 )// 2)

    def get_leftchild(self, i):
        return(2 * i + 1)

    def get_rightchild(self, i):
        return(2 * i + 2)

    def heapInsert(self, HuffmanNode):
        self.huffman_nodes.append(HuffmanNode)
        indx = len(self.huffman_nodes) - 1
        pindx = self.get_parent(indx)
        while indx > 0 and self.huffman_nodes[indx].val < self.huffman_nodes[pindx].val:
            tmpnode = self.huffman_nodes[indx]
            self.huffman_nodes[indx] =  self.huffman_nodes[pindx]
            self.huffman_nodes[pindx] = tmpnode
            indx = pindx
            pindx = self.get_parent(indx)

    def heapRemove(self):
        res = self.huffman_nodes[0]
        self.huffman_nodes[0] = self.huffman_nodes[-1]
        del self.huffman_nodes[-1]
        indx = 0
        lcindx = self.get_leftchild(indx)
        rcindx = self.get_rightchild(indx)
        mylen = len(self.huffman_nodes)
        while (indx < mylen and lcindx < mylen and rcindx < mylen ) and \
                (self.huffman_nodes[indx].val > self.huffman_nodes[lcindx].val or
                 self.huffman_nodes[indx].val > self.huffman_nodes[rcindx].val):
            if self.huffman_nodes[lcindx].val < self.huffman_nodes[rcindx].val:
                tmpnode = self.huffman_nodes[indx]
                self.huffman_nodes[indx] =  self.huffman_nodes[lcindx]
                self.huffman_nodes[lcindx] = tmpnode
                indx = lcindx
                lcindx = self.get_leftchild(indx)
            else:
                tmpnode = self.huffman_nodes[indx]
                self.huffman_nodes[indx] =  self.huffman_nodes[rcindx]
                self.huffman_nodes[rcindx] = tmpnode
                indx = rcindx
                rcindx = self.get_rightchild(indx)
        return res

    def makeHuffmanTree(self):
        while len(self.huffman_nodes) > 1:
            n1 = self.heapRemove()
            n2 = self.heapRemove()
            newHuff = HuffmanNode('*', n1.val+n2.val)
            newHuff.left = n1
            newHuff.right = n2
            self.huffman_nodes.append(newHuff)
        self.root = self.huffman_nodes[0]

    def displayHuffmanTree(self):
        self.display(self.root)

    def display(self, head):
        if head != None:
            print("level: " + str(HuffmanTree.level) + " Key: " + head.key + " Val: " + str(head.val))
            HuffmanTree.level += 1
            self.display(head.left)
            self.display(head.right)
            HuffmanTree.level -= 1

    def makeZipDict(self):
        self.translate(self.root, '')

    def makeunZipDict(self):
        self.unzipDict = {v: k for k, v in self.zipDict.items()}

    def translate(self, head, curstr):
        #print("curstr first: " + curstr)
        if head != None:
            if head.key == '*':
                curstr = curstr+str(0)
                self.translate(head.left, curstr)
                curstr = curstr[:-1]
                curstr = curstr+str(1)
                self.translate(head.right, curstr)
                curstr = curstr[:-1]
            else:
            #print("curstr last: " + curstr)
                self.zipDict[head.key] = curstr

    def decodeHuff1(self, s):
        if len(s) == 0:
            return
        head = self.root
        sign = '\0'
        i = 0
        while head.key == '*':
            if int(s[i]) == 1:
                head = head.right
            else:
                head = head.left
            i += 1
        self.fintxt += head.key
        self.decodeHuff1(s[i:])

    def decodeHuff2(self, s):
        head = self.root
        for i in s:
            if i == '1':
                head = head.right
            else:
                head = head.left
            if head.key != '*':
                print(head.key, end='')
                head = self.root
        print()





