player1 = input('viberite deystviye')
player2 = input('viberite deystvie')
if player1==player2:
    print('nichya')
elif player1=='kamen' and player2=='bumaga':
    print('player1 wins')
elif player1=='nojnici' and player2=='bumaga':
    print('player1 wins')
elif player1=='bumaga' and player2=='kamen':
    print('player2 wins')
elif player1=='kamen' and player2=='nojnici':
    print('player1 wins')
elif player1=='nojnici' and player2=='kamen':
    print('player2 wins')
elif player1=='bumaga' and player2=='nojnici':
    print('player2 wins')
else:
    print('ne pavilniy vvod')

