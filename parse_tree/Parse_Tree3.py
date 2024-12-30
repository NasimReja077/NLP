import nltk
from nltk.tree import Tree

# Define the Parse Tree structure
parse_tree = Tree('S', [
    Tree('NP', [
        Tree('Det', ['The']),
        Tree('N', ['cat'])
    ]),
    Tree('VP', [
        Tree('V', ['chased']),
        Tree('NP', [
            Tree('Det', ['a']),
            Tree('N', ['dog'])
        ])
    ])
])

# Display the tree
print("Parse Tree for 'The cat chased a dog':\n")
parse_tree.pretty_print()
