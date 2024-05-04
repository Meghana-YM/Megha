d={0:[1,4],1:[0,2,3],2:[1,3],3:[1,2,4],4:[0,3],5:[0]}
'''q=[0]
vis={0}
while q:
    a=q.pop()
    print(a)
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i)'''
def dfs(start,vis):
    vis .add(start)
    for i in d[start]:
        if i not in vis:
            return dfs(i,vis)
print(dfs(0,set()))  
'''class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
            q=[source]
            vis={source}
            while q:
                a=q.pop(0)
            if a==destination:
                return True    
        
            for i in d[a]:
                if i not in vis:
                    q.append(i)
                    vis.add(i)
            return False '''          

        

