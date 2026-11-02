import heapq
class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append([self.time,tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.following.get(userId, set()))
        users.add(userId)
        feed = []
        for i in users:
            for time, t in self.tweets.get(i, []):
                heapq.heappush(feed, [time, t])
                if len(feed) > 10:
                    heapq.heappop(feed)

        res = []
        while feed:
            res.append(heapq.heappop(feed)[1])
        return res[::-1]

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
