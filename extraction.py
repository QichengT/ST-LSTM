########################################################################################################################
### 从数据库里读取数据并进行预处理
### author:Qicheng Tang
########################################################################################################################
from pymongo import MongoClient
import pymongo
import csv
import numpy as np
import pandas as pd
import os
########################################################################################################################
# # 开启数据库连接
# # create connection
# c = MongoClient()
# # connect to db
# db = c.test
# # connect to account
# account = db.cardodmin
# # find OD data
########################################################################################################################
# # 创建索引（只需要跑一遍）
# db.cardodmin.create_index([
#    ('ostation',pymongo.ASCENDING),('dstation',pymongo.ASCENDING)
# ])
#
# # 创建索引
# db.cardodmin.create_index([
#    ('dstation',pymongo.ASCENDING)
# ])
#
# # 创建索引
# db.cardodmin.create_index([
#    ('ostation',pymongo.ASCENDING)
# ])
########################################################################################################################
# # 删除错误数据（只需要跑一遍）
# # 删除进站/出站为空的数据
# account.remove({'ostation': None})
# account.remove({'dstation': None})
# # 删除进站/出站异常的数据
# account.remove({'ostation': {'$gt':633}})
# account.remove({'dstation': {'$gt':633}})
# account.remove({'ostation': {'$lt':101}})
# account.remove({'dstation': {'$lt':101}})
########################################################################################################################
#  # 计算全网站点的10分钟级进站人数(只需要跑一遍)
# code = 101
# station_code = []
# for i in range(24):
#     station_code.append(code)
#     code += 1
# code = 201
# for i in range(25):
#     station_code.append(code)
#     code += 1
# code = 301
# for i in range(45):
#     station_code.append(code)
#     code += 1
# code = 601
# for i in range(28):
#     station_code.append(code)
#     code += 1
#
# minute = 630
# minute_st = []
# for i in range(3100):
#     minute_st.append(minute)
#     minute += 10
#     if minute % 100 == 60:
#         minute += 40
#     if minute == 2310:
#         minute = 630
#
# for i in range(len(station_code)):
#     station = station_code[i]
#     print(station)
#     count = [0 for i in range(3100)]
#     for item in account.find({'ostation': station}):
#         otime = int(item['oTime'][9:])
#         if otime >= 621 and otime <= 2300:
#             date = int(item['date'])
#             day = (date - 1) % 100
#             if otime % 100 == 0:
#                 tenmin = int((otime - 1) / 10) - 4
#             else:
#                 tenmin = int((otime - 1) / 10)
#             hour = int((otime - 1) / 100)
#             time = tenmin - ((hour - 6) * 4) + (day * 100) - 62
#
#             count[time] += 1
#
#     temp = []
#     date = 20170300
#     num = [[] for i in range(3100)]
#
#     for i in range(3100):
#         if (i % 100 == 0):
#             date += 1
#         temp = [station, date, minute_st[i], count[i]]
#         num[i] = temp
#
#     headers = ['station', 'date', 'time', 'In']
#     path = 'E:/InOut_data/In/In_' + str(station) + '_step10.csv'
#     with open(path, 'w',newline='') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerow(headers)
#         f_csv.writerows(num)
#
#     print('SUCCESS')
#######################################################################################################################
#  # 计算全网站点的10分钟级出站人数(只需要跑一遍)
# code = 101
# station_code = []
# for i in range(24):
#     station_code.append(code)
#     code += 1
# code = 201
# for i in range(25):
#     station_code.append(code)
#     code += 1
# code = 301
# for i in range(45):
#     station_code.append(code)
#     code += 1
# code = 601
# for i in range(28):
#     station_code.append(code)
#     code += 1
#
# minute = 630
# minute_st = []
# for i in range(3100):
#     minute_st.append(minute)
#     minute += 10
#     if minute % 100 == 60:
#         minute += 40
#     if minute == 2310:
#         minute = 630
#
# for i in range(len(station_code)):
#     station = station_code[i]
#     print(station)
#     count = [0 for i in range(3100)]
#     for item in account.find({'dstation': station}):
#         otime = int(item['dTime'][9:])
#         if otime >= 621 and otime <= 2300:
#             date = int(item['date'])
#             day = (date - 1) % 100
#             if otime % 100 == 0:
#                 tenmin = int((otime - 1) / 10) - 4
#             else:
#                 tenmin = int((otime - 1) / 10)
#             hour = int((otime - 1) / 100)
#             time = tenmin - ((hour - 6) * 4) + (day * 100) - 62
#
#             count[time] += 1
#
#     temp = []
#     date = 20170300
#     num = [[] for i in range(3100)]
#
#     for i in range(3100):
#         if (i % 100 == 0):
#             date += 1
#         temp = [station, date, minute_st[i], count[i]]
#         num[i] = temp
#
#     headers = ['station', 'date', 'time', 'Out']
#     path = 'E:/InOut_data/Out/Out_' + str(station) + '_step10.csv'
#     with open(path, 'w',newline='') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerow(headers)
#         f_csv.writerows(num)
#
#     print('SUCCESS')
########################################################################################################################
# # 计算全网各站点出站总人数(只需跑一边)
# code = 101
# station_code = []
# for i in range(24):
#     station_code.append(code)
#     code += 1
# code = 201
# for i in range(25):
#     station_code.append(code)
#     code += 1
# code = 301
# for i in range(45):
#     station_code.append(code)
#     code += 1
# code = 601
# for i in range(28):
#     station_code.append(code)
#     code += 1

