class ParseTreeNode:
    def __init__(self, value):  # Constructor for initializing a node
        self.value = value
        self.children = []  # Children nodes list

    def add_child(self, child):
        """Adds a child node to the current node."""
        self.children.append(child)

    def display(self, level=0):
        """Displays the tree structure recursively with indentation."""
        print("  " * level + str(self.value))  # Indent based on level
        for child in self.children:
            child.display(level + 1)


def create_parse_tree(sentence):
    """Creates a simple parse tree for a given sentence."""
    words = sentence.split()  # Tokenize the sentence into words

    if len(words) < 3:  # Validate if the sentence has enough words
        print("The sentence is too short to build a parse tree.")
        return None

    root = ParseTreeNode("S")  # Root of the parse tree representing the sentence

    # Noun Phrase (NP)
    np = ParseTreeNode("NP")
    np.add_child(ParseTreeNode("Det"))  # Determiner node
    np.children[0].add_child(ParseTreeNode(words[0]))  # First word as Determiner
    np.add_child(ParseTreeNode("N"))  # Noun node
    np.children[1].add_child(ParseTreeNode(words[1]))  # Second word as Noun
    root.add_child(np)

    # Verb Phrase (VP)
    vp = ParseTreeNode("VP")
    vp.add_child(ParseTreeNode("V"))  # Verb node
    vp.children[0].add_child(ParseTreeNode(words[2]))  # Third word as Verb

    # Handle any remaining words as part of the verb phrase (e.g., direct objects or prepositional phrases)
    if len(words) > 3:
        np_obj = ParseTreeNode("NP")  # Create another NP for the direct object
        np_obj.add_child(ParseTreeNode("Det"))
        np_obj.children[0].add_child(ParseTreeNode(words[3]))  # Determiner for object
        if len(words) > 4:  # Check for additional words like the object noun
            np_obj.add_child(ParseTreeNode("N"))
            np_obj.children[1].add_child(ParseTreeNode(words[4]))
        vp.add_child(np_obj)

    root.add_child(vp)  # Attach VP to the root

    return root


# Get user input
sentence = input("Enter a sentence (e.g., 'The cat chased a dog'): ").strip()
parse_tree = create_parse_tree(sentence)

if parse_tree:
    print("\nParse Tree:")
    parse_tree.display()
