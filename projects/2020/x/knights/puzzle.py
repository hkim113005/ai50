from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Cleaned up "double" implications with biconditionals

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # Game logic
    # Not(And(AKnight, AKnave)),
    # Or(AKnight, AKnave),
    Biconditional(AKnight, Not(AKnave)),

    # A says
    # Implication(AKnight, And(AKnight, AKnave)),
    # Implication(AKnave, Not(And(AKnight, AKnave)))
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Game logic
    # Or(AKnight, AKnave),
    # Not(And(AKnight, AKnave)),
    Biconditional(AKnight, Not(AKnave)),
    # Or(BKnight, BKnave),
    # Not(And(BKnight, BKnave)),
    Biconditional(BKnight, Not(BKnave)),

    # A says
    # Implication(AKnight, And(AKnave, BKnave)),
    # Implication(AKnave, Not(And(AKnave, BKnave)))
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Game logic
    # Or(AKnight, AKnave),
    # Not(And(AKnight, AKnave)),
    Biconditional(AKnight, Not(AKnave)),
    # Or(BKnight, BKnave),
    # Not(And(BKnight, BKnave)),
    Biconditional(BKnight, Not(BKnave)),

    # A says
    # Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B says
    # Implication(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
    Biconditional(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # Game logic
    # Or(AKnight, AKnave),
    # Not(And(AKnight, AKnave)),
    Biconditional(AKnight, Not(AKnave)),
    # Or(BKnight, BKnave),
    # Not(And(BKnight, BKnave)),
    Biconditional(BKnight, Not(BKnave)),
    # Or(CKnight, CKnave),
    # Not(And(CKnight, CKnave)),
    Biconditional(CKnight, Not(CKnave)),
    # A says
    # Implication(BKnight, Implication(AKnight, AKnave)),
    # Implication(BKnight, Implication(AKnave, Not(AKnave))),
    # Implication(BKnave, Implication(AKnight, AKnight)),
    # Implication(BKnave, Implication(AKnave, Not(AKnight))),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # B says
    # Implication(BKnight, CKnave),
    # Implication(BKnave, Not(CKnave)),
    Biconditional(BKnight, CKnave),
    # C says
    # Implication(CKnight, AKnight),
    # Implication(CKnave, AKnave)
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
