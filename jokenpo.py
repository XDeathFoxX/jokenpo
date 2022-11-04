from random import choice as cho


def jogar_novamente():
    escolhas='sim','nao'
    jogar_novamente=input('Deseja jogar novamente?(Sim/Não): ').lower().strip()
    jogar_novamente=jogar_novamente.replace('ã','a')
    if jogar_novamente=='sim':
        jokenpo()
    if jogar_novamente=='nao':
        exit()
    if jogar_novamente not in escolhas:
        while jogar_novamente not in escolhas:
            print('Digite Sim ou Não: ')
            jogar_novamente=input('Deseja jogar novamente?(Sim/Não): ').lower().strip()
        else:
            if jogar_novamente=='sim':
                jokenpo()
            if jogar_novamente=='nao':
                exit() 

def jokenpo():
    escolhas = 'pedra','papel','tesoura'
    escolhas0 = 'Pedra, Papel, Tesoura   '
    pedra = 'pedra'
    papel = 'papel'
    tesoura = 'tesoura'
    pc = cho(escolhas) 
    print()
    jogada = input(f'Escolha a sua mão: {escolhas0}').strip().lower()
    
    if jogada in escolhas:
        if jogada == pedra and pc == tesoura:
            print()
            print('Você venceu,Pedra vence Tesoura')
            print()
            jogar_novamente()  
        
        elif jogada == pc :
            print()
            print(f'Empate , {jogada.title()} não vence {jogada.title()}')
            print()
            jogar_novamente()
            
        elif jogada == pedra and pc == papel:
            print()
            print('Você perdeu,Papel vence Pedra')
            print()
            jogar_novamente()

        elif jogada == tesoura and pc == papel:
            print()
            print('Você venceu,Tesoura vence Papel')
            print()
            jogar_novamente()

        elif jogada == tesoura and pc == pedra:
            print()
            print('Você perdeu,Pedra vence Tesoura')
            print()
            jogar_novamente()

        elif jogada == papel and pc == pedra:
            print()
            print('Você venceu,Papel vence Pedra')
            print()
            jogar_novamente()

        elif jogada == papel and pc == tesoura:
            print()
            print('Você perdeu,Tesoura vence Papel')
            print()
            jogar_novamente()

    else:
        while jogada not in escolhas:
            print()
            print('Mão inexistente,digite Pedra ou Papel ou Tesoura  ')
            print()
            jogada = input(f'Escolha a sua mão: {escolhas0}').strip().lower()
        else:
            print(f'Você escolheu {jogada.title()} e o jogo escolheu {pc.title()}')
            if jogada == pedra and pc == tesoura:
                print()
                print('Você venceu,Pedra vence Tesoura')
                print()
                jogar_novamente()  
            
            elif jogada == pc :
                print()
                print(f'Empate , {jogada.title()} não vence {jogada.title()}')
                print()
                jogar_novamente()
            

            elif jogada == pedra and pc == papel:
                print()
                print('Você perdeu,Papel vence Pedra')
                print()
                jogar_novamente()

            elif jogada == tesoura and pc == papel:
                print()
                print('Você venceu,Tesoura vence Papel')
                print()
                jogar_novamente()

            elif jogada == tesoura and pc == pedra:
                print()
                print('Você perdeu,Pedra vence Tesoura')
                print()
                jogar_novamente()

            elif jogada == papel and pc == pedra:
                print()
                print('Você venceu,Papel vence Pedra')
                print()
                jogar_novamente()

            elif jogada == papel and pc == tesoura:
                print()
                print('Você perdeu,Tesoura vence Papel')
                print()
                jogar_novamente()

jokenpo()
