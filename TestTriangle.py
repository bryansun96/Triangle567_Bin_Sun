# -*- coding: utf-8 -*-
"""
Updated Feb 15, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Bin Sun
"""

import unittest

from Triangle import classifyTriangle    



class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(2,4,5),'Scalene','2,4,5 should be Scalene')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(1.1,1.1,1.1),'InvalidInput','1.1,1.1,1.1 should be InvalidInput')
    
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(1000,1000,1000),'InvalidInput','1000,1000,1000 should be InvalidInput')
    
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(201,150,150),'InvalidInput','201,105,105 should be InvalidInput')
    
    def testInvalidInputD(self): 
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 should be InvalidInput')
    
    def testInvalidInputE(self): 
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','-1,-1,-1 should be InvalidInput')
    
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')

    def testIsoceles(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')

    


if __name__ == '__main__':
    unittest.main()

