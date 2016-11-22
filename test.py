'''
    Created by pqh on 2016/8/27.
'''

from roundtable import RoundTable
from roundtableQuestion import RoundTableQuestion
import threading
import zhclient
from time import sleep


workingThread = 0 #正在工作的线程
mutex =threading.Lock() #线程锁

def proc(i ,zhuanlanList):
    while len(zhuanlanList) >0:
        global workingThread
        if mutex.acquire(1):
            workingThread +=1
            # 获取data
            zhuanlan=None
            if len(zhuanlanList) >0 :
                zhuanlan=zhuanlanList.pop(0)
            mutex.release()
            if zhuanlan is not None:
                try:
                    questions = RoundTableQuestion.getQuestionListByParent(zhuanlan)
                    #RoundTableQuestion.saveQuestions(questions,zhclient.ClientInstance._mongo._tbquestion)

                    #sleep(4)
                except Exception as e:
                    print("proc RoundTableQuestions error: {0}".format(e))
                else:
                    pass
                finally:
                    pass
            if mutex.acquire(1):
                workingThread -= 1
                mutex.release()
    return


# 主函数
if __name__ == '__main__':
    r= RoundTable()
    # 1、加载圆桌专题列表 ,2、后面将通过该列表逐一加载每个专题中的问题 ，3、再然后加载每个问题对应的回答
    r.loadRoundTableList()
    #用线程队列启动爬虫
    threads = []
    for i in range(1): #访问太快会被检测到并限制使用 ,需要权衡线程数量
        threads.append(threading.Thread(target=proc,args=(i,r._list)))
    for t in threads:
        t.setDaemon(True)
        t.start()
        #t.join()
    while (workingThread > 0):
        sleep(3)
        print (workingThread,' thread is in working... waiting... ')
    print ('all job is done....')






    '''
    json.dump(json.dumps(i.__dict__),f)
    f.write("----------------------------\n")
    for j in list :
        json.dump(json.dumps(j.__dict__), f)
    f.write("\n\n\n")
    #print (i._name ,i._href)
    '''

#list ,offset = r.getNextJsonPage (126)
#print (list )
#print (offset)
