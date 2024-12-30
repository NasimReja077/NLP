import nltk
from nltk.tree import Tree

# Define the Parse Tree structure
parse_tree = Tree('S', [
    Tree('NP', ['I']),  # Subject
    Tree('VP', [
        Tree('V', ['drive']),  # Verb
        Tree('NP', [          # Direct Object
            Tree('Det', ['a']),
            Tree('N', ['car'])
        ]),
        Tree('PP', [          # Prepositional Phrase
            Tree('P', ['to']),
            Tree('NP', [
                Tree('Det', ['my']),
                Tree('N', ['college'])
            ])
        ])
    ])
])

# Display the Parse Tree
print("Parse Tree for 'I drive a car to my college':\n")
parse_tree.pretty_print()
