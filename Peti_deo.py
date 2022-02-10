import numpy as np
import matplotlib.pyplot as plt

timeK=time[0:imaxwalk];  #time osa samo za 1 korak
odbK=np.arange(0, imaxwalk, 1)  #osa po odbircima za 1 korak
plt.figure()


  #imeK je osa samo za 1 korak
  #odbK je osa po odbircima za 1 korak
for i in range(0,len(minwalk)-1):
    gr=[];
    gr=brzR1[(minwalk[i]-poc):(minwalk[i+1]-poc)];
    print(len(gr))

    n=len(gr);
    plt.plot(odbK[0:n],gr);
   

odbKL=np.arange(0, imaxwalkL, 1)  #osa po odbircima za 1 korak



 
  #odbKL je osa po odbircima za 1 korak
for i in range(0,len(minwalkL)-1):
    gL=[];
    gL=brzL1[(minwalkL[i]-pocL):(minwalkL[i+1]-pocL)];
    print(len(gL))

    n=len(gL);
    plt.plot(odbKL[0:n],gL);
   
plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.title('Profili brzine')
plt.grid(True);
plt.show();
 



plt.figure()
 
  
# 
nputR=[];
for i in range(len(brzR)):
    nputR.append(0);
for i in range(0,len(brzR)):
    nputR[i]=putR[0][i];
      
  
  
for i in range(0, len(minwalk)-1):
    gr=[];
    gr=nputR[(minwalk[i]-poc):(minwalk[i+1]-poc)];
  
   
    n=len(gr);
  
    gr1=[];
    for j in range(0,n):
        gr1.append(0);
    if(i==0):
        for j in range(0,n):
            gr1[j]=gr[j]-gr[0];
    else:
        for j in range(0,n):
             gr1[j]=gr[j]-nputR[minwalk[i]-poc-i-1];
    
    plt.plot(odbK[0:n],gr1);

#za levu putevi
nputL=[];
for i in range(len(brzL)):
    nputL.append(0);
for i in range(0,len(brzL)):
    nputL[i]=putL[0][i];
      
  
  
for i in range(0, len(minwalkL)-1):
    gL=[];
    gL=nputL[(minwalkL[i]-pocL):(minwalkL[i+1]-pocL)];
  
   
    n=len(gL);
 
    gL1=[];
    for j in range(0,n):
        gL1.append(0);
    if(i==0):
        for j in range(0,n):
            gL1[j]=gL[j]-gL[0];
    else:
        for j in range(0,n):
             gL1[j]=gL[j]-nputL[minwalkL[i]-pocL-i-1];
    
    plt.plot(odbKL[0:n],gL1);
    
plt.title('Profili puta');
plt.xlabel('t [s]')
plt.ylabel('Put [m]')
plt.grid(True);
plt.show();












