# 从openpyxl库导入load_workbook函数
from openpyxl import load_workbook


class Store:
    # 输入方法
    def __init__(self):
        self.highest_score = self.highest_score_output()
        self.coin = self.goldencoin_output()
        self.attract_area_level = self.attractarea_level_output()
        self.speed_level = self.speed_level_output()
        self.penetrability = self.penetrability_level_output()
        self.frozen = self.frozen_output()
        self.attract_area_temporary = self.attractarea_temporary_output()
        self.speed_temporary = self.speed_temporary_output()
        self.clear = self.clear_output()
        self.wushuanglengque_output = self.wushuanglengque_output()
        self.seer = self.seer_output()

    # 用来存入数据的函数,其中value0为需要传入的变量，b为需要导入的单元格。
    def data_input(self, value0, b):
        # 打开”记录“的工作簿，获取活动工作表
        performance_wb = load_workbook('materials/cation hazard.xlsx')
        performance_ws = performance_wb.active
        # 单元格的输入
        performance_ws[b].value = value0
        # 保存并且关闭excel
        performance_wb.save('materials/cation hazard.xlsx')

    # 用来导出数据的函数,其中self为需要导出所存储的变量，b为需要导出的单元格。
    def data_output(self, b):
        # 打开”记录“的工作簿，获取活动工作表
        performance_wb = load_workbook('materials/cation hazard.xlsx')
        performance_ws = performance_wb.active
        # 单元格的输出
        a = performance_ws[b].value
        # 关闭excel
        performance_wb.save('materials/cation hazard.xlsx')
        return a

    # 基础类
    # 最高得分记录输入
    def highest_score_input(self, val):
        self.data_input(val, 'B2')
        return self

    # 最高得分记录的输出
    def highest_score_output(self):
        a = self.data_output('B2')
        return a

    # 金币输入
    def goldencoin_input(self, val):
        self.data_input(val, 'C2')
        return self

    # 金币的输出
    def goldencoin_output(self):
        a = self.data_output('C2')
        return a

    # 天赋类（被动）

    # 吸引面积等级的输入
    def attractarea_level_input(self, val):
        self.data_input(val, 'B5')
        return self

    # 吸引面积等级的输出
    def attractarea_level_output(self):
        a = self.data_output('B5')
        return a

    # 运动速度等级的输入
    def speed_level_input(self, val):
        self.data_input(val, 'C5')
        return self

    # 运动速度等级的输出
    def speed_level_output(self):
        a = self.data_output('C5')
        return a

    # 穿透性（概率）的输入
    def penetrability_level_input(self, val):
        self.data_input(val, 'D5')
        return self

    # 穿透性（概率）的输出
    def penetrability_level_output(self):
        a = self.data_output('D5')
        return a

    # 商店类（效果）

    # 时间类（冷却）的输入
    def frozen_input(self, val):
        self.data_input(val, 'B7')
        return self

    # 时间类（冷却）的输出
    def frozen_output(self):
        a = self.data_output('B7')
        return a

    # 短暂增大面积道具数目的输入
    def attractarea_temporary_input(self, val):
        self.data_input(val, 'C7')
        return self

    # 短暂增大面积道具数目的输出
    def attractarea_temporary_output(self):
        a = self.data_output('C7')
        return a

    # 暂时运动速度道具数目的输入
    def speed_temporary_input(self, val):
        self.data_input(val, 'D7')
        return self

    # 暂时运动速度道具数目的输出
    def speed_temporary_output(self):
        a = self.data_output('D7')
        return a

    # 清屏道具数目的输入
    def clear_input(self, val):
        self.data_input(val, 'D7')
        return self

    # 清屏道具数目的输出
    def clear_output(self):
        a = self.data_output('D7')
        return a

    # 技能类（主动）

    # 无双（冷却时间）——延长的输入
    def wushuanglengque_input(self, val):
        self.data_input(val, 'B9')
        return self

    # 无双（冷却时间）——延长的输出
    def wushuanglengque_output(self):
        a = self.data_output('B9')
        return a

    # 预知屏幕外的离子（小屏幕）——延长的输入
    def seer_input(self, val):
        self.data_input(val, 'C9')
        return self
    # 预知屏幕外的离子（小屏幕）——延长的输出
    def seer_output(self):
        a = self.data_output('C9')
        return a
