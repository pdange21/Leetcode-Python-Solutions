class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        root = -1
        indegree= [0] * n

        for left, right in zip(leftChild, rightChild):
            if left != -1:
                indegree[left] += 1
            if right != -1:
                indegree[right] += 1
        
        for index in range(n):
            if indegree[index] == 0:
                if root == -1:
                    root = index
                else:
                    return False

        seen = [False] * n
        def traverse(node):
            seen[node] = True
            if leftChild[node] != -1 and (seen[leftChild[node]] or not traverse(leftChild[node])):
                return False
            if rightChild[node] != -1 and (seen[rightChild[node]] or not traverse(rightChild[node])):
                return False
            return True
        
        return traverse(root) and all(seen)
