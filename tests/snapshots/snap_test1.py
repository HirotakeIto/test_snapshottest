# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test1 iris_info'] = FileSnapshot('snap_test1/test1 iris_info.csv')

snapshots['test2 iris_info2'] = '''index,sepal_length,sepal_width,petal_length,petal_width
count,150.0,150.0,150.0,150.0
mean,5.843333333333334,3.0573333333333337,3.7580000000000005,1.1993333333333336
std,0.828066127977863,0.4358662849366982,1.7652982332594662,0.7622376689603465
min,4.3,2.0,1.0,0.1
25%,5.1,2.8,1.6,0.3
50%,5.8,3.0,4.35,1.3
75%,6.4,3.3,5.1,1.8
max,7.9,4.4,6.9,2.5
'''
