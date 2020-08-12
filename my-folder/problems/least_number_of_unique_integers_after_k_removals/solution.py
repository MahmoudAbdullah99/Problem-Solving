class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        ls = sorted(dic.items(), key=lambda kv: kv[1])
        l = 0
        while k > 0:
            ll = list(ls[l])
            if ll[1] > k:
                ll[1] -= k
                break
            elif ll[1] == k:
                ls.pop(l)
                break
            else:
                ls.pop(l)
                k -= ll[1]

        return len(ls)