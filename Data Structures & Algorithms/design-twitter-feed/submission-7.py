class Twitter:

    def __init__(self):
        self.follow = defaultdict(set)
        self.tweet = defaultdict(deque)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweet[userId].append((self.count, tweetId))

        if len(self.tweet[userId]) > 10:
            self.tweet[userId].popleft()

        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        min_heap = []

        self.follow[userId].add(userId)

        for user in self.follow[userId]:
            if self.tweet[user]:
                heapq.heappush(min_heap, (-self.tweet[user][-1], tweetId, user, len(self.tweet[user])-1))

        output = []

        while min_heap and len(output) < 10:
            _, tweetId, user, index = heapq.heappop(min_heap)
            output.append(tweetId)

            if index > 0:
                count, tweetId = self.tweet[user][index-1]
                heapq.heappush(min_heap, (-count, tweetId, user, index-1))

        return output

    def follow(self, followerId: int, followeeId: int):
        if followerId == followeeId:
            return

        self.follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        if followerId == followeeId or followeeId not in self.follow[followerId]:
            return

        self.follow[followerId].remove(followeeId)
    
    """
    题目：设计简化版 Twitter，支持：
         - postTweet(userId, tweetId)：发推
         - getNewsFeed(userId)：返回该用户及其关注的人最近的 10 条推文 ID（从新到旧）
         - follow / unfollow：关注 / 取关
    思路：
    - 每个用户的推文按发布顺序存进一个队列，带上全局时间戳
    - 获取动态时，相当于"合并 k 个有序链表"（LeetCode 23）：
      每个关注对象的推文列表都已经按时间有序，用堆每次取出最新的一条，取满 10 条为止
    - 时间戳用递减的负数（0, -1, -2, …），越新越小，
      这样 Python 的最小堆堆顶就是最新的推文，不用再取负

    复杂度（F 为关注人数）：
    - postTweet：O(1)
    - getNewsFeed：O(F log F)（建堆）+ O(10 log F)（取 10 条）
    - follow / unfollow：O(1)

    小提示：
    - 每个用户只保留最近 10 条推文是很好的优化：动态最多只要 10 条，
      更早的推文永远不可能出现在任何人的动态里，可以直接丢弃，内存也是 O(10) 每人。
    - 对 deque 用下标访问一般是 O(n)，但这里每个队列最多 10 个元素，可以视为 O(1)。
    - 堆中元素 (时间戳, 推文ID, 用户, 下标)：时间戳全局唯一，永远不会出现平局去比较后面的项。
    - 初始化堆可以先 append 再 heapify，建堆从 O(F log F) 降到 O(F)。
    - getNewsFeed 里把自己加入 follows，是为了让自己的推文也出现在动态里，
      并且 unfollow 已经禁止取关自己，所以这个改动是安全的；
      另一种写法是在遍历时用 self.follows[userId] | {userId}，不修改关注集合。
    - defaultdict 在"读取"不存在的 key 时也会创建空条目
      （如 self.tweets[user] 对没发过推的用户），不影响正确性，但会多占一点内存。
    - unfollow 可以简化成一行 self.follows[followerId].discard(followeeId)：
      discard 在元素不存在时不会报错；但仍需保留"不能取关自己"的判断。
    """

    def __init__(self):

        # 用户 → 他最近发的推文队列，元素为 (时间戳, 推文ID)，按发布时间从旧到新
        self.tweets = defaultdict(deque)

        # 用户 → 他关注的人的集合（set 使 follow / unfollow 都是 O(1)）
        self.follows = defaultdict(set)

        # 全局时间戳，每发一条推文减 1，越新的推文时间戳越小
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        # 新推文加到队尾
        self.tweets[userId].append((self.count, tweetId))

        # 只保留最近 10 条，超出就丢掉最旧的（队头）
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

        # 时间戳递减，保证下一条推文"更小"（更新）
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        news = []       # 结果，按从新到旧排列
        min_heap = []   # 元素为 (时间戳, 推文ID, 用户, 该推文在用户队列中的下标)

        # 自己的推文也要出现在动态里，所以把自己加入关注集合
        self.follows[userId].add(userId)

        # ---------- 第 1 步：每个关注对象的"最新一条推文"入堆 ----------
        # 类似合并 k 个有序链表时，先把每条链表的头节点放进堆
        for user in self.follows[userId]:
            if self.tweets[user]:
                # 队尾是该用户最新的推文
                index = len(self.tweets[user]) - 1
                count, tweetId = self.tweets[user][index]
                heapq.heappush(min_heap, (count, tweetId, user, index))

        # ---------- 第 2 步：每次取出全局最新的一条，再补入该用户的下一条 ----------
        while min_heap and len(news) < 10:
            # 堆顶时间戳最小 = 最新的推文
            _, tweetId, user, index = heapq.heappop(min_heap)

            news.append(tweetId)

            # 该用户还有更早的推文，把前一条（更旧的）放进堆
            if index > 0:
                count, tweetId = self.tweets[user][index-1]
                heapq.heappush(min_heap, (count, tweetId, user, index-1))

        return news

    def follow(self, followerId: int, followeeId: int) -> None:

        # 不能关注自己（自己的推文在 getNewsFeed 里单独处理）
        if followerId == followeeId:
            return

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # 不能取关自己（否则 getNewsFeed 里加入的自己会被移除，看不到自己的推文）；
        # 没关注过的人也无需处理（直接 remove 会抛 KeyError）
        if followerId == followeeId or followeeId not in self.follows[followerId]:
            return

        self.follows[followerId].remove(followeeId)