from context import Context
from hundred_expression import HundredExpression
from one_expression import OneExpression
from ten_expression import TenExpression
from thousand_expression import ThousandExpression

if __name__ == "__main__":
    while True:
        text = str(input('chiffre romain : '))
        context = Context(text)

        interpreter_tree = [ThousandExpression(), HundredExpression(), TenExpression(), OneExpression()]

        for expression in interpreter_tree:
            expression.interpret(context)

        print(context.output)
