from collections import defaultdict
import queue

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        length = arr.__len__()
        visited = [0] * length
        ans = 0
        nowIdx = 0
        nextNode_List = defaultdict(list)
        for i, value in enumerate(arr):
            nextNode_List[value].append(i)

        que = queue.Queue()
        que.put([nowIdx, 0])
        visited[0] = True

        while que.empty() == False:
            nowNode = que.get()
            nowIdx = nowNode[0]
            nowCnt = nowNode[1]
            nowVal = arr[nowIdx]

            nextNodes = [nowIdx - 1, nowIdx + 1]
            nextNodes.extend(nextNode_List[nowVal])
            nextNode_List.pop(nowVal)
            for next in nextNodes:
                if 0 > next or next >= length or next == nowIdx:
                    continue
                if visited[next] == True:
                    continue
                if next == length - 1:
                    ans = nowCnt + 1
                    break
                visited[next] = True
                que.put([next, nowCnt+1])
            if ans != 0:
                break
        return ans