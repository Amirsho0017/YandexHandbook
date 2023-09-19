# LIFO, push(append), pop(pop), top, TC = O(1)
# exampleStack = [1,2,3]  with py list

# Balanced brackets
# Examples:
# input = "({})" // true
# input = "({}" // false
# input = "({[]" // false
# input = "()({[]})" // true
# input = "()()[]{}" // true
# input = "(([{}]]" // false


def is_balanced(value: str) -> bool:
    stack = []
    for i in value:
        if is_open(i):
            stack.append(i)
        else:
            if len(stack) and is_pair(stack[-1], i):
                stack.pop()
            else:
                return False

    return not bool(stack)


def is_open(bracket: str) -> bool:
    return bracket in "({["


def is_pair(open_bracket: str, close_bracket: str) -> bool:
    return ((open_bracket == "{" and close_bracket == "}") or
            (open_bracket == "[" and close_bracket == "]") or
            (open_bracket == "(" and close_bracket == ")"))


print(is_balanced(str(input('input value: '))))
