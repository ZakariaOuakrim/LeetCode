class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        L,R=0,1
        arr.sort()
        result=[]
        bestMin=float('inf');
        while L<R and R<len(arr):
            if abs(arr[L]-arr[R])==bestMin:
                bestMin=abs(arr[L]-arr[R])
                result.append([arr[L],arr[R]])
                L=R
                R+=1
            elif abs(arr[L]-arr[R])<bestMin: #found a new best min abs difference 
                result.clear()
                bestMin=abs(arr[L]-arr[R])
                result.append([arr[L],arr[R]])
                L=R
                R+=1
            else:
                L=R
                R+=1
        return result
            