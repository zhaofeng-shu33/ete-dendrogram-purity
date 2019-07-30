import unittest

from ete3 import Tree

from dendrogram_purity import set_purity, lca, dendrogram_purity

class TestDendrogramPurity(unittest.TestCase):
    def test_set_purity(self):
        A = [1,2,3]
        B = [2,3,4]
        p = set_purity(A, B)
        self.assertAlmostEqual(p, 2/3.0)
        A = [0,1,2,3]
        B = [2,3]
        p = set_purity(A, B)
        self.assertAlmostEqual(p, 0.5)

    def test_lca(self):
        t = Tree('(((1,2),3),4);')
        node_list = lca(t, 1, 3)
        self.assertEqual(node_list, [1,2,3])
        
    def test_dendrogram_purity(self):        
        t = Tree('(((0,1),2),3);')
        p = dendrogram_purity(t, [[0,1], [2,3]])
        self.assertAlmostEqual(p, 0.75)
        t = Tree('((0,1),(2,3));')
        p = dendrogram_purity(t, [[0,1], [2,3]])
        self.assertAlmostEqual(p, 1)
        
if __name__ == '__main__':
    unittest.main()