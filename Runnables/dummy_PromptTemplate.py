

class DummyPromptTemplate:
    def __init__(self, template: str, input_variables: list ):
        self.template = template
        self.input_variables = input_variables if input_variables is not None else []

    def format(self, input_dict) -> str:
        return self.template.format(**input_dict)
