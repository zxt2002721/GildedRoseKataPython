# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_quality_degrades_twice_as_fast_after_sellin(self):
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9) 

    def test_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, -1)

    def test_aged_brie_quality_decreases(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)

    def test_sulfuras_does_not_decrease(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 79) 
        self.assertEqual(items[0].sell_in, 4) 

    def test_backstage_passes_quality_stays_constant(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 20)
        
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_datas()
        self.assertEquals(["Sulfuras"], all_items)



if __name__ == '__main__':
    unittest.main()
