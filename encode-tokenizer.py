def get_stats(ids):
  counts = {}
  for pair in zip(ids, ids[1:]):
    counts[pair] = counts.get(pair, 0) + 1
  return counts


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

def encode(text):
  tokens = list(text.encode("utf-8"))
  while len(tokens) >= 2:#True:
    stats = get_stats(tokens)      #will simply give out all consective pairs of bytes in present text byte tokens
    candidates = [pair for pair in stats if pair in merges]    # will match those pair with merge dictionary which was made during training. these are only eligible to be merged
    if not candidates:
      break
    pair = min(candidates, key=lambda p: merges[p])    #Selects the pair having the smallest vocabulary index in merges
    tokens = merge(tokens, pair, merges[pair])
  return tokens

encode("hi i am ankur")
