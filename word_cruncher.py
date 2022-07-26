words = input().split(', ')
target = input()

words_by_idx = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1
    idx = 0
    while True:
        idx = target.find(word, idx)
        if idx < 0:
            break

        if idx not in words_by_idx:
            words_by_idx[idx] = []
        words_by_idx[idx].append(word)
        idx += len(word)


def find_all_solutions(idx, target, words_by_idx, words_count, used_words):
    if idx >= len(target):
        print(' '.join(used_words))
        return
    if idx not in words_by_idx:
        return
    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1
        find_all_solutions(idx+len(word), target,
                           words_by_idx, words_count, used_words)
        words_count[word] += 1
        used_words.pop()


find_all_solutions(0, target, words_by_idx, words_count, [])
