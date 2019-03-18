import math, collections

SENTENCE_BEGIN = '-BEGIN-'

corpus = [
    'I am Sam',
    'Sam I am',
    'I do not like green'
]
    
# Counting
unigram_counts = collections.defaultdict(int)
# uni-gram 모델을 카운팅함
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for word in words:
        unigram_counts[word] += 1

# 연속된 단어가 몇번 나왔는지를 카운트 해야함.
bigram_counts = collections.defaultdict(int)
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for i in range(len(words)-1):
        bigram_counts[(words[i], words[i+1])] += 1
        
# Bigram function
# 이전 단어가 나왔을 때 현재 단어가 나올 확률은
def bigram(prev_word, curr_word):
    # 연속된 두단어가 데이터셋에서 몇번 나왔는지 수와 앞에 있는 단어의 수로 나눈것.
    return float(bigram_counts[(prev_word, curr_word)]) / unigram_counts[prev_word]

# Printing results
print('\n- Bigram probabilities - ')
print(('P(-BEGIN-, I) = %f'%bigram(SENTENCE_BEGIN, 'I')))    
print(('P(-BEGIN-, Sam) = %f'%bigram(SENTENCE_BEGIN, 'Sam')))    
print(('P(I, do) = %f'%bigram('I', 'do')))
print(('P(like, green) = %f'%bigram('like', 'green')))
