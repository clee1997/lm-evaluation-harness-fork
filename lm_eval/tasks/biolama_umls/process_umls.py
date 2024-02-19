import json


def doc_to_text(doc):
    # umls
    pid2prompt_meta = {'UR44': {'template': '[X] treats [Y] .'}, 'UR221': {'template': '[X] has a genetic association with [Y] .'}, 'UR45': {'template': '[X] treats [Y] .'}, 'UR48': {'template': '[X] results in [Y] .'}, 'UR211': {'template': '[X] involves [Y] .'}, 'UR214': {'template': '[Y] causes [X] .'}, 'UR256': {'template': '[Y] has a genetic association with [X] .'}, 'UR588': {'template': '[X] involves [Y] process .'}, 'UR254': {'template': '[X] has symptoms such as [Y] .'}, 'UR180': {'template': '[Y] is finding of disease [X] .'}, 'UR116': {'template': '[X] is clinically associated with [Y] .'}, 'UR625': {'template': '[X] has a genetic association with [Y] .'}, 'UR46': {'template': '[X] should not be used in the presence of [Y] disease .'}, 'UR173': {'template': '[X] is caused by [Y] .'}, 'UR49': {'template': '[X] has a mechanism of action of [Y] .'}, 'UR50': {'template': '[X] is a therapeutic class of [Y] .'}, 'UR124': {'template': 'The most widely used drug for preventing [X] is [Y] .'}}
    # wikidata
    # pid2prompt_meta = {'P2176': {'template': 'The standard treatment for patients with [X] is a drug such as [Y].'}, 'P2175': {'template': '[X] has effects on diseases such as [Y].'}, 'P4044': {'template': '[X] cures diseases such as [Y].'}, 'P780': {'template': '[X] has symptoms such as [Y].'}, 'P2293': {'template': 'Gene [X] has a genetic association with diseases such as [Y].'}}
    # system_prompt = f"You are a helpful, respectful and honest assistant. You need to answer the given question less than 3 words.\n\n Example 1: \n Question: What kinds of diseases that bacterial toxin can prevent? \n Answer: Colonic Neoplasms. \n Your answer should be less than 3 words. Do not give any explainations."
    template =  pid2prompt_meta[doc["predicate_id"]]["template"]
    subject = doc["sub_label"]
    sentence = template.replace('[X]', subject).replace('[Y]', "<BLANK>")

    prefix = f'Consider the following sentence: "{sentence}"'
    suffix = '\n\n-> Which noun-phrase should <BLANK> be filled with? Give me 5 most probable candidates. Output your response in JSON format with keys "top_1", "top_2", "top_3", "top_4" and "top_5", where the value for key "top_1" is the most promising entity that would replace <BLANK>.'

    prompt = prefix + suffix
    
    # prompt = prompt + "please predict _____" # Which noun-phrase should <BLANK> be filled with? Give me 5 most probable candidates. Output your response in JSON format with keys "top_1", "top_2", "top_3", "top_4" and "top_5", where the value for key "top_1" is the most promising entity that would replace <BLANK>
    
    # print(prompt)
    return f"{prompt}\n"
    # return f"{sentence}\n"

def doc_to_target(doc):
    objects = []
    if 'obj_labels' in doc:
        objects = doc['obj_labels']  
    elif 'obj_label' in doc:
        objects = [doc['obj_label']]

    if 'obj_aliases' in doc:
        objects += [a for al in doc['obj_aliases'] for a in al]

    lower_objects = list(dict.fromkeys([obj.lower() for obj in objects]))

    print(f"lower_objects = {lower_objects}")

    return lower_objects # this returns a list. 

# # Usage example:
# prompts = load_prompts('path_to_your_prompts_file.jsonl')
# doc =  # Your document here
# prompt_text = doc_to_text(doc, prompts)
# target_text = doc_to_target(doc)

# Consider the following sentence: "Preseptal cellulitis is caused by <BLANK>."

# -> Which noun-phrase should <BLANK> be filled with? Give me 5 most probable candidates. Output your response in JSON format with keys "top_1", "top_2", "top_3", "top_4" and "top_5", where the value for key "top_1" is the most promising entity that would replace <BLANK>.

# am i supposed to implement my own metric function? -> 

