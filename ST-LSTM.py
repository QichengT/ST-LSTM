import numpy as np
# import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import csv
########################################################################################################################
###采用全连接层的结合方法
########################################################################################################################


# 定义常量
rnn_unit = 10  # hidden layer units
input_size = 1  # 输入层维度
output_size = 1  # 输出层维度
lr = 0.0006  # 学习率
# batch_size = 60   # 每批次数据个数
time_step = 20  # 时间步 LSTM的展开

# 全网站点序列
code = 102
station_code = []
for i in range(23):
    if code != 105:
        station_code.append(code)
    code += 1
code = 201
for i in range(24):
    if code != 223:
        station_code.append(code)
    code += 1
code = 301
for i in range(39):
    if code != 303 and code != 305 and code != 306 and code != 307:
        station_code.append(code)
    code += 1
code = 601
for i in range(26):
    if code != 603 and code != 604 and code != 612 and code != 622 and code != 623 and code != 625:
        station_code.append(code)
    code += 1


num = [[] for i in range(len(station_code) * 5)]
headers = ['Station', 'Part', 'ME', 'MAE', 'RMSE', 'MRE']

def get_train_data(batch_size=60):
    # 前28天做训练
    if t == 0:
        train_data1 = data1_1[(t + 1) * 600:3000]
        train_label = label_1[(t + 1) * 600:3000]

    else:
        if t == 4:
            train_data1 = data1_1[:t * 600]
            train_label = label_1[:t * 600]
        else:
            train_data1 = np.append(data1_1[0:t * 600], data1_2[(t + 1) * 600:3000])
            train_label = np.append(label_1[0:t * 600], label_2[(t + 1) * 600:3000])

    train_x = []
    train_y = []
    index_batch = []

    normalize_data = (train_data1 - np.mean(train_data1)) / np.std(train_data1)
    normalize_data = normalize_data[:, np.newaxis]
    normalize_label = (train_label - np.mean(train_label)) / np.std(train_label)
    normalize_label = normalize_label[:, np.newaxis]

    for i in range(len(normalize_data) - time_step):
        if i % batch_size == 0:
            index_batch.append(i)
        x = normalize_data[i:i + time_step]
        y = normalize_label[i:i + time_step]
        train_x.append(x.tolist())
        train_y.append(y.tolist())
    # index_batch.append((len(normalize_data) - time_step))  # batch_index
    return index_batch, train_x, train_y


# 获取测试数据
def get_test_data():
    # 后2天做测试
    test_data = data1_1[t * 600:(t + 1) * 600]
    test_label = label_1[t * 600:(t + 1) * 600]

    test_x = []
    test_y = []

    mean = np.mean(test_label)
    std = np.std(test_label)
    normalized_test_label = (test_label - mean) / std  # 标准化
    normalized_test_data = (test_data - np.mean(test_data)) / np.std(test_data)
    normalized_test_data = normalized_test_data[:, np.newaxis]
    size_step = (len(normalized_test_data) + 1 - time_step) // time_step


    for i in range(size_step - 1):
        x = normalized_test_data[i * time_step:(i + 1) * time_step]
        y = normalized_test_label[i * time_step:(i + 1) * time_step]
        test_x.append(x.tolist())  # tolist从普通的list转变为嵌套list
        test_y.extend(y)  # 将list中的元素添加到另一个list中
    test_x.append((normalized_test_data[(i + 1) * time_step:]).tolist())
    test_y.extend((normalized_test_label[(i + 1) * time_step:]).tolist())

    return mean, std, test_x, test_y

def lstm_model(X, batch_size):
    w_in = weights['in']
    b_in = biases['in']
    w_out = weights['out']
    b_out = biases['out']

    input = tf.reshape(X, [-1, input_size])
    input_layer = tf.matmul(input, w_in) + b_in
    input_layer = tf.reshape(input_layer, [-1, time_step, rnn_unit])
    cell = tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)
    # 执行完全动态展开的输入
    output, final_states = tf.nn.dynamic_rnn(cell, input_layer, initial_state=init_state, dtype=tf.float32)

    output = tf.reshape(output, [-1, rnn_unit])
    output_layer = tf.matmul(output, w_out) + b_out
    return output_layer
