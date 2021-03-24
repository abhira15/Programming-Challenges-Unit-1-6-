from collections import defaultdict
def contains(sorted_word, sorted_candidate):
    wchars = (c for c in sorted_word)
    for cc in sorted_candidate:
        while(True):
            if wchars < cc: continue
            if wchars == cc: break
            return False
    return True
d = defaultdict(list)
with open(r"C:\Users\91848\Desktop\practicals\CP01-PRA\Unit 6\word.txt", "r") as f:
    for line in f.readlines():
        if line[0].isupper(): continue
        word = line.strip()
        key = "".join(sorted(word.lower()))
        d[key].append(word)
        
w = sorted("cat")
result = []
for k in d.keys():
    if contains(w,k):
        result.extend(d[k])

print(sorted(result)[:20])