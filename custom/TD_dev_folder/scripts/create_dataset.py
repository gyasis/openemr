# %%

import random

# Define symptoms and associated phrases
symptoms = {
    'Weight Change': {
        'positive': 'has experienced weight loss',
        'negative': 'has not experienced weight loss',
        'phrase': 'weight loss',
        'positive_phrase': 'has lost weight',
        'negative_phrase': 'has no weight loss'
    },
    'Anorexia': {
        'positive': 'has a decreased appetite',
        'negative': 'has a normal appetite',
        'phrase': 'decreased appetite',
        'positive_phrase': 'lacks appetite',
        'negative_phrase': 'has no appetite loss'
    },
    'Night Sweats': {
        'positive': 'has experienced night sweats',
        'negative': 'has not experienced night sweats',
        'phrase': 'night sweats',
        'positive_phrase': 'has been sweating at night',
        'negative_phrase': 'has no night sweats'
    },
    'Heat or Cold': {
        'positive': 'is sensitive to temperature changes',
        'negative': 'is not sensitive to temperature changes',
        'phrase': 'temperature sensitivity',
        'positive_phrase': 'has temperature sensitivity',
        'negative_phrase': 'has no temperature sensitivity'
    },
    'Weakness': {
        'positive': 'feels weak',
        'negative': 'does not feel weak',
        'phrase': 'weakness',
        'positive_phrase': 'feels physically weak',
        'negative_phrase': 'has no physical weakness'
    },
    'Fever': {
        'positive': 'has a fever',
        'negative': 'does not have a fever',
        'phrase': 'fever',
        'positive_phrase': 'has elevated temperature',
        'negative_phrase': 'has no fever'
    },
    'Insomnia': {
        'positive': 'has trouble sleeping',
        'negative': 'can sleep normally',
        'phrase': 'insomnia',
        'positive_phrase': 'has sleeping trouble',
        'negative_phrase': 'has no trouble sleeping'
    },
    'Intolerance': {
        'positive': 'is intolerant to certain foods',
        'negative': 'has no food intolerance',
        'phrase': 'food intolerance',
        'positive_phrase': 'is intolerant to some foods',
        'negative_phrase': 'has no food intolerance'
    },
    'Fatigue': {
        'positive': 'feels fatigued',
        'negative': 'does not feel fatigued',
        'phrase': 'fatigue',
        'positive_phrase': 'feels excessively tired',
        'negative_phrase': 'has no excessive tiredness'
    },
    'Chills': {
        'positive': 'has experienced chills',
        'negative': 'has not experienced chills',
        'phrase': 'chills',
        'positive_phrase': 'has been experiencing chills',
        'negative_phrase': 'has no chills'
    },
    'Irritability': {
        'positive': 'feels irritable',
        'negative': 'does not feel irritable',
        'phrase': 'irritability',
        'positive_phrase': 'is experiencing irritability',
        'negative_phrase': 'has no irritability'
    },
    'Cough': {
        'positive': 'has a cough',
        'negative': 'does not have a cough',
        'phrase': 'cough',
        'positive_phrase': 'has coughing',
        'negative_phrase': 'has no coughing'
    }
}

# Define sentence formers
positive_formers = [
    'Patient is positive for {0}',
    'Patient has {0}',
    'Patient is showing {0}',
    'Patient exhibits {0}'
]

positive_formers_advanced = [
    'Patient is positive for {0}',
    'Patient has {0}',
    'Patient is showing {0}',
    'Patient exhibits {0}',
    '{0} is present in patient'
]

negative_formers = [ 
    'Patient is negative for {0}', 
    'Patient does not have {0}', 
    'Patient is not showing {0}', 
    'Patient shows no signs of {0}',
    '{0} is not present in the patient'
]

negative_formers_advanced = [
    'The patient does not have {0}', 
    'The patient is not experiencing {0}', 
    'The patient shows no indications of {0}',
    'No presence of {0} in the patient',
    '{0} is not observed in the patient'
]

# Define number of sentences to generate
num_sentences = 1000

# Define dataset
dataset = []

# Generate sentences
for i in range(num_sentences):
    # Determine number of symptoms for sentence
    num_symptoms = random.randint(1, len(symptoms))

    # Select symptoms
    selected_symptoms = random.sample(symptoms.keys(), num_symptoms)

    # Determine sentence type
    sentence_type = random.choice(['simple', 'advanced'])

    # Determine positive or negative phrase for each symptom
    symptom_phrases = {}
    for symptom in selected_symptoms:
        phrase_type = random.choice(['positive', 'negative'])
        phrase = symptoms[symptom][phrase_type]
        if phrase_type == 'positive':
            if sentence_type == 'advanced':
                symptom_phrases[symptom] = random.choice(positive_formers_advanced).format(symptoms[symptom]['phrase'])
            else:
                if symptom in positive_formers_simple:
                    symptom_phrases[symptom] = random.choice(positive_formers_simple).format(symptoms[symptom]['phrase'])
                else:
                    symptom_phrases[symptom] = phrase
        else:
            if sentence_type == 'advanced':
                symptom_phrases[symptom] = random.choice(negative_formers_advanced).format(symptoms[symptom]['phrase'])
            else:
                if symptom in negative_formers_simple:
                    symptom_phrases[symptom] = random.choice(negative_formers_simple).format(symptoms[symptom]['phrase'])
                else:
                    symptom_phrases[symptom] = phrase

    # Construct sentence
    sentence = ' '.join([symptom_phrases[s] for s in selected_symptoms])
    sentence = sentence.capitalize() + '.'
    
    # Create dictionary of sentence and symptoms
    sentence_dict = {'sentence': sentence, 'symptoms': {}}
    for symptom, phrase in symptom_phrases.items():
        if phrase == symptoms[symptom]['positive']:
            sentence_dict['symptoms'][symptom] = 1
        elif phrase == symptoms[symptom]['negative']:
            sentence_dict['symptoms'][symptom] = -1
        else:
            sentence_dict['symptoms'][symptom] = 0
            
    # Append to dataset
    dataset.append(sentence_dict)


# Print first 20 lines
for sentence in dataset[:20]:
    print(sentence)

# %%
