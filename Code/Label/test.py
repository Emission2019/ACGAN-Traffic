from scapy.all import *
import time, datetime

def GenerateLabel(InPcapPath):

    StartTime = '2017-06-17 15:27:00'
    OverTime = '2017-06-17 15:29:00'
    StartTimeArray = time.strptime(StartTime, "%Y-%m-%d %H:%M:%S")
    OverTimeArray = time.strptime(OverTime, "%Y-%m-%d %H:%M:%S")
    StartTimeStamp = float(time.mktime(StartTimeArray))
    OverTimeStamp = float(time.mktime(OverTimeArray))

    print(StartTimeStamp)
    print(OverTimeStamp)

    print('Now :'+InPcapPath)
    Packets = rdpcap(InPcapPath)
    count = 0
    for Packet in Packets:
        TempStamp = repr(Packet.time)
        TimeStamp = float(TempStamp[9:-2])
        if TimeStamp>=StartTimeStamp and TimeStamp<=OverTimeStamp:
            count+=1
    print(count)

    #print(SkipCount)

if __name__ == '__main__':
    InputDir = os.getcwd() + '\InputSet'  #当前输入目录
    #OutputDir = os.getcwd() + '\OutputSet' #当前输出目录
    InputName = "06_17_2017-be-20170216-apps-baby.com.SurpriseCollector.pcap"  #设置为当前要处理的文件名
    InPcapPath = InputDir +'\\'+ InputName
    GenerateLabel(InPcapPath)
