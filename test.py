import numpy as np
import matplotlib.pylab as plt


def TitleName(msg):
    print("\n\n\t★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\t")
    print("\t\t\t\t\t\t\t\t"+msg)
    print("\t★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\t\n")


def UnLine ():
    print("\t-----------------------------------------------------------------\t")



def AND_GATE (x1, x2):
    w1, w2, theta = 0.5 ,0.5 , 0.7
    tmp = w1*x1 + w2*x2
    if tmp <= theta:
        return 0
    elif tmp >theta:
        return 1

def OR_GATE (x1,x2):
    w1, w2, theta = 1, 1, 1
    tmp = w1 * x1 + w2 * x2
    if tmp < theta:
        return 0
    elif tmp >= theta:
        return 1

def NOT_GATE (a):
        if a >= 1:
            return 0
        else:
            return 1

def XOR_GATE (x1,x2):
    return AND_GATE(NOT_GATE(AND_GATE(x1, x2)), OR_GATE(x1, x2))



GATE_LIST = [[0,0],
             [0,1],
             [1,0],
             [1,1]]

print(GATE_LIST)


##1. Perceptron 이해
TitleName("SLP 기초 ")

print("start")
for a,b in GATE_LIST:
    print("\n<==== AND_GATE result ===>")
    print("a: " , a , "b: ",b)
    print(AND_GATE(a,b))


UnLine()


##2. Bias의 도입
TitleName("Bias 도입")

input_data = np.array([0,1])
weight_data = np.array([0.5,0.5])
bias = -0.7

print("input : ", input_data , "\tweight_data : ",weight_data, "\tbias :", bias)

## x1*w1 + x2+w2+ bias numpy 표현

out_data = np.sum(input_data*weight_data)+bias

print("output :", out_data)

UnLine()


## 3. MLP (Multi Layer Perceptron)
TitleName("MLP의 이해 ")
## XOR GATE   =-> (NAND ,OR) AND


for a,b in GATE_LIST:

    print(a,b,"\tXOR : ",XOR_GATE(a,b))

UnLine()


## 4. Step Functon

TitleName("계단 함수 구현")


def step_function(x):
    y= x>0
    return y.astype(np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))


x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)

print("x ramge : ", x.shape)

##plt.plot(x,y)
##plt.ylim(-0.1,1.1)
##plt.show()

UnLine()

## 5. 다차원 배열 계싼

TitleName("다차원 배열의 계산 ")


##  2*2 2*2 계산 np.dot 의 활용

a = np.array([[10,20],[30,40]])
b = np.array([[10,20],[30,40]])

print(" A Shape :" , a.shape, "\t B shape :", b.shape)

print(np.dot(a,b))


## 변형
a = np.array([[10,20,30,50],[30,40,30,10],[10,20,30,40]])
b = np.array([[10,20],[30,40],[30,20],[90,14]])

print(" A Shape :" , a.shape, "\t B shape :", b.shape)

print(np.dot(a,b))


UnLine()


## 6. 2개의 입력 3개의 출력  2 | 2*3  => 3

a = np.array([1,2])
b = np.array([[2,3,4],[7,8,9]])

result = np.dot(a,b)

print(" 2 Input and 3 ouput : ",result)


## 7. 확장된 입력

TitleName(" 확장된 입력")


####
#### Input 과 1층 노드 구현

x = np.array([1.0,2.0])
w1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.5]])
b1 = np.array([0.1,0.2,0.3])

result = np.dot(x,w1)+b1

print(x.shape)
print(w1.shape)
print(b1.shape)
print(result.shape)
print("Input: ",x,"\nWeight: \n", w1,"\nBias: ",b1)
UnLine()
print("hypothesis is : " , result)

new_input = sigmoid(result)
print("After activation function: ", new_input)

####
#### 1층의 결과 값과 2층 노드 구현 2층 노드는 4개로 구현 예정

print("\t======================2층=====================\n")

w2 = np.array([[0.1,0.2,0.3,0.4],[0.2,0.4,0.6,0.8],[0.1,0.3,0.5,0.7]])
b2 = np.array([0.6,0.4,0.3,0.2])
print(new_input.shape)
print(w2.shape)
print(b2.shape)
result = np.dot(new_input,w2) +b2
print(result.shape)


print("Input: ",x,"\nWeight: \n", w1,"\nBias: ",b1)
UnLine()
print("hypothesis is : " , result)
new_input = sigmoid(result)
print("After activation function: ", new_input)


####
#### 2층의 결과 값과 3층 노드 구현 3층 노드는 1개로 구현 예정

print("\t======================3층=====================\n")

w3 = np.array([[0.1],[0.2],[0.5],[0.6]])
b3 = np.array([-0.1])

print(new_input.shape)
print(w3.shape)
print(b3.shape)

result = np.dot(new_input,w3) +b3
print(result.shape)


print("Input: ",x,"\nWeight: \n", w1,"\nBias: ",b1)
UnLine()
print("hypothesis is : " , result)
new_input = sigmoid(result)
print("After activation function: ", new_input)
