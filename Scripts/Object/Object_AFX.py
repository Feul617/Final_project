from Scripts.FrameWork.FrameWork_AFX import *

from Scripts.Object.Tile.Tile import Tile
from Scripts.Object.Tile.Tile import TileType
from Scripts.Object.Tile.Tile import MakeTile_X
from Scripts.Stage.MainStage import MainStage
#from Scripts.Object.Character import Character


#def make_stool():
#     global stage1, stage2
#
#     stage1.block.clear()
#
#     if stage1.step == 1:
#         #                    좌, 아래, 우, 위
#         stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
#         stage1.block.append([330, 60, 470, 60])  # 1층 중앙
#         stage1.block.append([610, 60, 730, 60])  # 1층 오른쪽
#         stage1.block.append([185, 165, 370, 165])  # 2층 왼쪽
#         stage1.block.append([455, 165, 635, 165])  # 2층 오른쪽
#         stage1.block.append([120, 270, 330, 270])  # 3층 왼쪽
#         stage1.block.append([515, 270, 705, 270])  # 3층 오른쪽
#         stage1.block.append([210, 375, 370, 375])  # 4층 왼쪽
#         stage1.block.append([450, 375, 620, 375])  # 4층 오른쪽
#         stage1.block.append([230, 480, 370, 480])  # 5층 왼쪽
#         # stage1.block.append([190, 480, 200, 600])  # 5층 왼쪽 벽
#         stage1.block.append([450, 480, 580, 480])  # 5층 오른쪽
#
#     elif stage1.step == 2:
#         stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
#         stage1.block.append([340, 60, 470, 60])  # 1층 중앙
#         stage1.block.append([610, 60, 730, 60])  # 1층 오른쪽
#         stage1.block.append([115, 165, 270, 165])  # 2층 왼쪽
#         stage1.block.append([370, 165, 430, 165])  # 2층 중앙
#         stage1.block.append([530, 165, 670, 165])  # 2층 오른쪽
#         stage1.block.append([160, 270, 350, 270])  # 3층 왼쪽
#         stage1.block.append([440, 270, 630, 270])  # 3층 오른쪽
#         stage1.block.append([160, 375, 350, 375])  # 4층 왼쪽
#         stage1.block.append([440, 375, 630, 375])  # 4층 오른쪽
#         stage1.block.append([120, 480, 350, 480])  # 5층 왼쪽
#         stage1.block.append([440, 480, 670, 480])  # 5층 오른쪽
#
#     elif stage1.step == 3:
#         stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
#         stage1.block.append([340, 60, 470, 60])  # 1층 중앙
#         stage1.block.append([600, 60, 730, 60])  # 1층 오른쪽
#         stage1.block.append([120, 165, 350, 165])  # 2층 왼쪽
#         stage1.block.append([460, 165, 680, 165])  # 2층 오른쪽
#         stage1.block.append([160, 270, 770, 270])  # 3층
#         stage1.block.append([0, 375, 630, 375])  # 4층
#         stage1.block.append([160, 480, 770, 480])  # 5층
#
#     elif stage1.step == 4:
#         stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
#         stage1.block.append([340, 60, 470, 60])  # 1층 중앙
#         stage1.block.append([600, 60, 730, 60])  # 1층 오른쪽
#         stage1.block.append([140, 165, 320, 165])  # 2층 왼쪽
#         stage1.block.append([490, 165, 670, 165])  # 2층 오른쪽
#         stage1.block.append([0, 270, 240, 270])  # 3층 왼쪽
#         stage1.block.append([570, 270, 770, 270])  # 3층 오른쪽
#         stage1.block.append([0, 375, 190, 375])  # 4층 왼쪽
#         stage1.block.append([630, 375, 770, 375])  # 4층 오른쪽
#
#         stage1.block.append([330, 355, 360, 355])  # 3.5층 오른쪽
#         stage1.block.append([450, 355, 470, 355])  # 3.5층 왼쪽
#
#         stage1.block.append([300, 420, 330, 420])  # 4.5층 왼쪽
#         stage1.block.append([470, 420, 530, 420])  # 4.5층 오른쪽
#
#         stage1.block.append([0, 480, 130, 480])  # 5층 왼쪽
#         stage1.block.append([200, 480, 280, 480])  # 5층 중앙 왼쪽
#         stage1.block.append([530, 480, 610, 480])  # 5층 중앙 오른쪽
#         stage1.block.append([680, 480, 770, 480])  # 5층 오른쪽