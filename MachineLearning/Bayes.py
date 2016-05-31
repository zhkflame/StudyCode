import csv
import random
import math
def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

'''
朴素贝叶斯模型包含训练数据集中数据的特征，然后使用这个数据特征来做预测。

所收集的训练数据的特征，包含相对于每个类的每个属性的均值和标准差。举例来说，如果如果有2个类和7个数值属性，然后我们需要每一个属性（7）和类（2）的组合的均值和标准差，也就是14个属性特征。

在对特定的属性归属于每个类的概率做计算、预测时，将用到这些特征。

我们将数据特征的获取划分为以下的子任务：

1. 按类别划分数据
2. 计算均值
3. 计算标准差
4. 提取数据集特征
5. 按类别提取属性特征
'''

'''
首先将训练数据集中的样本按照类别进行划分，然后计算出每个类的统计数据。
我们可以创建一个类别到属于此类别的样本列表的的映射，并将整个数据集中的样本分类到相应的列表
'''
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):  #[-1]表示最后一个元素，从后往前数
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

'''
计算均值

我们需要计算在每个类中每个属性的均值。均值是数据的中点或者集中趋势，
在计算概率时，我们用它作为高斯分布的中值。

我们也需要计算每个类中每个属性的标准差。标准差描述了数据散布的偏差，
在计算概率时，我们用它来刻画高斯分布中，每个属性所期望的散布。

标准差是方差的平方根。方差是每个属性值与均值的离差平方的平均数。
注意我们使用N-1的方法（译者注：参见无偏估计），也就是在在计算方差时，
属性值的个数减1。
'''

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

'''
提取数据集的特征

现在我们可以提取数据集特征。
对于一个给定的样本列表（对应于某个类），我们可以计算每个属性的均值和标准差。

zip函数将数据样本按照属性分组为一个个列表，然后可以对每个属性计算均值和标准差。
'''
def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    #dataset的每个项都是一个列表，前两个表示特征，最后一个表示分类，这里是求特征的均值和方差
    del summaries[-1]
    return summaries


#合并代码，我们首先将训练数据集按照类别进行划分，然后计算每个属性的摘要。

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        #print(classValue,instances)
        summaries[classValue] = summarize(instances)
        #print(summarize(instances))
    return summaries
    #summaries保存的是每个类别的每类特征的方差和均值


#求给定x的高斯分布概率
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent


#求单一样本属于每个类别的概率，由probabilities保存
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):   #遍历每一个特征
            mean, stdev = classSummaries[i]    #取得每一个特征的均值和方差
            x = inputVector[i]                 #取得输入特征
            probabilities[classValue] *= calculateProbability(x, mean, stdev)  #将不同特征属于此类别概率乘积当成属于属于此类别的概率
    return probabilities

#对比数据每个类的概率，求得最应该属于哪个类
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

#对多有样本进行属于某个类
def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions

#根据测试集结果，计算分类准确路
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0


def main():
    filename = 'testBayes.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    print('Split %s rows into train=%d and test=%d rows'%(len(dataset), len(trainingSet), len(testSet)))
    # prepare model
    summaries = summarizeByClass(trainingSet)
    # test model
    predictions = getPredictions(summaries, testSet)
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: %f'%(accuracy))

main()





