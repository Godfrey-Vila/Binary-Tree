print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()



        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)
        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_max()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    my_name = ["G", "O", "D", "F", "R", "E", "Y", "C", "V", "I", "L", "A"]
    my_name_tree = build_tree(my_name)
    print("Your name in order Traversal list is: ", my_name_tree.in_order_traversal())
    print("Your name in  pre-order Traversal list is: ", my_name_tree.pre_order_traversal())
    print("Your name in  post-order Traversal list is: ", my_name_tree.post_order_traversal())

    print("")
    Input = input(str("What letter from GODFREY C VILA you want to delete in any tranversal order?: ")).upper()
    print("")
    my_name_tree.delete(Input)
    print("Your name in order Traversal list is: ", my_name_tree.in_order_traversal())
    print("Your name in  pre-order Traversal list is: ", my_name_tree.pre_order_traversal())
    print("Your name in  post-order Traversal list is: ", my_name_tree.post_order_traversal())
