# -*- coding: utf-8 -*-
'''LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.'''
def LongestCommonSubSequence(str1, str2):
    lcs = [[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)]
    for i in range(0,len(str1)+1):
        for j in range(0,len(str2)+1):
            if(i==0 or j==0):
                lcs[i][j] = 0
            elif(str1[i-1] == str2[j-1]):
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    print lcs
    return lcs[len(str1)][len(str2)]
 
print LongestCommonSubSequence("ABCDGH","AEDFHR")
print LongestCommonSubSequence("AGGTAB","GXTXAYB")