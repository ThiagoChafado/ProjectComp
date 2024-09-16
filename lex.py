def dfa(m, string):
    q, sigma, delta, q0, f = m
    qA = q0
    tokens = []

    # Split the string into tokens based on spaces
    token = ''
    for char in string:
        if char.isspace():
            if token:
                tokens.append(token)
                token = ''  # restart
        else:
            token += char

    # Adds last token
    if token:
        tokens.append(token)

    # Process tokens
    for token in tokens:
        if token in delta.get(qA, {}):
            qA = delta[qA][token]
        else:
            # Try to match multi-character tokens
            matched = False
            for key in delta.get(qA, {}):
                if token.startswith(key):
                    qA = delta[qA][key]
                    remaining_token = token[len(key):]
                    if remaining_token:
                        # Add remaining part of the token back to the list for further processing
                        tokens.insert(tokens.index(token) + 1, remaining_token)
                    matched = True
                    break
            if not matched:
                return False

    return qA in f
delta = {
    'q0': {
        'VAR': 'q1',
        'IF': 'q1',
        'ELSE': 'q1',
        'WHILE': 'q1'
    },
    'q1': { #q1 - q6 for VAR
        'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q2', 'e': 'q2', 'f': 'q2', 'g': 'q2', 'h': 'q2', 'i': 'q2',
        'j': 'q2', 'k': 'q2', 'l': 'q2', 'm': 'q2', 'n': 'q2', 'o': 'q2', 'p': 'q2', 'q': 'q2', 'r': 'q2',
        's': 'q2', 't': 'q2', 'u': 'q2', 'v': 'q2', 'w': 'q2', 'x': 'q2', 'y': 'q2', 'z': 'q2',
    },
    'q2': {
        '=': 'q3', 'END': 'qf', 'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q2', 'e': 'q2', 'f': 'q2', 'g': 'q2', 'h': 'q2', 'i': 'q2',
        'j': 'q2', 'k': 'q2', 'l': 'q2', 'm': 'q2', 'n': 'q2', 'o': 'q2', 'p': 'q2', 'q': 'q2', 'r': 'q2',
        's': 'q2', 't': 'q2', 'u': 'q2', 'v': 'q2', 'w': 'q2', 'x': 'q2', 'y': 'q2', 'z': 'q2', '0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2',
        '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2',
    },
    'q3': {
        'a': 'q4', 'b': 'q4', 'c': 'q4', 'd': 'q4', 'e': 'q4', 'f': 'q4', 'g': 'q4', 'h': 'q4', 'i': 'q4',
        'j': 'q4', 'k': 'q4', 'l': 'q4', 'm': 'q4', 'n': 'q4', 'o': 'q4', 'p': 'q4', 'q': 'q4', 'r': 'q4',
        's': 'q4', 't': 'q4', 'u': 'q4', 'v': 'q4', 'w': 'q4', 'x': 'q4', 'y': 'q4', 'z': 'q4', '0': 'q5', '1': 'q5', '2': 'q5', '3': 'q5', '4': 'q5', '5': 'q5',
        '6': 'q5', '7': 'q5', '8': 'q5', '9': 'q5',
    },
    'q5':{
        '0': 'q5', '1': 'q5', '2': 'q5', '3': 'q5', '4': 'q5', '5': 'q5',
        '6': 'q5', '7': 'q5', '8': 'q5', '9': 'q5','END':'qf'
    },
    'q4': {
        'END': 'qf', 'a': 'q4', 'b': 'q4', 'c': 'q4', 'd': 'q4', 'e': 'q4', 'f': 'q4', 'g': 'q4', 'h': 'q4', 'i': 'q4',
        'j': 'q4', 'k': 'q4', 'l': 'q4', 'm': 'q4', 'n': 'q4', 'o': 'q4', 'p': 'q4', 'q': 'q4', 'r': 'q4',
        's': 'q4', 't': 'q4', 'u': 'q4', 'v': 'q4', 'w': 'q4', 'x': 'q4', 'y': 'q4', 'z': 'q4', '0': 'q4', '1': 'q4', '2': 'q4', '3': 'q4', '4': 'q4', '5': 'q4',
        '6': 'q4', '7': 'q4', '8': 'q4', '9': 'q4',
    },

    'qf': {}
}


q = ['q0', 'q1', 'q2', 'q3', 'qf']
f = ['qf']
sigma = ['VAR', 'IF', 'ELSE', 'WHILE', '+', '-', '*', '/', '==', '>', '<', '>=', '<=', '!=', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'END']

print(dfa([q, sigma, delta, 'q0', f], 'VAR a23 = a5 END'))  # True
