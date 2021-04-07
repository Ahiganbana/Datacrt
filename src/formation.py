import copy
import math
#import numpy
class Formation():
    """
    生成主飞机的航迹数据,是一个二维数组
     formationType——队形，跟随队形或者菱形队形
     leader_cord——主机坐标
     num——机群数量，除了主机其余为僚机
     用圆的思想来处理，半径设置为1km
     math.pi/6 是30度的意思
     生成菱形队形的方法
    """
    def diamond_formation(self, leader_cord, num=1, r_var=500):
        """
        生成菱形编队
        leader_cord:主机坐标
        num:组成编队的飞机数量
        r:半径
        """
        # 更改角度
        beta = math.pi / 6
        deth = 0
        c_var = []
        # 第一个存的是主机数据
        c_var.append(leader_cord)
        if num == 1:
            left_num = 0
            right_num = 0
        else:
            if (num-1) % 2 == 0:
                # 偶数架撩机，那么让左侧和右侧飞机数量相同
                left_num = (int)((num - 1) / 2)
                right_num = (int)((num - 1) / 2)
            else:
                # 奇数架僚机，那么让左边的僚机多一个
                left_num = (int)((num - 2)/2 + 1)
                right_num = (int)((num - 2) / 2)
        # 对左侧每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(left_num):
            # 每架飞机有存储自己航迹的二维数组
            diamond_trace = []
            # 对每架飞机里的每个点做处理
            for dot in leader_cord:
                new_dot = copy.deepcopy(dot)
                # 处理左侧飞机的xy轴坐标
                # new_dot[0] = new_dot[0] + ((plane+1)*r_var)*math.sin(math.pi + beta + new_dot[3])
                new_dot[0] = new_dot[0] + ((plane+1)*r_var)*math.sin(math.pi + beta)
                # new_dot[1] = new_dot[1] + ((plane+1)*r_var)*math.cos(math.pi + beta + new_dot[3])
                new_dot[1] = new_dot[1] + ((plane+1)*r_var)*math.cos(math.pi + beta)
                new_dot[2] = new_dot[2] - (plane+1)*deth
                # 单个点处理完成后，将其放在航迹数组里
                diamond_trace.append(new_dot)
            c_var.append(diamond_trace)
            # 出第一层循环以后将该飞机的航迹数组生成文件或者输出

        # 对右侧每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(right_num):
            # 每架飞机有存储自己航迹的二维数组
            diamond_trace = []
            # 对每架飞机里的每个点做处理
            for dot in leader_cord:
                new_dot = copy.deepcopy(dot)
                # 处理右侧飞机的xy轴坐标
                # new_dot[0] = new_dot[0] + ((plane+1) * r) * math.sin(math.pi - beta + new_dot[3])
                new_dot[0] = new_dot[0] + ((plane+1) * r_var) * math.sin(math.pi - beta)
                # new_dot[1] = new_dot[1] + ((plane+1) * r_var) * math.cos(math.pi - beta + new_dot[3])
                new_dot[1] = new_dot[1] + ((plane+1) * r_var) * math.cos(math.pi - beta)
                new_dot[2] = new_dot[2] - (plane+1)*deth
                # 单个点处理完成后，将其放在航迹数组里
                diamond_trace.append(new_dot)
            c_var.append(diamond_trace)
        return c_var
    def linear_formation(self, leader_cord, number=1, r_var=500):
        """
        用于生成跟随主机的从机的线性编队
        输入:飞机的数量,引导线,
        输出:飞机的航迹
        参数:
            leader_cord:主机坐标
            number:飞机数量
            r_var:圆的半径
        """
        deth = 0
        c_var = []
        c_var.append(leader_cord)
        # 对每架飞机做循环，要输出一个这架飞机的航迹文件
        # if number == 1:
        num = number - 1
        # else:
        #     num = number
        for plane in range(num):
            lineartrace = []
            #遍历航线上的每个点
            for dot in leader_cord:
                print(dot)
                print("------")
                new_dot = copy.deepcopy(dot)
                # 处理跟随飞机的xyz坐标
                # new_dot[0] = new_dot[0] + (plane+1)*r_var * math.sin(math.pi  + new_dot[3])
                new_dot[1] = new_dot[1] + (plane+1)*r_var * math.sin(math.pi)
                # new_dot[1] = new_dot[1] + (plane+1)*r_var * math.cos(math.pi  + new_dot[3])
                new_dot[0] = new_dot[0] + (plane+1)*r_var * math.cos(math.pi)
                new_dot[2] = new_dot[2] - (plane+1) * deth
            # 坐标处理完毕，将点迹信息放入航迹数组中
                print(new_dot)
                lineartrace.append(new_dot)
            c_var.append(lineartrace)
        return c_var
