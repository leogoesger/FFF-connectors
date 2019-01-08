from inquirer import prompt, List
from utils.helpers import create_folders


class Introduction:
    def __init__(self):
        self.script = None
        self.get_script()
        self.input_output_folder_structure()

    def get_script(self):
        print('')
        questions = [
            List('script',
                 message="Which script to run?",
                 choices=['hydraulic suitability',
                          'hydraulic suitability TS',
                          'ffc result metrics',
                          'performance metrics'],
                 ),
        ]
        answers = prompt(questions)
        self.script = answers['script'].replace(" ", "_")

    def input_output_folder_structure(self):
        input_folder = ['files_input/{}'.format(self.script)]

        # For input folder needs multiple sub-folders
        if(self.script == 'hydraulic_suitability_TS'):
            input_folder.extend([input_folder[0] + '/flow_bins',
                                 input_folder[0] + '/suitability_table'])
        if(self.script == 'performance_metrics'):
            input_folder.extend([input_folder[0] + '/scenario',
                                 input_folder[0] + '/time_series'])

        output_folder = 'files_output/{}'.format(self.script)
        create_folders([*input_folder, output_folder])
