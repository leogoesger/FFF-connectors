from inquirer import prompt, List, Text

from utils.constants import CGREEN, CVIOLET, CEND


class UserInput:
    def __init__(self, number_of_func):
        self.number_of_func = number_of_func

        self.intro_message()
        self.user_inputs = {}
        self.get_user_inputs()
        self.display_user_inputs()

    def intro_message(self):
        print("")
        print(CGREEN + "Calculate senario based on optimal values."+CEND)

    def display_user_inputs(self):
        print("")
        print(CGREEN + "********* Here are your inputs *********"+CEND)
        for i in range(self.number_of_func):
            print(CVIOLET + "********* Function {} *********".format(i)+CEND)
            print("Function Type: {}".format(
                self.user_inputs["func_" + str(i)]["type"]))
            print("Start Date: {}".format(
                self.user_inputs["func_" + str(i)]["bioperiod_start_date"]))
            print("End Date: {}".format(
                self.user_inputs["func_" + str(i)]["bioperiod_end_date"]))
            print("")
            if "binnings" in self.user_inputs["func_" + str(i)]:
                print("Binnings: ")
                bins = self.user_inputs["func_" + str(i)]["binnings"]
                for index, b in enumerate(bins):
                    if index < len(bins) - 1:
                        print(
                            " Bin-{}: {} to {}".format(index, b, bins[index + 1]))
                print(
                    " Bin-{}: {} to infinity".format(len(bins) - 1, bins[-1], ))

        question = [
            List('is_correct',
                 message="Is this correct?",
                 choices=['Yes', 'No']),
        ]
        answers = prompt(question)
        if answers["is_correct"] == "No":
            self.get_user_inputs()

    def get_user_inputs(self):
        for i in range(self.number_of_func):
            print("")
            print(CVIOLET + "Enter Params for Function " + str(i + 1) + CEND)
            print("")
            _input = {}

            question = [
                List('type',
                     message="Which function type to run?",
                     choices=['magnitude', 'categorical']),
                Text('start',
                     message="Bioperiod Start Date. Example: 10/20",
                     validate=lambda _, d: d is not ''),
                Text('end',
                     message="Bioperiod End Date. Example: 06/20",
                     validate=lambda _, d: d is not '')
            ]

            answers = prompt(question)
            _input["type"] = answers['type']
            _input["bioperiod_start_date"] = answers['start']
            _input["bioperiod_end_date"] = answers['end']

            cate_question = [
                Text('binnings',
                     message="Define the binnings. Example: 0.3, 0.5 ",
                     validate=lambda _, d: d is not ''),
            ]
            if answers['type'] == 'categorical':
                cate_answer = prompt(cate_question)
                _input["binnings"] = [float(x.strip())
                                      for x in cate_answer['binnings'].split(',')]
                _input["binnings"].insert(0, 0)

            self.user_inputs["func_" + str(i)] = _input
