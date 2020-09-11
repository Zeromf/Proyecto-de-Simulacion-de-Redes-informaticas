# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()

class EscenaMenu(pilasengine.escenas.Escena):
	def iniciar(self):
		
		actor = pilas.actores.Actor()
		actor.imagen ="imagenes/fondomenu.png"		
		dialogo=pilas.actores.Dialogo()
		self.mono1 = pilas.actores.Mono()
		self.mono1.x=220
		self.mono1.y=-90
		
		
		dialogo.decir(self.mono1, "Presiona en mi")
		dialogo.decir(self.mono1, "Bienvenido a Monkeyquest and Riddlen of the world")
		dialogo.decir(self.mono1, "Presiona en mi")
		dialogo.decir(self.mono1, "Un gran juego para divertirse a lo grande y pasarla bien,elige monkeyquest,es mejor")
		dialogo.decir(self.mono1, "Si respondes 10 veces bien ganas, si erras 3 veces pierdes")
								  

		dialogo.comenzar()
		
		self.Mi_Menu = pilas.actores.Menu(
			[
				(u"Jugar", self.Ir_al_juego),
				(u"Tutorial", self.Ayuda),
				(u"Salir", self.Salir_de_Pilas),
			])
		cancion = pilas.musica.cargar('musica/Elsword.ogg')
		cancion.reproducir()
	
		Nombre_de_juego = pilas.actores.Texto(u"")
		Nombre_de_juego.color = pilas.colores.negro
		Nombre_de_juego.y = 200
	
	def actualizar(self):
		pass
		
	
	def Ayuda(self):
		pilas.escenas.EscenaAyuda()
		
	def Salir_de_Pilas(self): 
		pilas.terminar()	
		
	def Ir_al_juego(self): 
		pilas.escenas.EscenaJuego()		
	
class EscenaAyuda(pilasengine.escenas.Escena):
	def iniciar(self):
		actor = pilas.actores.Actor()
		actor.imagen ="imagenes/selva.png"
		
		dialogo=pilas.actores.Dialogo()
		self.mono1 = pilas.actores.Mono()
		self.mono1.x=210
		
		dialogo.decir(self.mono1, "Presiona en mi,para ver el tutotial")
		dialogo.decir(self.mono1, "Es muy simple si respondes 10 preguntas ganas,si no me pagas las bananas un mes")
		dialogo.decir(self.mono1, "Mueve con el teclado o mouse hacia la derecha y elige la pregunta")

		dialogo.comenzar()
	
		
		self.mono1.aprender('arrastrable') 
		self.mono1.aprender('MoverseConElTeclado') 
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = 220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		
	def Volver(self):	
		pilas.escenas.EscenaMenu()
		
	def actualizar(self):
		pass	

