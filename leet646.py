class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:p=pairs;p.sort(key=lambda p:p[-1]);o=0;e=-1001;[a>e and (o:=o+1) and (e:=b) for a,b in p];return o
#THIS IS SHITPOSTING I WOULD NEVER DO THIS PLS HIRE