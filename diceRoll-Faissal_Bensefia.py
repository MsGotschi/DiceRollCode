#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################LICENCE####################################
#Copyright (c) 2016 Faissal Bensefia
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
################################################################################
#Info:
# Date written:
#  20/09/2016
# Description:
#  A simple program that simulates a dice roll
import random

diceFaces = [
 "   \n"
 " ■ \n"
 "   \n",
 
 "■  \n"
 "   \n"
 "  ■\n",
 
 "■  \n"
 " ■ \n"
 "  ■\n",
 
 "■ ■\n"
 "   \n"
 "■ ■\n",
 
 "■ ■\n"
 " ■ \n"
 "■ ■\n",
 
 "■ ■\n"
 "■ ■\n"
 "■ ■\n"
]

#Clear the screen
print("\033[2J")
#Reset cursor, prompt for input.
while input("\033[1;1H🎲 Hit enter to roll [q to quit]:")[:1].lower()!="q":
	print(diceFaces[random.randrange(len(diceFaces))])
