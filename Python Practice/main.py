theboard = {'topl': 'X', 'topm': ' ', 'topr': 'o',
            'midl': 'X', 'midm': 'o', 'midr': ' ',
            'lowl': 'X', 'lowm': ' ', 'lowr': 'o'}


def board(b):
    print(b['topl']+'|'+b['topm']+'|'+b['topr'])
    print('-+-+-')
    print(b['midl']+'|'+b['midm']+'|'+b['midr'])
    print('-+-+-')
    print(b['lowl']+'|'+b['lowm']+'|'+b['lowr'])


board(theboard)
