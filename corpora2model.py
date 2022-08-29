import getdocs
from gensim.corpora import Dictionary
from gensim.models import LsiModel, LdaModel, TfidfModel


def prepare():
    documents, titles = getdocs.get_docs()
    dictionary = Dictionary(documents)
    dictionary.filter_extremes()
    corpus = [dictionary.doc2bow(text) for text in documents]
    return corpus, dictionary, titles


def create_lsi(topic: int = 10):
    corpus, dictionary, titles = prepare()
    lsi = LsiModel(corpus, id2word=dictionary,
                   num_topics=topic)
    return lsi, dictionary, corpus, titles


def create_lda():
    corpus, dictionary, titles = prepare()
    lda = LdaModel(corpus, id2word=dictionary, num_topics=10)
    return lda, dictionary, corpus, titles


def create_tfidf():
    corpus, dictionary, titles = prepare()
    tfidf = TfidfModel(corpus, id2word=dictionary)
    return tfidf, dictionary, corpus, titles


if __name__ == "__main__":
    import pprint
    #model, dictionary, corpus, titles = create_lsi(topic=20)
    #topics = model.show_topics()
    #pprint.pprint(topics)
    model1, dictionary1, corpus1, titles1 = create_lda()
    topics1 = model1.show_topics()
    pprint.pprint(topics1)
