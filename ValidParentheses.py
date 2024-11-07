def isValid(s):
    correspondances = {
    '(': ')',
    '{': '}',
    '[': ']'
    }
    pile = []
    for char in s:
        if char in correspondances:  # Si c'est une parenthèse ouvrante
            pile.append(char)
        else:
            if not pile:
                return False
            
            dernier_element = pile.pop()
            if correspondances[dernier_element] != char:
                return False
    return len(pile) == 0

print(isValid(']'))

    
