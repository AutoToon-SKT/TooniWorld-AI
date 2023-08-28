def input_preprocess(input):
    inputs = input.split('\n')
    story = inputs[-1]
    return story

def prompt_preprocess(prompt):
    panels = prompt.split('\n\n')
    prompts = []
    for p in panels:
        prompts.append(p.split('>')[1].strip().replace("\n"," "))
    return prompts