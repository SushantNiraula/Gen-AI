import random
class DummyLLM:
    def __init__(self):
        print('LLM Created')
    def __predict__(self, prompt):
        response_list=[
            'Kathmandu is the capital of Nepal.',
            'The city of Kathmandu is the capital of Nepal.',
            'Nepal\'s capital is Kathmandu.',
        ]
        return {'response':random.choice(response_list)}
