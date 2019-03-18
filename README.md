## 1. Dynamic Programming - dynamic_programming_search.py
###  # use self.future_dict
```
def future(self, problem, state):
        if self.memory_use and state in self.future_dict:
            actions, cost, _ = self.future_dict[state]
            return actions, cost, 0
```

## 2. Joint_task - joint_task.py
### space 바와 모음이 없는 상태에서 space와 모음을 동시에 추가해주는 작업
- pos , current_word = state[0], state[1]
- 첫번 째 for문이 space 추가 구문
- 두번 째 for문이 모음을 추가하는 구문

```
def succ_and_cost(self, state):
        pos, current_word = state
        for i in range(pos + 1, len(self.query)+1):
            vowel_removed_word = self.query[pos:i]
            fills = self.possibleFills(vowel_removed_word)
            for fill in fills:
                next_state = i,fill
                cost = self.bigramCost(current_word, fill)
                yield fill, next_state, cost  # return action, state, cost
```