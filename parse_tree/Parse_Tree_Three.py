class ParseTreeNode:
    def __init__(self, value):
        """Initialize a parse tree node with a value and an empty list of children."""
        self.value = value
        self.children = []

    def add_child(self, child):
        """Add a child node to the current node."""
        self.children.append(child)

    def display(self, level=0):
        """Recursively display the tree structure."""
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)


# Build the parse tree for "I drive a car to my college"

# Root (Sentence)
root = ParseTreeNode("S")

# Subject (Noun Phrase)
np = ParseTreeNode("NP")
np.add_child(ParseTreeNode("I"))  # Subject Pronoun

# Verb Phrase
vp = ParseTreeNode("VP")
vp.add_child(ParseTreeNode("V"))
vp.children[0].add_child(ParseTreeNode("drive"))  # Verb

# Direct Object (Noun Phrase)
np_obj = ParseTreeNode("NP")
np_obj.add_child(ParseTreeNode("Det"))
np_obj.children[0].add_child(ParseTreeNode("a"))  # Determiner
np_obj.add_child(ParseTreeNode("N"))
np_obj.children[1].add_child(ParseTreeNode("car"))  # Noun

# Prepositional Phrase
pp = ParseTreeNode("PP")
pp.add_child(ParseTreeNode("P"))
pp.children[0].add_child(ParseTreeNode("to"))  # Preposition
pp.add_child(ParseTreeNode("NP"))
pp.children[1].add_child(ParseTreeNode("Det"))
pp.children[1].children[0].add_child(ParseTreeNode("my"))  # Determiner
pp.children[1].add_child(ParseTreeNode("N"))
pp.children[1].children[1].add_child(ParseTreeNode("college"))  # Noun

# Assemble the tree
vp.add_child(np_obj)  # Add object NP to VP
vp.add_child(pp)      # Add prepositional phrase to VP
root.add_child(np)    # Add subject NP to root
root.add_child(vp)    # Add VP to root

# Display the tree
print("Parse Tree for 'I drive a car to my college':\n")
root.display()
