class RecentCounter:

    queue = []

    def __init__(self):
        self.queue.clear()

    def ping(self, t: int) -> int:
        i = 0
        requests = 0
        self.queue.append(t)
        while i < len(self.queue):
            if t - 3000 <= self.queue[i]:
                requests += 1
            else:
                del self.queue[i]
                i -= 1
            i += 1
        return requests
