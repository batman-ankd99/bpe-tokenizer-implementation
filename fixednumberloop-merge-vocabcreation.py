text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."

tokens = text.encode("utf-8")
tokens = list(map(int,tokens))

def get_stats(ids):
  counts = {}
  for pair in zip(ids, ids[1:]):
    counts[pair] = counts.get(pair, 0) + 1
  return counts

## functions to merge consective pari and replace with new vocab index
def merge(ids, most_pair, idx):    #ids -> list of tokens, to replace all consecutive occurrences of pair with new token index, pair -> top_pair
  new_ids = []
  i = 0

  while i < len(ids):
#    pair = (ids[i], ids[i+1])
    if i < (len(ids)-1) and (ids[i], ids[i+1]) == most_pair:
        new_ids.append(idx)
        i += 2
    else:
        new_ids.append(ids[i])
        i += 1

  return new_ids

vocab_size = 276 #total vocab size
num_merges = vocab_size - 256  #for i in num_merges
ids = list(tokens) #so original list isnt touched

merges = {}       #stores merge rules, merge_vocab[top_pair] = index_vocab

for i in range(num_merges):
    idx = 256 + i
    stats = get_stats(tokens)
    pair = max(stats, key=stats.get)
    ids = merge(ids, pair, idx)
    merges[pair] = idx
