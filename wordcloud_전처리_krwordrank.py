from krwordrank.hangle import normalize
'''
pip install krwordrank
pip install scipy
pip install sklearn

참고 : github/lovit/kr-wordrank
작업참고 : https://github.com/lovit/KR-WordRank/blob/master/tutorials/krwordrank_word_and_keyword_extraction.ipynb
'''

# 텍스트 파일 가져와서 전처리하기
def get_texts_scores(fname):
    with open(fname, encoding='utf-8') as f:
        docs = [doc.lower().replace('\n','').split('\t') for doc in f]
        docs = [doc for doc in docs if len(doc) == 2]

        if not docs:
            return [], []

        texts, scores = zip(*docs)
        return list(texts), list(scores)

# La La Land 라라랜드 텍스트 파일
fname = '/Users/mac/Documents/coding_python/python_WordCloud/data/134963.txt'
texts, scores = get_texts_scores(fname)


# text 정제화(불필요한 조사 및 기호들 제거)
    # 자동화 팁 : text는 스크래핑으로 리스트 형식으로 가져오

texts = [normalize(text, english=True, number=True) for text in texts]

print(texts)

from krwordrank.word import  KRWordRank

wordrank_extractor = KRWordRank(
    min_count=5,    #최소단어 출현 빈도수(그래프 생성시)
    max_length=10,  # 단어의 최대 길이
    verbose=True
)

beta = 0.85
max_iter = 10

keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print(f'{word} : {r}')
    # print('%8s:\t%4f' % (word, r))
