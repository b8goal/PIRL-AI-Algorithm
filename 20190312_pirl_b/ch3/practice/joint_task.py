import util
import wordsegUtil

_X_ = None

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    # space도 없고 모음도 없을 때
    # space와 모음을 추가해서 output 추가
    def start_state(self):
        # position before which text is reconstructed & previous word
        return 0, wordsegUtil.SENTENCE_BEGIN
        # 0 현재 까지 처리한 char 수 / 이전까지 만들었던 단어의 수
        # 구현할 때는 loop를 2번 사용해야함
        # loop 1개 : space 쪼개는 곳, loop 1개 : candidate 쪼개는 부분 2중 loop
    def is_end(self, state):
        return state[0] == len(self.query)

    def succ_and_cost(self, state):
        raise NotImplementedError
    # use "self.poosibleFills(vowel_removed_word)" instead of
    # "self.possibleFills(vowel_removed_word) | {vowel_removed_word}"
    #
    # user two overlapped loops

unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
smoothCost = wordsegUtil.smoothUnigramAndBigram(unigramCost, bigramCost, 0.2)
possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
problem = JointSegmentationInsertionProblem('mgnllthppl', smoothCost, possibleFills)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
# print(dps.solve(problem))

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=0)
print(ucs.solve(problem))
