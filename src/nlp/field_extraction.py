
from transformers import pipeline

nlp_extractor = pipeline('ner', model='bert-base-uncased')

def extract_fields(text):
    entities = nlp_extractor(text)
    extracted = {e['entity']: e['word'] for e in entities}
    return extracted