# count = [0 for i in range(650)]
# for item in account.find():
#     count[item['dstation']] += 1
#
# num = [[0]for i in range(len(count))]
# for i in range(len(count)):
#     num[i] = [count[i]]
#
# headers = ['out_count']
# path = 'E:/InOut_data/Out_count.csv'
# with open(path,'w',newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(num)
########################################################################################################################
#
# dstation = 334
#
# # 生成标准站点编号
# code = 101
# station_code = []
# for i in range(24):
#     station_code.append(code)
#     code += 1
# code = 201
# for i in range(25):
#     station_code.append(code)
#     code += 1
# code = 301
# for i in range(45):
#     station_code.append(code)
#     code += 1
# code = 601
# for i in range(28):
#     station_code.append(code)
#     code += 1
# #
# # for c in range(len(station_code)):
#
# # 计算d为目标站点的各站点od数
# count = [0 for i in range(len(station_code))]
# for item in account.find({'dstation': dstation}):
#     for i in range(len(station_code)):
#         if station_code[i] == item['ostation']:
#             count[i] += 1
#
# num = [[0] for i in range(len(station_code))]
# for i in range(len(station_code)):
#     num[i] = [dstation, station_code[i], count[i]]
#
# headers = ['dstation', 'ostation', 'od_count']
# path = 'E:/InOut_data/Out_' + str(dstation) + '/data/OD_' + str(dstation) + '_count.csv'
# with open(path, 'w', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(num)
#######################################################################################################################
# # 计算目标站点的10分钟级出站人数
# count = [0 for i in range(3100)]
# for item in account.find({'dstation': dstation}):
#     dtime = int(item['dTime'][9:])
#     if dtime >= 621 and dtime <= 2300:
#         date = int(item['date'])
#         day = (date - 1) % 100
#         if dtime % 100 == 0:
#             tenmin = int((dtime - 1) / 10) - 4
#         else:
#             tenmin = int((dtime - 1) / 10)
#         hour = int((dtime - 1) / 100)
#         time = tenmin - ((hour - 6) * 4) + (day * 100) - 62
#
#         count[time] += 1
#
# temp = []
# date = 20170300
# num = [[] for i in range(3100)]
# minute = 630
# minute_st = []
# for i in range(3100):
#     minute_st.append(minute)
#     minute += 10
#     if minute % 100 == 60:
#         minute += 40
#     if minute == 2310:
#         minute = 630
#
# for i in range(3100):
#     if (i % 100 == 0):
#         date += 1
#     temp = [dstation, date, minute_st[i], count[i]]
#     num[i] = temp
#     print(temp)
#
# headers = ['station', 'date', 'time', 'Out']
# path = 'E:/InOut_data/Out_' + str(dstation) + '/data/Out_' + str(dstation) + '_step10.csv'
# with open(path, 'w', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(num)
######################################################################################################################
# # 计算两站点间10分钟级od数
# code = 101
# station_code = []
# for i in range(24):
#     station_code.append(code)
#     code += 1
# code = 201
# for i in range(25):
#     station_code.append(code)
#     code += 1
# code = 301
# for i in range(45):
#     station_code.append(code)
#     code += 1
# code = 601
# for i in range(28):
#     station_code.append(code)
#     code += 1
#
# minute = 630
# minute_st = []
# for i in range(3100):
#     minute_st.append(minute)
#     minute += 10
#     if minute % 100 == 60:
#         minute += 40
#     if minute == 2310:
#         minute = 630
# for k in range(len(station_code)):
#     dstation = station_code[k]
#     print(dstation)
#     for i in range(len(station_code)):
#         ostation = station_code[i]
#         count = [0 for i in range(3100)]
#         for item in account.find({'ostation': ostation, 'dstation': dstation}):
#             otime = int(item['oTime'][9:])
#             if otime >= 621 and otime <= 2300:
#                 date = int(item['date'])
#                 day = (date - 1) % 100
#                 if otime % 100 == 0:
#                     tenmin = int((otime - 1) / 10) - 4
#                 else:
#                     tenmin = int((otime - 1) / 10)
#                 hour = int((otime - 1) / 100)
#                 time = tenmin - ((hour - 6) * 4) + (day * 100) - 62
#
#                 count[time] += 1
#
#         temp = []
#         date = 20170300
#         num = [[] for i in range(3100)]
#
#         for i in range(3100):
#             if (i % 100 == 0):
#                 date += 1
#             temp = [ostation, dstation, date, minute_st[i], count[i]]
#             num[i] = temp
#
#         headers = ['ostation', 'dstation', 'date', 'time', 'od_In']
#         path = 'E:/Experiment/' + str(dstation) + '/OD/OD_from_' + str(ostation) + '_to_' + str(dstation) + '.csv'
#         with open(path, 'w', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerow(headers)
#             f_csv.writerows(num)
#
#     print('SUCCESS')


