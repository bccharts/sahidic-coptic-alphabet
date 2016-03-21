# Class to create a graded list of items

import random
import math

class GradedList:
    item_list = []
    graded_list = []
    new_pool = []
    review_pool = []
    remaining_pool = []

    recent_size = 4
    top_size = 4
    remaining_limit = 4

    first_size = 3
    first_set = 6
    first_ratio = 1.0

    new_at_a_time = 4
    loop_set = 20
    loop_ratio = 0.5

    last_set = 30
    last_ratio = 0.5
    last_size = 6

    full_review_set = 160
    full_review_ratio = 0.0

    neglected_set = 60
    neglected_ratio = 0.8

    def __init__(self, item_list=None):
        """ Constructor, pass in list of items to use. """

        if item_list is not None:
            self.item_list = item_list

    def get_next(self, new_ratio=1.0):
        """ Get the next item for the graded list. """

        # Decide which pool to use
        selector = random.random()
        if selector < new_ratio:
            # Use new pool unless it's empty, then use review pool
            pool = self.new_pool if len(self.new_pool) > 0 else self.review_pool
        else:
            # Use review pool unless it's empty, then use new pool
            pool = self.review_pool if len(self.review_pool) > 0 else self.new_pool

        # Get a random item from the top 6 items in the list, making sure it's
        # not in the list of recent items
        top_items = pool[:self.top_size]
        recent_list = self.graded_list[-self.recent_size:] if len(self.graded_list) > 0 else ['']
        item = recent_list[-1]
        count = 0
        while item in recent_list:
            item_index = random.randint(0, len(top_items) - 1)
            item = pool[item_index]

            # If we do this too many times, just make sure it's not the same
            # as the last character
            count += 1
            if count >= 5:
                recent_list = [self.graded_list[-1]]

        # Now that we have the item, remove it from the list and add to the end
        # so that we don't use it again too soon
        pool.pop(item_index)
        pool.append(item)

        return item

    def add_items(self, new_ratio=1.0, num=10):
        """ Add num items to the graded list. """

        for x in range(0, num):
            # Get the next item
            self.graded_list.append(self.get_next(new_ratio=new_ratio))

    def count_items(self):
        # Now find the items that weren't reviewed as much and add them in more
        counts = {}
        for x in self.graded_list:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        return counts

    def make(self, item_list=None):
        """ Generate the graded list of items. """

        if item_list is not None:
            self.item_list = item_list

        # Clear things out so reuse actually works
        self.graded_list = []
        self.new_pool = []
        self.review_pool = []
        self.remaining_pool = []

        # Start out with a few (4) in the new pool
        self.new_pool = self.item_list[0:self.first_size]
        self.remaining_pool = self.item_list[self.first_size:]

        # Get the first set
        self.add_items(new_ratio=self.first_ratio, num=self.first_set)

        # Now progressively move through the list
        while len(self.remaining_pool) > 0:
            # Move the new pool items to the review pool
            self.review_pool += self.new_pool

            # Repopulate the new pool with the next set of items
            self.new_pool = self.remaining_pool[0:self.new_at_a_time]
            self.remaining_pool = self.remaining_pool[self.new_at_a_time:]

            # If there are less than remaining_limit remaining, add to the list
            # So we don't have a new pool of less than remaining_limit
            if len(self.remaining_pool) < self.remaining_limit:
                self.review_pool += self.remaining_pool
                self.remaining_pool = []

            self.add_items(new_ratio=self.loop_ratio, num=self.loop_set)

        # Focus extra on the end of the list (the last 6 items)
        self.new_pool = self.item_list[-self.last_size:]
        self.add_items(new_ratio=self.last_ratio, num=self.last_set)

        # Full review of everything
        self.new_pool = []
        self.add_items(new_ratio=self.full_review_ratio, num=self.full_review_set)

        # Now find the items that weren't reviewed as much and add them in more
        counts = self.count_items()

        self.new_pool = sorted(counts, key=lambda k: counts[k])[0:10]
        self.add_items(new_ratio=self.neglected_ratio, num=self.neglected_set)

        return self.graded_list
