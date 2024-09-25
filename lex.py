def dfa(m, string):
    q, sigma, delta, q0, f = m
    qA = q0
    token = ''
    tape = ''
    for x in string:
        try:
            token += x
            if x == ' ' or x == '=':
                if qA in f and token.strip() != '=':
                    print(f'token "{token.strip()}" is valid')
                    tape += token
                    token = ''
                if x == '=':
                    print(f'token "=" is valid')
                    tape += token
                    token = '' 
                qA = 'q0'
                continue
            
            qA = delta[qA][x]

        except KeyError:
            print(f"ERRO com token '{token.strip()}'")
            return False

    if qA in f and token.strip():
        print(f'token "{token.strip()}" is valid')
        tape +=token
        return tape
    else:
        print(f"ERRO com token '{token.strip()}'")
        return False


delta = {
    'q0': {
        'V': 'q1',  # q1 for VAR
        'I': 'q10',  # q2 for IF
        'E': 'q20',  # q3 for ELSE
        'W': 'q30',  # q4 for WHILE
        'a': 'q40', 'b': 'q40', 'c': 'q40', 'd': 'q40', 'e': 'q40', 'f': 'q40', 'g': 'q40', 'h': 'q40',
        'i': 'q40', 'j': 'q40', 'k': 'q40', 'l': 'q40', 'm': 'q40', 'n': 'q40', 'o': 'q40', 'p': 'q40',
        'q': 'q40', 'r': 'q40', 's': 'q40', 't': 'q40', 'u': 'q40', 'v': 'q40', 'w': 'q40', 'x': 'q40',
        'y': 'q40', 'z': 'q40',
        '0': 'q50', '1': 'q50', '2': 'q50', '3': 'q50', '4': 'q50', '5': 'q50', '6': 'q50', '7': 'q50',
        '8': 'q50', '9': 'q50',
    }, 'q1': {
        'A': 'q2',
    }, 'q2': {
        'R': 'q3',
    }, 'q10': {
        'F': 'q11',
    }, 'q20': {
        'L': 'q21',
    }, 'q21': {
        'S': 'q22',
    }, 'q22': {
        'E': 'q23',
    }, 'q30': {
        'H': 'q31',
    }, 'q31': {
        'I': 'q32',
    }, 'q32': {
        'L': 'q33',
    }, 'q33': {
        'E': 'q34'
    }, 'q40': {  # Variables
        'a': 'q40', 'b': 'q40', 'c': 'q40', 'd': 'q40', 'e': 'q40', 'f': 'q40', 'g': 'q40', 'h': 'q40',
        'i': 'q40', 'j': 'q40', 'k': 'q40', 'l': 'q40', 'm': 'q40', 'n': 'q40', 'o': 'q40', 'p': 'q40',
        'q': 'q40', 'r': 'q40', 's': 'q40', 't': 'q40', 'u': 'q40', 'v': 'q40', 'w': 'q40', 'x': 'q40',
        'y': 'q40', 'z': 'q40',
    }, 'q50': {  # Nums
        '0': 'q50', '1': 'q50', '2': 'q50', '3': 'q50', '4': 'q50', '5': 'q50', '6': 'q50', '7': 'q50',
        '8': 'q50', '9': 'q50',
    }
}

q = ['q0', 'q1', 'q2', 'q3', 'q10', 'q11', 'q20', 'q21', 'q22', 'q23', 'q30', 'q31', 'q32', 'q33', 'q34', 'q40', 'q50']
f = ['q3', 'q11', 'q23', 'q34', 'q40', 'q50']
sigma = ['V', 'A', 'R', 'I', 'F', 'E', 'L', 'S', 'E', 'W', 'H', 'I', 'L', 'E', '+', '-', '*', '/', '==', '>', '<', '>=', '<=', '!=', 
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '{', '}']


print(dfa([q, sigma, delta, 'q0', f], 'ELSE a == 2'))  # True
