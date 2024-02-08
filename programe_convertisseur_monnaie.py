import pygame
import sys
import openpyxl
from openpyxl import load_workbook

import update_data_conversion
#permet de refresh les taux de change

pygame.init()

#TAILLE FENÊTRE
x=700
y=800



screen=pygame.display.set_mode((x,y))
pygame.display.set_caption('convertisseur de monnaies')

#FOND
image_fond=pygame.image.load('photos/fond-dollar-uni.jpg').convert_alpha()
image_fond=pygame.transform.scale(image_fond,(x,y))
image_fond_rect=image_fond.get_rect(center=(x/2,y/2))

text_font = pygame.font.Font('texte_font.ttf', 50)
small_text_font = pygame.font.Font('texte_font.ttf', 25)


#AGENCEMENT
nb_monnaies=8
espacement_y=150
hauteur_image=(y-150-((nb_monnaies/2)-1)*espacement_y)*2/nb_monnaies
color_text='White'#(0,0,0)

back_image=pygame.image.load('photos/back.png').convert_alpha()
back_image=pygame.transform.scale(back_image,(hauteur_image*0.75,hauteur_image*0.75))
back_image_rect=back_image.get_rect(center=(x/2-300,y-50))

home_image=pygame.image.load('photos/home.png').convert_alpha()
home_image=pygame.transform.scale(home_image,(hauteur_image*0.75,hauteur_image*0.75))
home_image_rect=home_image.get_rect(center=(x/2-225,y-50))

fleche_image=pygame.image.load('photos/right-arrow.png').convert_alpha()
fleche_image=pygame.transform.scale(fleche_image,(hauteur_image,hauteur_image))
fleche_image_rect=fleche_image.get_rect(center=(x/2,200))

convert_image=pygame.image.load('photos/converter.png').convert_alpha()
convert_image=pygame.transform.scale(convert_image,(hauteur_image*1.75,hauteur_image*1.75))
convert_image_rect=convert_image.get_rect(center=(x/2,425))
#DOLLAR US
y_dollarUS=200
dollarUS_image=pygame.image.load('photos/usa.png').convert_alpha()
dollarUS_image=pygame.transform.scale(dollarUS_image,(hauteur_image*1.25,hauteur_image))
dollarUS_image_rect=dollarUS_image.get_rect(topleft=(x/2-100,y_dollarUS))
dollarUS_text=small_text_font.render('dollar US', True, color_text)
dollarUS_text_rect=dollarUS_text.get_rect(topleft=(x/2-250,y_dollarUS+15))

monnaie_us=pygame.image.load('photos/us-dollar.png')
monnaie_us=pygame.transform.scale(monnaie_us,(hauteur_image*1.25,hauteur_image*1.25))


#DOLLAR CANADIEN
y_dollarCANADA=y_dollarUS+espacement_y
dollarCANADA_image=pygame.image.load('photos/canada.png').convert_alpha()
dollarCANADA_image=pygame.transform.scale(dollarCANADA_image,(hauteur_image*1.25,hauteur_image))
dollarCANADA_image_rect=dollarCANADA_image.get_rect(topleft=(x/2-100,y_dollarCANADA))
dollarCANADA_text=small_text_font.render('dollar CANADIEN', True, color_text)
dollarCANADA_text_rect=dollarCANADA_text.get_rect(topleft=(x/2-325,y_dollarCANADA+15))

monnaie_canada=pygame.image.load('photos/canadian-dollar.png')
monnaie_canada=pygame.transform.scale(monnaie_canada,(hauteur_image*1.25,hauteur_image*1.25))

#DOLLAR AUSTRALIEN
y_dollarAUSTRALIEN=y_dollarCANADA+espacement_y
dollarAUSTRALIEN_image=pygame.image.load('photos/australia.png').convert_alpha()
dollarAUSTRALIEN_image=pygame.transform.scale(dollarAUSTRALIEN_image,(hauteur_image*1.25,hauteur_image))
dollarAUSTRALIEN_image_rect=dollarAUSTRALIEN_image.get_rect(topleft=(x/2-100,y_dollarAUSTRALIEN))
dollarAUSTRALIEN_text=small_text_font.render('dollar AUSTRALIEN', True, color_text)
dollarAUSTRALIEN_text_rect=dollarAUSTRALIEN_text.get_rect(topleft=(x/2-325,y_dollarAUSTRALIEN+15))

