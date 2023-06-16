# 1 Задание:

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.out_idx = 0
        self.in_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.out_idx >= len(self.list_of_list):
            raise StopIteration

        while self.in_idx >= len(self.list_of_list[self.out_idx]):
            self.out_idx += 1
            self.in_idx = 0

            if self.out_idx >= len(self.list_of_list):
                raise StopIteration

        item = self.list_of_list[self.out_idx][self.in_idx]
        self.in_idx += 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    test_1()

# 2 Задание:

import types


def flat_generator(list_of_lists):
    for list in list_of_lists:
        for l in list:
            yield l


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


# if __name__ == '__main__':
#     test_2()
