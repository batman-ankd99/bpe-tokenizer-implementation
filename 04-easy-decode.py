vocab_tokenizer = {idx : bytes([idx]) for idx in range(256)}

for (i,y), idx in merges.items():
  vocab_tokenizer[idx] = vocab_tokenizer[i] + vocab_tokenizer[y]

def decode(list1):
  str1=[]
  for tokenn in list1:
    str1.append(vocab_tokenizer[tokenn])
  decoded_bytes = b"".join(str1)
  text = decoded_bytes.decode("utf-8")
  return text

print(decode([123,6]))
