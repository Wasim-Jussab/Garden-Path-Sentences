
import spacy

nlp = spacy.load("en_core_web_sm")

# Garden path sentences
gardenpathSentences = [
    "The old man the boat.",
    "The man whistling tunes pianos.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Entities:")
    for ent in doc.ents:
        print(ent.text, "-", ent.label_, "-", spacy.explain(ent.label_))
    print()

# Look up and print the meanings of entities
print("Entity explanations:")
print("CARDINAL:", spacy.explain("CARDINAL"))
print("GPE:", spacy.explain("GPE"))

# Explanation of entities:
# 1. CARDINAL: Numerals that do not fall under another type
#    Example: "The old man the boat." - "old" (CARDINAL)
#    Yes, the entity makes sense in terms of the word "old" being a numeral.

# 2. GPE: Countries, cities, states
#    Example: "The cotton clothing is made of grows in Mississippi." - "Mississippi" (GPE)
#    Yes, the entity makes sense in terms of "Mississippi" being a state.
