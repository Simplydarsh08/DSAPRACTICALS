class Node:
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, data):
        if self.root == None:
            self.root = Node(data)
            print(data , " Inserted Successfully.")
            return
        if root.data > data:
            if root.left:
                self.insert(root.left,data)
            else:
                root.left = Node(data)
                print(data , " Inserted Successfully.")
        elif root.data < data:
            if root.right:
                self.insert(root.right,data)
            else:
                root.right = Node(data)
                print(data , " Inserted Successfully.")
        else:
            print("Can't insert",data, "since it's a duplicate!")
            return
    
    def search(self, root, key):
        if self.root == None:
            print("Tree is Empty!")
            return
        if root.data > key:
            if root.left:
                self.search(root.left,key)
            else:
                print("Key not found.")
        elif root.data < key:
            if root.right:
                self.search(root.right,key)
            else:
                print("Key not found.")
        else:
            print(key, "Found Successfully.")
    
    def dfs(self,root): # Inorder Traversal
        if root:
            self.dfs(root.left)
            print(root.data , end = ' ')
            self.dfs(root.right)
            
    def depth(self,root):
        if root == None:
            return 0
        
        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)
        
        if rdepth > ldepth:
            return rdepth + 1
        return ldepth + 1
    
    def mirror(self,root):
        if root is None:
            return None
        
        root.left, root.right = self.mirror(root.right), self.mirror(root.left)
        return root
    
    def copy_tree(self,root):
        if root is None:
            return None
        
        new_root = Node(root.data)
        new_root.left = self.copy_tree(root.left)
        new_root.right = self.copy_tree(root.right)
        return new_root
    
    def bfs(self): # Level Wise Traversal
        stack = []
        stack.append(self.root)
        while stack:
            temp = stack.pop(0)
            print(temp.data, end = " ")
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
    
    def leaf_nodes(self,root): # Similar to dfs
        if root:
            self.leaf_nodes(root.left)
            if not root.left and not root.right:
                print(root.data , end = " ")
            self.leaf_nodes(root.right)
            
    def parent_child(self, root):
        if root:
            if root.left or root.right:
                print(root.data , end = " ") 
            if root.left:
                print(" Left child -> " , root.left.data, end = " ")
            if root.right:
                print(" Right child -> " , root.right.data)
            self.parent_child(root.left)
            self.parent_child(root.right)
            
    def delete_node(self, root, key):
        if not root:
            return None

        # Step 1: Find the node
        if key < root.data:
            root.left = self.delete_node(root.left, key)
            return root
        if key > root.data:
            root.right = self.delete_node(root.right, key)
            return root

        # Step 2: Node found
        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:  # No left child
            return root.right
        if not root.right:  # No right child
            return root.left

        # Case 3: Node has 2 children
        # Find inorder successor
        succ = root.right
        while succ.left:
            succ = succ.left

        # Copy successor's value to current node
        root.data = succ.data
        # Delete successor
        root.right = self.delete_node(root.right, succ.data)

        return root

                

bst = BST()


while True:
    print("\n--- BST MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal (DFS)")
    print("4. Depth of Tree")
    print("5. Create Mirror Copy")
    print("6. Display Mirror Tree (DFS)")
    print("7. Copy Tree")
    print("8. BFS (Level-wise)")
    print("9. Display Leaf Nodes")
    print("10. Display Parent-Child")
    print("11. Delete Node")
    print("12. Exit")
    
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        data = int(input("Enter value to insert: "))
        bst.insert(bst.root, data)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        bst.search(bst.root, key)
    elif choice == 3:
        bst.dfs(bst.root)
        print()
    elif choice == 4:
        print("Depth of tree:", bst.depth(bst.root))
    elif choice == 5:
        mirror_bst = BST()
        mirror_bst.root = bst.copy_tree(bst.root)
        mirror_bst.mirror(mirror_bst.root)
        print("Mirrored copy created successfully.")
    elif choice == 6:
        if mirror_bst:
            mirror_bst.dfs(mirror_bst.root)
            print()
        else:
            print("Mirror copy not created yet.")
    elif choice == 7:
        new_bst = BST()
        new_bst.root = bst.copy_tree(bst.root)
        print("Tree copied successfully.")
    elif choice == 8:
        bst.bfs()
        print()
    elif choice == 9:
        bst.leaf_nodes(bst.root)
        print()
    elif choice == 10:
        bst.parent_child(bst.root)
    elif choice == 11:
        key = int(input("Enter node value to delete: "))
        bst.root = bst.delete_node(bst.root, key)
        print("Node deleted if it existed.")
    elif choice == 12:
        break
    else:
        print("Invalid choice! Try again.")


