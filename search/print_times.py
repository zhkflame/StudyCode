import time

import times


#import的引入路径已工程路径文件夹为基准，比如times直接在此文件夹下，不需要前面加文件名和‘。’，而三个搜索函数在
#serch文件夹下，则需要加文件名和'.'

def print_times(v,L):

    t1=time.time()
    L.index(v)
    t2=time.time()
    index_time=(t2-t1)*1000.

    basic_time=times.time_it(StudyCode.DP.search.liner_search_2.liner_search, v, L)
    for_time=times.time_it(StudyCode.DP.search.bsearch.bsearch, v, L)
    sentinel_time=times.time_it(StudyCode.DP.search.liner_search_3.liner_search, v, L)

    print("%d\t%.03f\t%04f\t%.05f\t%.06f" % \
          (v,basic_time,for_time,sentinel_time,index_time))

L=list(range(1000001))
#search.liner_search_1.liner_search(10,L)
print_times(10,L)
print_times(52353,L)
print_times(876457,L)
