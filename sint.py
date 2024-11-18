grammar = {
    "S'": [["S"]],  
    "S": ["A", "S"],   # S -> AS 
    "A": [
        ["VAR", "B"],  # A -> VAR B
        ["VAR", "B", "=", "E"],  # A -> VAR B = E
        ["IF", "(", "C", ")", "{", "S", "}", "ELSE", "{", "S", "}"],  # A -> IF ( C ) { S } ELSE { S }
        ["WHILE", "(", "C", ")", "{", "S", "}"],  # A -> WHILE ( C ) { S }
        ["B", "F", "B"],  # A -> B F B
    ],
    "B": [["IDENTIFIER"]],  
    "C": [["B", "D", "B"]],  # C -> B D B
    "D": [["<"], [">"], ["!="], ["="]],  # D -> < | > | != | =
    "E": ["IDENTIFIER"], # E -> (a-z)* | (0-9)*
    "F": [["="], ["+"], ["-"], ["*"], ["/"]],  # F -> = | + | - | * | /
}

slr_table = {
    'action': {
        (0, 'VAR'): 's3',
        (0, 'IF'): 's4',
        (0, 'WHILE'): 's5',
        (0, '$'): 'r2',
        
        (1,'$'):'acc',
        
        (2,'VAR'):'s3',
        (2,'IF'):'s4',
        (2,'WHILE'):'s5',
        (2, '$'): 'r2',
        
        (4,'(C)'):'s10',
        
        (5,'(C)'):'s11',
        
        (6,'='):'s13',
        (6,'+'):'s14',
        (6,'-'):'s15',
        (6,'/'):'s16',
        (6,'*'):'s17',
        
        (7,'VAR'):'r8',
        (7,'IF'):'r8',
        (7,'='):'r8',
        (7,'WHILE'):'r8',
        (7,'<'):'r8',
        (7,'>'):'r8',
        (7,'!='):'r8',
        (7,'+'):'r8',
        (7,'/'):'r8',
        (7,'*'):'r8',
        (7,'$'):'r8',
        
        (8, '$'): 'r1',
        
        (9,'VAR'):'r3',
        (9,'='):'s18',
        (9,'IF'):'r3',
        (9,'WHILE'):'r3',
        (9, '$'): 'r3',
        
        
        (10,'{ S }'):'s19',
        
        (11,'{ S }'):'s20',
        
        
        
        (19,'ELSE'):'s24',
        
        (20,'VAR'):'r6',
        (20,'IF'):'r6',
        (20,'WHILE'):'r6',
        (20,'$'):'r6',
        
        (21,'VAR'):'r7',
        (21,'IF'):'r7',
        (21,'WHILE'):'r7',
        (21,'$'):'r7',
        
        (22,'VAR'):'r4',
        (22,'IF'):'r4',
        (22,'WHILE'):'r4',
        (22,'$'):'r4',
        
        (23,'VAR'):'r14',
        (23,'IF'):'r14',
        (23,'WHILE'):'r14',
        (23,'$'):'r14',
        
        
        
        (24,'{ S }'):'s25',
        
        (25,'VAR'):'r5',
        (25,'IF'):'r5',
        (25,'WHILE'):'r5',
        (25,'$'):'r5',
        
        (0, 'IDENTIFIER'):'s7',
        (2, 'IDENTIFIER'):'s7',  
        (3, 'IDENTIFIER'):'s7',
        (7 ,'IDENTIFIER'):'r8',
        (9, 'IDENTIFIER'):'r3',
        (12, 'IDENTIFIER'):'s7',
        (13,'IDENTIFIER'):'r15',
        (14,'IDENTIFIER'):'r16',
        (15,'IDENTIFIER'):'r17',
        (16,'IDENTIFIER'):'r18',
        (17,'IDENTIFIER'):'R19',
        (18,'IDENTIFIER'):'s23',
        (19,'IDENTIFIER'):'r5',
        (20,'IDENTIFIER'):'r6',
        (21,'IDENTIFIER'):'r7',
        (22,'IDENTIFIER'):'r4',
        (23,'IDENTIFIER'):'r14',
        (24,'IDENTIFIER'):'r4',
        (25,'IDENTIFIER'):'r5',

    },
    'goto': {
        (0, 'S'): 1,
        (0, 'A'): 2,
        (0,'B'):6,
        
        (2,'S') : 8,
        (2,'A'):2,
        (2,'B'):6,
        
        (3,'B'):9,
        
        (6,'F'):12,
        
        (3,'F'):12,
        (12,'B'):21,
        (17,'E'):21,
        (18,'E'):22
        
    }
}

def slr_parse(token_stream, grammar, slr_table):
    stack = [0]
    pointer = 0

    while True:
        
        state = stack[-1]


        if pointer < len(token_stream):
            current_token = token_stream[pointer][0] 
        else:
            current_token = '$' 

        action = slr_table['action'].get((state, current_token))
        print(action)

        if not action:
            print(f"Erro: Nenhuma ação definida para estado {state} e token '{current_token}'")
            return False

        if action == 'acc':  
            print("Entrada aceita!")
            return True

        elif action.startswith('s'):  # Shift
            next_state = int(action[1:])
            stack.append(next_state)  
            pointer += 1  

        elif action.startswith('r'):  # Reduce
            production_index = int(action[1:])
            left_side, right_side = list(grammar.items())[production_index]

            for i in range(len(right_side[0])):
                stack.pop()

            top_state = stack[-1]
            stack.append(slr_table['goto'][(top_state, left_side)])

            print(f"Redução: {left_side} -> {' '.join(right_side[0])}")
        else:
            print(f"Erro desconhecido na ação '{action}'")
            return False


def tokenize(input_string):
    tokens = []
    words = input_string.split()  
    
    for word in words:
        if word == 'VAR':
            tokens.append(('VAR', 'VAR'))
        elif word.isalpha():  
            tokens.append(('IDENTIFIER', word))
        elif word == '=':
            tokens.append(('=', '='))
        elif word.isdigit():
            tokens.append((word, word))
        elif word == '{':
            tokens.append(('{', '{'))
        elif word == '}':
            tokens.append(('}', '}'))
        elif word == 'WHILE':
            tokens.append(('WHILE', 'WHILE'))
        else:
            print(f"Token desconhecido: {word}")
            return None
    return tokens

input_string = "VAR a ="


tokens = tokenize(input_string)

if tokens:
    slr_parse(tokens, grammar, slr_table)
