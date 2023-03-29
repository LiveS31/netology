from main import Stack
def balanced(s):
    stack = Stack()
    balance = True
    index = 0
    while index < len(s) and balance:
        symbol = s[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
             if stack.is_empty():
                 balance = False
             else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.is_empty():
        return "сбалансировано"
    else:
        return "несбалансировано"

def matches(opens, closers):
    opens = "([{"
    closers = ")]}"
    return opens.index(opens) == closers.index(closers)

#сбалансированные
s1 = '(((([{}]))))'
s2 = '[([])((([[[]]])))]{()}'
s3 = '{{[()]}}'

#несбалансированные
sn1 = '}{}'
sn2 = '{{[(])]}}'
sn3 = '[[{())}]'

if __name__ == '__main__':
    balanced(s1)