monnaie_australie=pygame.image.load('photos/australian-dollar.png')
monnaie_australie=pygame.transform.scale(monnaie_australie,(hauteur_image*1.25,hauteur_image*1.25))

#LIVRE STERLING
y_STERLING=y_dollarAUSTRALIEN+espacement_y
STERLING_image=pygame.image.load('photos/england.png').convert_alpha()
STERLING_image=pygame.transform.scale(STERLING_image,(hauteur_image*1.25,hauteur_image))
STERLING_image_rect=STERLING_image.get_rect(topleft=(x/2-100,y_STERLING))
STERLING_text=small_text_font.render('livre sterling', True, color_text)
STERLING_text_rect=STERLING_text.get_rect(topleft=(x/2-250,y_STERLING+15))

monnaie_sterling=pygame.image.load('photos/pound.png')
monnaie_sterling=pygame.transform.scale(monnaie_sterling,(hauteur_image*1.25,hauteur_image*1.25))

#EURO
y_EURO=200
EURO_image=pygame.image.load('photos/european-union.png').convert_alpha()
EURO_image=pygame.transform.scale(EURO_image,(hauteur_image*1.25,hauteur_image))
EURO_image_rect=EURO_image.get_rect(topright=(x/2+100,y_EURO))
EURO_text=small_text_font.render('EURO', True, color_text)
EURO_text_rect=EURO_text.get_rect(topleft=(x/2+150,y_EURO+15))

monnaie_euro=pygame.image.load('photos/euro.png')
monnaie_euro=pygame.transform.scale(monnaie_euro,(hauteur_image*1.25,hauteur_image*1.25))

#FRANC SUISSE
y_FRANC_SUISSE=y_EURO+espacement_y
FRANC_SUISSE_image=pygame.image.load('photos/switzerland.png').convert_alpha()
FRANC_SUISSE_image=pygame.transform.scale(FRANC_SUISSE_image,(hauteur_image*1.25,hauteur_image))
FRANC_SUISSE_image_rect=FRANC_SUISSE_image.get_rect(topright=(x/2+100,y_FRANC_SUISSE))
FRANC_SUISSE_text=small_text_font.render('franc suisse', True, color_text)
FRANC_SUISSE_text_rect=FRANC_SUISSE_text.get_rect(topleft=(x/2+150,y_FRANC_SUISSE+15))

monnaie_franc=pygame.image.load('photos/swiss-franc.png')
monnaie_franc=pygame.transform.scale(monnaie_franc,(hauteur_image*1.25,hauteur_image*1.25))

#YEN
y_YEN=y_FRANC_SUISSE+espacement_y
YEN_image=pygame.image.load('photos/japan.png').convert_alpha()
YEN_image=pygame.transform.scale(YEN_image,(hauteur_image*1.25,hauteur_image))
YEN_image_rect=YEN_image.get_rect(topright=(x/2+100,y_YEN))
YEN_text=small_text_font.render('YEN', True, color_text)
YEN_text_rect=YEN_text.get_rect(topleft=(x/2+150,y_YEN+15))

monnaie_yen=pygame.image.load('photos/yen.png')
monnaie_yen=pygame.transform.scale(monnaie_yen,(hauteur_image*1.25,hauteur_image*1.25))

#RAND
y_RAND=y_YEN+espacement_y
RAND_image=pygame.image.load('photos/south-africa.png').convert_alpha()
RAND_image=pygame.transform.scale(RAND_image,(hauteur_image*1.25,hauteur_image))
RAND_image_rect=RAND_image.get_rect(topright=(x/2+100,y_RAND))
RAND_text=small_text_font.render('RAND', True, color_text)
RAND_text_rect=YEN_text.get_rect(topleft=(x/2+150,y_RAND+15))

monnaie_rand=pygame.image.load('photos/south-african-rand.png')
monnaie_rand=pygame.transform.scale(monnaie_rand,(hauteur_image*1.25,hauteur_image*1.25))

