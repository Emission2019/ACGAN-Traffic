# 数据集标签
---
- 因为原始数据集是Pcap形式的原始流量，因此我们需要自行对其每一分类做出标签。


## 主要思路
---
以数据集主页提供信息以及CIC实验室所给出的它们标签好的CSV格式数据集的信息为参考
1. 因为所提供的Pcap原始文件体积都偏大，Python脚本无法直接处理。因此先利用Wireshark所提供的命令行工具Editcap，筛选出某事时间段内的通信流量。
	- 例如，参考信息中所提供的标签A的流量通信时间为StartTime-OverTime，则先筛选出这个时间段类流量；
2. 通过第一步筛选，可能数据包仍然很大，Python脚本依旧无法直接处理，继续使用Editcap工具将大Pcap包切分成若干个小的Pcap包处理；
3. 利用Python脚本 GenerateLabel.py ，根据上述提到的参考信息，通过设置时间和IP地址的方法，筛选出所需流量。
4. 主要时差和夏令时的问题，数据集使用的为 -4区 时间。

# 具体处理过程
---
## Botnet
- IP列表: ['205.174.165.73','192.168.10.9','192.168.10.8','192.168.10.5','192.168.10.15','192.168.10.14']
- 时间段: 2017-07-07 10:00:00 -- 2017-07-07 13:00:00

## PortScan
- IP列表: ['172.16.0.1','192.168.10.50']
- 时间段: 2017-07-07 13:00:00 -- 2017-07-07 15:30:00

## DDos
- 从Csv格式的该项数据发现，16：10之后相同IP下含有许多标签为Benign数据，因此抛弃之后数据。
- IP列表: ['192.168.10.50', '172.16.0.1']
- 时间段: 2017-07-07 15:55:00 -- 2017-07-07 16:10:00

## Web Attack - Brute Force
- IP列表:['192.168.10.50', '172.16.0.1'] 
- 时间段: 2017-07-06 09:20:00 -- 2017-07-06 10:00:00

## Web Attack - XSS
- IP列表:['192.168.10.50', '172.16.0.1'] 
- 时间段: 2017-07-06 10:15:00 -- 2017-07-06 10:35:00

## Web Attack - Sql Injection
- IP列表:['192.168.10.50', '172.16.0.1'] 
- 时间段: 2017-07-06 10:40:00 -- 2017-07-06 10:42:00

## Benign
- Monday 全体流量均为正常流量