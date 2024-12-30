class ParseTreeNode:
    def __init__(self, value):  # Constructor to initialize the node
        self.value = value
        self.children = []  # List to hold child nodes

    def add_child(self, child):
        """Adds a child node to the current node."""
        self.children.append(child)

    def display(self, level=0):
        """Recursively displays the tree structure."""
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)


# Example Parse Tree for "The cat chased a dog."
root = ParseTreeNode("S")  # Start symbol

# NP subtree (The cat)
np1 = ParseTreeNode("NP")
np1.add_child(ParseTreeNode("Det"))  # Determiner
np1.children[0].add_child(ParseTreeNode("The"))
np1.add_child(ParseTreeNode("N"))  # Noun
np1.children[1].add_child(ParseTreeNode("cat"))

# VP subtree (chased a dog)
vp = ParseTreeNode("VP")
vp.add_child(ParseTreeNode("V"))  # Verb
vp.children[0].add_child(ParseTreeNode("chased"))

np2 = ParseTreeNode("NP")
np2.add_child(ParseTreeNode("Det"))  # Determiner
np2.children[0].add_child(ParseTreeNode("a"))
np2.add_child(ParseTreeNode("N"))  # Noun
np2.children[1].add_child(ParseTreeNode("dog"))

vp.add_child(np2)  # Attach second NP to VP

# Attach NP and VP to the root
root.add_child(np1)
root.add_child(vp)

# Display the tree
print("Parse Tree for 'The cat chased a dog':\n")
root.display()