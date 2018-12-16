from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict(
    {
        Token.Separator: "#cc5454",
        Token.QuestionMark: "#673ab7 bold",
        Token.Selected: "#cc5454",  # default
        Token.Pointer: "#673ab7 bold",
        Token.Instruction: "",  # default
        Token.Answer: "#f44336 bold",
        Token.Question: "",
    }
)


questions = [
    {
        "type": "checkbox",
        "message": "Select toppings",
        "name": "toppings",
        "choices": [
            Separator("= The Meats ="),
            {"name": "Ham"},
            {"name": "Ground Meat"},
            {"name": "Bacon"},
            Separator("= The Cheeses ="),
            {"name": "Mozzarella", "checked": True},
            {"name": "Cheddar"},
            {"name": "Parmesan"},
            Separator("= The usual ="),
            {"name": "Mushroom"},
            {"name": "Tomato"},
            {"name": "Pepperoni"},
            Separator("= The extras ="),
            {"name": "Pineapple"},
            {"name": "Olives", "disabled": "out of stock"},
            {"name": "Extra cheese"},
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    }
]

answers = prompt(questions, style=style)
pprint(answers)
