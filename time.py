import time
def outfunction(func):
    def inner(*args,**kwargs):
        starttime=time.time()
        func(*args,**kwargs)
        excectiontime=time.time()-starttime
        print(f"functionname {func} and excectiontime {excectiontime}")
    return inner
@outfunction
def s():
    result=0
    for i in range(0,2):
        result=result+i
    return result
s()
