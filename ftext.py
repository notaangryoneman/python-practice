text = "X-DSPAM-Confidence:    0.8475 "
ftext = text.find('0.8475')
# print(ftext)
stext = text.find(' ',ftext)
# print(stext)
numb = text[ftext : stext]
nnumb = float(numb)

print(nnumb)

