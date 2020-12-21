import os
import os.path

filenames = os.listdir('GauSeng')
with open('gauseng.txt', 'w', encoding='utf-8') as outf:
    for names in filenames:
        with open("GauSeng/{0}".format(names), 'r', encoding='utf-8') as f:
            for line in f:
                outf.write(line.strip())
                outf.write('\n')
        print(names)
