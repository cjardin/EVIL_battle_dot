from antlr4 import * 
from battle_dotLexer import battle_dotLexer
from battle_dotParser import battle_dotParser
from dot_generator import dot_generator
import time
import glob


def main():

    for f in glob.glob("tests/*.bdot"):
        print (f)
        lexer = battle_dotLexer (FileStream(f, encoding='utf-8'))
        token_stream = CommonTokenStream(lexer)
        parser = battle_dotParser(token_stream)
        visitor = dot_generator()

        tree = parser.start()
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)


if __name__ == '__main__':
    main()
