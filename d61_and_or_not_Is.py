"""
Estruturas condicionais:
and, or, not, is
"""

ativo = False
logado = False
chevrolet = False
honda = False

"""
-Operadores unários:
    - not, is
    
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo
    
-Operadores binários:
    - and, or
    
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
    

"""
if ativo:
    if not logado:
        print("Você precisa entrar com login e senha!")
    elif ativo and logado:
        print("Bem-vindo, usuário!")
else:
    print("Deseja criar uma conta?")

if chevrolet or honda:
    print("Deseja fazer sua revisão?")
    if chevrolet is True:
        print("Temos promoções na troca dos pneus!")
    elif honda is True:
        print("Temos promoções na troca de óleo!")
else:
    print("Não trabalhamos com outras marcas!")
