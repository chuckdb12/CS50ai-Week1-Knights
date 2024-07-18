from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

sentences = set()

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    #Information about the problem itself
    
    #If player A is a knave, he is not a knight
    Biconditional(AKnave,Not(AKnight)),

    #Info about what the caracter said

    #If player A is a knave, he is not a knight and a knave
    Implication(AKnave,Not(And(AKnight,AKnave))),

    #If player A is a knight, he is a knight and a knave
    Implication(AKnight,(And(AKnight,AKnave)))
    


)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    #Information about the problem itself
    
    #If player A is a knave, he is not a knight
    Biconditional(AKnave,Not(AKnight)),
    Biconditional(BKnave,Not(BKnight)),

    #Info about what the caracter said

    #If player A is a knave, they are not both knaves
    Implication(AKnave,Not(And(AKnave,BKnave))),

    #If player A is a knight, they are both knaves (impossible)
    Implication(AKnight,(And(AKnave,BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    #If player A is a knave, he is not a knight

    Biconditional(AKnave,Not(AKnight)),
    Biconditional(BKnave,Not(BKnight)),

    #Info about what the caracter said

    #If A is a knave or B is a knight, both player need to be of different kinds
    Implication(Or(AKnave,BKnight),And(Biconditional(AKnave,BKnight),Biconditional(AKnight,BKnave))),
    #If A is a knight of B is a knave, both player need to be the same kind 
    Implication(Or(AKnight,BKnave),And(Biconditional(AKnave,BKnave),Biconditional(AKnight,BKnight))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
    #If player A is a knave, he is not a knight

    Biconditional(AKnave,Not(AKnight)),
    Biconditional(BKnave,Not(BKnight)),
    Biconditional(CKnave,Not(CKnight)),
    
    #Info about what the caracter said

    #A is either a knight, or he is lying about being a knave
    Or(AKnight,Not(AKnave)),
    #If A is a knave, B is a knight and vice-versa
    Biconditional(AKnave,BKnight),
    #If A is a knight, B must be a knave and vice-versa
    Biconditional(AKnight,BKnave),
    #If C is a knave, B must be a knight and vice-versa
    Biconditional(CKnave,BKnight),
    #If C is a knight, B must be a knave and vice-versa
    Biconditional(CKnight,BKnave),
    #If A is a knight, C must be a knight and vice-versa
    Biconditional(AKnight,CKnight),
    #If A is a knave, C must be a knave and vice-versa
    Biconditional(AKnave,CKnave)




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
