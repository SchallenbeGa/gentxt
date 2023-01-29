from transformers import pipeline

generator = pipeline('text-generation', model="asi/gpt-fr-cased-base")
print("==================================================================")
print(generator("Je suis intéresser par ce poste parce que", max_length=50, num_return_sequences=1))
print("==================================================================")
print(generator("Je suis patient et", max_length=50, num_return_sequences=1))
print("==================================================================")
print(generator("Dans l'attente votre réponse je vous présente", max_length=50, num_return_sequences=1))