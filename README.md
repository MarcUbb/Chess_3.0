# Chess_3.0
README - AI PROGRAMMING

--------------------------------------------------------------------------------------------------------------------------------

Your AI will be called as followed:

	FIELD_CHOSEN, FIELD_MOVE, AI_MESSAGES = constants.AI_1.ai_function(constants.BOARD, constants.TURN)

Your AI function in your python file MUST HAVE THE FOLLOWING HEADLINE:

	def ai_function(board, team):
	
And MUST HAVE FOLLOWINT RETURNS:
	
	return(FIELD_CHOSEN, FIELD_MOVE, AI_MESSAGES)
	
--------------------------------------------------------------------------------------------------------------------------------

ARGUMENTS:

Since the AI is not allowed to have access to the games parameters it will be given the current positioning in form of board object and its team.

BOARD:

Field:
A field contains all necesssary information about its position on the board and the figure it contains.

Initialisation:
A field is usually initialised via the board but can also be initialized as followed:

	example_field = Field(line, collum, figure_team, figure_type)

Attributes:
"line"          - line in Board or y-coordinate in pygame window
"collum"        - collum in Board or x-coordinate in pygame window
"figure_team"   - team of figure which is on the field (0-no team, 1-white, 2-black)
"figure_type"   - type of figure (0-no figure, 1-pawn, 2-rook, 3-knight, 4-bishop, 5-queen, 6-king)

A field also contains following attributes which are not necessare to initialize:
"active"        - state of field e.g. for marking possible moves (bool value)
"figure_moved"  - True-figure has been moved False-figure hasn't been moved yet
"move_pattern"  - function "pattern_generator" automatically generates a move pattern for figure ONLY IF FIELD WAS INITIALIZED!
"rochade_flag"  - only relevant for rochade


Board:
A board consists of a 2D-array of fields to represent a specific positioning of figures.

Initialisation:
A board is initialized with an 3D-array that contains "figure_team" and "figure_type" for every field in the game. It is initialized as followed:

	example_board = Board(position)

"positioning" for start position of chess:

	example_start_pos = [[[2,2],[2,3],[2,4],[2,5],[2,6],[2,4],[2,3],[2,2]],
                            [[2,1],[2,1],[2,1],[2,1],[2,1],[2,1],[2,1],[2,1]],
                            [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                            [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                            [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                            [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                            [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]],
                            [[1,2],[1,3],[1,4],[1,5],[1,6],[1,4],[1,3],[1,2]]]


Attributes:
"fields"                - 2D-array of Field objects which are initialized via "fields_fill" function

--------------------------------------------------------------------------------------------------------------------------------

RETURNS:

"FIELD_CHOSEN"          - the field on which the figure your AI wants to move is
"FIELD_MOVE"            - the field your AI wants to move the figure from "FIELD_CHOSEN" to
"AI_MESSAGES[0]"        - the figure type your AI wants to chose if a pawn reaches the end (2-rook, 3-knight, 4-bishop, 5-queen)
"AI_MESSAGES[1]"        - not used yet

--------------------------------------------------------------------------------------------------------------------------------