class EscenaJuego(pilasengine.escenas.Escena):		
	def iniciar(self):
		actor = pilas.actores.Actor()
		actor.imagen ="imagenes/champlote.jpg"
		self.nombre=raw_input("Ingrese su nombre: ")
		self.lista=[["Messi en que seleccion juega", "Argentina", "Colombia", "Espana"],["La programacion en que se representa mas", "Logica", "matematicas", "Historia"],["Fundamentos de informatica en que lenguaje se especializa", "Python", "Java", "Rubi"], ["Argentina cuantas copas del mundo tiene", "2", "3", "4"],["Segun el refran, el que se acuesta a dormir, es porque cria", "Fama", "Flojera", "Suenio"], ["En que anio se construyo la Unaj", "2009", "2010", "2011"], ["Si aprobas con 4 vas a","Final","Recursas","Ninguna de las anteriores"],["La raiz cuadrada de 4 es ", "2", "4", "ninguna de las anteriores"],["El numero pi vale", "3.14", "5.17", "10"], ["A la carcel va el", "El condenado", "el diputado", "El acusado"],[" El mundial 2014 ,el campeon fue", "Alemania", "Holanda", "Argentina"],["La moneda de estados unidos es ", "Dolar", "Pesos", "Yenes"],["Que son los humanos","Omnivoros", "Carnivoros", "Herbivoros"],["En que anio llego Cristobal Colon a America", "1492", "1490", "1495"],["Quien es el presidente actual de la Argentina ","Macri", "Cristina","Peron"],["Cual es el pais mas grande del mundo", "Rusia", "Canada", "Alemania"],["Donde se encuentra la famosa Torre Eiffel", "Francia", "Ecuador", "Croacia"],["El pais mas frio de la tierra es","Antartida","Tierra del fuego","Brasil"],["En que anio comenzo la Segunda Guerra Mundial de Argentina es","1939","1918","1945"],["Cual es el pais mas pobre de America", "Venezuela", "colombia", "chile"]]
		self.fondo_juego = pilas.fondos.Galaxia()
		self.puntaje = pilas.actores.Puntaje(color="negro") #self
		
		self.puntaje.x = -150 #self
		self.puntaje.y = -190 #self
		self.puntaje.valor = 0 #añadido
		self.correctosaparecer=pilas.actores.Texto("Correctos:")
		self.correctosaparecer.x=-220
		self.correctosaparecer.y=-190
		
		self.error=pilas.actores.Puntaje(color="amarillo")
		self.error.valor=0
		self.error.x=-150
		self.error.y=-220
		self.incorrectosaparecer=pilas.actores.Texto("Incorrectos:")
		self.incorrectosaparecer.x=-230
		self.incorrectosaparecer.y=-220
		
		self.mono = pilas.actores.Mono()
		self.mono.escala = 0.8 #añadido, el mono era muy grande
		self.mono.aprender('arrastrable') #modificado
		self.mono.aprender('MoverseConElTeclado') #modificado
		self.mono.decir("Bienvenido/a "+ self.nombre + " puedes arrastrarme")
		self.mono.x=[0,200],1
		
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = -220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		
		
		#Agrego las colisiones
		pilas.colisiones.agregar('banana', 'mono', self.el_mono_come)#añadido
		
		#Agrego tarea
		pilas.tareas.agregar(3, self.Preguntando)
		
	def Reiniciar(self):
    # Obtiene todos los actores de la pantalla.
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.puntaje, self.fondo_juego, self.mono,self.error,self.correctosaparecer,self.incorrectosaparecer,self.Boton_Volver]:
				actor.eliminar()

    # Genera una pregunta nueva
		self.Preguntando()
	def crear_una_nueva_pregunta():
			pilas.eventos.pulsa_tecla_escape.conectar(self.regresar)

	
	def Preguntando(self):	
		self.b1=pilas.actores.Banana()
		self.b1.x=-300
		self.b1.y=100
		self.b1.esverdadera=False
		self.b2=pilas.actores.Banana()
		self.b2.x=-300
		self.b2.y=0
		self.b2.esverdadera=False
		self.b3=pilas.actores.Banana()
		self.b3.x=-300
		self.b3.y=-100
		self.b3.esverdadera=False
		
		self.poslista=pilas.azar(0,19)
		self.encuentrapreg=self.lista[self.poslista][0]
		self.mostrar_pregunta=pilas.actores.Texto(self.encuentrapreg)
		self.mostrar_pregunta.y=220
		self.mostrar_pregunta.escala=0.8
		
		self.respuesta_correcta = self.lista[self.poslista][1] #Respuesta Correcta
		self.respuesta_incorrecta_1 = self.lista[self.poslista][2] #Respuesta incorrecta 1
		self.respuesta_incorrecta_2 = self.lista[self.poslista][3] #Respuesta incorrecta 2
		
		self.rta_1 = pilas.actores.Texto("")
		self.rta_1.x=-250
		self.rta_1.y=100
		self.rta_2 = pilas.actores.Texto("")
		self.rta_2.x=-250
		self.rta_2.y=0
		self.rta_3 = pilas.actores.Texto("")
		self.rta_3.x=-250
		self.rta_3.y=-100
		
		#Banana verdadera
		self.bananas_posibles = [self.b1,self.b2,self.b3]
		self.textos_posibles = [self.rta_1,self.rta_2,self.rta_3]
		self.indiceok=pilas.azar(0,2)
		self.banana_verdadera=self.bananas_posibles[self.indiceok]
		self.banana_verdadera.esverdadera=True
		self.texto_respuesta_verdadera=self.textos_posibles[self.indiceok]
		self.texto_respuesta_verdadera.texto=str(self.respuesta_correcta)
		
		if self.b1.esverdadera:
			self.rta_1.texto=str(self.respuesta_correcta)
			self.rta_2.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b2.esverdadera:
			self.rta_2.texto=str(self.respuesta_correcta)
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b3.esverdadera:
			self.rta_3.texto= str(self.respuesta_correcta)
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_2.texto = str(self.respuesta_incorrecta_2)
				
	def ganaste(self):
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		actor = pilas.actores.Actor()
		actor.imagen ="imagenes/burbuja.png"
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = 220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor))
		self.puntajefinal.escala=2
		self.cartelfelicidades=pilas.actores.Texto("Felicidades "+self.nombre+" has ganado")
		self.cartelfelicidades.y=220
		self.cartelfelicidades=pilas.actores.Texto("Comelon esta feliz y lleno")
		self.cartelfelicidades.y=150
		self.cartelpuntaje=pilas.actores.Texto("Tu puntaje es: ")
		self.cartelpuntaje.x=-100
		self.errorestotales=pilas.actores.Texto(str(self.error.valor))
		self.errorestotales.y=-100
		self.errorestotales.escala=2
		self.cartelerror=pilas.actores.Texto("Cantidad de errores: ")
		self.cartelerror.x=-150
		self.cartelerror.y=-100
		self.mono.sonreir()
	
	def perdiste(self):
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		actor = pilas.actores.Actor()
		actor.imagen ="imagenes/gameover.jpg"
		actor.escala=0.55
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = 220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor))
		self.puntajefinal.escala=2
		self.cartelfelicidades=pilas.actores.Texto(self.nombre+ " Intentalo de nuevo :)")
		self.cartelfelicidades.y=220
		self.cartelfelicidades=pilas.actores.Texto("No pudiste haber perdido era muy facil :/")
		self.cartelfelicidades.y=150
		self.cartelpuntaje=pilas.actores.Texto("Tu puntaje es: ")
		self.cartelpuntaje.x=-100
		self.errorestotales=pilas.actores.Texto(str(self.error.valor))
		self.errorestotales.y=-100
		self.errorestotales.escala=2
		self.cartelerror=pilas.actores.Texto("Cantidad de errores: ")
		self.cartelerror.x=-150
		self.cartelerror.y=-100
		self.mono.gritar()
		
	def Volver(self):	
		pilas.escenas.EscenaMenu()
		
	def actualizar(self):
		pass	
		

	def el_mono_come(self, bananas, mono):
		if not bananas.esverdadera: #bananas es la banana colisionada
			if self.error.valor<2:
				pilas.camara.vibrar()
				bananas.eliminar()
				mono.gritar()
				mono.decir("MAL MAL MAL")
				self.error.aumentar() #aumenta 1 error. En total puede ser hasta 3 errores.
				pilas.tareas.agregar(3, self.Reiniciar)
				
			else:
				pilas.avisar("Fin del juego")
				self.error.aumentar()
				self.perdiste()
				
		else:
			if self.puntaje.valor<9:
				bananas.eliminar() #hay que eliminar la banana colisionada
				mono.rotacion=[0,360]
				mono.decir("Excelente")
				estrella = pilas.actores.Estrella()
				estrella.x = bananas.x
				estrella.y = bananas.y
				estrella.escala = 0.2
				estrella.escala = [2, 1] * 2
				self.puntaje.aumentar()
				pilas.tareas.agregar(3, self.Reiniciar)
			else:
				pilas.avisar("Felicidades has ganado")
				self.puntaje.aumentar()
				self.ganaste()
				
				
		
	def Volver(self):	
		pilas.escenas.EscenaMenu()
		
	def actualizar(self):
		pass
		




pilas.escenas.vincular(EscenaAyuda)
pilas.escenas.vincular(EscenaMenu)
pilas.escenas.vincular(EscenaJuego)
pilas.escenas.EscenaMenu()

pilas.ejecutar()
