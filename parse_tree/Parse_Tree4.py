import nltk
from nltk.tree import Tree

def create_parse_tree(sentence):
    """Creates a parse tree for a given sentence using NLTK."""
    words = sentence.split()  # Tokenize the sentence into words

    # Ensure the sentence has at least 3 words
    if len(words) < 3:
        print("The sentence is too short to build a parse tree.")
        return None

    # Create the parse tree structure
    parse_tree = Tree('S', [
        Tree('NP', [  # Noun Phrase
            Tree('Det', [words[0]]),  # First word as Determiner
            Tree('N', [words[1]])  # Second word as Noun
        ]),
        Tree('VP', [  # Verb Phrase
            Tree('V', [words[2]])  # Third word as Verb
        ])
    ])

    # Handle remaining words (e.g., objects or prepositional phrases)
    if len(words) > 3:
        direct_object = Tree('NP', [
            Tree('Det', [words[3]]),  # Determiner for object
            Tree('N', [words[4]]) if len(words) > 4 else None  # Noun for object
        ])
        parse_tree[1].append(direct_object)  # Add direct object to VP

    return parse_tree


# Get user input
sentence = input("Enter a sentence (e.g., 'The cat chased a dog'): ").strip()
tree = create_parse_tree(sentence)

if tree:
    print("\nParse Tree:")
    tree.pretty_print()  # Print the tree structure