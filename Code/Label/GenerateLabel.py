# 因为每一个原始数据集体积过于庞大，因此不进行批量化处理
#输入目录：.\InputSet
#输出目录：.\OutputSet
#流程 ：  1、将待处理Pcap文件放入.\InputSet目录
#         2、将InputName设为待处理的文件名
#         3、设置OutputName
#         4、在IPSet中设置 IP地址
#         5、Go


from scapy.all import *


def GenerateLabel(InPcapPath,IpSet,OutPcapPath):

    #================时间设置=============================
    StartTime = '2017-06-17 15:27:00'
    OverTime = '2017-06-17 15:29:00'
    #=====================================================

    StartTimeArray = time.strptime(StartTime, "%Y-%m-%d %H:%M:%S")
    OverTimeArray = time.strptime(OverTime, "%Y-%m-%d %H:%M:%S")
    StartTimeStamp = float(time.mktime(StartTimeArray))
    OverTimeStamp = float(time.mktime(OverTimeArray))


    print('Now :'+InPcapPath)
    Packets = rdpcap(InPcapPath)
    OutPcap = PcapWriter(OutPcapPath)
    SkipCount = 0
    for Packet in Packets:
        TempStamp = repr(Packet.time)
        TimeStamp = float(TempStamp[9:-2])
        if TimeStamp >= StartTimeStamp and TimeStamp <= OverTimeStamp:
            try:
                if (Packet['IP'].src in IpSet) and  (Packet['IP'].dst in IpSet):
                    print(repr(Packet))
                    OutPcap.write(Packet)
            except:
                SkipCount+=1
                continue
    print(SkipCount)

if __name__ == '__main__':
    InputDir = os.getcwd() + '\InputSet'  #当前输入目录
    OutputDir = os.getcwd() + '\OutputSet' #当前输出目录
    InputName = "06_17_2017-be-20170216-apps-baby.com.SurpriseCollector.pcap"  #设置为当前要处理的文件名
    OutputName = "Test.pcap"
    InPcapPath = InputDir +'\\'+ InputName
    OutPcapPath = OutputDir +'\\' + OutputName    #输出文件名
    IpSet=['52.94.232.33','10.42.0.211']        #填入需获取的IP地址
    GenerateLabel(InPcapPath,IpSet,OutPcapPath)
