import numpy as np
from random import shuffle

depth_total=0

class Node:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string


class searchtree:
      
      def __init__(self): #constructor of class
          self.depth = 0
          
          self.root = None


      def create(self,val):  #create binary search tree nodes

          if self.root == None:

             self.root = Node(val)

          else:

             current = self.root

             while 1:
                 self.depth=self.depth+1
                 if val < current.info:

                   if current.left:
                      current = current.left
                   else:
                      current.left = Node(val)
                      break;      

                 elif val > current.info:
                 
                    if current.right:
                       current = current.right
                    else:
                       current.right = Node(val)
                       break;      

                 else:
                    break 

      
      def preorder(self,node):
          
           if node is not None:
              
              print (node.info)
              self.preorder(node.left)
              self.preorder(node.right)
              
              
      @staticmethod
      def height(root):
        if root is None:
          return 0
        else:
          return max(searchtree.height(root.left), searchtree.height(root.right)) + 1



toplam = 0

for i in range(100):
    tree = searchtree()
    arr = np.arange(100)
    shuffle(arr)
   
    for i in arr:
        tree.create(i)
    
        
    toplam = tree.depth

print (toplam/100)