rect1=[x/2-150,350]
rect2=[x/2+150,350]
rect3=[x/2-150,500]
rect4=[x/2+150,500]
rect5=[x/2-150,650]
rect6=[x/2+150,650]
rect7=[x/2,750]

rect_list=[rect1,rect2,rect3,rect4,rect5,rect6,rect7]

list_image_pays=[dollarUS_image, 'US',  dollarCANADA_image, 'CANADA',dollarAUSTRALIEN_image,'AUSTRALIEN', STERLING_image, 'STERLING',EURO_image, 'EURO',FRANC_SUISSE_image, 'FRANC',YEN_image,'YEN', RAND_image, 'RAND']
list_monnaie=[monnaie_us,'US',monnaie_canada,'CANADA',monnaie_australie,'AUSTRALIEN',monnaie_sterling,'STERLING',monnaie_euro,'EURO',monnaie_franc,'FRANC',monnaie_yen,'YEN',monnaie_rand,'RAND']
activation_ecran_conversion=True
activation_affichage_conversion=True

#PROBLEME RETOUR EN ARRIERE PAS POSSIBLE DE SELECTIONNER LA MONNAIE D'ARRIVEE
def ecran_accueil():
    titre_texte=text_font.render('Convertisseur de monnaies', True, color_text)
    titre_texte_rect=titre_texte.get_rect(center=(x/2,100))
    screen.blit(image_fond, image_fond_rect)
    screen.blit(titre_texte,titre_texte_rect)
    screen.blit(dollarUS_image, dollarUS_image_rect)
    screen.blit(dollarUS_text, dollarUS_text_rect)
    screen.blit(dollarCANADA_image, dollarCANADA_image_rect)
    screen.blit(dollarCANADA_text, dollarCANADA_text_rect)
    screen.blit(dollarAUSTRALIEN_image, dollarAUSTRALIEN_image_rect)
    screen.blit(dollarAUSTRALIEN_text, dollarAUSTRALIEN_text_rect)
    screen.blit(STERLING_image, STERLING_image_rect)
    screen.blit(STERLING_text, STERLING_text_rect)
    screen.blit(EURO_image, EURO_image_rect)
    screen.blit(EURO_text, EURO_text_rect)
    screen.blit(FRANC_SUISSE_image, FRANC_SUISSE_image_rect)
    screen.blit(FRANC_SUISSE_text, FRANC_SUISSE_text_rect)
    screen.blit(YEN_image, YEN_image_rect)
    screen.blit(YEN_text, YEN_text_rect)
    screen.blit(RAND_image, RAND_image_rect)
    screen.blit(RAND_text, RAND_text_rect)
