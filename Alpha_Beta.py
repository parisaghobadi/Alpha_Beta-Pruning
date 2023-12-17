# Creating a class for node

class Node:
    def __init__(self,value= None):
        self.value = value
        self.children = []

# Creating function for the algorithm!
        
def alpha_beta(node, depth, alpha, beta , maximizing_player):
    if depth==0 or not node.children:
        return node.value
        
    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta(child,depth-1 , alpha , beta, False))
            alpha = max(alpha , value)
            print(f'MAX node? : {maximizing_player} / node value = {value} --> Alpha is: {alpha} and Beta is:{beta}')
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min( value, alpha_beta(child , depth-1 ,alpha, beta, True ))
            beta = min(beta , value)
            print(f'MAX node? : {maximizing_player} / node value = {value} --> Alpha is: {alpha} and Beta is:{beta}')
            if alpha >= beta:
                break
        return value
    

# Creating an example!
    
# The valus of nodes : 
    
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node(9)
node5 = Node(1)
node6 = Node(2)

# The children of nodes : 

node1.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6]

# See the result !

result = alpha_beta(node1, 2, float('-inf'), float('inf'), True)
print('\n  And the optimal value is:', result , '\n')