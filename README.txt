README - AI PROGRAMMING (DE)

Eine AI erhält als Argumente das Schachbrett array und als Integer welchem Team sie angehört

	Bsp.:
	def deep_blue(board, team, [MESSAGE_STATUS]):


BOARD:
Das Board ist ein 2D Array mit FIELD Objekten

Attribute:

	fields = field[8][8]


	ACHTUNG!
	Die Addressierung der Felder erfolg über Bsp.:
	board.fields[y][x] <--- Hier sind die X und Y Addressierungen vertauscht


FIELD:
Ein Field enthält die für das Spiel notwendigen Figuren mit Informationen dazu, oder keine Figur.

Attribute:
	
	bool active = False 		#ein Feld ist "active" wenn es von der mark_move_pattern() Funktion 
					#als mögliche Zugvariante für die Figur auf angegebenem Feld ist
	int pos_x 			#die Angabe zur X Koordinate des Feldes
	int pos_y 			#die Angabe zur Y Koordinate des Feldes
	figure_moved = False		#ist True, sobald die Figur einmal bewegt wurde
	figure_team			#Angabe über das Team, in welchem die Figur auf dem Feld ist 
					#(0 - kein Team(keine Figur), 1 - Team weiß, 2 - Team schwarz)
	figure_type			#Angabe über den Figurtyp, welcher auf dem Feld steht
					#(0 - keine Figur, 1 - Bauer, 2 - Turm, 3 - Springer,
					# 4 - Läufer, 5 - Dame, 6 - König)
	move_pattern			#enthält das figurtypeigene Bewegungsmuster (nicht für AI gedacht)
	rochade_flag			#markiert




AI_MESSAGE System:

AI_INPUT:


AI_OUTPUT: