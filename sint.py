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
    "B": [["VAR"]],  
    "C": [["B", "D", "B"]],  # C -> B D B
    "D": [["<"], [">"], ["!="], ["="]],  # D -> < | > | != | =
    "E": [["VAR"], ["0-9"]],  # E -> (a-z)* | (0-9)*
    "F": [["="], ["+"], ["-"], ["*"], ["/"]],  # F -> = | + | - | * | /
}

slr_table = {
    'action': {
        (0, 'VAR'): 's3',
        (0, 'IF'): 's4',
        (0, 'WHILE'): 's5',
        (1,'$'):'acc',
        (2,'VAR'):'s3',
        (2,'IF'):'s4',
        (2,'WHILE'):'s5',
        (4,'(C)'):'s10',
        (5,'(C)'):'s11',
        (6,'='):'s13',
        (6,'+'):'s14',
        (6,'/'):'s15',
        (6,'*'):'s16',
        (7,'VAR'):'r7',
        (7,'IF'):'r7',
        (7,'='):'r7',
        (7,'WHILE'):'r7',
        (7,'<'):'r7',
        (7,'>'):'r7',
        (7,'!='):'r7',
        (7,'+'):'r7',
        (7,'/'):'r7',
        (7,'*'):'r7',
        (9,'VAR'):'r2',
        (9,'='):'s17',
        (9,'IF'):'r2',
        (9,'WHILE'):'r2',
        (10,'ELSE'):'s18',
        (11,'{ S }'):'s19',
        (17,'0'):'s23',
        (18,'{ S }'):'s24',
        (19,'VAR'):'r5',
        (19,'IF'):'r5',
        (19,'WHILE'):'r5',
        (20,'VAR'):'r6',
        (20,'IF'):'r6',
        (20,'WHILE'):'r6',
        (21,'VAR'):'r3',
        (21,'IF'):'r3',
        (21,'WHILE'):'r3',
        (22,'VAR'):'r13',
        (22,'IF'):'r13',
        (22,'WHILE'):'r13',
        (23,'VAR'):'r14',
        (23,'IF'):'r14',
        (23,'WHILE'):'r14',
        (24,'VAR'):'r4',
        (24,'IF'):'r4',
        (24,'WHILE'):'r4',
        (0, 'IDENTIFIER'):'s7',
        (2, 'IDENTIFIER'):'s7',  
        (3, 'IDENTIFIER'):'s7',
        (7 ,'IDENTIFIER'):'r7',
        (9, 'IDENTIFIER'):'r2',
        (12, 'IDENTIFIER'):'s7',
        (13,'IDENTIFIER'):'r15',
        (14,'IDENTIFIER'):'r16',
        (15,'IDENTIFIER'):'r17',
        (16,'IDENTIFIER'):'r18',
        (17,'IDENTIFIER'):'s22',
        (19,'IDENTIFIER'):'r5',
        (20,'IDENTIFIER'):'r6',
        (21,'IDENTIFIER'):'r3',
        (22,'IDENTIFIER'):'r13',
        (23,'IDENTIFIER'):'r14',
        (24,'IDENTIFIER'):'r4',

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
        (12,'B'):20,
        (17,'E'):21
        
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

            for _ in range(len(right_side[0])):
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
    tokens.append(('END', '$'))  
    return tokens

input_string = "VAR a = 1 { VAR b = 3 } WHILE"


tokens = tokenize(input_string)

if tokens:
    slr_parse(tokens, grammar, slr_table)