######################################################################################################################
# 计算全网站点到目标站点的10分钟级T
# code = 101
# station_code = []
# for i in range(24):
#     station_code.append(code)
#     code += 1
# code = 201
# for i in range(25):
#     station_code.append(code)
#     code += 1
# code = 301
# for i in range(45):
#     station_code.append(code)
#     code += 1
# code = 601
# for i in range(28):
#     station_code.append(code)
#     code += 1
#
# minute = 630
# minute_st = []
# for i in range(3100):
#     minute_st.append(minute)
#     minute += 10
#     if minute % 100 == 60:
#         minute += 40
#     if minute == 2310:
#         minute = 630
#
#
# for k in range(len(station_code)):
#     dstation = station_code[k]
#     print(dstation)
#     for i in range(len(station_code)):
#         station = station_code[i]
#         numtime_work = [0 for i in range(100)]
#         count_work = [0 for i in range(100)]
#         numtime_wend = [0 for i in range(100)]
#         count_wend = [0 for i in range(100)]
#         for item in account.find({'ostation': station, 'dstation': dstation}):
#             otime = int(item['oTime'][9:])
#             if otime >= 621 and otime <= 2300:
#                 dtime = int(item['dTime'][9:])
#                 date = int(item['date'])
#                 min = (int(dtime / 100) - int(otime / 100)) * 60 + (dtime % 100) - (otime % 100)
#                 day = (date - 1) % 100
#                 if otime % 100 == 0:
#                     tenmin = int((otime - 1) / 10) - 4
#                 else:
#                     tenmin = int((otime - 1) / 10)
#                 hour = int((otime - 1) / 100)
#                 time = tenmin - ((hour - 6) * 4) + (day * 100) - 62
#                 # 判断星期几
#                 y = int(date / 10000)
#                 m = int(date / 100) - y * 100
#                 d = date - y * 10000 - m * 100
#                 if m == 1 or m == 2:
#                     m += 12
#                     y -= 1
#                 W = int((d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7) + 1
#
#                 if W <= 5:
#                     count_work[time % 100] += 1
#                     numtime_work[time % 100] += min
#                 if W >= 6:
#                     count_wend[time % 100] += 1
#                     numtime_wend[time % 100] += min
#
#         odtime_work = [0 for i in range(100)]
#         for i in range(100):
#             if count_work[i] == 0:
#                 odtime_work[i] = 0
#             else:
#                 odtime_work[i] = round(numtime_work[i] / count_work[i] / 10)
#
#         odtime_wend = [0 for i in range(100)]
#         for i in range(100):
#             if count_wend[i] == 0:
#                 odtime_wend[i] = 0
#             else:
#                 odtime_wend[i] = round(numtime_wend[i] / count_wend[i] / 10)
#
#         num = [[] for i in range(100)]
#         for i in range(100):
#             temp = [station, dstation, minute_st[i], odtime_work[i]]
#             num[i] = temp
#
#         headers = ['ostation', 'dstation', 'time', 'T_work']
#         path = 'E:/Experiment/' + str(dstation) + '/T/T_from_' + str(station) + '_to_' + str(dstation) + '_work.csv'
#         with open(path, 'w', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerow(headers)
#             f_csv.writerows(num)
#
#         num = [[] for i in range(100)]
#         for i in range(100):
#             temp = [station, dstation, minute_st[i], odtime_wend[i]]
#             num[i] = temp
#
#         headers = ['ostation', 'dstation', 'time', 'T_wend']
#         path = 'E:/Experiment/' + str(dstation) + '/T/T_from_' + str(station) + '_to_' + str(dstation) + '_wend.csv'
#         with open(path, 'w', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerow(headers)
#             f_csv.writerows(num)
#
#     print('SUCCESS')

