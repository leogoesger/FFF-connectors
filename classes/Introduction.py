import inquirer
from utils.helpers import create_folders


class Introduction:
    def __init__(self):
        self.script = None
        self.get_script()
        self.input_output_folder_structure()

    def get_script(self):
        print('')
        questions = [
            inquirer.List('script',
                          message="Which script to run?",
                          choices=['hydraulic performance',
                                   'hydraulic suitability timeserie', ],
                          ),
        ]
        answers = inquirer.prompt(questions)
        self.script = answers['script']

    def input_output_folder_structure(self):
        create_folders(['files_input/{}'.format(self.script.replace(" ", "_")),
                        'files_output/{}'.format(self.script.replace(" ", "_"))])
