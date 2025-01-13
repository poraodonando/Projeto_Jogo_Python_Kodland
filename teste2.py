import pgzrun

# Definindo a largura e altura da tela
WIDTH = 800
HEIGHT = 600

# Variável para controlar qual tela está ativa
tela_atual = "menu"  # Pode ser "menu" ou "jogo"

# Função que desenha o conteúdo de cada tela
def draw():
    global tela_atual

    if tela_atual == "menu":
        desenha_menu()
    elif tela_atual == "jogo":
        desenha_jogo()

# Função que desenha o menu
def desenha_menu():
    screen.clear()
    screen.fill((0, 0, 0))  # Cor de fundo preta
    screen.draw.text("Menu Principal", center=(WIDTH // 2, HEIGHT // 4), fontsize=50, color="white")
    screen.draw.text("1. Começar", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=30, color="white")
    screen.draw.text("2. Sair", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=30, color="white")

# Função que desenha o jogo (primeira fase)
def desenha_jogo():
    screen.clear()
    screen.fill((0, 0, 255))  # Cor de fundo azul, como se fosse a fase do jogo
    screen.draw.text("Primeira Fase do Jogo!", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="white")

# Função para capturar os eventos de teclado
def on_key_down(key):
    global tela_atual

    if tela_atual == "menu":
        if key == keys._1:  # Pressionar "1" para começar o jogo
            tela_atual = "jogo"  # Mudar para a tela do jogo
        elif key == keys._2:  # Pressionar "2" para sair
            exit()
    elif tela_atual == "jogo":
        if key == keys.ESCAPE:  # Pressionar "Escape" para voltar ao menu
            tela_atual = "menu"

# Inicializa o Pygame Zero
pgzrun.go()
# Escreva o seu código aqui :-)
