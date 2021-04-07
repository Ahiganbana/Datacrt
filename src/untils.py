import csv
import numpy as np
import pandas as pd
import time
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#用于保存数据和场景文件
class Utils(object):
    def saveData(self, data, C = ['x坐标', 'y坐标', '高度', '距离', '角度', '俯仰角','航向角','速度','雷达频率','占空比','功率密度','重复频率','脉冲宽度',]):
        dictc = {}
        time_start1 = time.time()
        dataList = {}
        radarList = {}
        H = len(C)
        num = len(data)
        #创建飞机轨迹数据字典和雷达数据字典
        for i in range(num):
            for j in range(len(data[i].planes)):
                print("in utils",len(data[i].planes[j].trackData), len(data[i].planes[j].radarData))
                for k in range(len(data[i].planes[j].trackData)):
                    key = str(i) + '-' + str(j) + '-' + str(k)
                    dataList[key] = data[i].planes[j].trackData[k]
                    radarList[key] = data[i].planes[j].radarData[k]
                    print(len(dataList[key]), len(radarList[key]))
        for key in dataList:
            T = len(dataList[key])
            plisti = dataList[key]
            rlisti = radarList[key]
            x = [l[0] for l in plisti]
            y = [l[1] for l in plisti]
            z = [l[2] for l in plisti]
            dis = [l[3] for l in plisti]
            ang = [l[4] for l in plisti]
            upang = [l[5] for l in plisti]
            direct = [l[6] for l in plisti]
            speed = [l[7] for l in plisti]
            radarFre = [m[0] for m in rlisti]
            pwm = [m[1] for m in rlisti]
            pds = [m[2] for m in rlisti]
            sf = [m[3] for m in rlisti]
            sw = [m[4] for m in rlisti]
            dictc[key + 'x坐标'] = x
            dictc[key + 'y坐标'] = y
            dictc[key + '高度'] = z
            dictc[key + '距离'] = dis
            dictc[key + '角度'] = ang
            dictc[key + '俯仰角'] = upang
            dictc[key + '航向角'] = direct
            dictc[key + '速度'] = speed
            dictc[key + '雷达频率'] = radarFre
            dictc[key + '占空比'] = pwm
            dictc[key + '功率密度'] = pds
            dictc[key + '重复频率'] = sf
            dictc[key + '脉冲宽度'] = sw
        print(len(x), len(y), len(z), len(dis), len(ang), len(upang),len(direct), len(speed), len(radarFre),len(pwm),len(pds),len(sf), len(sw))
        time_end1 = time.time()
        print("创建字典花费的时间为:" , time_end1 - time_start1)
        time_start2 = time.time()
        #从字典中取出数据并写入表格
        ditcq = {}
        for i in range(num):
            for j in range(len(data[i].planes)):
                for k in range(len(data[i].planes[j].trackData)):
                    for l in range(len(C)):
                        keystr = str(i) + '-' + str(j) + '-' + str(k) + C[l]
                        ditcq[C[l]] = dictc[keystr]
                    filename = str(i) + '-' + str(j) + '-' + str(k) + ".csv"
                    dataForSave = pd.DataFrame(ditcq)
                    dataForSave.to_csv(filename, encoding = 'gbk')
        time_end2 = time.time()
        print("存数据的花费的时间为:" , time_end2 - time_end1)
        # for i in range(len(data)):
        #     for j in range(len(data[i].plane)):
        #         for k in range(len(C)):
        #             keystr = str(i) + '-' + str(j) + C[k]
        #             ditcq[C[k]] = dictc[keystr]
        #         filename = str(i) + "-" + str(j) + ".csv"
        #         dataForSave = pd.DataFrame(ditcq)
        #         dataForSave.to_csv(filename, encoding = 'gbk')
        # time_end2 = time.time()
        # print("存数据的花费的时间为:" , time_end2 - time_end1)
        # for i in range(len(data)):
        #     filename = data[i].action_list[0] + str(i) + '.csv'
        #     C = ['X坐标', 'Y坐标', 'Z坐标', '距离', '角度', '仰角','航向角','速度','雷达频率/GHZ','雷达信号占空比','功率密度/mW每平方米','信号重复频率/KHZ','信号脉冲宽度/us','飞机种类']
        #     out = open(filename, 'a', newline='')
        #     csv_write = csv.writer(out, dialect='excel')
        #     csv_write.writerow(C)
        #     for j in range(len(self.form_data[i].plane)):
        #         for k in range(len(self.form_data[i].plane[j].Q) - 1):
        #             csv_write.writerow(self.form_data[i].plane[j].Q[k] + self.form_data[i].plane[j].radar.Q[k] + [self.form_data[i].plane_type])
        #     out.close() 
        QtWidgets.QMessageBox.information(QWidget(), "提示", "保存完毕!")
    def saveScene(self, scene):
        info = {}
        info["任务"] = scene.mission
        info["编队类型"] = scene.formationType
        length = len(scene.formationList)
        typeInfo = ""
        numInfo = ""
        detailInfo = ""
        for i in range(length):
            typeInfo = scene.formationList[i].plane_type
            numInfo = str(scene.formationList[i].plane_num)
            detailInfo += typeInfo + " : " + numInfo
        info["详细信息"] = detailInfo
        filename = scene.name
        with open(filename, 'w') as fileObj:
            json.dump(info, fileObj)

        