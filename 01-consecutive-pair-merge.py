text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."

tokens = text.encode("utf-8")
tokens = list(map(int,tokens))

def get_stats(ids):
  counts = {}
  for pair in zip(ids, ids[1:]):
    counts[pair] = counts.get(pair, 0) + 1
  return counts

stats = get_stats(tokens) #stats is a dictionary now with tuples of consective bytes and with their count of occurrence
top_pair = max(stats, key=stats.get) #applying max function on stats -> it gives key, values - how to sort keys - so funciton key=stats.get gives value so condition is this for sorting
#top_pair

def merge(ids, pair, idx):    #ids -> list of tokens, pair-> pair of bytes that we want to replace ; idx -> pair will be replaced with this new index
  new_ids = []
  i = 0
  while i < len(ids):
#    pair = (ids[i], ids[i+1])
    if i < (len(ids)-1) and (ids[i], ids[i+1]) == most_pair:  #checking for condition for last byte, if last bye then it will be handled with else
        new_ids.append(idx)
        i += 2
    else:
        new_ids.append(ids[i])
        i += 1
  return new_ids

new_ids_tokens = merge(tokens, top_pair, (256))
new_ids_tokens
