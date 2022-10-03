import pygame, string, random
from sys import exit

# from pyparsing import delimited_list
# word_to_guess = input("Word to guess: ")


pygame.init()
width, height = 1700,900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()
l = [
"Achilles",
"Agni",
"Ah Muzen Cab",
"Ah Puch",
"Amaterasu",
"Anhur",
"Anubis",
"Ao Kuang",
"Aphrodite",
"Apollo",
"Arachne",
"Ares",
"Artemis",
"Artio",
"Athena",
"Atlas",
"Awilix",
"Baba Yaga",
"Bacchus",
"Bakasura",
"Baron Samedi",
"Bastet",
"Bellona",
"Cabrakan",
"Camazotz",
"Cerberus",
"Cernunnos",
"Chaac",
"Chang e",
"Charybdis",
"Chernobog",
"Chiron",
"Chronos",
"Cliodhna",
"Cthulhu",
"Cu Chulainn",
"Cupid",
"Da Ji",
"Danzaburou",
"Discordia",
"Erlang Shen",
"Eset",
"Fafnir",
"Fenrir",
"Freya",
"Ganesha",
"Geb",
"Gilgamesh",
"Guan Yu",
"Hachiman",
"Hades",
"He Bo",
"Heimdallr",
"Hel",
"Hera",
"Hercules",
"Horus",
"Hou Yi",
"Hun Batz",
"Izanami",
"Janus",
"Jing Wei",
"Jormungandr",
"Kali",
"Khepri",
"King Arthur",
"Kukulkan",
"Kumbhakarna",
"Kuzenbo",
"Loki",
"Medusa",
"Mercury",
"Merlin",
"Morgan Le Fay",
"Mulan",
"Ne Zha",
"Neith",
"Nemesis",
"Nike",
"Nox",
"Nu Wa",
"Odin",
"Olorun",
"Osiris",
"Pele",
"Persephone",
"Poseidon",
"Ra",
"Raijin",
"Rama",
"Ratatoskr",
"Ravana",
"Scylla",
"Serqet",
"Set",
"Shiva",
"Skadi",
"Sobek",
"Sol",
"Sun Wukong",
"Susano",
"Sylvanus",
"Terra",
"Thanatos",
"The Morrigan",
"Thor",
"Thoth",
"Tiamat",
"Tsukuyomi",
"Tyr",
"Ullr",
"Vamana",
"Vulcan",
"Xbalanque",
"Xing Tian",
"Yemoja",
"Ymir",
"Zeus",
"Zhong Kui"

]
def main():
    global done, event, letter_rect
    font = pygame.font.SysFont("couriernew", 30)
    loser = pygame.font.SysFont("couriernew", 50)

    alphabet = list(string.ascii_uppercase)
    space = 50

    word_to_guess = random.choice(l)
    #You can set the word to guess here
    word_to_guess = 'Tennessee'
    alpha_list = ['_'] * len(word_to_guess)
    letter_dic = {a: (100 + (i * 50), 700) for i, a in enumerate(alphabet)}

    a,b = set(), set()
    x = []
    s = 0
    while True:

        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            key =pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                main()
        gul_top = pygame.Rect(1200,100,300,10)
        gul_body = pygame.Rect(1490,100,10,500)
        gul_bottom = pygame.Rect(1150,600,410,10)
        gul_hook = pygame.Rect(1200,100,10,40)

        pygame.draw.rect(screen, 'white', gul_top)
        pygame.draw.rect(screen, 'white', gul_body)
        pygame.draw.rect(screen, 'white', gul_bottom)
        pygame.draw.rect(screen, 'white', gul_hook)

        score = font.render((f'Score: {s}'), False, 'red')
        score_rect = score.get_rect(center = (100, height/2))

        loser_txt = loser.render((f'YOU LOSE!'), False, 'red')
        loser_txt_rect = loser_txt.get_rect(center=(width/2, height/2-70))

        loser_cor = loser.render(f"THE CORRECT WORD IS \"{word_to_guess.upper()}\"",False,'red')
        loser_cor_rect = loser_cor.get_rect(center=(width/2, height/2))


        win_txt = loser.render((f'YOU GUSSED THE WORD!'), False, 'red')
        win_txt_rect = win_txt.get_rect(center=(width/2, height/2))

        play_again = loser.render((f'PRESS SPACE TO PLAY AGAIN!'), False, 'red')
        play_again_rect = play_again.get_rect(center=(width/2, height/2+70))

        
        num_guesses = alphabet.count(' ')
        num_gs = font.render((f'Total: {num_guesses}'), False, 'red')
        num_gs_rect = num_gs.get_rect(center=(1500, 810))

        num_right = len(a)
        num_cor = font.render((f'Correct: {num_right}'), False, 'red')
        num_cor_rect = num_cor.get_rect(center=(100, 810))

        num_wrong = num_guesses-len(a)
        num_rong = font.render((f'Incorrect: {num_wrong}'), False, 'red')
        num_rong_rect = num_cor.get_rect(center=(700, 810))

        gussed_lable = font.render(('Letter Gussed: '), False, 'red')
        gussed_lable_rect = gussed_lable.get_rect(midleft = (50, 750))

        for j,i in enumerate(sorted(b)):

            letters_guessed = font.render((i+','), False, 'red')
            letter_gussed_rect = letters_guessed.get_rect(center=(350+(j*space), 750))
            screen.blit(letters_guessed, letter_gussed_rect)

        screen.blit(num_gs,num_gs_rect)
        screen.blit(num_cor,num_cor_rect)
        screen.blit(num_rong,num_rong_rect)
        screen.blit(gussed_lable,gussed_lable_rect)
        screen.blit(score,score_rect)

        mouse = pygame.mouse.get_pos()

        for k, i in enumerate(alphabet):
            letter = font.render((i), False, ('white'))
            letter_rect = letter.get_rect(center=(100+(k*space), 700))
            screen.blit(letter,letter_rect)
            for index, j in enumerate(alpha_list):
                letters_in_word = font.render((j), False, ('white'))
                letter_in_word_rect = letters_in_word.get_rect(center=(100+(index*space), 200))
                screen.blit(letters_in_word, letter_in_word_rect)
            # for points in letter_dic:
            for ind, let in enumerate(word_to_guess):
                if letter_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    if list(letter_dic.keys())[list(letter_dic.values()).index(letter_rect.center)] == let.upper():
                        alpha_list[ind] = list(letter_dic.keys())[list(letter_dic.values()).index(letter_rect.center)]
                        a.add(list(letter_dic.keys())[list(letter_dic.values()).index(letter_rect.center)])
                    b.add(list(letter_dic.keys())[list(letter_dic.values()).index(letter_rect.center)])
                    alphabet = list(''.join(alphabet).replace(i,' '))
        head = pygame.Rect(1155,140,100,100)
        body = pygame.Rect(1205,240,1,200)
        x.append(num_wrong)
        if 1 in x:
            pygame.draw.ellipse(screen,'white',head, width= 1)
        if 2 in x:
            pygame.draw.rect(screen,'white',body, width= 0)
        if 3 in x:
            pygame.draw.line(screen, 'white', (1205, 340), (1155, 290))
        if 4 in x:
            pygame.draw.line(screen, 'white', (1205, 340), (1255, 290))
        if 5 in x:
            pygame.draw.line(screen, 'white', (1155, 530), (1205, 440))
        if 6 in x:
            pygame.draw.line(screen, 'white', (1205, 440), (1255, 530))
        if num_wrong >= 6:
            screen.blit(loser_txt,loser_txt_rect)
            screen.blit(loser_cor,loser_cor_rect)
            screen.blit(play_again,play_again_rect)



        elif ''.join(alpha_list).replace('_', " ") == word_to_guess.upper():
            screen.blit(win_txt,win_txt_rect)
            screen.blit(play_again,play_again_rect)


        pygame.display.update()
        clock.tick(60)

main()