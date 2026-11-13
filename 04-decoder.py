reverse_merges = {v: k for k, v in merges.items()}

def decode_sub(token):
    if token not in reverse_merges:
        return [token]

    token_sub = []

    for t in reverse_merges[token]:
        token_sub.extend(decode_sub(t))

    return token_sub


def decode(ids):
  ids_expanded =[]
  for token in ids:
    ids_expanded.extend(decode_sub(token))
  return ids_expanded


ids_full = decode(ids)
print(ids_full)
print(len(ids_full))
