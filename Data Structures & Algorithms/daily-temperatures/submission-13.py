from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # ==========================================
        # Method 1: 單調疊合法 (Monotonic Stack)
        # ==========================================

        # ------------------------------------------
        # 1-1. Stack 反方向（從後往前遍歷）
        # ------------------------------------------
        '''
        stack = []                           # 儲存溫度的「索引」，維持單調遞減（疊合底到疊合頂溫度由高到低）
        output = [0] * len(temperatures)     # 初始化答案陣列

        # 從最後一天倒著往前遍歷
        for i in range(len(temperatures)-1, -1, -1):
            # 只要疊合不為空，且當前溫度大於或等於疊合頂端的溫度
            # 代表疊合頂端的那幾天比較冷，對當前第 i 天來說沒有參考價值，直接彈出
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # 彈出所有較低溫度後，如果疊合內還有剩餘元素
            # 疊合頂端就是離第 i 天最近的「更高溫的天數索引」
            if stack:
                output[i] = stack[-1] - i    # 計算兩者的天數差
            else:
                output[i] = 0                # 若疊合空了，代表後面沒有比今天更高的溫度
                
            stack.append(i)                  # 將當前天的索引壓入疊合，供前面的天數比較

        return output
        # 時間複雜度 O(n): 每個索引最多進出疊合一次
        # 空間複雜度 O(n): 額外使用了 stack 空間

        # ------------------------------------------
        # 1-2. Stack 正方向（從前往後遍歷）
        # ------------------------------------------
        stack = []                           # 儲存「還在等待更高溫」的天數索引
        output = [0] * len(temperatures)     # 初始化答案陣列

        # 從第一天順著往後遍歷
        for i in range(len(temperatures)):
            # 只要疊合不為空，且今天的溫度大於疊合頂端（過去某天）的溫度
            # 代表疊合頂端那一天「終於等到了更高溫的今天」
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_i = stack.pop()          # 取出該天的索引
                output[pre_i] = i - pre_i    # 計算從那天到今天等了幾天
                
            stack.append(i)                  # 把今天的索引壓入疊合，開始等待未來的更高溫

        return output
        '''
        # 時間複雜度 O(n): 每個索引最多進出疊合一次
        # 空間複雜度 O(n): 額外使用了 stack 空間


        # ==========================================
        # Method 2: 動態規劃 (Dynamic Programming)
        # ==========================================
        # 利用後面已經算好的答案，直接在 output 上做「跳躍式」查找，省去額外疊合空間
        
        n = len(temperatures)
        output = [0] * n                     # 初始化答案陣列（預設為 0）

        # 從倒數第二天開始，由後往前遍歷（最後一天的答案一定是 0，不用算）
        for i in range(n-2, -1, -1):
            next_i = i + 1                   # 從隔壁第一天開始往後尋找
            
            # 當前溫度大於或等於我們正在比對的溫度（next_i）時，需要繼續往後找
            while next_i < n and temperatures[i] >= temperatures[next_i]:
                # 如果 next_i 這一天後續「再也沒有更高溫」（output 為 0）
                # 既然連 next_i 都等不到更高溫，那比它更熱（或一樣熱）的第 i 天也必然等不到
                if output[next_i] == 0:
                    next_i = n               # 強制讓 next_i 出界，代表找不到
                    break                    # 提前結束尋找
                
                # 【核心跳躍邏輯】
                # 既然第 next_i 天在等待 output[next_i] 天後才有更高溫
                # 那中途那些比 next_i 矮的溫度也必定比第 i 天矮，可以直接跳過不用看
                next_i = next_i + output[next_i]

            # 離開迴圈後，如果 next_i 沒有超出陣列範圍，說明成功找到了第一個更高溫的天數
            if next_i < n:
                output[i] = next_i - i       # 計算天數差並寫入答案

        return output
        # 時間複雜度 O(n): 平均而言，利用跳躍機制讓每個元素被訪問的次數為常數級別
        # 空間複雜度 O(1): 除了回傳必要的 output 之外，沒有使用任何額外的資料結構（如 stack）
