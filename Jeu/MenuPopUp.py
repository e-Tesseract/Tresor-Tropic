import pygame

# Recupere la taille de l'ecran
pygame.init()
infoObject = pygame.display.Info()
largeur_ecran, hauteur_ecran = infoObject.current_w, infoObject.current_h
taille_ajustee = 0.5
largeur_fenetre, hauteur_fenetre = int(largeur_ecran * taille_ajustee), int(hauteur_ecran * taille_ajustee)

def menu_popup(screen):

    screen_width, screen_height = screen.get_size()
    menu_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    menu_surface.fill((0, 0, 0, 128)) 

    font = pygame.font.Font(None, 30)
    options = ["Reprendre", "Sauvegarder", "Quitter"]
    selected_option = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    print(options[selected_option])
                    return options[selected_option]

            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                for i, option in enumerate(options):
                    text = font.render(option, True, (0, 0, 0))
                    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + i * 30))
                    if text_rect.collidepoint(x, y):
                        selected_option = i
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(options[selected_option])

        # Dessiner le menu et les options du menu sur menu_surface au lieu de screen
        menu_surface.fill((0, 0, 0, 128))
        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected_option else (100, 100, 100)
            text = font.render(option, True, color)
            menu_surface.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2 + i * 30))

        # Dessinez menu_surface sur screen
        screen.blit(menu_surface, (0, 0))

        pygame.display.update()

    pygame.event.clear(pygame.KEYDOWN)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    menu_popup(screen)