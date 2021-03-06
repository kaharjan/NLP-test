# -*- coding:utf-8 -*-
'''
  author: songboyu
  create: 2013-10-27
  summary: 逆向最大匹配
'''

from common import u

CODEC='utf-8'

def bwd_mm_seg(wordDict, maxLen, str):
    wordList = []
    segStr = str
    segStrLen = len(segStr)
    while segStrLen > 0:
        if segStrLen > maxLen:
            wordLen = maxLen
        else:
            wordLen = segStrLen
        subStr = segStr[-wordLen:None]
        while wordLen > 1:
            if subStr in wordDict:
                break
            else:
                wordLen = wordLen - 1
                subStr = subStr[-wordLen:None]
        wordList.append(subStr)
        segStr = segStr[0: -wordLen]
        segStrLen = segStrLen - wordLen
    wordList.reverse()
    return wordList
        
            
def main():
    fp_dict = open('../dict.txt')
    wordDict = {}
    for eachWord in fp_dict:
        wordDict[u(eachWord.split('\t')[0].strip(), 'utf-8')] = 1
    segStr = u'巴勒斯坦自治领导机构主席阿拉法特'
    print segStr
    bwd_mm_seg(wordDict, 4, segStr)
    wordList = bwd_mm_seg(wordDict, 4, segStr)
    for wordstr in wordList:
        print wordstr,

if __name__ == '__main__':
    main()
    
    