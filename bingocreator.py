import codecs
import random
import tempfile
from string import Template
import subprocess
import os


class BingoCreator(object):
    def __init__(self, questions_file, latex_file):
        self.questions = self.__read_in_file(questions_file).split("\n")
        self.latex_content = self.__read_in_file(latex_file)

        self.pdfs_dir = os.path.join(os.path.dirname(__file__), "pdfs")

    def __read_in_file(self, file):
        return codecs.open(file, 'r', "utf8").read().replace("\r", "")

    def __get_random_24_fields(self):
        return random.sample(self.questions, 25)

    def create_pdfs(self, num_pdfs):
        for i in range(0, num_pdfs):
            self.__create_latex("bingo_"+str(i))

        all_outputs = os.listdir(self.pdfs_dir)

        for output in all_outputs:
            if not output.endswith(".pdf") and not output.endswith(".gitignore"):
                os.remove(os.path.join(self.pdfs_dir, output))



    def __create_latex(self, output_name):
        template = "\\begin{tabular}{|>{\RaggedRight}p{2.7cm}|>{\RaggedRight}p{2.7cm}|>{\RaggedRight}p{2.7cm}|>{\RaggedRight}p{2.7cm}|>{\RaggedRight}p{2.7cm}|} \n \hline \n"
        underline = "\\underline{\hspace{2.5cm}}"

        fields = self.__get_random_24_fields()

        n_row = 0
        n_column = 0
        for field in fields:
            n_column += 1
            if n_row == 2 and n_column == 3:
                field_entry = "\multicolumn{1}{c|}{JOKER}"
            else:
                field_entry = underline+" "+field

            if n_column == 5:
                template += field_entry+" \\\\\n"
                template += "\hline \n"
                n_column = 0
                n_row += 1
            else:
                template += field_entry+" & "
        template += "\end{tabular}"
        s = Template(self.latex_content)
        new_file = s.substitute(latextable=template)

        # Store file
        with codecs.open("./pdfs/temp.tex", 'w', "utf8") as f:
            f.write(new_file)

        cmd =['pdflatex', '-job-name='+output_name, "temp.tex"]
        subprocess.run(cmd, shell=True, cwd=self.pdfs_dir)






