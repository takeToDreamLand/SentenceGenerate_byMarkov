# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:35:22 2018

@author: Administrator
"""

import random 
import jieba

#dataset_file = ["I like to eat apples","You eat oranges"]
dataset_file = ["你喜欢吃苹果","我吃橘子","我不使用苹果电脑","我们使用橘子平台打游戏","我们使用Steam平台打游戏",'你使用树莓派电脑',"大家都使用苹果电脑","没人使用诺基亚"]
model = {}
for line in dataset_file:
    # Uncomment below sentence if dataset include Chinese word 
    line = list(jieba.cut(line,cut_all=False))
#    line = line.lower().split()
    for i, word in enumerate(line):
        if i == len(line)-1:   
            model['END'] = model.get('END', []) + [word]
        else:    
            if i == 0:
                model['START'] = model.get('START', []) + [word]
            model[word] = model.get(word, []) + [line[i+1]]

generated = []
while True:
    if not generated:
        words = model['START']
    elif generated[-1] in model['END']:
        break
    else:
        words = model[generated[-1]]
    generated.append(random.choice(words))

print(''.join(generated));
