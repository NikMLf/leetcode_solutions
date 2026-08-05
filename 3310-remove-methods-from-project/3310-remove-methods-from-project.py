class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        is_suspicious = [False] * n
        stack = [k]
        is_suspicious[k] = True

        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not is_suspicious[neighbor]:
                    is_suspicious[neighbor] = True
                    stack.append(neighbor)

        for u, v in invocations:
            if not is_suspicious[u] and is_suspicious[v]:

                return list(range(n))

        result = [i for i in range(n) if not is_suspicious[i]]
        return result