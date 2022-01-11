# Jogo da Forca
# POO

# Import
import random

# Definindo especificacoes e metodos
# tabuleiro
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

    +---+
    |   |   
    |	    
    |	    
    |	    
    |	    
=================''', '''

    +---+
    |   |   
    |   O   
    |  	    
    |	    
    |	    
=================''', '''

    +---+
    |   |   
    |   O   
    |   |   
    |	    
    |	    
=================''', '''

     +---+
     |   |   
     |   O   
     |  /|   
     |       
     |	     
==================''', '''

     +---+
     |   |   
     |   O   
     |  /|/  
     |	     
     |	     
==================''', '''

     +---+
     |   |	 
     |   O	 
     |  /|/  
     |  /    
     |	     
==================''', '''

     +---+
     |   |   
     |   O   
     |  /|/  
     |  / /  
     |       
==================''']


# Classe
class Forca:

	# Metodo para construtir
	def __init__(self, palavra):
		# Palavra alvo
		self.palavra = palavra
		# lista para letras erradas
		self.perdidas_letras = []
		# lista para letras certas
		self.corretas_letras = []

	# Metodo para adivinhar a letra. O que fazer com a letra inserida?
	def guess(self, letra):
		# Se a letra estiver dentro da palavra e nao estiver dentro da lista de letras corretas
		if letra in self.palavra and letra not in self.corretas_letras:
			# Vou inserir na lista certas
			self.corretas_letras.append(letra)
		# Se a letra nao estiver na palavra e a letra nao estiver na lista de palavras perdidas
		elif letra not in self.palavra and letra not in self.perdidas_letras:
			# Vou inserir na lista perdidas
			self.perdidas_letras.append(letra)
		else:
			return False
		return True
		
	# Metodo para verificar se o jogo terminou
	def forca_over(self):
		# Ou chamaremos o fim vencedor ou teremos 6 vidas
		return self.forca_won() or (len(self.perdidas_letras) == 6)
		
	# Metodo para verificar se o jogador venceu
	def forca_won(self):
		# Se nao tiver underline, vence o jogo (True). Se tiver underline perde o jogo (False).
		if '_' not in self.hide_palavra():
			return True
		return False

	# Metodo para não mostrar a letra no board
	def hide_palavra(self):
		rtn = ''
		# Para cada letra dentro da palavra alvo
		for letra in self.palavra:
			# Se a letra nao estiver dentro das corretas retorna underline
			if letra not in self.corretas_letras:
				rtn += '_'
			# Se estiver, preencha com a letra
			else:
				rtn += letra
		return rtn

	# Metodo para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		# Usando o fatiamento para trazer cada elemento da lista pela posicao no board [0, 1, 2, 3, 4, 5]
		print(board[len(self.perdidas_letras)])
		print('\nPalavra: ' + self.hide_palavra())
		print('\nLetras erradas: ',)
		for letra in self.perdidas_letras:
			print(letra,)
		print()
		print('Letras corretas: ',)
		for letra in self.corretas_letras:
			print(letra,)
		print()

# Metodo para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
		with open("palavras.txt", "rt") as f:
				bank = f.readlines()
		# Buscando de maneira aleatoria a palavra
		return bank[random.randint(0, len(bank))].strip()


# Metodo Main - Execucao do Programa
def main():

	# Objeto
	game = Forca(rand_palavra())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.forca_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)

	# Verifica o status do jogo
	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuario
	if game.forca_won():
		print('\nParabéns! Você venceu!!')
	else:
		print('\nGame over! Você perdeu.')
		print('A palavra era ' + game.palavra)
		
	print('\nJogue novamente!\n')

# Executa o programa
if __name__ == "__main__":
	main()
