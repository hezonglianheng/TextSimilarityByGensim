import testdoc
import corpora2model
from gensim import similarities


path1 = r'd:\人类语言与人工智能\期末作业\项目\articles from CNN for test'
documents, test_titles = testdoc.articles2docs(path1)

file_name1 = r'tfidf_similarity.txt'
file1 = open(file_name1, encoding='utf8', mode='w+')
model, dictionary1, corpus1, corpus_titles1 = corpora2model.create_tfidf()
index1 = similarities.MatrixSimilarity(model[corpus1])
vectors1 = [dictionary1.doc2bow(doc) for doc in documents]
models = [model[vec] for vec in vectors1]
sims1 = [index1[v] for v in models]
sorted_sims1 = [sorted(list(enumerate(sims1[i])), key=lambda item: -item[1]) for i in range(len(test_titles))]
for j in range(len(sorted_sims1)):
    for k in range(10):
        file1.write(corpus_titles1[sorted_sims1[j][k][0]])
        file1.write('\t')
        file1.write(str(sorted_sims1[j][k][1]))
        file1.write('\n')
    file1.write('\n')
file1.close()

