'''
Checks the per-image counts calculated by MulticlassSQL.
'''

import wx
import MulticlassSQL
import numpy
from DBConnect import *
from Properties import Properties
from DataModel import DataModel
from StringIO import StringIO


if __name__ == "__main__":
    from TrainingSet import TrainingSet
    from StringIO import StringIO
    import FastGentleBoostingMulticlass
    from DataGrid import DataGrid
    import wx

    app = wx.PySimpleApp()
    
    p = Properties.getInstance()
    db = DBConnect.getInstance()
    dm = DataModel.getInstance()
    
    testdata = [
                {'props'  : '../test_data/nirht_test.properties',
                 'ts'     : '../test_data/nirht_2class_test.txt',
                 'nRules' : 5,
                 'filter' : 'MAPs',
                 'vals'   : [[0L, 5L, 77, 0], [0L, 6L, 37, 0], [0L, 7L, 80, 0], [0L, 8L, 153, 1], [0L, 13L, 5, 0], [0L, 14L, 5, 0], [0L, 15L, 6, 0], [0L, 16L, 5, 0], [0L, 21L, 64, 3], [0L, 22L, 84, 6], [0L, 23L, 112, 7], [0L, 24L, 147, 10], [0L, 29L, 58, 5], [0L, 30L, 117, 3], [0L, 31L, 175, 6], [0L, 32L, 202, 6], [0L, 37L, 6, 0], [0L, 38L, 2, 1], [0L, 39L, 10, 0], [0L, 40L, 15, 0], [0L, 45L, 132, 9], [0L, 46L, 113, 4], [0L, 47L, 443, 24], [0L, 48L, 335, 10], [0L, 53L, 39, 4], [0L, 54L, 64, 3], [0L, 55L, 166, 7], [0L, 56L, 101, 3], [0L, 61L, 82, 7], [0L, 62L, 109, 11], [0L, 63L, 247, 16], [0L, 64L, 157, 8], [0L, 69L, 68, 4], [0L, 70L, 101, 13], [0L, 71L, 306, 35], [0L, 72L, 139, 20], [0L, 77L, 56, 1], [0L, 78L, 73, 5], [0L, 79L, 111, 4], [0L, 80L, 25, 1], [0L, 85L, 52, 11], [0L, 86L, 95, 20], [0L, 87L, 199, 37], [0L, 88L, 103, 16], [0L, 93L, 157, 2], [0L, 94L, 301, 10], [0L, 95L, 243, 20], [0L, 96L, 156, 5], [0L, 197L, 8, 0], [0L, 198L, 17, 3], [0L, 199L, 58, 2], [0L, 200L, 18, 0], [0L, 205L, 149, 5], [0L, 206L, 201, 13], [0L, 207L, 196, 7], [0L, 208L, 374, 21], [0L, 213L, 261, 9], [0L, 214L, 256, 11], [0L, 215L, 361, 17], [0L, 216L, 528, 23], [0L, 221L, 83, 5], [0L, 222L, 74, 2], [0L, 223L, 45, 8], [0L, 224L, 105, 2], [0L, 229L, 77, 6], [0L, 230L, 85, 5], [0L, 231L, 155, 15], [0L, 232L, 166, 24], [0L, 237L, 101, 3], [0L, 238L, 139, 1], [0L, 239L, 242, 21], [0L, 240L, 181, 8], [0L, 245L, 56, 8], [0L, 246L, 58, 0], [0L, 247L, 136, 1], [0L, 248L, 71, 3], [0L, 253L, 56, 0], [0L, 254L, 68, 0], [0L, 255L, 139, 7], [0L, 256L, 95, 9]]
                 },
                {'props'  : '../test_data/nirht_test.properties',
                 'ts'     : '../test_data/nirht_3class_test.txt',
                 'nRules' : 5,
                 'filter' : 'MAPs',
                 'vals'   : [[0L, 5L, 0, 77, 0], [0L, 6L, 0, 37, 0], [0L, 7L, 0, 80, 0], [0L, 8L, 1, 153, 0], [0L, 13L, 0, 5, 0], [0L, 14L, 0, 5, 0], [0L, 15L, 0, 6, 0], [0L, 16L, 0, 5, 0], [0L, 21L, 1, 65, 1], [0L, 22L, 3, 85, 2], [0L, 23L, 3, 114, 2], [0L, 24L, 11, 145, 1], [0L, 29L, 3, 59, 1], [0L, 30L, 2, 117, 1], [0L, 31L, 6, 175, 0], [0L, 32L, 2, 203, 3], [0L, 37L, 0, 6, 0], [0L, 38L, 1, 2, 0], [0L, 39L, 0, 10, 0], [0L, 40L, 0, 15, 0], [0L, 45L, 3, 132, 6], [0L, 46L, 2, 113, 2], [0L, 47L, 9, 444, 14], [0L, 48L, 5, 335, 5], [0L, 53L, 1, 40, 2], [0L, 54L, 1, 64, 2], [0L, 55L, 6, 166, 1], [0L, 56L, 1, 102, 1], [0L, 61L, 6, 81, 2], [0L, 62L, 7, 109, 4], [0L, 63L, 10, 248, 5], [0L, 64L, 7, 156, 2], [0L, 69L, 4, 68, 0], [0L, 70L, 6, 102, 6], [0L, 71L, 27, 306, 8], [0L, 72L, 15, 139, 5], [0L, 77L, 1, 56, 0], [0L, 78L, 4, 74, 0], [0L, 79L, 2, 112, 1], [0L, 80L, 1, 25, 0], [0L, 85L, 5, 53, 5], [0L, 86L, 14, 96, 5], [0L, 87L, 27, 199, 10], [0L, 88L, 11, 103, 5], [0L, 93L, 1, 157, 1], [0L, 94L, 6, 302, 3], [0L, 95L, 13, 242, 8], [0L, 96L, 3, 157, 1], [0L, 197L, 0, 8, 0], [0L, 198L, 2, 17, 1], [0L, 199L, 2, 58, 0], [0L, 200L, 0, 18, 0], [0L, 205L, 1, 150, 3], [0L, 206L, 8, 202, 4], [0L, 207L, 1, 199, 3], [0L, 208L, 17, 373, 5], [0L, 213L, 6, 261, 3], [0L, 214L, 6, 256, 5], [0L, 215L, 10, 361, 7], [0L, 216L, 17, 529, 5], [0L, 221L, 5, 82, 1], [0L, 222L, 1, 74, 1], [0L, 223L, 5, 45, 3], [0L, 224L, 3, 104, 0], [0L, 229L, 6, 76, 1], [0L, 230L, 4, 85, 1], [0L, 231L, 13, 156, 1], [0L, 232L, 15, 166, 9], [0L, 237L, 1, 102, 1], [0L, 238L, 1, 139, 0], [0L, 239L, 15, 243, 5], [0L, 240L, 5, 183, 1], [0L, 245L, 5, 57, 2], [0L, 246L, 0, 58, 0], [0L, 247L, 1, 136, 0], [0L, 248L, 1, 71, 2], [0L, 253L, 1, 55, 0], [0L, 254L, 0, 68, 0], [0L, 255L, 7, 139, 0], [0L, 256L, 3, 97, 4]]
                 },
                {'props'  : '../test_data/nirht_area_test.properties',
                 'ts'     : '../test_data/nirht_2class_test.txt',
                 'nRules' : 5,
                 'filter' : 'MAPs',
                 'vals'   : [[0L, 5L, 77, 0, 11966.0, 0.0], [0L, 6L, 37, 0, 6202.0, 0.0], [0L, 7L, 80, 0, 13530.0, 0.0], [0L, 8L, 153, 1, 23878.0, 194.0], [0L, 13L, 5, 0, 482.0, 0.0], [0L, 14L, 5, 0, 487.0, 0.0], [0L, 15L, 6, 0, 599.0, 0.0], [0L, 16L, 5, 0, 384.0, 0.0], [0L, 21L, 64, 3, 8749.0, 650.0], [0L, 22L, 84, 6, 9950.0, 897.0], [0L, 23L, 112, 7, 14401.0, 1530.0], [0L, 24L, 147, 10, 18174.0, 1885.0], [0L, 29L, 58, 5, 8033.0, 773.0], [0L, 30L, 117, 3, 15699.0, 307.0], [0L, 31L, 175, 6, 24165.0, 848.0], [0L, 32L, 202, 6, 28137.0, 906.0], [0L, 37L, 6, 0, 580.0, 0.0], [0L, 38L, 2, 1, 212.0, 134.0], [0L, 39L, 10, 0, 1118.0, 0.0], [0L, 40L, 15, 0, 1021.0, 0.0], [0L, 45L, 132, 9, 14159.0, 1183.0], [0L, 46L, 113, 4, 12974.0, 442.0], [0L, 47L, 443, 24, 49969.0, 3044.0], [0L, 48L, 335, 10, 36700.0, 1156.0], [0L, 53L, 39, 4, 4642.0, 381.0], [0L, 54L, 64, 3, 7130.0, 233.0], [0L, 55L, 166, 7, 18145.0, 982.0], [0L, 56L, 101, 3, 11114.0, 641.0], [0L, 61L, 82, 7, 10335.0, 842.0], [0L, 62L, 109, 11, 12948.0, 1210.0], [0L, 63L, 247, 16, 30129.0, 2510.0], [0L, 64L, 157, 8, 18761.0, 1058.0], [0L, 69L, 68, 4, 7085.0, 569.0], [0L, 70L, 101, 13, 10775.0, 1913.0], [0L, 71L, 306, 35, 31808.0, 5204.0], [0L, 72L, 139, 20, 15276.0, 2618.0], [0L, 77L, 56, 1, 8437.0, 272.0], [0L, 78L, 73, 5, 10765.0, 829.0], [0L, 79L, 111, 4, 17972.0, 714.0], [0L, 80L, 25, 1, 4103.0, 327.0], [0L, 85L, 52, 11, 6724.0, 1898.0], [0L, 86L, 95, 20, 13146.0, 3577.0], [0L, 87L, 199, 37, 28011.0, 6003.0], [0L, 88L, 103, 16, 14349.0, 2657.0], [0L, 93L, 157, 2, 17008.0, 252.0], [0L, 94L, 301, 10, 33214.0, 1527.0], [0L, 95L, 243, 20, 29356.0, 3237.0], [0L, 96L, 156, 5, 17710.0, 505.0], [0L, 197L, 8, 0, 1097.0, 0.0], [0L, 198L, 17, 3, 1858.0, 244.0], [0L, 199L, 58, 2, 6050.0, 248.0], [0L, 200L, 18, 0, 1697.0, 0.0], [0L, 205L, 149, 5, 14010.0, 585.0], [0L, 206L, 201, 13, 19544.0, 1475.0], [0L, 207L, 196, 7, 20297.0, 904.0], [0L, 208L, 374, 21, 38232.0, 2363.0], [0L, 213L, 261, 9, 32591.0, 1091.0], [0L, 214L, 256, 11, 29999.0, 1452.0], [0L, 215L, 361, 17, 45024.0, 2072.0], [0L, 216L, 528, 23, 62081.0, 3075.0], [0L, 221L, 83, 5, 9443.0, 489.0], [0L, 222L, 74, 2, 8244.0, 257.0], [0L, 223L, 45, 8, 4340.0, 690.0], [0L, 224L, 105, 2, 11838.0, 158.0], [0L, 229L, 77, 6, 11653.0, 1090.0], [0L, 230L, 85, 5, 12116.0, 1292.0], [0L, 231L, 155, 15, 23191.0, 3070.0], [0L, 232L, 166, 24, 25626.0, 4018.0], [0L, 237L, 101, 3, 11258.0, 416.0], [0L, 238L, 139, 1, 15288.0, 128.0], [0L, 239L, 242, 21, 29623.0, 2823.0], [0L, 240L, 181, 8, 21545.0, 1491.0], [0L, 245L, 56, 8, 6642.0, 883.0], [0L, 246L, 58, 0, 6796.0, 0.0], [0L, 247L, 136, 1, 15809.0, 114.0], [0L, 248L, 71, 3, 7926.0, 258.0], [0L, 253L, 56, 0, 9089.0, 0.0], [0L, 254L, 68, 0, 10564.0, 0.0], [0L, 255L, 139, 7, 20411.0, 1580.0], [0L, 256L, 95, 9, 14089.0, 1091.0]]
                 },
                {'props'  : '../test_data/nirht_area_test.properties',
                 'ts'     : '../test_data/nirht_3class_test.txt',
                 'nRules' : 5,
                 'filter' : 'MAPs',
                 'vals'   : [[0L, 5L, 0, 77, 0, 0.0, 11966.0, 0.0], [0L, 6L, 0, 37, 0, 0.0, 6202.0, 0.0], [0L, 7L, 0, 80, 0, 0.0, 13530.0, 0.0], [0L, 8L, 1, 153, 0, 194.0, 23878.0, 0.0], [0L, 13L, 0, 5, 0, 0.0, 482.0, 0.0], [0L, 14L, 0, 5, 0, 0.0, 487.0, 0.0], [0L, 15L, 0, 6, 0, 0.0, 599.0, 0.0], [0L, 16L, 0, 5, 0, 0.0, 384.0, 0.0], [0L, 21L, 1, 65, 1, 356.0, 8886.0, 157.0], [0L, 22L, 3, 85, 2, 421.0, 10080.0, 346.0], [0L, 23L, 3, 114, 2, 760.0, 14748.0, 423.0], [0L, 24L, 11, 145, 1, 1910.0, 18016.0, 133.0], [0L, 29L, 3, 59, 1, 403.0, 8257.0, 146.0], [0L, 30L, 2, 117, 1, 228.0, 15699.0, 79.0], [0L, 31L, 6, 175, 0, 848.0, 24165.0, 0.0], [0L, 32L, 2, 203, 3, 272.0, 28392.0, 379.0], [0L, 37L, 0, 6, 0, 0.0, 580.0, 0.0], [0L, 38L, 1, 2, 0, 134.0, 212.0, 0.0], [0L, 39L, 0, 10, 0, 0.0, 1118.0, 0.0], [0L, 40L, 0, 15, 0, 0.0, 1021.0, 0.0], [0L, 45L, 3, 132, 6, 311.0, 14168.0, 863.0], [0L, 46L, 2, 113, 2, 266.0, 12974.0, 176.0], [0L, 47L, 9, 444, 14, 980.0, 50124.0, 1909.0], [0L, 48L, 5, 335, 5, 502.0, 36714.0, 640.0], [0L, 53L, 1, 40, 2, 56.0, 4829.0, 138.0], [0L, 54L, 1, 64, 2, 68.0, 7130.0, 165.0], [0L, 55L, 6, 166, 1, 865.0, 18145.0, 117.0], [0L, 56L, 1, 102, 1, 262.0, 11367.0, 126.0], [0L, 61L, 6, 81, 2, 841.0, 10194.0, 142.0], [0L, 62L, 7, 109, 4, 849.0, 12948.0, 361.0], [0L, 63L, 10, 248, 5, 1735.0, 30204.0, 700.0], [0L, 64L, 7, 156, 2, 1008.0, 18643.0, 168.0], [0L, 69L, 4, 68, 0, 569.0, 7085.0, 0.0], [0L, 70L, 6, 102, 6, 814.0, 10993.0, 881.0], [0L, 71L, 27, 306, 8, 4096.0, 31808.0, 1108.0], [0L, 72L, 15, 139, 5, 2043.0, 15276.0, 575.0], [0L, 77L, 1, 56, 0, 272.0, 8437.0, 0.0], [0L, 78L, 4, 74, 0, 750.0, 10844.0, 0.0], [0L, 79L, 2, 112, 1, 261.0, 18319.0, 106.0], [0L, 80L, 1, 25, 0, 327.0, 4103.0, 0.0], [0L, 85L, 5, 53, 5, 1153.0, 6959.0, 510.0], [0L, 86L, 14, 96, 5, 2738.0, 13264.0, 721.0], [0L, 87L, 27, 199, 10, 4546.0, 28011.0, 1457.0], [0L, 88L, 11, 103, 5, 1896.0, 14349.0, 761.0], [0L, 93L, 1, 157, 1, 117.0, 17008.0, 135.0], [0L, 94L, 6, 302, 3, 880.0, 33531.0, 330.0], [0L, 95L, 13, 242, 8, 2557.0, 29039.0, 997.0], [0L, 96L, 3, 157, 1, 302.0, 17779.0, 134.0], [0L, 197L, 0, 8, 0, 0.0, 1097.0, 0.0], [0L, 198L, 2, 17, 1, 145.0, 1858.0, 99.0], [0L, 199L, 2, 58, 0, 248.0, 6050.0, 0.0], [0L, 200L, 0, 18, 0, 0.0, 1697.0, 0.0], [0L, 205L, 1, 150, 3, 110.0, 14122.0, 363.0], [0L, 206L, 8, 202, 4, 1073.0, 19662.0, 284.0], [0L, 207L, 1, 199, 3, 151.0, 20736.0, 314.0], [0L, 208L, 17, 373, 5, 2020.0, 38171.0, 404.0], [0L, 213L, 6, 261, 3, 783.0, 32591.0, 308.0], [0L, 214L, 6, 256, 5, 818.0, 29999.0, 634.0], [0L, 215L, 10, 361, 7, 1332.0, 45024.0, 740.0], [0L, 216L, 17, 529, 5, 2422.0, 62255.0, 479.0], [0L, 221L, 5, 82, 1, 544.0, 9318.0, 70.0], [0L, 222L, 1, 74, 1, 131.0, 8244.0, 126.0], [0L, 223L, 5, 45, 3, 453.0, 4340.0, 237.0], [0L, 224L, 3, 104, 0, 222.0, 11774.0, 0.0], [0L, 229L, 6, 76, 1, 1141.0, 11498.0, 104.0], [0L, 230L, 4, 85, 1, 991.0, 12116.0, 301.0], [0L, 231L, 13, 156, 1, 2856.0, 23260.0, 145.0], [0L, 232L, 15, 166, 9, 2192.0, 25686.0, 1766.0], [0L, 237L, 1, 102, 1, 160.0, 11405.0, 109.0], [0L, 238L, 1, 139, 0, 128.0, 15288.0, 0.0], [0L, 239L, 15, 243, 5, 2110.0, 29716.0, 620.0], [0L, 240L, 5, 183, 1, 991.0, 21901.0, 144.0], [0L, 245L, 5, 57, 2, 620.0, 6708.0, 197.0], [0L, 246L, 0, 58, 0, 0.0, 6796.0, 0.0], [0L, 247L, 1, 136, 0, 114.0, 15809.0, 0.0], [0L, 248L, 1, 71, 2, 73.0, 7926.0, 185.0], [0L, 253L, 1, 55, 0, 119.0, 8970.0, 0.0], [0L, 254L, 0, 68, 0, 0.0, 10564.0, 0.0], [0L, 255L, 7, 139, 0, 1530.0, 20461.0, 0.0], [0L, 256L, 3, 97, 4, 321.0, 14273.0, 586.0]]
                 },
                {'props'  : '../test_data/nirht_area_test.properties',
                 'ts'     : '../test_data/nirht_3class_test.txt',
                 'nRules' : 5,
                 'filter' : None,
                 'vals'   : [[0L, 1L, 8, 85, 1, 1178.0, 10364.0, 169.0], [0L, 2L, 5, 67, 5, 760.0, 7983.0, 740.0], [0L, 3L, 1, 61, 1, 252.0, 7939.0, 59.0], [0L, 4L, 8, 121, 3, 1307.0, 15920.0, 542.0], [0L, 5L, 0, 77, 0, 0.0, 11966.0, 0.0], [0L, 6L, 0, 37, 0, 0.0, 6202.0, 0.0], [0L, 7L, 0, 80, 0, 0.0, 13530.0, 0.0], [0L, 8L, 1, 153, 0, 194.0, 23878.0, 0.0], [0L, 9L, 3, 282, 4, 313.0, 36364.0, 550.0], [0L, 10L, 0, 104, 2, 0.0, 13969.0, 243.0], [0L, 11L, 11, 163, 5, 990.0, 22712.0, 576.0], [0L, 12L, 9, 389, 6, 872.0, 49303.0, 519.0], [0L, 13L, 0, 5, 0, 0.0, 482.0, 0.0], [0L, 14L, 0, 5, 0, 0.0, 487.0, 0.0], [0L, 15L, 0, 6, 0, 0.0, 599.0, 0.0], [0L, 16L, 0, 5, 0, 0.0, 384.0, 0.0], [0L, 17L, 2, 63, 1, 356.0, 7487.0, 116.0], [0L, 18L, 3, 89, 0, 610.0, 11033.0, 0.0], [0L, 19L, 3, 141, 4, 607.0, 18314.0, 637.0], [0L, 20L, 1, 109, 1, 133.0, 14548.0, 57.0], [0L, 21L, 1, 65, 1, 356.0, 8886.0, 157.0], [0L, 22L, 3, 85, 2, 421.0, 10080.0, 346.0], [0L, 23L, 3, 114, 2, 760.0, 14748.0, 423.0], [0L, 24L, 11, 145, 1, 1910.0, 18016.0, 133.0], [0L, 25L, 0, 65, 0, 0.0, 12036.0, 0.0], [0L, 26L, 1, 87, 1, 140.0, 15658.0, 63.0], [0L, 27L, 2, 192, 1, 147.0, 33481.0, 135.0], [0L, 28L, 1, 120, 0, 66.0, 20957.0, 0.0], [0L, 29L, 3, 59, 1, 403.0, 8257.0, 146.0], [0L, 30L, 2, 117, 1, 228.0, 15699.0, 79.0], [0L, 31L, 6, 175, 0, 848.0, 24165.0, 0.0], [0L, 32L, 2, 203, 3, 272.0, 28392.0, 379.0], [0L, 33L, 0, 70, 0, 0.0, 7209.0, 0.0], [0L, 34L, 1, 67, 2, 219.0, 7844.0, 92.0], [0L, 35L, 0, 111, 0, 0.0, 11320.0, 0.0], [0L, 36L, 0, 105, 1, 0.0, 10942.0, 123.0], [0L, 37L, 0, 6, 0, 0.0, 580.0, 0.0], [0L, 38L, 1, 2, 0, 134.0, 212.0, 0.0], [0L, 39L, 0, 10, 0, 0.0, 1118.0, 0.0], [0L, 40L, 0, 15, 0, 0.0, 1021.0, 0.0], [0L, 41L, 0, 39, 0, 0.0, 6636.0, 0.0], [0L, 42L, 0, 31, 0, 0.0, 5828.0, 0.0], [0L, 43L, 2, 123, 0, 518.0, 23398.0, 0.0], [0L, 44L, 2, 94, 0, 233.0, 18429.0, 0.0], [0L, 45L, 3, 132, 6, 311.0, 14168.0, 863.0], [0L, 46L, 2, 113, 2, 266.0, 12974.0, 176.0], [0L, 47L, 9, 444, 14, 980.0, 50124.0, 1909.0], [0L, 48L, 5, 335, 5, 502.0, 36714.0, 640.0], [0L, 49L, 0, 63, 1, 0.0, 8047.0, 131.0], [0L, 50L, 2, 117, 3, 229.0, 14610.0, 315.0], [0L, 51L, 12, 250, 2, 1692.0, 33327.0, 270.0], [0L, 52L, 10, 165, 2, 1202.0, 20085.0, 165.0], [0L, 53L, 1, 40, 2, 56.0, 4829.0, 138.0], [0L, 54L, 1, 64, 2, 68.0, 7130.0, 165.0], [0L, 55L, 6, 166, 1, 865.0, 18145.0, 117.0], [0L, 56L, 1, 102, 1, 262.0, 11367.0, 126.0], [0L, 57L, 0, 84, 1, 0.0, 14617.0, 129.0], [0L, 58L, 2, 163, 1, 380.0, 25243.0, 47.0], [0L, 59L, 7, 363, 1, 1174.0, 52896.0, 145.0], [0L, 60L, 8, 228, 1, 1607.0, 34699.0, 68.0], [0L, 61L, 6, 81, 2, 841.0, 10194.0, 142.0], [0L, 62L, 7, 109, 4, 849.0, 12948.0, 361.0], [0L, 63L, 10, 248, 5, 1735.0, 30204.0, 700.0], [0L, 64L, 7, 156, 2, 1008.0, 18643.0, 168.0], [0L, 65L, 0, 20, 0, 0.0, 2780.0, 0.0], [0L, 66L, 3, 163, 1, 277.0, 21814.0, 139.0], [0L, 67L, 2, 295, 1, 316.0, 38912.0, 208.0], [0L, 68L, 4, 206, 0, 597.0, 28293.0, 0.0], [0L, 69L, 4, 68, 0, 569.0, 7085.0, 0.0], [0L, 70L, 6, 102, 6, 814.0, 10993.0, 881.0], [0L, 71L, 27, 306, 8, 4096.0, 31808.0, 1108.0], [0L, 72L, 15, 139, 5, 2043.0, 15276.0, 575.0], [0L, 73L, 0, 6, 0, 0.0, 638.0, 0.0], [0L, 74L, 0, 2, 0, 0.0, 77.0, 0.0], [0L, 75L, 0, 5, 0, 0.0, 478.0, 0.0], [0L, 76L, 0, 8, 0, 0.0, 840.0, 0.0], [0L, 77L, 1, 56, 0, 272.0, 8437.0, 0.0], [0L, 78L, 4, 74, 0, 750.0, 10844.0, 0.0], [0L, 79L, 2, 112, 1, 261.0, 18319.0, 106.0], [0L, 80L, 1, 25, 0, 327.0, 4103.0, 0.0], [0L, 81L, 5, 40, 0, 1024.0, 4468.0, 0.0], [0L, 82L, 10, 90, 4, 2188.0, 11493.0, 574.0], 
                             [0L, 83L, 18, 170, 7, 3168.0, 20857.0, 1257.0], [0L, 84L, 7, 75, 5, 1279.0, 9546.0, 1039.0], [0L, 85L, 5, 53, 5, 1153.0, 6959.0, 510.0], [0L, 86L, 14, 96, 5, 2738.0, 13264.0, 721.0], [0L, 87L, 27, 199, 10, 4546.0, 28011.0, 1457.0], [0L, 88L, 11, 103, 5, 1896.0, 14349.0, 761.0], [0L, 89L, 3, 47, 1, 555.0, 5577.0, 80.0], [0L, 90L, 6, 159, 0, 1097.0, 18220.0, 0.0], [0L, 91L, 4, 189, 0, 813.0, 21014.0, 0.0], [0L, 92L, 2, 176, 0, 397.0, 19995.0, 0.0], [0L, 93L, 1, 157, 1, 117.0, 17008.0, 135.0], [0L, 94L, 6, 302, 3, 880.0, 33531.0, 330.0], [0L, 95L, 13, 242, 8, 2557.0, 29039.0, 997.0], [0L, 96L, 3, 157, 1, 302.0, 17779.0, 134.0], [0L, 97L, 2, 106, 5, 245.0, 13010.0, 764.0], [0L, 98L, 3, 53, 4, 487.0, 6770.0, 640.0], [0L, 99L, 3, 36, 1, 383.0, 4651.0, 106.0], [0L, 100L, 9, 114, 6, 2214.0, 14315.0, 821.0], [0L, 101L, 2, 72, 0, 299.0, 11617.0, 0.0], [0L, 102L, 0, 43, 1, 0.0, 6163.0, 310.0], [0L, 103L, 7, 112, 0, 1154.0, 17438.0, 0.0], [0L, 104L, 8, 208, 8, 1721.0, 34005.0, 1334.0], [0L, 105L, 3, 71, 1, 584.0, 13060.0, 107.0], [0L, 106L, 0, 61, 1, 0.0, 11124.0, 274.0], [0L, 107L, 2, 54, 0, 264.0, 10108.0, 0.0], [0L, 108L, 4, 150, 0, 619.0, 26143.0, 0.0], [0L, 109L, 8, 39, 1, 1616.0, 5875.0, 152.0], [0L, 110L, 4, 43, 3, 951.0, 6645.0, 321.0], [0L, 111L, 7, 48, 1, 1274.0, 8515.0, 141.0], [0L, 112L, 10, 65, 1, 1829.0, 10524.0, 89.0], [0L, 113L, 12, 78, 3, 1436.0, 8770.0, 303.0], [0L, 114L, 4, 66, 2, 480.0, 6713.0, 167.0], [0L, 115L, 4, 131, 2, 519.0, 14619.0, 226.0], [0L, 116L, 3, 185, 1, 307.0, 19979.0, 97.0], [0L, 117L, 0, 46, 0, 0.0, 6619.0, 0.0], [0L, 118L, 1, 40, 0, 184.0, 6300.0, 0.0], [0L, 119L, 2, 79, 0, 301.0, 9926.0, 0.0], [0L, 120L, 1, 145, 0, 136.0, 18844.0, 0.0], [0L, 121L, 1, 50, 0, 434.0, 7897.0, 0.0], [0L, 122L, 1, 43, 0, 136.0, 6963.0, 0.0], [0L, 123L, 4, 86, 4, 850.0, 11618.0, 635.0], [0L, 124L, 2, 89, 1, 596.0, 14667.0, 153.0], [0L, 125L, 2, 83, 1, 412.0, 9834.0, 124.0], [0L, 126L, 9, 71, 2, 1446.0, 9839.0, 331.0], [0L, 127L, 4, 178, 0, 482.0, 25302.0, 0.0], [0L, 128L, 11, 209, 4, 1282.0, 28285.0, 645.0], [0L, 129L, 2, 60, 1, 287.0, 10026.0, 105.0], [0L, 130L, 1, 64, 1, 131.0, 9602.0, 106.0], [0L, 131L, 7, 268, 2, 1593.0, 40303.0, 369.0], [0L, 132L, 9, 177, 4, 1308.0, 26526.0, 433.0], [0L, 133L, 2, 79, 2, 463.0, 11385.0, 303.0], [0L, 134L, 3, 63, 1, 1253.0, 9950.0, 238.0], [0L, 135L, 7, 184, 2, 1352.0, 26223.0, 574.0], [0L, 136L, 12, 202, 6, 2328.0, 27666.0, 891.0], [0L, 137L, 0, 28, 0, 0.0, 4195.0, 0.0], [0L, 138L, 1, 35, 0, 323.0, 5123.0, 0.0], [0L, 139L, 4, 172, 1, 549.0, 23300.0, 140.0], [0L, 140L, 6, 91, 2, 1065.0, 13990.0, 273.0], [0L, 141L, 11, 133, 9, 1818.0, 18587.0, 1107.0], [0L, 142L, 4, 123, 1, 583.0, 15178.0, 119.0], [0L, 143L, 21, 268, 8, 2995.0, 36993.0, 1020.0], [0L, 144L, 7, 163, 3, 906.0, 22127.0, 280.0], [0L, 145L, 1, 56, 0, 161.0, 7194.0, 0.0], [0L, 146L, 0, 80, 2, 0.0, 10018.0, 298.0], [0L, 147L, 4, 261, 1, 603.0, 33463.0, 195.0], [0L, 148L, 8, 274, 0, 1442.0, 36721.0, 0.0], [0L, 149L, 2, 46, 0, 255.0, 6381.0, 0.0], [0L, 150L, 0, 48, 0, 0.0, 5875.0, 0.0], [0L, 151L, 0, 125, 0, 0.0, 15904.0, 0.0], [0L, 152L, 0, 73, 0, 0.0, 9570.0, 0.0], [0L, 153L, 1, 35, 2, 220.0, 5435.0, 263.0], [0L, 154L, 3, 66, 0, 429.0, 9316.0, 0.0], [0L, 155L, 13, 144, 6, 1838.0, 22631.0, 688.0], [0L, 156L, 13, 132, 13, 2276.0, 18655.0, 2131.0], [0L, 157L, 3, 214, 3, 402.0, 27039.0, 418.0], [0L, 158L, 2, 178, 3, 254.0, 23910.0, 456.0], [0L, 159L, 28, 469, 23, 3169.0, 62505.0, 2167.0], [0L, 160L, 13, 283, 13, 2039.0, 37280.0, 1327.0], 
                             [0L, 161L, 2, 44, 0, 259.0, 6489.0, 0.0], [0L, 162L, 0, 57, 0, 0.0, 8105.0, 0.0], [0L, 163L, 3, 211, 2, 645.0, 30181.0, 293.0], [0L, 164L, 3, 116, 1, 543.0, 17087.0, 107.0], [0L, 165L, 0, 12, 0, 0.0, 1390.0, 0.0], [0L, 166L, 0, 32, 0, 0.0, 3587.0, 0.0], [0L, 167L, 0, 56, 2, 0.0, 6782.0, 140.0], [0L, 168L, 0, 28, 0, 0.0, 3578.0, 0.0], [0L, 169L, 12, 55, 4, 1553.0, 6239.0, 447.0], [0L, 170L, 7, 31, 6, 945.0, 3882.0, 732.0], [0L, 171L, 42, 187, 9, 6406.0, 22064.0, 1547.0], [0L, 172L, 37, 137, 6, 4976.0, 16173.0, 632.0], [0L, 173L, 2, 14, 1, 488.0, 2326.0, 116.0], [0L, 174L, 1, 13, 0, 138.0, 1830.0, 0.0], [0L, 175L, 3, 39, 2, 416.0, 5140.0, 330.0], [0L, 176L, 2, 19, 1, 249.0, 2823.0, 132.0], [0L, 177L, 0, 18, 0, 0.0, 3064.0, 0.0], [0L, 178L, 4, 65, 0, 571.0, 9731.0, 0.0], [0L, 179L, 2, 88, 0, 243.0, 13670.0, 0.0], [0L, 180L, 2, 70, 0, 277.0, 11240.0, 0.0], [0L, 181L, 2, 9, 0, 144.0, 923.0, 0.0], [0L, 182L, 0, 7, 0, 0.0, 609.0, 0.0], [0L, 183L, 0, 3, 0, 0.0, 295.0, 0.0], [0L, 184L, 0, 6, 0, 0.0, 512.0, 0.0], [0L, 185L, 0, 1, 0, 0.0, 100.0, 0.0], [0L, 186L, 0, 4, 0, 0.0, 458.0, 0.0], [0L, 187L, 0, 9, 0, 0.0, 893.0, 0.0], [0L, 188L, 0, 3, 0, 0.0, 269.0, 0.0], [0L, 189L, 1, 51, 2, 91.0, 8474.0, 242.0], [0L, 190L, 4, 153, 2, 939.0, 25957.0, 326.0], [0L, 191L, 2, 88, 0, 372.0, 14832.0, 0.0], [0L, 192L, 3, 17, 0, 473.0, 2828.0, 0.0], [0L, 193L, 7, 192, 3, 1258.0, 26291.0, 589.0], [0L, 194L, 1, 72, 0, 162.0, 9348.0, 0.0], [0L, 195L, 3, 108, 3, 677.0, 14997.0, 405.0], [0L, 196L, 2, 130, 1, 445.0, 16792.0, 147.0], [0L, 197L, 0, 8, 0, 0.0, 1097.0, 0.0], [0L, 198L, 2, 17, 1, 145.0, 1858.0, 99.0], [0L, 199L, 2, 58, 0, 248.0, 6050.0, 0.0], [0L, 200L, 0, 18, 0, 0.0, 1697.0, 0.0], [0L, 201L, 5, 140, 2, 609.0, 19073.0, 251.0], [0L, 202L, 1, 69, 1, 146.0, 11486.0, 168.0], [0L, 203L, 4, 120, 4, 1011.0, 17958.0, 453.0], [0L, 204L, 11, 178, 1, 1790.0, 23628.0, 156.0], [0L, 205L, 1, 150, 3, 110.0, 14122.0, 363.0], [0L, 206L, 8, 202, 4, 1073.0, 19662.0, 284.0], [0L, 207L, 1, 199, 3, 151.0, 20736.0, 314.0], [0L, 208L, 17, 373, 5, 2020.0, 38171.0, 404.0], [0L, 209L, 1, 51, 0, 146.0, 6163.0, 0.0], [0L, 210L, 1, 58, 0, 221.0, 7157.0, 0.0], [0L, 211L, 1, 56, 0, 167.0, 6983.0, 0.0], [0L, 212L, 1, 73, 2, 149.0, 9048.0, 269.0], [0L, 213L, 6, 261, 3, 783.0, 32591.0, 308.0], [0L, 214L, 6, 256, 5, 818.0, 29999.0, 634.0], [0L, 215L, 10, 361, 7, 1332.0, 45024.0, 740.0], [0L, 216L, 17, 529, 5, 2422.0, 62255.0, 479.0], [0L, 217L, 0, 5, 0, 0.0, 361.0, 0.0], [0L, 218L, 0, 4, 0, 0.0, 268.0, 0.0], [0L, 219L, 0, 5, 0, 0.0, 470.0, 0.0], [0L, 220L, 0, 3, 0, 0.0, 339.0, 0.0], [0L, 221L, 5, 82, 1, 544.0, 9318.0, 70.0], [0L, 222L, 1, 74, 1, 131.0, 8244.0, 126.0], [0L, 223L, 5, 45, 3, 453.0, 4340.0, 237.0], [0L, 224L, 3, 104, 0, 222.0, 11774.0, 0.0], [0L, 225L, 3, 56, 2, 729.0, 9358.0, 604.0], [0L, 226L, 4, 60, 2, 894.0, 8604.0, 373.0], [0L, 227L, 11, 204, 6, 1947.0, 30534.0, 996.0], [0L, 228L, 5, 147, 2, 900.0, 24627.0, 310.0], [0L, 229L, 6, 76, 1, 1141.0, 11498.0, 104.0], [0L, 230L, 4, 85, 1, 991.0, 12116.0, 301.0], [0L, 231L, 13, 156, 1, 2856.0, 23260.0, 145.0], [0L, 232L, 15, 166, 9, 2192.0, 25686.0, 1766.0], [0L, 233L, 1, 112, 0, 194.0, 13601.0, 0.0], [0L, 234L, 2, 89, 1, 295.0, 11833.0, 122.0], [0L, 235L, 4, 144, 1, 495.0, 19062.0, 118.0], [0L, 236L, 4, 279, 3, 461.0, 36459.0, 295.0], [0L, 237L, 1, 102, 1, 160.0, 11405.0, 109.0], [0L, 238L, 1, 139, 0, 128.0, 15288.0, 0.0], [0L, 239L, 15, 243, 5, 2110.0, 29716.0, 620.0], [0L, 240L, 5, 183, 1, 991.0, 21901.0, 144.0], 
                             [0L, 241L, 3, 115, 0, 479.0, 14982.0, 0.0], [0L, 242L, 6, 111, 1, 1008.0, 15150.0, 118.0], [0L, 243L, 13, 314, 1, 2034.0, 41613.0, 133.0], [0L, 244L, 20, 240, 5, 2924.0, 32015.0, 636.0], [0L, 245L, 5, 57, 2, 620.0, 6708.0, 197.0], [0L, 246L, 0, 58, 0, 0.0, 6796.0, 0.0], [0L, 247L, 1, 136, 0, 114.0, 15809.0, 0.0], [0L, 248L, 1, 71, 2, 73.0, 7926.0, 185.0], [0L, 249L, 0, 41, 0, 0.0, 5530.0, 0.0], [0L, 250L, 0, 26, 0, 0.0, 3890.0, 0.0], [0L, 251L, 1, 66, 0, 128.0, 9559.0, 0.0], [0L, 252L, 1, 54, 1, 123.0, 8715.0, 146.0], [0L, 253L, 1, 55, 0, 119.0, 8970.0, 0.0], [0L, 254L, 0, 68, 0, 0.0, 10564.0, 0.0], [0L, 255L, 7, 139, 0, 1530.0, 20461.0, 0.0], [0L, 256L, 3, 97, 4, 321.0, 14273.0, 586.0], [0L, 257L, 2, 120, 5, 254.0, 13433.0, 952.0], [0L, 258L, 2, 255, 2, 254.0, 30364.0, 390.0], [0L, 259L, 8, 459, 7, 943.0, 55175.0, 1011.0], [0L, 260L, 6, 219, 6, 1014.0, 27235.0, 738.0], [0L, 261L, 0, 39, 1, 0.0, 6972.0, 151.0], [0L, 262L, 0, 54, 0, 0.0, 9133.0, 0.0], [0L, 263L, 2, 110, 1, 506.0, 18175.0, 117.0], [0L, 264L, 0, 82, 1, 0.0, 14407.0, 140.0], [0L, 265L, 5, 65, 3, 608.0, 7953.0, 414.0], [0L, 266L, 3, 161, 2, 422.0, 18029.0, 258.0], [0L, 267L, 7, 294, 5, 1018.0, 30883.0, 629.0], [0L, 268L, 2, 121, 3, 393.0, 13335.0, 267.0], [0L, 269L, 5, 32, 0, 822.0, 3610.0, 0.0], [0L, 270L, 1, 40, 0, 128.0, 4571.0, 0.0], [0L, 271L, 8, 93, 1, 1319.0, 11748.0, 106.0], [0L, 272L, 1, 30, 0, 85.0, 4074.0, 0.0], [0L, 273L, 0, 8, 0, 0.0, 823.0, 0.0], [0L, 274L, 0, 8, 0, 0.0, 865.0, 0.0], [0L, 275L, 1, 14, 0, 137.0, 1493.0, 0.0], [0L, 276L, 0, 14, 0, 0.0, 1028.0, 0.0], [0L, 277L, 0, 50, 2, 0.0, 7864.0, 252.0], [0L, 278L, 1, 199, 1, 120.0, 29395.0, 461.0], [0L, 279L, 1, 202, 2, 77.0, 29365.0, 193.0], [0L, 280L, 0, 68, 0, 0.0, 10449.0, 0.0], [0L, 281L, 2, 65, 1, 321.0, 11111.0, 135.0], [0L, 282L, 0, 65, 0, 0.0, 10720.0, 0.0], [0L, 283L, 3, 74, 0, 470.0, 14163.0, 0.0], [0L, 284L, 0, 39, 1, 0.0, 6693.0, 133.0], [0L, 285L, 4, 40, 0, 358.0, 6351.0, 0.0], [0L, 286L, 5, 231, 2, 583.0, 32524.0, 143.0], [0L, 287L, 3, 129, 1, 192.0, 18070.0, 109.0], [0L, 288L, 0, 64, 0, 0.0, 7966.0, 0.0], [0L, 289L, 6, 89, 1, 974.0, 9927.0, 75.0], [0L, 290L, 1, 44, 2, 190.0, 5169.0, 237.0], [0L, 291L, 2, 85, 0, 394.0, 10162.0, 0.0], [0L, 292L, 2, 97, 1, 343.0, 10964.0, 110.0], [0L, 293L, 1, 84, 0, 100.0, 9407.0, 0.0], [0L, 294L, 3, 52, 0, 340.0, 6155.0, 0.0], [0L, 295L, 3, 43, 0, 336.0, 4924.0, 0.0], [0L, 296L, 2, 125, 4, 292.0, 14331.0, 390.0], [0L, 297L, 4, 77, 6, 689.0, 9406.0, 749.0], [0L, 298L, 1, 62, 1, 158.0, 7124.0, 154.0], [0L, 299L, 1, 49, 0, 130.0, 6333.0, 0.0], [0L, 300L, 1, 114, 6, 140.0, 13042.0, 1112.0], [0L, 301L, 0, 100, 0, 0.0, 15053.0, 0.0], [0L, 302L, 3, 69, 0, 723.0, 10934.0, 0.0], [0L, 303L, 1, 88, 0, 130.0, 12184.0, 0.0], [0L, 304L, 0, 131, 0, 0.0, 18683.0, 0.0], [0L, 305L, 2, 108, 4, 274.0, 14924.0, 594.0], [0L, 306L, 7, 157, 5, 769.0, 19704.0, 732.0], [0L, 307L, 6, 148, 3, 1047.0, 20263.0, 462.0], [0L, 308L, 12, 130, 3, 2021.0, 15369.0, 499.0], [0L, 309L, 26, 484, 12, 2344.0, 46270.0, 1195.0], [0L, 310L, 10, 329, 5, 1333.0, 32157.0, 636.0], [0L, 311L, 3, 326, 7, 402.0, 31894.0, 845.0], [0L, 312L, 3, 279, 3, 421.0, 27346.0, 292.0], [0L, 313L, 0, 9, 0, 0.0, 844.0, 0.0], [0L, 314L, 0, 12, 0, 0.0, 983.0, 0.0], [0L, 315L, 0, 6, 0, 0.0, 619.0, 0.0], [0L, 316L, 0, 21, 0, 0.0, 1967.0, 0.0], [0L, 317L, 1, 187, 2, 192.0, 26546.0, 128.0], [0L, 318L, 17, 449, 10, 2160.0, 60119.0, 917.0], [0L, 319L, 22, 421, 9, 2544.0, 56494.0, 886.0], [0L, 320L, 28, 615, 8, 3953.0, 77702.0, 817.0], 
                             [0L, 321L, 7, 156, 1, 1246.0, 24577.0, 82.0], [0L, 322L, 5, 266, 3, 698.0, 38555.0, 368.0], [0L, 323L, 10, 296, 3, 1569.0, 46397.0, 422.0], [0L, 324L, 9, 287, 5, 1440.0, 43282.0, 581.0], [0L, 325L, 2, 90, 0, 309.0, 14772.0, 0.0], [0L, 326L, 4, 225, 1, 582.0, 33896.0, 123.0], [0L, 327L, 8, 177, 2, 1309.0, 28018.0, 414.0], [0L, 328L, 10, 214, 2, 1617.0, 33319.0, 352.0], [0L, 329L, 1, 20, 0, 99.0, 2078.0, 0.0], [0L, 330L, 0, 10, 0, 0.0, 711.0, 0.0], [0L, 331L, 0, 14, 0, 0.0, 1427.0, 0.0], [0L, 332L, 0, 21, 0, 0.0, 2065.0, 0.0], [0L, 333L, 0, 31, 1, 0.0, 2947.0, 178.0], [0L, 334L, 0, 12, 0, 0.0, 1897.0, 0.0], [0L, 335L, 0, 39, 0, 0.0, 4353.0, 0.0], [0L, 336L, 1, 41, 2, 117.0, 4441.0, 251.0], [0L, 337L, 0, 19, 0, 0.0, 1635.0, 0.0], [0L, 338L, 0, 7, 0, 0.0, 674.0, 0.0], [0L, 339L, 0, 11, 0, 0.0, 929.0, 0.0], [0L, 340L, 1, 42, 0, 100.0, 3743.0, 0.0], [0L, 341L, 0, 27, 0, 0.0, 2607.0, 0.0], [0L, 342L, 0, 39, 0, 0.0, 3987.0, 0.0], [0L, 343L, 0, 50, 1, 0.0, 5274.0, 110.0], [0L, 344L, 0, 9, 0, 0.0, 1102.0, 0.0], [0L, 345L, 2, 129, 1, 276.0, 15190.0, 79.0], [0L, 346L, 0, 92, 0, 0.0, 11101.0, 0.0], [0L, 347L, 4, 232, 1, 620.0, 27848.0, 124.0], [0L, 348L, 3, 178, 5, 373.0, 22166.0, 470.0], [0L, 349L, 3, 35, 1, 746.0, 5159.0, 46.0], [0L, 350L, 6, 49, 3, 846.0, 7371.0, 397.0], [0L, 351L, 3, 38, 0, 500.0, 6177.0, 0.0], [0L, 352L, 2, 40, 4, 233.0, 5259.0, 543.0], [0L, 353L, 2, 56, 0, 260.0, 8008.0, 0.0], [0L, 354L, 3, 137, 1, 489.0, 19767.0, 123.0], [0L, 355L, 14, 349, 5, 2223.0, 46328.0, 382.0], [0L, 356L, 4, 159, 2, 707.0, 22513.0, 337.0], [0L, 357L, 3, 83, 4, 458.0, 10703.0, 481.0], [0L, 358L, 1, 80, 3, 286.0, 10025.0, 586.0], [0L, 359L, 3, 132, 2, 533.0, 17990.0, 359.0], [0L, 360L, 1, 156, 3, 152.0, 20562.0, 609.0], [0L, 361L, 1, 41, 0, 188.0, 7086.0, 0.0], [0L, 362L, 7, 95, 1, 1296.0, 15108.0, 276.0], [0L, 363L, 8, 257, 4, 1943.0, 37038.0, 631.0], [0L, 364L, 5, 78, 1, 847.0, 12947.0, 106.0], [0L, 365L, 13, 179, 7, 1474.0, 21923.0, 536.0], [0L, 366L, 8, 367, 3, 1017.0, 44567.0, 358.0], [0L, 367L, 14, 545, 13, 1806.0, 65471.0, 1407.0], [0L, 368L, 18, 489, 9, 2519.0, 61189.0, 1068.0], [0L, 369L, 0, 8, 0, 0.0, 583.0, 0.0], [0L, 370L, 0, 2, 0, 0.0, 103.0, 0.0], [0L, 371L, 0, 4, 0, 0.0, 447.0, 0.0], [0L, 372L, 0, 8, 0, 0.0, 749.0, 0.0], [0L, 373L, 2, 60, 3, 407.0, 9165.0, 431.0], [0L, 374L, 3, 84, 3, 582.0, 11416.0, 426.0], [0L, 375L, 4, 114, 3, 707.0, 15439.0, 705.0], [0L, 376L, 2, 45, 0, 403.0, 6214.0, 0.0], [0L, 377L, 8, 36, 1, 1057.0, 4977.0, 87.0], [0L, 378L, 9, 37, 1, 1412.0, 5512.0, 117.0], [0L, 379L, 3, 45, 3, 765.0, 5935.0, 240.0], [0L, 380L, 6, 38, 3, 1100.0, 4570.0, 217.0], [0L, 381L, 0, 5, 0, 0.0, 312.0, 0.0], [0L, 382L, 0, 16, 0, 0.0, 1909.0, 0.0], [0, 383, 0, 0, 0, 0, 0, 0], [0L, 384L, 0, 2, 0, 0.0, 99.0, 0.0]]
                 },
                ] 

    for test in testdata:
        props  = test['props']
        ts     = test['ts']
        nRules = test['nRules']
        filter = test['filter']
        vals   = test['vals']
        
        p.LoadFile(props)
        dm.PopulateModel()
        MulticlassSQL.CreateFilterTables()
        trainingSet = TrainingSet(p)
        trainingSet.Load(ts)
        output = StringIO()
        print 'Training classifier with '+str(nRules)+' rules...'
        weaklearners = FastGentleBoostingMulticlass.train(trainingSet.colnames,
                                                          nRules, trainingSet.label_matrix, 
                                                          trainingSet.values, output)
        def update(frac):
            print '%d%% Complete'%(frac * 100.)
        table = MulticlassSQL.PerImageCounts(weaklearners, filter=filter, cb=update)
#        MulticlassSQL.create_perobject_class_table(trainingSet.labels, weaklearners)
        table.sort()
    
        labels = ['table', 'image'] + list(trainingSet.labels)
        if p.area_scoring_column:
            labels += list(trainingSet.labels)

        grid = DataGrid(numpy.array(table), labels, key_col_indices=[0,1])
        grid.Show()
#        print grid.grid.GetTable().data.tolist()
        assert grid.grid.GetTable().data.tolist()==vals, "Test failed."

    app.MainLoop()
    
