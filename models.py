class BargeError(Exception): pass
class SectionEmptyError(BargeError): pass
class FuelMismatchError(BargeError): pass
class OverloadError(BargeError): pass
class SectionNotFoundError(BargeError): pass

class Node:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def push(self, fuel_type):
        new_node = Node(fuel_type)
        new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        if self.top_node is None:
            raise SectionEmptyError()
        fuel = self.top_node.fuel_type
        self.top_node = self.top_node.next
        self.size -= 1
        return fuel

    def peek(self):
        if self.top_node is None:
            return None
        return self.top_node.fuel_type

    def is_empty(self):
        return self.top_node is None

    def get_size(self):
        return self.size

class Barge:
    def __init__(self, count, max_boxes):
        if count < 1 or max_boxes < 1:
            raise ValueError()
        self.sections = [Stack() for _ in range(count)]
        self.max_total = max_boxes
        self.curr_total = 0
        self.max_reached = 0

    def get_count(self):
        return len(self.sections)

    def get_total(self):
        return self.curr_total

    def get_max(self):
        return self.max_reached

    def load(self, num, fuel):
        if num < 1 or num > len(self.sections):
            raise SectionNotFoundError()
        if self.curr_total >= self.max_total:
            raise OverloadError()

        self.sections[num - 1].push(fuel)
        self.curr_total += 1
        if self.curr_total > self.max_reached:
            self.max_reached = self.curr_total

    def unload(self, num, expected):
        if num < 1 or num > len(self.sections):
            raise SectionNotFoundError()

        actual = self.sections[num - 1].pop()
        self.curr_total -= 1
        if actual != expected:
            raise FuelMismatchError()

    def is_empty(self):
        return self.curr_total == 0
