import random

sentences = []
temp_segs = []

with open('gauseng.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip() == '':
            sentences.append(temp_segs)
            temp_segs = []
        else:
            ss = line.strip().split('\t')
            if len(ss) >= 2:
                char = ss[0]
                tag = ss[1]
                temp_segs.append( (char, tag) )

comp_count = 0
filter_sentences = []
for sent in sentences:
    isComp = False
    for w,t in sent:
        if '[' in w:
            isComp = True
            break
    if not isComp:
        filter_sentences.append(sent)

random.shuffle(filter_sentences)

split_index = int(len(filter_sentences) * 0.8)

train_sentences = filter_sentences[:split_index]
test_sentences = filter_sentences[split_index:]
print(len(train_sentences))
print(len(test_sentences))

with open('train.txt', 'w', encoding='utf-8') as f:
    for sent in train_sentences:
        for w, t in sent:
            f.write("{0}\t{1}\n".format(w, t))
        f.write('\n')

with open('test.txt', 'w', encoding='utf-8') as f:
    for sent in test_sentences:
        for w, t in sent:
            f.write("{0}\t{1}\n".format(w, t))
        f.write('\n')
