# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest 

from Triangle1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        return 'Passed'

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Right triangle')
        return 'Passed'

        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        return 'Passed'

    
    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(2,3,3),'Isosceles','1,1,1 should be Isosceles')
        return 'Passed'


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

