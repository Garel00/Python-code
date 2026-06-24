#Clases

class personaje:
	nombre = "Default"
	fuerza = 0
	inteligencia = 0
	defensa = 0
	vida = 0
	
	def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
		self.nombre = nombre
		self.fuerza = fuerza
		self.inteligencia = inteligencia
		self.defensa = defensa
		self.vida = vida
	
	def atributos(self):
		print("\n")
		print(self.nombre, ":", sep=" ")
		print("|Fuerza: ", self.fuerza)
		print("|Inteligencia: ", self.inteligencia)
		print("|Defensa: ", self.defensa)
		print("|Vida: ", self.vida)
	
	def lvl_up(self, fuerza, inteligencia, defensa):
		self.fuerza = self.fuerza + fuerza
		self.inteligencia = self.inteligencia + inteligencia
		self.defensa = self.defensa + defensa
	
	def drink_potion(self, vida):
		self.vida += vida
	
	def drink_anti_potion(self, vida):
		self.vida = self.vida  - vida
		
	def esta_vivo(self):
		return self.vida > 0
		
	def matar(self):
		self.vida = 0
		print(self.nombre, "te mataste, wey")
	def daño(self, enemigo):
		daño_base = self.fuerza - enemigo.defensa
		if daño_base < 0:
			return 1
		
		else:
			return daño_base
		
	def atacar(self, enemigo):
		daño = self.daño(enemigo)
		enemigo.vida = enemigo.vida - daño
		print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
		if enemigo.esta_vivo():
			print("La vida de", enemigo.nombre, "es", enemigo.vida)
		else:
			enemigo.matar()


#Metodo para crear subclases
class warrior(personaje):
	
	def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
		super().__init__(nombre, fuerza, inteligencia, defensa, vida)
		self.espada = espada
	
	def cambiar_arma(self):

		opcion = int(input("Elige un arma: (1) Martillo de gigante, daño 10. (2) Matadragones, daño 12."))
		if opcion == 1:
			self.espada = 10
		elif opcion == 2:
			self.espada = 12
		else:
			print("numero incorrecto")
		
	def atributos(self):
		super().atributos()
		print("|Espada:", self.espada)
	
	def daño(self, enemigo):
		return self.fuerza*self.espada - enemigo.defensa
		
class mago(personaje):
	
	def __init__(self, nombre, fuerza, inteligencia, defensa, vida, grimorio):
		super().__init__(nombre, fuerza, inteligencia, defensa, vida)
		self.grimorio = grimorio
	
	def cambiar_grimorio(self):

		opcion = int(input("Elige un grimorio: (1) Enchilidion, daño 12, inteligencia 15. (2) Libro negro, daño 17."))
		if opcion == 1:
			self.grimorio = 12
			
		elif opcion == 2:
			self.grimorio = 17
		else:
			print("numero incorrecto")
		
	def atributos(self):
		super().atributos()
		print("|Grimorio:", self.grimorio)
	
	def daño(self, enemigo):
		return self.inteligencia*self.grimorio - enemigo.defensa
	
guts = warrior("Berserk", 66, 24, 54, 88, 4)
guts.atributos()

frieren = mago("Frieren", 18, 67, 80, 33, 8)
frieren.atributos()

frieren.atacar(guts)
