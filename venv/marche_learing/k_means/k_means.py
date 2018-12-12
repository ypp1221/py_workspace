from numpy import *
import time
import matplotlib.pyplot as plt

def get_length(a,b):
    return sqrt(sum(power(a-b,2)))

def initCentroids(dataSet,k):
    #get sample dim
    numSample,dim = dataSet.shape
    #save this data to centroids
    centroids = zeros((k,dim))
    for i in range(k):
        index = int(random.uniform(0,numSample))
        centroids[i,:] = dataSet[index,:]
    return centroids



def k_means1(dataSet , k):
    numSamples = dataSet.shape[0]
    clusterAssment = mat(zeros((numSamples,2)))
    clusterChanged = True

    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        for i in xrange(numSamples):
            min_length = 100000.00
            min_index = 0
            for j in range(k):
                length = get_length(dataSet[i,:],centroids[j,:])
                if min_length > length:
                    min_length = length
                    min_index = j

            if clusterAssment[i,0] != min_index:
                clusterChanged= True

                clusterAssment[i,:] = min_index, min_length**2

        #update centroids
        for j in range(k):
            point = dataSet[nonzero(clusterAssment[:,0].A== j)[0]]
          #  s = mean(point,axis=0)
            #if get_length(centroids[j,:],s) > 0.5:
        #        clusterChanged = True
            centroids[j,:] = mean(point,axis=0)

        return centroids,clusterAssment


def showCluster(dataSet,k,centroids,clusterAssment):
    numSamples ,dim = dataSet.shape
    if dim !=2 :
        print  "sorry! I can not draw because the dimension of you data is not 2"
        return 1
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']

    for i in xrange(numSamples):
        markIndex =int(clusterAssment[i,0])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
		plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
    plt.show()




def getData():
    dataSet = []
    file = open('./test.txt')
    for line in file.readlines():
        lineAttr = line.strip().split('\t')
        dataSet.append([float(lineAttr[0]),float(lineAttr[1])])

    dataSet = mat(dataSet)
    k = 4
    centroids, clusterAssment = k_means1(dataSet,k)
    showCluster(dataSet,k,centroids,clusterAssment)
getData()
