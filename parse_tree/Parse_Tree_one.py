class ParseTreeNode:
    def __init__(self, value):
        """Initialize the node with a value and an empty list of children."""
        self.value = value
        self.children = []

    def add_child(self, child_value):
        """Add a child node to the current node."""
        child_node = ParseTreeNode(child_value)
        self.children.append(child_node)
        return child_node  # Return the child node for chaining

    def display(self, level=0):
        """Recursively display the tree structure."""
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)


# Building the Parse Tree for "A boy eats an apple."
root = ParseTreeNode("S")  # Start symbol (Sentence)

# Noun Phrase (NP)
np = root.add_child("NP")
np.add_child("Det").add_child("A")  # Determiner
np.add_child("N").add_child("boy")  # Noun

# Verb Phrase (VP)
vp = root.add_child("VP")
vp.add_child("V").add_child("eats")  # Verb

# Noun Phrase (NP)
np2 = vp.add_child("NP")
np2.add_child("Det").add_child("an")  # Determiner
np2.add_child("N").add_child("apple")  # Noun

# Display the tree
print("Parse Tree for 'A boy eats an apple':\n")
root.display()
