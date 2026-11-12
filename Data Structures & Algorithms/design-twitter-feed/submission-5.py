class Twitter:

    def __init__(self):
        
        self.tweets = defaultdict(deque)
        self.follows = defaultdict(set)

        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweets[userId].append((self.count, tweetId))
        
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        news = []
        min_heap = []

        self.follows[userId].add(userId)

        for user in self.follows[userId]:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                count, tweetId = self.tweets[user][index]
                heapq.heappush(min_heap, (count, tweetId, user, index))
        
        while min_heap and len(news) < 10:
            _, tweetId, user, index = heapq.heappop(min_heap)

            news.append(tweetId)

            if index > 0:
                count, tweetId = self.tweets[user][index-1]
                heapq.heappush(min_heap, (count, tweetId, user, index-1))
        
        return news
        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            return

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId or followeeId not in self.follows[followerId]:
            return

        self.follows[followerId].remove(followeeId)
