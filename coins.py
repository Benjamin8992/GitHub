class Coin :

	def __init__(self, rare=False, clean=True, heads=True, **kwargs):
		#Avec **kwargs la méthode va récupérer les variables de notre classe Euro et créer un dictionnaire dans lequel elle va PACK les données. Il faut donc créer une boucle : 

		#Utile pour les classes enfants !!!!!!
		for key, value in kwargs.items():
			setattr(self,key,value) # Set attrbitue. Il va passer les variable en revue en disant self.original_value = 1 ...

		self.is_rare = rare
		self.is_clean = clean
		self.heads = heads

		#Si une pièce est rare on augmente sa valeur de 25% : 
		if self.is_rare:
			self.value = self.original_value * 1.25
		else:
			self.value = self.original_value
		#Si une pièce est propre sa couleur n'est pas forcément Silver and Gold : 
		if self.is_clean:
			self.colour = self.clean_colour
		else: 
			self.colour = self.rusty_colour

	#Créons maintenant une méthode qui va faire rouiller notre pièce. Problème ici, toutes les pièces ne sont pas greenish quand elles rouillent :
	def rust(self):
		self.colour = self.rusty_colour # Quand une pièce rouille, elle sa couleur change selon sa propre couleur.

	def clean(self):   #Toutes les pièces propres ne sont pas de couleur Silver and Gold
		self.colour = self.clean_colour

	def __del__(self):
		print("Coin spent!")

	def flip(self):
		heads_options = [True, False]
		choice = random.choice(heads_options)
		self.heads = choice

#Maintenant on va créer notre classe Euro en faisant en sorte qu'elle hérite de la classe Coin : 
#Au dessus on a pas créer de variable pour nos rusty.couleur, clean_colour car elles sont spécifiques à chaque pièce.

class Euro(Coin) :

	def __init__(self):
		data = {
			"original_value": 1.00, 
			"clean_colour": "Silver and Gold",
			"rusty_colour": "red",
			"num_edges": 1, 
			"diameter": 23.25,
			"thickness": 2.33,
			"mass": 7.50
		}
		super().__init__(**data) # Ceci va relire la classe coin et attribuer les bonnes valeurs aux variables que nous n'avons pas définies (original_colour, rusty_colour...); On unpack les données. Pour que la classe Coin les accepte il faut Unpack.


#faisons les tests : 
one_euro_coin = Euro()
print(one_euro_coin.colour)
# On la fait rouiller 
one_euro_coin.rust()
print(one_euro_coin.colour)