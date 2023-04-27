str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
splits = str.split()
one_ch = [1, 5, 6, 7, 8, 9, 15, 16, 19]  
nlp = {}
for i, word in enumerate(splits):
  if i + 1 in one_ch:
    nlp[word[:1]] = i + 1  
  else:
    nlp[word[:2]] = i + 1  
print(nlp)