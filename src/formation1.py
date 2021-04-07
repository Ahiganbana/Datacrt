from planeGroup import PlaneGroup

class Formation(object):
    """
    编队实体,描述每个飞机组的动作方式,自身不存储数据.
    """
    # 拿到主机的航迹数据，三维数组
    # formationType——队形，跟随（纵队）队形、梯队、横队、或者菱形队形、箭队
    # leaderCord——主机坐标
    # num——机群数量，除了主机其余为僚机
    # 用圆的思想来处理，半径设置为1km
    # math.pi/6 是30度的意思
    # 生成梯队编队
    # angle:飞机与Y轴顺时针所成夹角，范围是0~pi
    def __init__(self,form_id, form_type, mission="unknow"):
        """
        form_id : 编队 id
        form_type : 编队类型
        planes : 属于编队的飞机组
        info : 描述编队中每种飞机各有几个的字典
        """
        self.form_id = form_id
        self.ftype = form_type
        self.planes = []
        self.info = []
        self.mission = mission
    
    def setInfo(self, info):
        self.info = info
    
    def setPlanes(self, planes):
        self.planes = planes
    
    def __str__(self):
        return '编号: %d  飞机组长度: %d 编队类型: %s 详细信息: %s'  %(self.form_id, len(self.planes), self.ftype, self.info)