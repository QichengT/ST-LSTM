import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# s = 0
# for c in range(len(station_code)):
# dstation = 334
    # # # ########################################################################################################################
    # 将带有T时间差的od进站人数求和作为空间影响数据流
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
# count = [0 for i in range(3100)]
# for i in range(len(station_code)):
#     station = station_code[i]
#
#     path = 'E:/InOut_data/Out_' + str(dstation) + '/OD/OD_In_' + str(station) + '_' + str(dstation) + '_step10.csv'
#     f = pd.read_csv(path, encoding='gbk')
#     df = np.array(f['od_In'])
#     od_in = df[0:len(df)]
#     df = np.array(f['date'])
#     date = df[0:len(df)]
#
#     path = 'E:/InOut_data/Out_' + str(dstation) + '/T/T_' + str(station) + '_' + str(dstation) + '_step10_work.csv'
#     f = pd.read_csv(path, encoding='gbk')
#     df = np.array(f['T_work'])
#     num_T_work = df[0:len(df)]
#
#     path = 'E:/InOut_data/Out_' + str(dstation) + '/T/T_' + str(station) + '_' + str(dstation) + '_step10_wend.csv'
#     f = pd.read_csv(path, encoding='gbk')
#     df = np.array(f['T_wend'])
#     num_T_wend = df[0:len(df)]
#
#     for k in range(len(od_in)):
#         y = int(date[k] / 10000)
#         m = int(date[k] / 100) - y * 100
#         d = date[k] - y * 10000 - m * 100
#         W = int((d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7) + 1
#
#         n = k % 100
#         if W <= 5:
#             if n + num_T_work[n] < 99:
#                 count[k + num_T_work[n]] += od_in[k]
#
#         if W >= 6:
#             if n + num_T_wend[n] < 99:
#                 count[k + num_T_wend[n]] += od_in[k]
#
# temp = []
# date = 20170300
# num = [[0] for i in range(len(count))]
#
# for i in range(3100):
#     if (i % 100 == 0):
#         date += 1
#     temp = [dstation, date, minute_st[i], count[i]]
#     num[i] = temp
#     print(temp)
#
# headers = ['dstation', 'date', 'time', 'num_od']
# path = 'E:/InOut_data/Out_' + str(dstation) + '/data/Out_' + str(dstation) + '_od_step10.csv'
# with open(path, 'w', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(num)

########################################################################################################################
# # # 计算10分钟级平均ODC
# # code = 101
# # station_code = []
# # for i in range(24):
# #     station_code.append(code)
# #     code += 1
# # code = 201
# # for i in range(25):
# #     station_code.append(code)
# #     code += 1
# # code = 301
# # for i in range(45):
# #     station_code.append(code)
# #     code += 1
# # code = 601
# # for i in range(28):
# #     station_code.append(code)
# #     code += 1
# #
# minute = 630
# minute_st = []
# for i in range(100):
#     minute_st.append(minute)
#     minute += 10
#     if minute % 100 == 60:
#         minute += 40
#     if minute == 2310:
#         minute = 630
#
# for k in range(len(station_code)):
#     dstation = station_code[k]
#     print(dstation)
#     for i in range(len(station_code)):
#         station = station_code[i]
#
#         path = 'E:/Experiment/' + str(dstation) + '/OD/OD_from_' + str(station) + '_to_' + str(dstation) + '.csv'
#         f = pd.read_csv(path, encoding='gbk')
#         df = np.array(f['od_In'])
#         od_in = df[0:len(df)]
#
#         path = 'E:/Experiment/Inflow/In_' + str(station) + '_step10.csv'
#         f = pd.read_csv(path, encoding='gbk')
#         df = np.array(f['In'])
#         num_in = df[0:len(df)]
#         df = np.array(f['date'])
#         date = df[0:len(df)]
#
#         num_odc_work = [0 for i in range(100)]
#         num_odc_wend = [0 for i in range(100)]
#         count_work = 0
#         count_wend = 0
#         for i in range(len(od_in)):
#             y = int(date[i] / 10000)
#             m = int(date[i] / 100) - y * 100
#             d = date[i] - y * 10000 - m * 100
#             if m == 1 or m == 2:
#                 m += 12
#                 y -= 1
#             W = int((d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7) + 1
#             if W <= 5:
#                 count_work += 1
#             if W >= 6:
#                 count_wend += 1
#
#             if num_in[i] == 0:
#                 continue
#             else:
#                 odc = od_in[i] / num_in[i]
#                 if W <= 5:
#                     num_odc_work[i % 100] += odc
#                 if W >= 6:
#                     num_odc_wend[i % 100] += odc
#
#         count_work = int(count_work / 100)
#         count_wend = int(count_wend / 100)
#         for i in range(100):
#             num_odc_work[i] = num_odc_work[i] / count_work
#             num_odc_wend[i] = num_odc_wend[i] / count_wend
#
#         num = [[] for i in range(100)]
#         for i in range(100):
#             temp = [station, dstation, minute_st[i], num_odc_work[i]]
#             num[i] = temp
#
#         headers = ['ostation', 'dstation', 'time', 'SCM_work']
#         path = 'E:/Experiment/' + str(dstation) + '/SCM/SCM_from_' + str(station) + '_to_' + str(
#             dstation) + '_work.csv'
#         with open(path, 'w', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerow(headers)
#             f_csv.writerows(num)
#
#         num = [[] for i in range(100)]
#         for i in range(100):
#             temp = [station, dstation, minute_st[i], num_odc_wend[i]]
#             num[i] = temp
#
#         headers = ['ostation', 'dstation', 'time', 'SCM_wend']
#         path = 'E:/Experiment/' + str(dstation) + '/SCM/SCM_from_' + str(station) + '_to_' + str(
#             dstation) + '_wend.csv'
#         with open(path, 'w', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerow(headers)
#             f_csv.writerows(num)
#
#     print('SUCCESS')