def ecran_conversion(monnaie):

    global list_image_pays, rect_list, activation_ecran_conversion, list_monnaie

    monnaie_depart_caractere=None
    # Create a text input box
    i=0
    while i<len(list_image_pays) :
        if list_image_pays[i]==monnaie:
            monnaie_depart_caractere=list_monnaie[i]
        i+=2

    list_image_rect_associe=[]
    list_image_associee=[]

    pays_positionnes = 0
    rect_positionnes = 0
    while pays_positionnes<(len(list_image_pays)):
        if monnaie!=(list_image_pays[pays_positionnes]):
            list_image_associee.append(list_image_pays[pays_positionnes])
            rect_image=list_image_pays[pays_positionnes].get_rect(center=(rect_list[rect_positionnes][0], rect_list[rect_positionnes][1]))
            list_image_rect_associe.append(rect_image)
            rect_positionnes += 1

        pays_positionnes+=2

    if activation_ecran_conversion :
        screen.blit(image_fond, image_fond_rect)
        monnaie_image = pygame.transform.scale(monnaie, (hauteur_image * 2, hauteur_image * 1.75))
        monnaie_rect = monnaie.get_rect(center=(x / 2 +100, 185))
        titre_texte = text_font.render('Argent à convertir', True, color_text)
        titre_texte_rect = titre_texte.get_rect(center=(x / 2, 100))
        depart_texte= small_text_font.render('Monnaie de départ', True, color_text)
        depart_texte_rect=depart_texte.get_rect(center=(x/2-75, 205))
        screen.blit(depart_texte,depart_texte_rect)
        screen.blit(titre_texte, titre_texte_rect)
        vers_texte = text_font.render('Vers...', True, color_text)
        vers_texte_rect = vers_texte.get_rect(center=(x / 2, 450))
        screen.blit(vers_texte, vers_texte_rect)
        screen.blit(monnaie_image, monnaie_rect)
        screen.blit(back_image,back_image_rect)
        index = 0
        while index < len(list_image_rect_associe):
            screen.blit(list_image_associee[index], list_image_rect_associe[index])
            index += 1



    while activation_ecran_conversion:
        #print(pygame.mouse.get_pos())


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_image_rect.collidepoint(event.pos):
                    activation_ecran_conversion=False
                    ecran_accueil()

                rect=0
                while rect<(len(list_image_rect_associe)):
                    if list_image_rect_associe[rect].collidepoint(event.pos):
                        if list_image_associee[rect]==dollarCANADA_image:
                            affichage_conversion(monnaie,dollarCANADA_image,[monnaie_depart_caractere,monnaie_canada])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==dollarUS_image:
                            affichage_conversion(monnaie,dollarUS_image,[monnaie_depart_caractere,monnaie_us])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==dollarAUSTRALIEN_image:
                            affichage_conversion(monnaie,dollarAUSTRALIEN_image,[monnaie_depart_caractere,monnaie_australie])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==FRANC_SUISSE_image:
                            affichage_conversion(monnaie,FRANC_SUISSE_image,[monnaie_depart_caractere,monnaie_franc])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==YEN_image:
                            affichage_conversion(monnaie,YEN_image,[monnaie_depart_caractere,monnaie_yen])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==EURO_image:
                            affichage_conversion(monnaie,EURO_image,[monnaie_depart_caractere,monnaie_euro])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==RAND_image:
                            affichage_conversion(monnaie,RAND_image,[monnaie_depart_caractere,monnaie_rand])
                            activation_ecran_conversion=False

                        if list_image_associee[rect]==STERLING_image:
                            affichage_conversion(monnaie,STERLING_image,[monnaie_depart_caractere,monnaie_sterling])
                            activation_ecran_conversion=False
                    rect+=1



        pygame.display.flip()