# 训练模型

def lstm_train():
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    Y = tf.placeholder(tf.float32, shape=[None, time_step, output_size])
    index_batch, train_x, train_y = get_train_data()
    # print(index_batch)
    pred = lstm_model(X, batch_size=60)

    # 损失函数
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1]) - tf.reshape(Y, [-1])))
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)
    saver = tf.train.Saver(tf.global_variables())
    keep_prob = tf.placeholder(tf.float32)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # saver.restore(sess, module_file)
        # 重复训练2000次
        for i in range(3000):
            for step in range(len(index_batch) - 1):
                _, loss_ = sess.run([train_op, loss], feed_dict={Y: train_y[index_batch[step]:index_batch[step + 1]],
                                                                 X: train_x[index_batch[step]:index_batch[step + 1]],
                                                                 keep_prob: 0.5})
                # print(i, step, index_batch[step+1])
            print(i, loss_)
            if (i + 1) % 300 == 0:
                print("保存模型：", saver.save(sess, save_model_path, global_step=i))



def prediction():
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    mean, std, test_x, test_y = get_test_data()
    pred = lstm_model(X, batch_size=1)
    saver = tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        # 参数恢复
        module_file = tf.train.latest_checkpoint(read_model_path)
        saver.restore(sess, module_file)
        test_predict = []
        for step in range(len(test_x) - 1):
            # print(len(test_x[step]), [test_x[step]])
            prob = sess.run(pred, feed_dict={X: [test_x[step]]})
            predict = prob.reshape((-1))
            test_predict.extend(predict)
        test_y = np.array(test_y) * std + mean
        test_predict = np.array(test_predict) * std + mean
        test_y = test_y[:len(test_predict)]

        # print('test_predict:', test_predict)
        # print('test_y:', test_y)

        # 去除实际值过小的点
        acc_num = 0
        count = 0
        for i in range(len(test_predict)):
            if test_y[i] > 5:
                acc_num += np.abs(test_predict[i] - test_y[i]) / test_y[i]
                count += 1
        if count != 0:
            acc = 1 - acc_num / count  # 偏差

        average = np.average(np.abs(test_predict - test_y))
        max = np.max(np.abs(test_predict - test_y))
        RMSE = np.sqrt(np.average((test_predict - test_y) ** 2))

        print(dstation)

        print('误差最大值：', max)
        print('绝对平均误差：', average)
        print('均方根误差：', RMSE)
        print('准确率百分比', acc)


        temp = [dstation, t + 1, max, average, RMSE, acc]
        num[k * 5 + t] = temp


for k in range(1):
    dstation = 102

    # 数据集
    df = pd.read_csv('E:/Experiment/Outflow/Out_' + str(dstation) + '_step10.csv',
                     encoding='gbk')
    df = np.array(df['Out'])
    data1_1 = df[0:len(df) - 1]
    data1_2 = df[0:len(df) - 1]
    label_1 = df[1:len(df)]
    label_2 = df[1:len(df)]

    for t in range(5):
        print(dstation)
        print('Part', t + 1)
        save_model_path = 'E:/Experiment/' + str(dstation) + '/Models/LSTM/Part' + str(
            t + 1) + '/mydeep-model'
        read_model_path = 'E:/Experiment/' + str(dstation) + '/Models/LSTM/Part' + str(
            t + 1) + '/'


        # 获取训练数据  前28天做训练
        #
        # print(data1)
        # print(data2)
        # print(label)


        # 定义权重和偏置
        weights = {
            'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
            'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
        }
        biases = {
            'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
            'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
        }

        lstm_train()

        tf.reset_default_graph()


        weights = {
            'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
            'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
        }
        biases = {
            'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
            'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
        }

        prediction()

        tf.reset_default_graph()

# path = 'E:/Experiment/Results/Results_LSTM.csv'
# with open(path, 'w', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(num)
