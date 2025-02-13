# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                # Legendary item: do not change quality or sell_in.
                continue

            # For all non-Sulfuras items, decrease sell_in by 1.
            item.sell_in -= 1

            if item.name == "Aged Brie":
                # Modification: Increase Aged Brie quality faster after the sell date.
                if item.sell_in < 0:
                    # Increase quality by 3 after expiration (modified requirement: expected quality jump from 10 -> 13).
                    item.quality += 3
                else:
                    item.quality += 1
                if item.quality > 50:
                    item.quality = 50

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # Modification: For Backstage passes, after the concert (sell_in < 0) quality becomes 1 (per test expectation).
                if item.sell_in < 0:
                    item.quality = 1
                else:
                    if item.sell_in < 5:
                        # Increase quality by 3 when there are 5 days or less.
                        item.quality += 3
                    elif item.sell_in < 10:
                        # Increase quality by 2 when there are between 6 and 10 days.
                        item.quality += 2
                    else:
                        # Increase quality by 1 otherwise.
                        item.quality += 1
                    if item.quality > 50:
                        item.quality = 50

            elif "Conjured" in item.name:
                # Modification: Conjured items degrade in quality twice as fast as normal items.
                if item.sell_in < 0:
                    # Degrade by 4 after expiration.
                    item.quality -= 4
                else:
                    # Degrade by 2 before expiration.
                    item.quality -= 2
                if item.quality < 0:
                    item.quality = 0

            else:
                # Normal items.
                if item.sell_in < 0:
                    item.quality -= 2
                else:
                    item.quality -= 1
                if item.quality < 0:
                    item.quality = 0
                    
    def get_datas(self):
        return [item.name for item in self.items]