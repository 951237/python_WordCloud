from krwordrank.hangle import normalize

# text 정제화(불필요한 조사 및 기호들 제거)
    # 자동화 팁 : text는 스크래핑으로 리스트 형식으로 가져오
texts = ['이것은 예문입니다.', '각자의 데이터를 준비하세요.', '이것은 예문입니다.', '각자의 데이터를 준비하세요.', '이것은 예문입니다.', '각자의 데이터를 준비하세요.', '이것은 예문입니다.', '각자의 데이터를 준비하세요.', '이것은 예문입니다.', '각자의 데이터를 준비하세요.']
texts = [normalize(texts, english=True, number=True) for text in texts]

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
    print('%8s:\t%4f' % (word, r))
