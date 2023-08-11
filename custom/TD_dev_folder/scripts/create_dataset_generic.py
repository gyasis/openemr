import random

# Define symptoms and associated phrases
symptoms = {
    'Weight Change': {
        'positive': 'has experienced weight loss',
        'negative': 'has not experienced weight loss',
        'phrase': 'weight loss'
    },
    'Anorexia': {
        'positive': 'has a decreased appetite',
        'negative': 'has a normal appetite',
        'phrase': 'decreased appetite'
    },
    'Night Sweats': {
        'positive': 'has experienced night sweats',
        'negative': 'has not experienced night sweats',
        'phrase': 'night sweats'
    },
    'Heat or Cold': {
        'positive': 'is sensitive to temperature changes',
        'negative': 'is not sensitive to temperature changes',
        'phrase': 'temperature sensitivity'
    },
    'Weakness': {
        'positive': 'feels weak',
        'negative': 'does not feel weak',
        'phrase': 'weakness'
    },
    'Fever': {
        'positive': 'has a fever',
        'negative': 'does not have a fever',
        'phrase': 'fever'
    },
    'Insomnia': {
        'positive': 'has trouble sleeping',
        'negative': 'can sleep normally',
        'phrase': 'insomnia'
    },
    'Intolerance': {
        'positive': 'is intolerant to certain foods',
        'negative': 'has no food intolerance',
        'phrase': 'food intolerance'
    },
    'Fatigue': {
        'positive': 'feels fatigued',
        'negative': 'does not feel fatigued',
        'phrase': 'fatigue'
    },
    'Chills': {
        'positive': 'has experienced chills',
        'negative': 'has not experienced chills',
        'phrase': 'chills'
    },
    'Irritability': {
        'positive': 'feels irritable',
        'negative': 'does not feel irritable',
        'phrase': 'irritability'
    },
    'Cough': {
        'positive': 'has a cough',
        'negative': 'does not have a cough',
        'phrase': 'cough'
    }
}

# Define sentence formers
positive_formers = [
    'The patient is exhibiting {}',
    'The patient has {}',
    'Positive for {}'
]

negative_formers = [
    'The patient is negative for {}',
    'The patient does not have {}',
    '{} is absent in the patient'
]

# Define number of sentences to generate
num_sentences = 1000

# Generate sentences
sentences = []

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
    symptom_phrases = list(symptom_phrases.values())
    if sentence_type == 'advanced':
        if phrase_type == 'positive':
            sentence = 'Patient is exhibiting ' + ', '.join(symptom_phrases) + '.'
        else:
            sentence = 'Patient is negative for ' + ', '.join(symptom_phrases) + '.'
    else:
        if phrase_type == 'positive':
            sentence = 'Patient is positive for ' + ', '.join(symptom_phrases) + '.'
        else:
            sentence = 'Patient is negative for ' + ', '.join(symptom_phrases) + '.'

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
