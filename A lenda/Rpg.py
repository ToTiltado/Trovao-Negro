import os
from time import sleep
from pygame import mixer
os.system('clear')
mixer.init()
mixer.music.load('Cobblestone Village.mp3')
mixer.music.play(loops=1000)
nomep = str(input('Digite o nome do seu personagem: '))
os.system('clear')
print('Há muito tempo atrás,demônios invadiram o reino de Grã-Bretanha.\nSim,Você {} foi os escolhido para ser o portador do poder do Trovão negro\nTerá que cumprir a profecia de salvar a Grã-Bretanha'.format(nomep))
pular99 = int(input('Digite 1 para pular:\n'))
if pular99 == 1:
    os.system('clear')
    print('-----------')
    print('HISTÓRIA')
    print('-----------')
    print('Você {} nasceu em uma família muito pobre,mas mesmo assim não deixava a vida te derrubar você estava sempre animado\nAlém disso você não conhece seu pai,ele largou você e sua mãe quando você ainda não era nascido\nUma certa noite você com seus 15 anos estava na cama se preparando para dormir\nQuando do nada um Trovão negro caio sobre você atravessando o teto da casa e colocando fogo nela\nSua mãe desesperada foi para seu quarto e viu você divido ao meio,você estava quase morto\nMas do nada as partes dividas do seu corpo começaram a se juntar,por uma energia desconhecida.'.format(nomep))
    pular1 = int(input('Digite 1 para pular:\n'))
    if pular1 == 1:
        os.system('clear')
        mixer.music.pause()
        mixer.init()
        mixer.music.load('Musica de Batalha RPG Parte 1.mp3')
        mixer.music.play(loops=1000, start=0.0)
        print('----------')
        print('FASE 01:')
        print('----------')
        f1 = int(input('Após se recuperar no hospital você encontra uns garotos zuando um menina por ser pobre oque você faz?\n1:Faz nada\n2:Pede para parar\n3:Tenta impedir\n4:Bates neles\n'))
        if f1 == 1:
            os.system('clear')
            print('O menina acabou apanhando,e você não fez nada')
            sleep(2)
            print('Você perdeu,o jogo irá recomeçar daqui 10 segundos')
            mixer.music.pause()
            sleep(10)
            os.system('clear')
            os.system('python3 Rpg.py')
        elif f1 == 2:
            os.system('clear')
            print('Você pediu para parar,mas eles fizeram e tacarem pedras em você')
            sleep(2)
            print('Você perdeu,o jogo irá recomeçar daqui 10 segundos')
            mixer.music.pause()
            sleep(10)
            os.system('clear')
            os.system('python3 Rpg.py')
        elif f1 == 3:
            os.system('clear')
            print('Você tentou impedir,mas acabaram te batendo e você nunca mais saiu de casa')
            sleep(2)
            print('Você perdeu,o jogo irá recomeçar daqui 10 segundos')
            mixer.music.pause()
            sleep(10)
            os.system('clear')
            os.system('python3 Rpg.py')
        elif f1 == 4:
            os.system('clear')
            print('Você deu um soco tão forte em um dos garotos,que ela acabou voando para metros de distancia')
            sleep(3.5)
            print('----------')
            print('FASE 02')
            print('----------')
            f2 = int(input('Após quebrar todo mundo na porrada você descobriu que o nome dessa menina é Glyni\nE vocês viraram muito amigos 5 anos se passaram e vocês continuam amigos\nEntão certo dia Glyni pediu pra que você cortasse umas árvores na frenta da casa dela\nMas não tinha nada para cortar então escolha uma opção:\n1:Fazer nada\n2:Ficar puto ficar socando e chutando as coisas\n'))
            if f2 == 1:
                os.system('clear')
                print('----------')
                print('FASE 03')
                print('----------')
                print('Glyni ficou estresada mas te entendeu.')
                f3 = int(input('Então no mesmo dia,vocês foram ao ferrero,para pedir para que ele fizesse um machado para vocês\nEntão no outro dia vocês foram buscar o machado,mas do nada vocês sentiram tremores,então saiu umas especie de demônios do chão o que você vai fazer?\n1:Fugir com a Glyni\n2:Lutar com seu machado\n'))
                if f3 == 1:
                    os.system('clear')
                    print('Você e Glyni tentaram fugir,mas o demônio jogou uma magia nas costas da Glyni\nMas você conseguiu levantar ela,e fugiram')
                    print('----------')
                    print('FASE 04')
                    print('----------')
                    f4 = int(input('Você verifica se esta tudo bem com a Glyni,você olhou e aparentemente ela estava bem\nO que você faz?\n1:Levar Glyni para casa dela,pois e mais perto da sua casa,para que você veja como está sua mãe\n2:Levar a Glyni para o hospital,e depois ver sua mãe\n'))
                    if f4 == 1:
                        os.system('clear')
                        print('----------')
                        print('FASE 05')
                        print('----------')
                        f5 = int(input('Quando você chegou na sua casa,viu sua mãe jogada no chão,ela estava bem,mas estava desmaiada\nEntão você ouviu um barulho vindo da cozinha,quando você chegou lá você viu um demônio de 2 metro\nOque você faz?\n1:Lutar\n2:Mete o pé\n'))
                        if f5 == 1:
                            os.system('clear')
                            print('----------')
                            print('FASE 06')
                            print('----------')
                            f6 = int(input('Você ficou putasso e foi para cima dando logo um socão na cara do demônio para ele ficar esperto\nEle decidiu atacar,enquanto o soco dele estava vindo\noque você faz?\n1:Esquivar\n2:Da um soco na mão dele\n'))
                            if f6 == 1:
                                os.system('clear')
                                print('----------')
                                print('FASE 07')
                                print('----------')
                                f7  = int(input('Você se esquivou,mas você não tinha visto que sua mãe estava indo ver como você estava,e ela acabou recebendo o soco do demônio\nFoi um soco tão forte,que ela foi decapitada,Você ficou mais puto do que já estava,então com um unico soco\nVocê matou o demônio e destruiu sua casa ao mesmo tempo\nOque você faz agora\n1:Enterrar sua mãe e andar pelas ruas chorando\n2:Enterrar sua mãe e ir para a casa da Glyni\n'))
                                if f7 == 1:
                                    os.system('clear')
                                    print('----------')
                                    print('FASE 08')
                                    print('----------')
                                    f8 = int(input('Você saiu pelas ruas chorando,ai você senta em um banco\nO que você faz agora?\n1:Volta para casa da Glyni\n2:Ficar andando por ai chorando\n'))
                                    if f8 == 1:
                                        os.system('clear')
                                        print('----------')
                                        print('FASE 09')
                                        print('----------')
                                        f9 = int(input('Quando você chegou na casa da Glyni,você viu sangue no chão,e depois ouviu barulho da Glyni gritando\nTinha um demônio devorando\nO que você faz\n1:Atacar sem piedade\n2:Testa pegar a Glyni e leva ela embora puxando o braço dela\n'))
                                        if f9 == 1:
                                            os.system('clear')
                                            print('----------')
                                            print('FASE 10')
                                            print('----------')
                                            f10 = int(input(''))
                                    elif f8 == 2:
                                        os.system('clear')
                                        print('Brotou um demônio do nada do seu lado,e te deu um soco,você estava sem vontade de viver\nEntão o demônio enfiou a mão dele no seu peito\nVocê morreu')
                                        p = int(input('1:Recomeçar\n2:Parar\n'))
                                        if p == 1:
                                            os.system('clear')
                                            os.system('python3 Rpg.py')
                                        elif p == 2:
                                            exit()
                                        else:
                                            print('Digite um numero valido')
                                            p = int(input('1:Recomeçar\n2:Parar\n'))
                                            if p != 1 or p != 2:
                                                x = 1
                                                while x != 0:
                                                    if p != 1 or p != 2:
                                                        print('Escreva um numero valido animal')
                                                        sleep(5)
                                                        os.system('clear')
                                                        p = int(input('1:Recomeçar\n2:Parar\n'))
                                                        x += 0
                                                    else:
                                                        x -= 1
            elif f2 == 2:
                os.system('clear')
                print('Você acabou socando uma árvore,e derrubou ela com um único soco')
                sleep(2.5)
                print('----------')
                print('FASE 03')
                print('----------')
                print('Você descoobriu que tem algo muito errado com você desde daquele dia que você foi atingido por um trovão')
                f3 = int(input('Você mostrou para a Glyni que você derrubou tudo no soco\nMas ela duvidou,então você explicou tudo,todavia ela pediu para você provar\nMas você está cansado para provar\n1:Falar que está cansado,e dormir\n2:Provar para ela\n'))
                if f3 == 1:
                    os.system('clear')
                    f4 = int(('Você teve que provar no dia em seguinte,deu certo,mas pelo esforço que você fez,gerou muita energia\nIsso chamou atenção dos demônios que estavam dispostos a entrar em guerra com o mundo para obter seu poder\nQuando os demônios estam prestes a sair do inferno você sente a energia deles oque fazer\n1:Avisar todo mundo para fugirem,e fugir junto\n2:Avisar para todo mundo fugir,e lutar com os demônios\n'))
                else:
                    os.system('clear')
                    print('Escreva um numero valido')
                    sleep(2)
                    mixer.music.pause()
                    print('O programa reniciará daqui 10 segundos')
                    sleep(10)
                    os.system('clear')
                    os.system('python3 Rpg.py')
            else:
                os.system('clear')
                print('Escreva um numero valido')
                sleep(2)
                mixer.music.pause()
                print('O programa reniciará daqui 10 segundos!')
                sleep(10)
                os.system('clear')
                os.system('python3 Rpg.py')
        else:
            os.system('clear')
            print('Digite um numero valido\nO programa reniciará em 10 segundos!!')
            mixer.music.pause()
            sleep(10)
            os.system('clear')
            os.system('python3 Rpg.py')
    else:
        os.system('clear')
        print('escreva um numero valido\nPrograma reniciará em 10 segundos!!')
        sleep(10)
        mixer.music.pause()
        os.system('clear')
        os.system('python3 Rpg.py')
else:
    os.system('clear')
    print('Escreva um numero valido\nO programa reniciará em 10 segundos')
    mixer.music.pause()
    sleep(10)
    os.system('clear')
    os.system('python3 Rpg.py')
print('FIM\nCRIADOR:LEANDRO\nPROGRAMADOR:LEANDRO\nROTEIRISTA:LEANDRO\nIDEIA DE FAZER O RPG:ESDRAS')
