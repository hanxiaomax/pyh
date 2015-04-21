PyH by Emmanuel Turlay (turlay@cern.ch)
=======================================

PyH is a simple python module (pyh.py) that lets you 
generate html output in a convinient and intuitive manner.
For more instruction go to 
http://code.google.com/p/pyh

Installation
============
simply issue :

sudo ./setup.py install

Usage
=====
in your python script :

from pyh import *
see the online documentation for the rest at
http://code.google.com/p/pyh


在此基础上，进行了一些修改

- 修改了并添加了一些tag
- 正确处理unicode以便输出中文
- 添加了两个函数，从文件导入css,js代码段