########################################################################################################################
# 计算ODC与In相差T相乘的总和
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

minute = 630
minute_st = []
for i in range(3100):
    minute_st.append(minute)
    minute += 10
    if minute % 100 == 60:
        minute += 40
    if minute == 2310:
        minute = 630

for k in range(len(station_code)):
    dstation = station_code[k]
    print(dstation)
    num_od = [0 for i in range(3100)]
    for i in range(len(station_code)):
        station = station_code[i]
        path = 'E:/Experiment/Inflow/In_' + str(station) + '_step10.csv'
        f = pd.read_csv(path, encoding='gbk')
        df = np.array(f['In'])
        num_in = df[0:len(df)]
        df = np.array(f['date'])
        date = df[0:len(df)]

        path = 'E:/Experiment/' + str(dstation) + '/SCM/SCM_from_' + str(station) + '_to_' + str(
            dstation) + '_work.csv'
        f = pd.read_csv(path, encoding='gbk')
        df = np.array(f['SCM_work'])
        num_odc_work = df[0:len(df)]

        path = 'E:/Experiment/' + str(dstation) + '/SCM/SCM_from_' + str(station) + '_to_' + str(
            dstation) + '_wend.csv'
        f = pd.read_csv(path, encoding='gbk')
        df = np.array(f['SCM_wend'])
        num_odc_wend = df[0:len(df)]

        path = 'E:/Experiment/' + str(dstation) + '/T/T_from_' + str(station) + '_to_' + str(dstation) + '_work.csv'
        f = pd.read_csv(path, encoding='gbk')
        df = np.array(f['T_work'])
        num_T_work = df[0:len(df)]

        path = 'E:/Experiment/' + str(dstation) + '/T/T_from_' + str(station) + '_to_' + str(dstation) + '_wend.csv'
        f = pd.read_csv(path, encoding='gbk')
        df = np.array(f['T_wend'])
        num_T_wend = df[0:len(df)]

        for k in range(len(num_in)):
            y = int(date[k] / 10000)
            m = int(date[k] / 100) - y * 100
            d = date[k] - y * 10000 - m * 100
            W = int((d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7) + 1

            n = k % 100
            if W <= 5:
                if n + num_T_work[n] < 99:
                    od = num_in[k] * num_odc_work[n]
                    num_od[k + num_T_work[n]] += od

            if W >= 6:
                if n + num_T_wend[n] < 99:
                    od = num_in[k] * num_odc_wend[n]
                    num_od[k + num_T_wend[n]] += od

    temp = []
    date = 20170300
    num = [[0] for i in range(len(num_od))]

    for i in range(3100):
        if (i % 100 == 0):
            date += 1
        od = int(round(num_od[i]))
        temp = [dstation, date, minute_st[i], od]
        num[i] = temp
        print(temp)

    headers = ['dstation', 'date', 'time', 'S_features']
    path = 'E:/Experiment/' + str(dstation) + '/S_features/S_features_' + str(dstation) + '_work_wend.csv'
    with open(path, 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(num)

    print('SUCCESS')





    # # ########################################################################################################################
    # # 原数据与空间影响量折线图
    # path = 'E:/InOut_data/Out_' + str(dstation) + '/data/Out_' + str(dstation) + '_step10.csv'
    # f = pd.read_csv(path, encoding='gbk')
    # df = np.array(f['Out'])
    # out1 = df[0:len(df)]
    # #
    # path = 'E:/InOut_data/Out_' + str(dstation) + '/data/Out_' + str(dstation) + '_odc_num_step10_work-end.csv'
    # # path = 'E:/InOut_data/Out_' + str(dstation) + '/data/Out_' + str(dstation) + '_od_step10.csv'
    # f = pd.read_csv(path, encoding='gbk')
    # df = np.array(f['num_odc'])
    # # df = np.array(f['num_od'])
    # out2 = df[0:len(df)]
    #
    # acc_num = 0
    # count = 0
    # for i in range(len(out2)):
    #     if out1[i] > 10:
    #         acc_num += np.abs(out2[i] - out1[i]) / out1[i]
    #         count += 1
    # acc = 1 - (acc_num / count)  # 偏差
    #
    # average = np.average(np.abs(out2 - out1))
    # max = np.max(np.abs(out2 - out1))
    # RMSE = np.sqrt(np.average((out2 - out1) ** 2))
    #
    # # print((3100 - count)/31)
    # print('误差最大值：', max)
    # print('绝对平均误差：', average)
    # print('均方根误差：', RMSE)
    # print('准确率百分比', acc)
    #
    # plt.figure()
    # plt.title(' ')
    # plt.plot(list(range(len(out1))), out1, color='r')
    # # plt.plot(list(range(len(out2))), out2, color='b')
    # plt.show()