def affichage_conversion(monnaie_depart, monnaie_arrivee, list_monnaie_associee):

    global activation_affichage_conversion, activation_ecran_conversion

    color_passive = pygame.Color('White')
    color_active = pygame.Color('#338b34')
    color = color_passive
    input_text = ""
    text_box_rect = pygame.Rect(x / 2 -50, 300, 100, 40)
    active_text_box = None

    monnaie_depart_signe_rect=list_monnaie_associee[0].get_rect(center=(x/2+150,325))
    monnaie_arrivee_signe_rec=list_monnaie_associee[1].get_rect(center=(x/2+150,550))

    if activation_affichage_conversion:
        screen.blit(image_fond, image_fond_rect)
        monnaie_depart1 = pygame.transform.scale(monnaie_depart, (hauteur_image * 1.75, hauteur_image * 1.5))
        monnaie_arrivee1 = pygame.transform.scale(monnaie_arrivee, (hauteur_image * 1.75, hauteur_image * 1.5))
        monnaie_depart_rect = monnaie_depart1.get_rect(center=(x / 2 - 100, 200))
        monnaie_arrivee_rect = monnaie_arrivee1.get_rect(center=(x / 2 + 100, 200))
        titre_texte = text_font.render('Conversion', True, color_text)
        titre_texte_rect = titre_texte.get_rect(center=(x / 2, 100))
        screen.blit(titre_texte, titre_texte_rect)
        screen.blit(monnaie_depart1, monnaie_depart_rect)
        screen.blit(monnaie_arrivee1, monnaie_arrivee_rect)
        screen.blit(home_image,home_image_rect)
        screen.blit(back_image,back_image_rect)
        screen.blit(fleche_image,fleche_image_rect)
        screen.blit(convert_image,convert_image_rect)
        screen.blit(list_monnaie_associee[0],monnaie_depart_signe_rect)


    while activation_affichage_conversion:
        #print(pygame.mouse.get_pos())


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and active_text_box:
                if event.key == pygame.K_RETURN:
                    # Handle the input (you can convert input_text to a numeric value here)
                    monnaie_convertie=int(input_text)*(taux_conversion(monnaie_depart,monnaie_arrivee))
                    monnaie_convertie = "{:.3f}".format(monnaie_convertie)
                    monnaie_convertie_text = text_font.render(f'{monnaie_convertie}', True, color_text)
                    monnaie_convertie_text_rect = monnaie_convertie_text.get_rect(center=(x / 2, 550))
                    screen.blit(list_monnaie_associee[1],monnaie_arrivee_signe_rec)
                    screen.blit(monnaie_convertie_text, monnaie_convertie_text_rect)

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:

                if text_box_rect.collidepoint(event.pos):
                    active_text_box = text_box_rect
                    color=color_active

                if home_image_rect.collidepoint(event.pos):
                    activation_affichage_conversion=False
                    ecran_accueil()

                if back_image_rect.collidepoint(event.pos):
                    ecran_conversion(monnaie_depart)
                    activation_ecran_conversion=True
                    activation_affichage_conversion=False

                if convert_image_rect.collidepoint(event.pos):
                    monnaie_convertie = (float(input_text) * (taux_conversion(monnaie_depart, monnaie_arrivee)))
                    monnaie_convertie = "{:.3f}".format(monnaie_convertie)
                    monnaie_convertie_text=text_font.render(f'{monnaie_convertie}',True, color_text)
                    monnaie_convertie_text_rect=monnaie_convertie_text.get_rect(center=(x/2,550))
                    screen.blit(monnaie_convertie_text,monnaie_convertie_text_rect)
                    screen.blit(list_monnaie_associee[1], monnaie_arrivee_signe_rec)
                    screen.blit(monnaie_convertie_text, monnaie_convertie_text_rect)

            if activation_affichage_conversion:
                pygame.draw.rect(screen, color, text_box_rect)
                text_surface = text_font.render(input_text, True, color_text)
                screen.blit(text_surface, (text_box_rect.x +5, text_box_rect.y -10))

            if active_text_box is not None:
                active_text_box.w = max(100, text_surface.get_width() + 10)
            pygame.display.flip()
        pygame.display.flip()

def taux_conversion(monnaie_depart, monnaie_arrivee):

    wb=load_workbook('convertisseur_table_updated.xlsx')
    wa=wb.active
    list_monnaies=[0,1,[dollarUS_image,'dollar'],[EURO_image,'Euro'],[YEN_image,'Japanese Yen'],[STERLING_image,'British Pound'],[FRANC_SUISSE_image,'Swiss Franc'],[dollarCANADA_image,'Canadian Dollar'],[dollarAUSTRALIEN_image,'Australian Dollar'],[RAND_image,'South African Rand']]
    for i in range (2,len(list_monnaies)):

        if monnaie_depart==list_monnaies[i][0]:
            valeur1=wa['B'+str(i)].value
        if monnaie_arrivee==list_monnaies[i][0]:
            valeur2=wa['B'+str(i)].value


    taux_de_change=(valeur1)/(valeur2)
    return taux_de_change








accueil=True



while True:

    activation_ecran_conversion=True
    activation_affichage_conversion=True

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    if accueil :
        ecran_accueil()

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if dollarUS_text_rect.collidepoint(mouse_pos) or dollarUS_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(dollarUS_image)

        if dollarCANADA_text_rect.collidepoint(mouse_pos) or dollarCANADA_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(dollarCANADA_image)

        if dollarAUSTRALIEN_text_rect.collidepoint(mouse_pos) or dollarAUSTRALIEN_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(dollarAUSTRALIEN_image)

        if FRANC_SUISSE_text_rect.collidepoint(mouse_pos) or FRANC_SUISSE_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(FRANC_SUISSE_image)

        if EURO_text_rect.collidepoint(mouse_pos) or EURO_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(EURO_image)

        if YEN_text_rect.collidepoint(mouse_pos) or YEN_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(YEN_image)

        if RAND_text_rect.collidepoint(mouse_pos) or RAND_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(RAND_image)

        if STERLING_text_rect.collidepoint(mouse_pos) or STERLING_image_rect.collidepoint(mouse_pos):
            accueil=False
            ecran_conversion(STERLING_image)




    pygame.display.update()


