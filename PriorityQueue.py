import heapq as hq

class PriorityQueue():
    """Class to store and implement a Priority Queue using a heap"""

    def __init__(self):
        self.queue = []
        self.entry_map = {}
        self.REMOVED = 'removed'

    def push_with_priority(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_map:
            self.remove_task(task)
        entry = [priority, task]
        self.entry_map[task] = entry
        hq.heappush(self.queue, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_map.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.queue:
            priority, task = hq.heappop(self.queue)
            if task is not self.REMOVED:
                del self.entry_map[task]
                return (priority, task)
        raise KeyError('pop from an empty priority queue')


