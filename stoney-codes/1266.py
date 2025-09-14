class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        i,j=0,0
        result=0
        while i<len(points):
            while j<len(points[i]):
 
                if abs(points[i+1][j]-points[i][j])>abs(points[i][j]-points[i][j+1]):
                    result+= abs(points[i+1][j]-points[i][j])
                else:
                    result+= abs(points[i][j]-points[i][j+1])
                j+=1
            i+=1
        return result