import nltk
from nltk.tree import Tree

# Define the Parse Tree structure for "A boy eats an apple"
parse_tree = Tree('S', [
    Tree('NP', [
        Tree('Det', ['A']),
        Tree('N', ['boy'])
    ]),
    Tree('VP', [
        Tree('V', ['eats']),
        Tree('NP', [
            Tree('Det', ['an']),
            Tree('N', ['apple'])
        ])
    ])
])

# Display the parse tree
print("Parse Tree for 'A boy eats an apple':\n")
parse_tree.pretty_print()
