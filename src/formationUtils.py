import numpy
import copy
import math
import random

class FormationUtils(object):
    def echelonFormation(self,leaderCord, num=1, r=500, angle=math.pi/ 4):
        deth = 0
        C = []
        # 第一个存的是主机数据
        C.append(leaderCord)
        num = num - 1
        # 对梯队每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(num): 
            # 每架飞机有存储自己航迹的二维数组
            echelonTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理右侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane+1) * r) * math.sin(math.pi - beta + newDot[3])
                newDot[0] = newDot[0] + ((plane + 1) * r)
                # newDot[1] = newDot[1] + ((plane+1) * r) * math.cos(math.pi - beta + newDot[3])
                #newDot[1] = newDot[1] + ((plane + 1) * r) * math.sin(angle)
                newDot[1] = newDot[1] + ((plane + 1) * r) * math.tan(math.pi/2 - angle)
                newDot[2] = newDot[2] - (plane + 1) * deth
                #newDot[3] = math.sqrt(newDot[0]*newDot[0] + newDot[1]*newDot[1] + newDot[2] * newDot[2])
                # 单个点处理完成后，将其放在航迹数组里
                echelonTrace.append(newDot)
            C.append(echelonTrace)
            #print(echelonTrace[plane])
        return C

    def diamondFormation(self, leaderCord, num=1, r=500, angle=math.pi * 3 / 4):
        # 此处的angle为右侧僚机与Y轴正方向按顺时针所成的夹角度数
        # 因此，左侧僚机与Y轴所成夹角为 math.pi - angle
        beta = math.pi - angle
        deth = 0
        C = []
        # 第一个存的是主机数据
        C.append(leaderCord)
        if num == 1:
            leftNum = 0
            rightNum = 0
        else:
            if (num - 1) % 2 == 0:
                # 偶数架撩机，那么让左侧和右侧飞机数量相同
                leftNum = (int)((num - 1) / 2)
                rightNum = (int)((num - 1) / 2)
            else:
                # 奇数架僚机，那么让左边的僚机多一个
                leftNum = (int)((num - 2) / 2 + 1)
                rightNum = (int)((num - 2) / 2)

        # 对左侧每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(leftNum):
            # 每架飞机有存储自己航迹的三维数组
            diamondTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理左侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane + 1) * r) * math.sin(math.pi + beta)
                # newDot[1] = newDot[1] + ((plane + 1) * r) * math.cos(beta)
                newDot[0] = newDot[0] + ((plane+1)*r)*math.sin(math.pi + beta)
                newDot[1] = newDot[1] + ((plane+1)*r)*math.cos(math.pi + beta)
                newDot[2] = newDot[2] - (plane + 1) * deth
                #newDot[3] = math.sqrt(newDot[0]*newDot[0] + newDot[1]*newDot[1] + newDot[2] * newDot[2])
                # 单个点处理完成后，将其放在航迹数组里
                diamondTrace.append(newDot)
            C.append(diamondTrace)
            # 出第一层循环以后将该飞机的航迹数组生成文件或者输出

        # 对右侧每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(rightNum):
            # 每架飞机有存储自己航迹的三维数组
            diamondTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理右侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane + 1) * r) * math.sin(math.pi + angle)
                # newDot[1] = newDot[1] + ((plane + 1) * r) * math.cos(angle)
                newDot[0] = newDot[0] + ((plane+1) * r) * math.sin(math.pi - beta)
                newDot[1] = newDot[1] + ((plane+1) * r) * math.cos(math.pi - beta)
                newDot[2] = newDot[2] - (plane + 1) * deth
                #newDot[3] = math.sqrt(newDot[0]*newDot[0] + newDot[1]*newDot[1] + newDot[2] * newDot[2])
                # 单个点处理完成后，将其放在航迹数组里
                diamondTrace.append(newDot)
            C.append(diamondTrace)
        return C
         # 生成蛇形编队
    def snakelikeFormation(self, leaderCord, num=1, r=500, angle=math.pi / 4):
        # 此处的angle为侧边上奇数边的僚机与Y轴正方向按顺时针所成的夹角度数
        # bate为中轴线上的僚机
        beta = math.pi/2
        deth = 0
        C = []
        # 第一个存的是主机数据
        C.append(leaderCord)
        if num == 1:
            sideNum = 0
            middleNum = 0
        else:
            if (num - 1) % 2 == 0:
                # 偶数架撩机，那么让侧边和中线上的飞机数量相同
                sideNum = (int)((num - 1) / 2)
                middleNum = (int)((num - 1) / 2)
            else:
                # 奇数架僚机，那么让侧边的僚机多一个
                sideNum = (int)((num - 2) / 2 + 1)
                middleNum = (int)((num - 2) / 2)

        if sideNum % 2 == 0:
            # 侧边撩机为偶数架，那么让侧边上的奇数侧和偶数侧的飞机数量相同
            oddNum = (int)(sideNum / 2)
            evenNum = (int)(sideNum / 2)
        else:
            # 侧边有奇数架僚机，那么让记述侧的僚机多一个
            oddNum = (int)((sideNum - 1) / 2 + 1)
            evenNum = (int)((sideNum - 1) / 2)
        # 对奇侧边每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(oddNum):
            # 每架飞机有存储自己航迹的三维数组
            snakelikeTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理左侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane+1)*r)*math.sin(math.pi + beta + newDot[3])
                newDot[0] = newDot[0] + ((4 * plane + 1) * r) * math.sin(math.pi + angle)
                # newDot[1] = newDot[1] + ((plane+1)*r)*math.cos(math.pi + beta + newDot[3])
                newDot[1] = newDot[1] + r * math.cos(angle)
                newDot[2] = newDot[2] - (4 * plane + 1) * deth
               #newDot[3] = math.sqrt(newDot[0]*newDot[0] + newDot[1]*newDot[1] + newDot[2] * newDot[2])
                # 单个点处理完成后，将其放在航迹数组里
                snakelikeTrace.append(newDot)
            C.append(snakelikeTrace)
            # 出第一层循环以后将该飞机的航迹数组生成文件或者输出
            # 对偶侧边每架飞机的循环，循环一次出一个飞机的航迹文件
            for plane in range(evenNum):
                # 每架飞机有存储自己航迹的三维数组
                snakelikeTrace = []
                # 对每架飞机里的每个点做处理
                for dot in leaderCord:
                    newDot = copy.deepcopy(dot)
                    # 处理左侧飞机的xy轴坐标
                    # newDot[0] = newDot[0] + ((plane+1)*r)*math.sin(math.pi + beta + newDot[3])
                    newDot[0] = newDot[0] + ((4 * plane + 3) * r) * math.sin(math.pi + angle)
                    # newDot[1] = newDot[1] + ((plane+1)*r)*math.cos(math.pi + beta + newDot[3])
                    newDot[1] = newDot[1] + r * math.cos(math.pi - angle)
                    newDot[2] = newDot[2] - (4 * plane + 3) * deth
                    #newDot[3] = math.sqrt(newDot[0]*newDot[0] + newDot[1]*newDot[1] + newDot[2] * newDot[2])
                    # 单个点处理完成后，将其放在航迹数组里
                    snakelikeTrace.append(newDot)
                C.append(snakelikeTrace)
                # 出第一层循环以后将该飞机的航迹数组生成文件或者输出

        # 对中轴线上的每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(middleNum):
            # 每架飞机有存储自己航迹的三维数组
            snakelikeTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理右侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane+1) * r) * math.sin(math.pi - beta + newDot[3])
                newDot[0] = newDot[0] + ((2 * plane + 2) * r) * math.sin(math.pi + angle)
                # newDot[1] = newDot[1] + ((plane+1) * r) * math.cos(math.pi - beta + newDot[3])
                newDot[1] = newDot[1]
                newDot[2] = newDot[2] - (2 * plane + 2) * deth
                #newDot[3] = math.sqrt(newDot[0]*newDot[0] + newDot[1]*newDot[1] + newDot[2] * newDot[2])
                # 单个点处理完成后，将其放在航迹数组里
                snakelikeTrace.append(newDot)
            C.append(snakelikeTrace)
        return C