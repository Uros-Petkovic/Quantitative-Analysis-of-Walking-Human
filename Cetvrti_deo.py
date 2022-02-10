import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.interpolate import interp1d
import math
from numpy import matrix



##INTEGRAL BRZINE

brzR=integrate.cumtrapz(acc_FR1[0],time[poc:kraj]);


plt.figure()
plt.plot(time[poc:(kraj-1)],brzR);
plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.title('Brzina sa baznom desno')
plt.legend('x');
plt.grid (True);
plt.show();


ntackeRx=[];
for i in range(2):
    row=[];
    for j in range(len(tackeRR[0])*2-4):
        row.append(0);
    ntackeRx.append(row);


l=0;
ntackeRx[0][l]=poc;
ntackeRx[1][l]=brzR[0];
l=l+1;
for i in range(1,len(tackeRR[0])-3):
    if(i==1):
        ntackeRx[0][l]=tackeRR[0][i];
        ntackeRx[1][l]=brzR[ntackeRx[0][l]-poc];
        l=l+1;
    
    
    t1=np.argmax(gyro_FR0[0][tackeRR[0][i]:tackeRR[0][i+1]]);
    t1=t1+tackeRR[0][i];
    
    t2=np.argmax(gyro_FR0[0][tackeRR[0][i+1]:tackeRR[0][i+2]]);
    t2=t2+tackeRR[0][i+1];
    
    t=math.floor((t1+t2)/2);
    print(t);
    if(t>tackeRR[0][i+1]):
        ntackeRx[0][l]=tackeRR[0][i+1];
        ntackeRx[1][l]=brzR[ntackeRx[0][l]-poc];
        l=l+1;
        ntackeRx[0][l]=t;
        ntackeRx[1][l]=brzR[ntackeRx[0][l]-poc];
        l=l+1;
    else:
        ntackeRx[0][l]=t;
        ntackeRx[1][l]=brzR[ntackeRx[0][l]-poc];
        l=l+1;
        ntackeRx[0][l]=tackeRR[0][i+1];
        ntackeRx[1][l]=brzR[ntackeRx[0][l]-poc];
        l=l+1;

ntackeRx[0][len(ntackeRx[0])-2]=tackeRR[0][len(tackeRR[0])-2];
ntackeRx[1][len(ntackeRx[0])-2]=brzR[tackeRR[0][len(tackeRR[0])-2]-poc];
ntackeRx[0][len(ntackeRx[0])-1]=kraj;
ntackeRx[1][len(ntackeRx[0])-1]=brzR[len(brzR)-1];

   

osa=np.arange(poc, kraj+1, 1) ;
baznaRb=[];




for i in range(1):
    row=[] 
    for j in range(len(osa)): 
        row.append(0) 
    baznaRb.append(row)

ntackeRx[1]=ntackeRx[1][0:10];

baznaRb[0]=interp1d(ntackeRx[0],ntackeRx[1])(osa)
brzR1=brzR-baznaRb[0][0:len(brzR)];

plt.figure()
plt.plot(time[poc:(kraj-1)],brzR1);
plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.title('Brzina bez bazne desno')
plt.legend('x');
plt.grid(True);
plt.show();

plt.figure()
plt.plot(time[poc:(kraj-1)],brzR);
plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.legend('x');
plt.grid(True);
plt.show();

plt.figure()
plt.plot(time[poc:(kraj-1)],brzR1);

for i in range (len(minwalk)-1):
    
    plt.plot(time[minwalk[i]],0,color='green',marker='^',markerfacecolor='green', markersize=8);
    

plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.legend('x');
plt.grid(True);
plt.show();




putR=[];


for i in range(1):
    row=[];
for j in range(len(brzR1)):
    row.append(0);
    putR.append(row);






for i in range(0,len(minwalk)-1):
    sr=0;

    br=0;
    br1=0;
    sr1=0;
    for j in range (minwalk[i],minwalk[i+1]):
             if(brzR1[j-poc-1]>0):
                 if(j<trenuciKi[i+1]):
                     sr1=sr1+brzR1[j-poc-1];
                     br1=br1+1;
                 else:
                     sr=sr+brzR1[j-poc-1];
                     br=br+1;
                 
             
        
    sr=sr/br;
    sr1=sr1/br1;

    for j in range (minwalk[i],minwalk[i+1]):
          if(j<trenuciKi[i+1]):
              if(i==0):
                  putR[0][j-poc-1]=sr1/100;
              else:
                  putR[0][j-poc-1]=putR[0][minwalk[i]-poc-2]+sr1/100;
            
          else:
              putR[0][j-poc-1]=putR[0][j-poc-2]+sr/100;


plt.figure()
plt.plot(time[poc:(kraj-1)],putR[0]);

