import sys,os

print("python execution : ",sys.executable)
print("current path : ",os.getcwd())
print("os list : ",os.listdir(os.path.join(os.getcwd(),"PECNett")))