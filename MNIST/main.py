import random
#파이토치
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor
#인공지능 클래스 만들기
import torch.nn as nn
#데이터로더 import
from torch.utils.data import DataLoader
#이미지 보기 위한 라이브러리
import matplotlib.pyplot as plt

#1. Collect data 데이터 수집, 데이터 타입ToTensor 으로 전환
#MNIST에 있는 traingdataset 수집(test_data는 train=False로 둬서 차이둠.)
train_dataset=datasets.MNIST(root='data',train=True,download=True, transform=ToTensor())
test_dataset=datasets.MNIST(root='data',train=False,download=True, transform=ToTensor())

#First training_dataset 확인하기 
#image, label =train_dataset[0]
#plt.imshow(image,cmap='gray')
#plt.show()
#label 을 통해 5임을 확인할 수 있다.
#print('label:',label) 

#2. Prepare data 데이터 준비
#모델 그룹화:한번에 처리할 양
batch_size=100 #100개의 이미지를 processing
train_dataloader = DataLoader(train_dataset,batch_size=batch_size,shuffle=True)
test_dataloader = DataLoader(test_dataset,batch_size=batch_size)#test이기 때문에 shuffleX

#Device 설정
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Device: {device}')

#3. model 만들기
#입력: 픽셀의 갯수
input_size=28*28
#출력: 0~9 예측
output_size=10

#nn.Module(전반적인 틀)을 이용해 클래스 선언
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        #픽셀 이미지가 정사각형 이미지이므로 28*28이 아닌 flat한 748로 만들기
        self.flatten = nn.Flatten()
        #핵심, 머신러닝 기본알고리즘:Linear, input_size와 output_size를 파라미터로 예측
        self.linear= nn.Linear(input_size, output_size)

    #x= input, flatten에 의해 flat된 뒤 한줄로 나온 픽셀값들은 linear에 들어가 알고리즘 작동
    def forward(self,x):
        out=self.flatten(x)
        out=self.linear(out)
        return out

model= NeuralNet().to(device)

#4. training data 모델 훈련
#4-1. laerning rate: 학습 속도, 최적화된 값을 통해 학습시킨다.(책 읽는 것과 동일)
learning_rate=0.001
#4-2. loss_function: 실제 값과 오차
loss_fn=nn.CrossEntropyLoss()
#4-3. optimizer: 차이 줄이기위한 역할 
optimizer= torch.optim.SGD(model.parameters(),lr=learning_rate)

#train함수 만들기
def train(train_dataloader,model,loss_fin,optimizer):
    #traind_dataloader를 가져와서 batch로 processing X:이미지의 픽셀, y:답
    for batch,(X,y) in enumerate(train_dataloader):
        X,y=X.to(device), y.to(device)
        #예측값
        pred=model(X)
        
        #실제값y와 차이 비교
        loss=loss_fn(pred,y)
        #로스율 줄이기 위한 방법
        loss.backward()
        #optimizer가 parameter를 바꿔서 정확도 증진
        optimizer.step()
        optimizer.zero_grad()

    #batch가 100번 반복할때 마다 출력
        if batch%100==0:
            loss=loss.item()
            #로스율과 배치 갯수 확인
            print(f'loss:{loss}, batch:{batch}')

#5. test data
#test 함수 만들기
def test(test_dataloader,model,loss_fin):
    size=len(test_dataloader.dataset)
    num_batches=len(test_dataloader)
    test_loss,correct=0,0

    #test 파라미터 유지시키기
    with torch.no_grad():
        for X,y in test_dataloader:
            X,y =X.to(device), y.to(device)
            pred= model(X)
            test_loss+=loss_fn(pred,y).item()
            correct+=(pred.argmax(1)==y).type(torch.float).sum().item()
    test_loss/=num_batches
    correct/=size
    print(f"Test Error:\n Accuracy:{(100*correct):0.1f}%, Avg loss:{test_loss:>8f}\n")

#코드 반복 횟수 10회
epochs=10
for t in range(epochs):
    print(f"Epoch {t+1}\n -----------------")
    train(train_dataloader,model,loss_fn,optimizer)
    test(test_dataloader,model,loss_fn)
print("done!")

#결과 확인
real_test_dataset=datasets.MNIST(root='data',train=False,download=True)
rand=random.randint(0,9999)
X,y=test_dataset[rand][0],test_dataset[rand][1]
A=real_test_dataset[rand][0]

with torch.no_grad():
    pred=model(X)
    predicted,actual=pred[0].argmax(0),y
    print(f"predicted:{predicted},actual:{actual}")
    plt.imshow(A,cmap='gray')
    plt.show()