from bingocreator import BingoCreator


def get_24_random_fields():
    pass


def read_in_file():
    pass








# File einlesen mit einer Frage pro Zeile

# Aufteilen der Fragen mittels split

#

bingo_creator = BingoCreator("./questions.txt", "./latex_template.tex")
bingo_creator.create_pdfs(4)