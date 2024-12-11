class Stone:
    def __init__(self, value, last):
        self.value = value
        self.next = None
        self.last = last

    def __str__(self):
        return f"Stone: {self.value}"


class StoneLinkedList:
    def __init__(self, stones):
        self.head = Stone(stones[0], None)
        self.last = self.head
        for s in stones[1:]:
            next = Stone(s, self.last)
            self.last.next = next
            self.last = next

    def __str__(self):
        s = ""
        cur = self.head
        while cur is not None:
            s += str(cur.value) + " "
            cur = cur.next
        return s

    def split(self, stone):
        len_stone_value = len(str(stone.value))
        left_digits = int(str(stone.value)[: len_stone_value // 2])
        right_digits = int(str(stone.value)[len_stone_value // 2 :])
        left = Stone(left_digits, stone.last)
        right = Stone(right_digits, left)
        left.next = right
        right.next = stone.next
        return left, right

    def do_blink(self):
        cur = self.head
        while cur is not None:
            # Case 1: Stone engraved with 0 -> 1
            if cur.value == 0:
                # print(f"Case 1: {cur}")
                cur.value = 1
                cur = cur.next
                continue

            # Case 2: Stone engraved with even number of digits -> split
            if len(str(cur.value)) % 2 == 0:
                left, right = self.split(cur)
                # print(f"Case 2: {cur} new: {left} {right}")
                if cur.last is not None:
                    cur.last.next = left
                else:
                    self.head = left
                if cur.next is not None:
                    cur.next.last = right
                cur = cur.next
                continue
            # Case 3: No other rule apply -> value * 2024
            # print(f"Case 3: {cur}")
            cur.value *= 2024
            cur = cur.next
            continue

    def get_count_stones(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count


with open("../input") as f:
    stones = list(map(int, f.read().strip().split("\n")[0].split(" ")))
    # print(stones)
    sll = StoneLinkedList(stones)
    # print(sll)
    for i in range(25):
        sll.do_blink()
    print(f"Result Part 1: {sll.get_count_stones()}")
