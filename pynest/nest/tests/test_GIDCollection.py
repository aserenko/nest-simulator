# -*- coding: utf-8 -*-
#
# test_GIDCollection.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""
GIDCollections
"""

import unittest
import nest


@nest.check_stack
class GIDCollectionTestCase(unittest.TestCase):
    """Test GIDCollection."""

    def setUp(self):
        nest.ResetKernel()

    def test_GIDCollection_addition(self):
        """Addition of GIDCollections"""

        nodes_a = nest.Create("iaf_psc_alpha", 2)
        nodes_b = nest.Create("iaf_psc_alpha", 2)
        all_nodes = nodes_a + nodes_b
        all_nodes_list = [n for n in all_nodes]
        test_list = [1, 2, 3, 4]
        self.assertEqual(all_nodes_list, test_list)

    def test_GIDCollection_membership(self):
        """Membership in GIDCollections"""

        nodes = nest.Create("iaf_psc_alpha", 10)

        self.assertTrue(5 in nodes)
        self.assertTrue(10 in nodes)
        self.assertFalse(11 in nodes)

    def test_GIDCollection_slices(self):
        """Slices of GIDCollections"""

        nodes = nest.Create("iaf_psc_alpha", 50)
        nodes_slice_a = nodes[:20]
        slice_list = [i for i in nodes_slice_a]
        test_list = [i for i in range(1, 21)]
        self.assertEqual(slice_list, test_list)

    def test_GIDCollection_iteration(self):
        """Iteration of GIDCollections"""

        nodes = nest.Create("iaf_psc_alpha", 10)
        for i, gid in enumerate(nodes):
            self.assertEqual(i+1, gid)

    def test_GIDCollection_index(self):
        """Index of GIDCollections"""

        nodes = nest.Create("iaf_psc_alpha", 10)
        for i in range(10):
            self.assertEqual(i+1, nodes[i])

    def test_GIDCollection_equal(self):
        """Equality of two GIDCollections"""

        nodes_a = nest.Create("iaf_psc_alpha", 10)
        nodes_b = nodes_a

        for i in range(10):
            self.assertEqual(nodes_a[i], nodes_b[i])
        self.assertTrue(nodes_a == nodes_b)


def suite():
    suite = unittest.makeSuite(GIDCollectionTestCase, 'test')
    return suite


def run():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


if __name__ == "__main__":
    run()
