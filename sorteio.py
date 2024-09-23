from random import randint
computador = randint(0, 100)
nome=str(input('Olá,poderia me informar seu nome primeiro para iniciar o jogo:'))
jogador = int(input("que numero eu pensei?"))
if jogador == computador:
    print(f"você acertou, parabéns {nome}!")
else :
    print(f'você perdeu!!!Eu pensei no numero {computador} e não no numero {jogador}')
    print (f'obrigada por jogar,{nome}!')
           
