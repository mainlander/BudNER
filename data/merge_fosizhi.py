import os
import os.path

filenames = os.listdir('FoSiZhi')
with open('fosizhig.txt', 'w', encoding='utf-8') as outf:
    for names in filenames:
        with open("FoSiZhi/{0}".format(names), 'r', encoding='utf-8') as f:
            for line in f:
                outf.write(line.strip())
                outf.write('\n')
        print(names)