########################################################################################################################
#     # # 修复T？还在考虑需不需要修复
# 生成目标文件夹
code = 101
station_code = []
for i in range(24):
    station_code.append(code)
    code += 1
code = 201
for i in range(25):
    station_code.append(code)
    code += 1
code = 301
for i in range(45):
    station_code.append(code)
    code += 1
code = 601
for i in range(28):
    station_code.append(code)
    code += 1

# path = 'E:/Experiment'
for i in range(len(station_code)):
    # if os.path.isdir(path):
    #     os.mkdir(os.path.join(path,str(station_code[i])))
    # path = 'E:/Experiment/' + str(station_code[i])
    # if os.path.isdir(path):
    #     # os.mkdir(os.path.join(path2, 'OD'))
    #     # os.mkdir(os.path.join(path2, 'T'))
    #     os.mkdir(os.path.join(path, 'Models'))
    path = 'E:/Experiment/' + str(station_code[i]) + '/Models'
    if os.path.isdir(path):
        os.mkdir(os.path.join(path,'LSTM'))
    path = 'E:/Experiment/' + str(station_code[i]) + '/Models/LSTM'
    if os.path.isdir(path):
        os.mkdir(os.path.join(path, 'Part1'))
        os.mkdir(os.path.join(path, 'Part2'))
        os.mkdir(os.path.join(path, 'Part3'))
        os.mkdir(os.path.join(path, 'Part4'))
        os.mkdir(os.path.join(path, 'Part5'))

