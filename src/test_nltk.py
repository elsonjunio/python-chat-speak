import pickle
from nltk.classify import accuracy
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('portuguese')

dados = [
    ("Abrir a janela", "abrir_janela"),
    ("Fechar a porta", "fechar_porta"),
    ("Criar um arquivo", "criar_arquivo")
]

all_words = set(word.lower()
                for passage in dados for word in word_tokenize(passage[0]) if word.lower() not in stop_words)

processed_data = [({word: (word in word_tokenize(x[0]))
                    for word in all_words}, x[1]) for x in dados]


print(processed_data)


# Divide os dados em conjuntos de treinamento e teste
training_size = int(len(processed_data) * 0.8)
training_data = processed_data[:training_size]
testing_data = processed_data[training_size:]

# Treina o modelo usando o algoritmo NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(training_data)

classifier.show_most_informative_features()

# Avalia a precisão do modelo
print("Precisão do modelo:", accuracy(classifier, testing_data))


# frase = "Abrir a porta"
# tokens = word_tokenize(frase)
# acao_prevista = classifier.classify(tokens)
#
# print("Ação prevista:", acao_prevista)

test_sentence = "Quebrar a janela"

test_sent_features = {word: (word in word_tokenize(
    test_sentence.lower())) for word in all_words}

response = classifier.classify(test_sent_features)

print(response)
prob = classifier.prob_classify(test_sent_features)


print(f'{response}:{prob.prob(response)}')

# save_classifier = open("naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()
#
# classifier_f = open("naivebayes.pickle", "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()
