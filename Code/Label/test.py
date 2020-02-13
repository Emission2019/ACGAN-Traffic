from scapy.all import *


def GenerateLabel(InPcapPath,IpSet,OutPcapPath):
    print('Now :'+InPcapPath)
    Packets = rdpcap(InPcapPath)
    OutPcap = PcapWriter(OutPcapPath)
    SkipCount = 0
    for Packet in Packets:

        print(repr(Packet))
        OutPcap.write(Packet)

    #print(SkipCount)

if __name__ == '__main__':
    InputDir = os.getcwd() + '\InputSet'  #当前输入目录
    OutputDir = os.getcwd() + '\OutputSet' #当前输出目录
    InputName = "Tuesday-WorkingHours" \
                ".pcap"  #设置为当前要处理的文件名
    OutputName = "Test.pcap"
    InPcapPath = InputDir +'\\'+ InputName
    OutPcapPath = OutputDir +'\\' + OutputName    #输出文件名
    IpSet=['52.94.232.33','10.42.0.211']        #填入需获取的IP地址
    GenerateLabel(InPcapPath,IpSet,OutPcapPath)
