from spacy.lang.en import English
import re
import os


def article2doc(path: str):
    """
    将路径对应的文件进行切词，去除标点符号、空格和停用词后输出词列表\n
    默认文本为英文，不检测语言
    """
    file = open(path, encoding='utf8', mode='r+')
    file_lines = file.readlines()
    text_title = file_lines[0]
    file_text = ""
    catch = r'\(.+\)'
    for para in file_lines[1:]:
        match = re.match(catch, para)
        if match:
            para = para[:match.start()] + para[match.end():]
        file_text += para.lower()
    nlp = English()
    doc = nlp(file_text)
    saved_tokens = []
    for token in doc:
        if (not token.is_stop) and (not token.is_punct) and \
                (not token.is_space):
            saved_tokens.append(str(token))
    return saved_tokens, text_title


def articles2docs(directory: str):
    documents = []
    titles = []
    if os.path.isdir(directory):
        iter1 = os.walk(directory)
        for i in iter1:
            for name in i[-1]:
                file_path = os.path.join(directory, name)
                documents.append(article2doc(file_path)[0])
                titles.append(article2doc(file_path)[1])
    return documents, titles


if __name__ == '__main__':
    import pprint
    path1 = r'd:\人类语言与人工智能\期末作业\项目\articles from CNN for test'
    pprint.pprint(articles2docs(path1))
