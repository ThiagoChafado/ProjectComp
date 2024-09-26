def dfa(m, string):
    delta, q0, f = m
    qA = q0
    token = ''
    tape = ''
    # tabela como dicionario
    symbols_tab = {} 

    def add_symbols(token, type):
        token = token.strip() 
        if token and token not in symbols_tab:
            symbols_tab[token] = {'type': type, 'scope': 'global'}
            print(f"Added in symbols table: {token} ({type})")
        elif token:
            print(f"Token '{token}' already exists in symbols table")

    for x in string:
        try:
            token += x
            if x.isspace(): 
                if qA in f and token.strip(): 
                    print(f'token "{token.strip()}" is valid')
                    tape += token
                    if token.strip().isalpha(): #define tipo e adiciona na tabela
                        add_symbols(token.strip(), 'id')
                    elif token.strip().isdigit():  
                        add_symbols(token.strip(), 'number')
                    token = ''
                qA = 'q0'
                continue
            
            if x == '=': 
                if qA in f and token.strip(): 
                    print(f'token "{token.strip()}" is valid')
                    tape += token
                    add_symbols(token.strip(), 'id')
                print(f'token "=" is valid')
                tape += '='
                token = ''
                qA = 'q0'
                continue

            if x == '{':
                print(f'token "{{" is valid')
                tape += '{'
                token = ''
                qA = 'q0'
                continue
            
            if x == '}': 
                print(f'token "}}" is valid')
                tape += '}'
                token = ''
                qA = 'q0'
                continue

            qA = delta[qA][x]

        except KeyError:
            if token.strip():  
                print(f"ERRO with token '{token.strip()}'")
            else:
                print("ERRO: found empty token")
            return symbols_tab  

    if qA in f and token.strip():  
        print(f'token "{token.strip()}" is valid')
        tape += token
        if token.strip().isalpha():
            add_symbols(token.strip(), 'id')
        elif token.strip().isdigit(): 
            add_symbols(token.strip(), 'number')
        return symbols_tab
    else:
        if token.strip(): 
            print(f"ERRO with token '{token.strip()}'")
        return symbols_tab

delta = {
    'q0': {
        'V': 'q1',  # VAR
        'I': 'q10',  # IF
        'E': 'q20',  # ELSE
        'W': 'q30',  # WHILE
        'a': 'q40', 'b': 'q40', 'c': 'q40', 'd': 'q40', 'e': 'q40', 'f': 'q40', 'g': 'q40', 'h': 'q40',
        'i': 'q40', 'j': 'q40', 'k': 'q40', 'l': 'q40', 'm': 'q40', 'n': 'q40', 'o': 'q40', 'p': 'q40',
        'q': 'q40', 'r': 'q40', 's': 'q40', 't': 'q40', 'u': 'q40', 'v': 'q40', 'w': 'q40', 'x': 'q40',
        'y': 'q40', 'z': 'q40',
        '0': 'q50', '1': 'q50', '2': 'q50', '3': 'q50', '4': 'q50', '5': 'q50', '6': 'q50', '7': 'q50',
        '8': 'q50', '9': 'q50',
        '{': 'q60',  
        '}': 'q61', 
    },
    'q1': {
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
    }, 'q40': { 
        'a': 'q40', 'b': 'q40', 'c': 'q40', 'd': 'q40', 'e': 'q40', 'f': 'q40', 'g': 'q40', 'h': 'q40',
        'i': 'q40', 'j': 'q40', 'k': 'q40', 'l': 'q40', 'm': 'q40', 'n': 'q40', 'o': 'q40', 'p': 'q40',
        'q': 'q40', 'r': 'q40', 's': 'q40', 't': 'q40', 'u': 'q40', 'v': 'q40', 'w': 'q40', 'x': 'q40',
        'y': 'q40', 'z': 'q40',
    }, 'q50': { 
        '0': 'q50', '1': 'q50', '2': 'q50', '3': 'q50', '4': 'q50', '5': 'q50', '6': 'q50', '7': 'q50',
        '8': 'q50', '9': 'q50',
    }
}

f = ['q3', 'q11', 'q23', 'q34', 'q40', 'q50', 'q60', 'q61']

symbols_tab = dfa([delta, 'q0', f], 'VAR a = 1 + 2 { VAR b = 3 }')
print(symbols_tab)
