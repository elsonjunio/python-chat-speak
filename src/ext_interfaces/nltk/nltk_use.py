import pickle

from nltk.classify import accuracy
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from .nltk_words import DATA, TEST_DATA
import os.path


class NLTKUse(object):
    def __init__(self, file_path: str):
        self.stop_words = stopwords.words("portuguese")
        self.data = DATA

        self.all_words = set(
            word.lower()
            for passage in self.data
            for word in word_tokenize(passage[0])
            if word.lower() not in self.stop_words
        )

        if os.path.exists(file_path):
            self.load(file_path)
        else:
            self.train()
            self.save(file_path)

    def train(self):

        training_data = [
            ({word: (word in word_tokenize(x[0])) for word in self.all_words}, x[1])
            for x in self.data
        ]

        test_data = TEST_DATA

        test_words = set(
            word.lower()
            for passage in test_data
            for word in word_tokenize(passage[0])
            if word.lower() not in self.stop_words
        )

        testing_data = [
            ({word: (word in word_tokenize(x[0])) for word in test_words}, x[1])
            for x in test_data
        ]

        print(training_data)
        print(testing_data)

        self.classifier = NaiveBayesClassifier.train(training_data)
        print("Precisão do modelo:", accuracy(self.classifier, testing_data))

        self.classifier.show_most_informative_features()

    def load(self, file: str):
        classifier_f = open(file, "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()

    def save(self, file: str):
        save_classifier = open(file, "wb")
        pickle.dump(self.classifier, save_classifier)
        save_classifier.close()

    def text(self, text: str):
        test_sentence = text

        test_sent_features = {
            word: (word in word_tokenize(test_sentence.lower()))
            for word in self.all_words
        }

        response = self.classifier.classify(test_sent_features)

        print(response)
        prob = self.classifier.prob_classify(test_sent_features)

        print(f"{response}:{prob.prob(response)}")

        return response
