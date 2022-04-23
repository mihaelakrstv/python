class Raspberrypi:
    #constructor
    def __init__(self,cpu,memory,model):
        self.cpu=cpu
        self.memory=memory
        self.model=model
    @staticmethod
    def showcpu():
        print("broadcom_cortex72")
    @staticmethod
    def showmemory():
        print("4GB/8GB")
    @staticmethod
    def showmodel():
        print("four")
print(Raspberrypi.showmodel())
print(Raspberrypi.showcpu())
print(Raspberrypi.showmemory())