#for i in range(0,len(minwalk)-1):
#     plt.plot(time[minwalk[i]],0,color='green',marker='^',markerfacecolor='green', markersize=8);

plt.xlabel('t [s]')
plt.ylabel('Put [m]')
plt.legend('x');
plt.title('Put desno')
plt.grid(True);
plt.show();










##isto sve za levu


brzL=integrate.cumtrapz(acc_FL1[0],time[pocL:krajL]);


plt.figure()
plt.plot(time[pocL:(krajL-1)],brzL);
plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.title('Brzina sa baznom levo')
plt.legend('x');
plt.grid (True);
plt.show();


ntackeLx=[];
for i in range(2):
    row=[];
    for j in range(len(tackeLL[0])*2-4):
        row.append(0);
    ntackeLx.append(row);


l=0;
ntackeLx[0][l]=pocL;
ntackeLx[1][l]=brzL[0];
l=l+1;
for i in range(1,len(tackeLL[0])-3):
    if(i==1):
        ntackeLx[0][l]=tackeLL[0][i];
        ntackeLx[1][l]=brzR[ntackeLx[0][l]-pocL];
        l=l+1;
    
    
    t1=np.argmax(gyro_FL0[0][tackeLL[0][i]:tackeLL[0][i+1]]);
    t1=t1+tackeLL[0][i];
    
    t2=np.argmax(gyro_FL0[0][tackeLL[0][i+1]:tackeLL[0][i+2]]);
    t2=t2+tackeLL[0][i+1];
    
    t=math.floor((t1+t2)/2);
    print(t);
    if(t>tackeLL[0][i+1]):
        ntackeLx[0][l]=tackeLL[0][i+1];
        ntackeLx[1][l]=brzL[ntackeLx[0][l]-pocL];
        l=l+1;
        ntackeLx[0][l]=t;
        ntackeLx[1][l]=brzL[ntackeLx[0][l]-pocL];
        l=l+1;
    else:
        ntackeLx[0][l]=t;
        ntackeLx[1][l]=brzL[ntackeLx[0][l]-pocL];
        l=l+1;
        ntackeLx[0][l]=tackeLL[0][i+1];
        ntackeLx[1][l]=brzL[ntackeLx[0][l]-pocL];
        l=l+1;

ntackeLx[0][len(ntackeLx[0])-2]=tackeLL[0][len(tackeLL[0])-2];
ntackeLx[1][len(ntackeLx[0])-2]=brzL[tackeLL[0][len(tackeLL[0])-2]-pocL];
ntackeLx[0][len(ntackeLx[0])-1]=krajL;
ntackeLx[1][len(ntackeLx[0])-1]=brzL[len(brzL)-1];


  

osaL=np.arange(pocL, krajL+1, 1) ;
baznaLb=[];




for i in range(1):
    row=[] 
    for j in range(len(osa)): 
        row.append(0) 
    baznaLb.append(row)

ntackeLx[1]=ntackeLx[1][0:10];

baznaLb[0]=interp1d(ntackeLx[0],ntackeLx[1])(osaL)
brzL1=brzL-baznaLb[0][0:len(brzL)];

plt.figure()
plt.plot(time[pocL:(krajL-1)],brzL1);
plt.xlabel('t [s]')
plt.ylabel('Brzina [m/s]')
plt.legend('x');
plt.title('Brzina bez bazne levo')
plt.grid(True);
plt.show();






putL=[];


for i in range(1):
    row=[];
for j in range(len(brzL1)):
    row.append(0);
    putL.append(row);






for i in range(0,len(minwalkL)-1):
    sr=0;

    br=0;
    br1=0;
    sr1=0;
    for j in range (minwalkL[i],minwalkL[i+1]):
             if(brzR1[j-pocL-1]>0):
                 if(j<trenuciKiL[i+1]):
                     sr1=sr1+brzL1[j-pocL-1];
                     br1=br1+1;
                 else:
                     sr=sr+brzL1[j-pocL-1];
                     br=br+1;
                 
             
        
    sr=sr/br;
    sr1=sr1/br1;

    for j in range (minwalkL[i],minwalkL[i+1]):
          if(j<trenuciKiL[i+1]):
              if(i==0):
                  putL[0][j-pocL-1]=sr1/100;
              else:
                  putL[0][j-pocL-1]=putL[0][minwalkL[i]-pocL-2]+sr1/100;
            
          else:
              putL[0][j-pocL-1]=putL[0][j-pocL-2]+sr/100;


plt.figure()
plt.plot(time[pocL:(krajL-1)],putL[0]);

#for i in range(0,len(minwalkL)-1):
#     plt.plot(time[minwalkL[i]],0,color='green',marker='^',markerfacecolor='green', markersize=8);

plt.xlabel('t [s]')
plt.ylabel('Put [m]')
plt.title('Put levo')
plt.legend('x');
plt.grid(True);
plt.show();






