#!/usr/bin/env python3

'''
@author: Christian Wressnegger
'''

import sys
import unittest
import numpy as np
sys.path.append('.')


import ex08_testdata as testdata

try:
    from src.roc import ROC
except ImportError:
    pass

unittest.TestLoader.sortTestMethodsUsing = None
PYTHON = "python3"
PYERROR = "For running your solution we call '{}'.\nThe name might be different for your installation (e.g. on Windows)\n"
roc_obj = ROC()

class Ex08(unittest.TestCase):

    def test_00_tpr(self):
        for tup in testdata.TPR_test:
            self.assertTrue(np.isclose(tup[-1], roc_obj.calc_tpr(*tup[:3])))

    def test_01_fpr(self):
        for tup in testdata.FPR_test:
            self.assertTrue(np.isclose(tup[-1],roc_obj.calc_fpr(*tup[:3])))

    def test_02_auc(self):
        self.assertTrue(np.isclose(testdata.AUC_test[-1], roc_obj.calc_auc(testdata.y, testdata.y_hat), atol=1e-4))


if __name__ == "__main__":
    unittest.main()
