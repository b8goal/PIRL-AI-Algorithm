import util
import wordsegUtil

_X_ = None

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        return 0, wordsegUtil.SENTENCE_BEGIN  # word position & previous reconstructed word
    # state는 이전까지 이용한 단어의수 / 이전에 처리했던 단어를 의미

    def is_end(self, state):
        return state[0] == len(self.queryWords)

    def succ_and_cost(self, state):
        pos, prev_word = state
        vowel_removed_word = self.queryWords[pos]
        # 서로의 Set을 합쳐주기 위해 fills를 다음과 같이 선언
        fills = self.possibleFills(vowel_removed_word) | {vowel_removed_word}  # use self.possibleFills
        for fill in fills:
            next_state = pos +1 , fill
            cost = self.bigramCost(prev_word, fill)
            yield fill, next_state, cost  # return action, state, cost
    
unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
problem = VowelInsertionProblem('thts m n th crnr'.split(), bigramCost, possibleFills)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
# print(dps.solve(problem))

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=0)
print(ucs.solve(problem))
