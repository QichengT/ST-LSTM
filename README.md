# ST-LSTM
A Deep Learning Approach Combined Spatio-Temporal Features for Short-Term Forecast in Rail Transit
本项目代码是论文“ST-LSTM: A Deep Learning Approach Combined Spatio-Temporal Features for Short-Term Forecast in Rail Transit”中的模型的实现。
论文网址：https://www.hindawi.com/journals/jat/2019/8392592/
论文中的数据下载：https://drive.google.com/open?id=1RuH080U_9PHdh9B9VoOjNurODWnHAYaf

简介：传统的采用机器学习的交通客流预测，是将时序交通数据通过LSTM等人工神经网络进行学习。本文的模型在此基础上，引入了另一特征——空间特征作为输入。
因为城市轨道交通的特性：站点间的固定距离、稳定的行驶速度、稳定的发车班次。站点间空间距离的远近就可以用旅行时间差来表达，这样站点间空间关系的影响
就可以转化为带有时间滞的时序数据，加入到客流预测中。实验证明预测精度有所提升。

本项目代码分为三个文件：
extraction.py：从MongoDB中读取目标站点的刷卡数据，并计算各类相关的信息，比如进出站人数，个站点间的平均时耗。
spatial features.py：根据extraction.py中提取到的数据计算目标站点的SCM（空间关系矩阵）和TCM（时间差矩阵）矩阵，并计算每一时刻的空间特征。
ST-LSTM.py：预测模型的实现，采用Tensorflow框架。将时间特征和空间特征结合预测目标站点的出站客流。
