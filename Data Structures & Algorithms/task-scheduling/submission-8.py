class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        题目：CPU 执行任务，每个时间单位执行一个任务或者待命（idle）。
             相同种类的任务之间必须间隔至少 n 个时间单位，求完成所有任务的最短时间。
        思路：贪心 + 最大堆 + 冷却队列（模拟）
             每个时间单位，从"当前可执行"的任务里选剩余次数最多的那种来执行。
             为什么选最多的：剩余最多的任务最难安排（它需要的冷却间隔最多），
             越早开始执行它，越不容易在最后产生大量 idle。
             - 最大堆 count：存可执行任务的剩余次数（取负实现最大堆）
             - 冷却队列 cooling：存刚执行过、还在冷却中的任务 (剩余次数, 执行时刻 + n)
        例：tasks = ["A","A","A","B","B","B"], n = 2
            时刻：  0  1  2     3  4  5     6  7
            执行：  A  B  idle  A  B  idle  A  B   → 共 8

        小提示：
        - 冷却队列天然按"可再次执行的时刻"递增排列（每个时刻最多加入一个任务），
          所以只需要看队头，用 deque 即可，不需要第二个堆。
          同理每个时刻最多只有一个任务冷却结束，所以 if 而不是 while 也是对的。
        - 统计次数可以直接用 Counter(tasks)，比 defaultdict 手动计数更简洁。
        - 弹出冷却队列时第二个值用不上，可以写成 remain, _ = cooling.popleft()。
        - 这题有 O(n) 的数学解法，面试常被追问：
          设出现次数最多的任务出现 max_count 次，有 num_max 种任务都出现了 max_count 次，
          把最多的任务排成 max_count - 1 个"块"，每块长 n + 1，最后再补一行 num_max 个：
              A _ _ | A _ _ | A        （n = 2，max_count = 3）
              → (max_count - 1) * (n + 1) + num_max
          其他任务填进空位；如果空位不够填（任务种类很多），就完全不需要 idle，答案就是 len(tasks)。
          所以答案 = max(len(tasks), (max_count - 1) * (n + 1) + num_max)：
              counts = Counter(tasks).values()
              max_count = max(counts)
              num_max = sum(1 for c in counts if c == max_count)
              return max(len(tasks), (max_count - 1) * (n + 1) + num_max)
        """

        # ---------- 第 1 步：统计每种任务的次数 ----------
        count = defaultdict(int)

        for task in tasks:
            count[task] += 1

        # 只关心次数，不关心任务名；取负存入，实现最大堆
        count = [ -val for val in count.values() ]

        heapq.heapify(count)

        # 冷却队列，元素为 (剩余次数（负数）, 最后执行的时刻 + n)
        # 时刻 t 执行的任务，最早能在 t + n + 1 再次执行
        cooling = deque()

        cycles = 0   # 当前时刻，也是已经过去的时间单位数

        # ---------- 第 2 步：逐个时间单位模拟 ----------
        # 堆里还有可执行的任务，或者还有任务在冷却，都说明没做完
        while count or cooling:
            # 队头任务冷却结束：cycles > 执行时刻 + n，即 cycles >= 执行时刻 + n + 1
            # 放回堆中，这个时刻就可以被选中执行
            if cooling and cooling[0][1] < cycles:
                remain, times = cooling.popleft()
                heapq.heappush(count, remain)

            # 有可执行的任务：执行剩余次数最多的那个
            # 没有可执行的任务（全在冷却）：这个时刻 idle，什么都不做
            if count:
                # 存的是负数，执行一次后剩余次数减 1，对负数来说就是 +1
                remain = heapq.heappop(count) + 1

                # 还没执行完，进入冷却队列，记录本次执行时刻 + n
                if remain != 0:
                    cooling.append((remain, cycles + n))

            # 时间前进一个单位（执行任务或 idle 都算一个单位）
            cycles += 1

        return cycles