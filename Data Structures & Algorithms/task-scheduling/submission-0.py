from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)

        # Optimal solution would prioritize doing the tasks with the most frequencies first
        # so we need to greedily complete the tasks with the highest frequency

        # use a max heap to decide which task is the one with the most frequencies, and a queue to decide when the task can be re-added to the max heap

        # Example: ['A', 'A', 'A', 'B', 'C'] => [3, 1, 1]
        # max_heap = [1, 1] (left most element is the max)
        # queue = [(2, 4), ()] (left most element is front of queue)
        # at t = 1, we do the task with 3
            # decrement to 2, and add (2, 4) to the queue, this task will only be avaible again when t > t_prev + n
        # at t = 2, we do the task with 1
            # since this task type is complete, we do not add to the queue
        # at t = 3, we do the task with 1
            # task is complete, so we do not add to the queue
        # since max_heap is empty, we jump straight to the first element available in the queue, which is at t = 5
            # readd 2 into the heap
        # at t = 5, we do the task with 2, add (1, 8) into the queue
        # since max heap is empty, we jump straight to the first element available in the queue, which is at t = 9
            # readd 1 into the heap
        # at t = 9, we do the task with 1
        # since both heap and queue are empty, we return t = 9

        heap = []
        queue = deque()

        for task_count in task_counter.values():
            heapq.heappush(heap, -task_count) # we add as negative to get a max heap

        # terminate before we increment the time
        cpu_cycles = 1
        while heap or queue:
            # check if the queue has any tasks that can be redone, pop and add to the heap
            if queue:
                task_count, avail_time = queue[-1]
                if cpu_cycles == avail_time:
                    heapq.heappush(heap, -queue.pop()[0])

            # jump to the next available task, if there are no tasks in the heap
            if not heap:
                cpu_cycles = queue[-1][1]
                continue

            # otherwise, take a task from the heap
            task_count = -heapq.heappop(heap)
            if task_count - 1 > 0:
                queue.appendleft((task_count - 1, cpu_cycles + n + 1))
            cpu_cycles += 1

        return cpu_cycles - 1


