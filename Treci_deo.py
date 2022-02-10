import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import matrix


#TRANSLACIJA IZ MATLABA

#za desnu nogu


TetR[1]=-TetR[1];
acc_FR01=acc_FR0;
acc_FR01[0]=-acc_FR01[0];
acc_FR01[2]=-acc_FR01[2];



acc_FR1=[];
for i in range(3):
    row=[] 
    for j in range(poc,kraj): 
        row.append(0) 
    acc_FR1.append(row)
                  
for i in range(3):
    acc_FR1[0]=acc_FR01[0][poc:kraj];
    acc_FR1[1]=acc_FR01[1][poc:kraj];
    acc_FR1[2]=acc_FR01[2][poc:kraj];






g=9.801;
G=[[0],[-g],[0]];

for m in range(0,kraj-poc-1):

    Rx=[[1,0,0],[0,math.cos(TetR[0][m]),-math.sin(TetR[0][m])],[0,math.sin(TetR[0][m]),math.cos(TetR[0][m])]];
    Ry=[[math.cos(TetR[1][m]),0,math.sin(TetR[1][m])],[0,1,0],[-math.sin(TetR[1][m]),0,math.cos(TetR[1][m])]];
    Rz=[[math.cos(TetR[2][m]),-math.sin(TetR[2][m]),0],[math.sin(TetR[2][m]),math.cos(TetR[2][m]),0],[0,0,1]];

    result=[];
    for i in range(3):
        row=[];
        for j in range(3):
            row.append(0);
        result.append(row);

    R=[];
    for i in range(3):
        row=[];
        for j in range(3):
            row.append(0);
        R.append(row);

    GG=[];
    for i in range(3):
        row=[];
        for j in range(1):
            row.append(0);
        GG.append(row);

    for i in range(len(Ry)):
        
        for j in range(len(Rx[0])):
    
            for k in range(len(Rx)):
                result[i][j] += Ry[i][k] * Rx[k][j];

    for i in range(len(result)):
        for j in range(len(Rz[0])):
            for k in range(len(Rz)):
                R[i][j] += result[i][k] * Rz[k][j];

    for i in range(len(R)):
        for j in range(len(G[0])):
            for k in range(len(G)):
                GG[i][j] += R[i][k] * G[k][j];

    
    acc_FR1[0][m]=acc_FR1[0][m] - GG[0];
    acc_FR1[1][m]=acc_FR1[1][m] - GG[1];
    acc_FR1[2][m]=acc_FR1[2][m] - GG[2];
                


    temp=[];
    O=[];
    P=[];
    O=matrix(R);
    temp=O.I;
    temp=np.array(temp);
    P=[[acc_FR1[0][m]],[acc_FR1[1][m]],[acc_FR1[2][m]]];
    M=[];
    for i in range(3):
        row=[];
        for j in range(1):
            row.append(0);
        M.append(row)
        
    for i in range(len(temp)):
        for j in range(len(P[0])):
            for k in range(len(P)):
                M[i][j] += temp[i][k] * P[k][j];
    
    acc_FR1[0][m]=M[0][0];
    acc_FR1[1][m]=M[1][0];
    acc_FR1[2][m]=M[2][0];
    
    
    





plt.figure();
plt.plot(time[poc:kraj],acc_FR1[0]);
plt.xlabel('t [s]');
plt.ylabel('Ubrzanje [m/s^2]');
plt.title('Desna ubrzanje globalno')
plt.grid(True);
plt.show();








        
#Sve isto za levu




TetL[1]=-TetL[1];
acc_FL01=acc_FL0;
acc_FL01[0]=-acc_FL01[0];
#acc_FL01[1]=-acc_FL01[1];
acc_FL01[2]=-acc_FL01[2];

acc_FL1=[];
for i in range(3):
    row=[] 
    for j in range(pocL,krajL): 
        row.append(0) 
    acc_FL1.append(row)
                  
for i in range(3):
    acc_FL1[0]=acc_FL01[0][pocL:krajL];
    acc_FL1[1]=acc_FL01[1][pocL:krajL];
    acc_FL1[2]=acc_FL01[2][pocL:krajL];

g=9.801;
G=[[0],[-g],[0]];



for m in range(0,krajL-pocL-1):

    Rx=[[1,0,0],[0,math.cos(TetL[0][m]),-math.sin(TetL[0][m])],[0,math.sin(TetL[0][m]),math.cos(TetL[0][m])]];
    Ry=[[math.cos(TetL[1][m]),0,math.sin(TetL[1][m])],[0,1,0],[-math.sin(TetL[1][m]),0,math.cos(TetL[1][m])]];
    Rz=[[math.cos(TetL[2][m]),-math.sin(TetL[2][m]),0],[math.sin(TetL[2][m]),math.cos(TetL[2][m]),0],[0,0,1]];

    result=[];
    for i in range(3):
        row=[];
        for j in range(3):
            row.append(0);
        result.append(row);

    R=[];
    for i in range(3):
        row=[];
        for j in range(3):
            row.append(0);
        R.append(row);

    GG=[];
    for i in range(3):
        row=[];
        for j in range(1):
            row.append(0);
        GG.append(row);

    for i in range(len(Ry)):
        
        for j in range(len(Rx[0])):
    
            for k in range(len(Rx)):
                result[i][j] += Ry[i][k] * Rx[k][j];

    for i in range(len(result)):
        for j in range(len(Rz[0])):
            for k in range(len(Rz)):
                R[i][j] += result[i][k] * Rz[k][j];

    for i in range(len(R)):
        for j in range(len(G[0])):
            for k in range(len(G)):
                GG[i][j] += R[i][k] * G[k][j];

    
    acc_FL1[0][m]=acc_FL1[0][m] - GG[0];
    acc_FL1[1][m]=acc_FL1[1][m] - GG[1];
    acc_FL1[2][m]=acc_FL1[2][m] - GG[2];

    temp=[];
    O=[];
    P=[];
    O=matrix(R);
    temp=O.I;
    temp=np.array(temp);
    P=[[acc_FL1[0][m]],[acc_FL1[1][m]],[acc_FL1[2][m]]];
    M=[];
    for i in range(3):
        row=[];
        for j in range(1):
            row.append(0);
        M.append(row);
        
    for i in range(len(temp)):
        for j in range(len(P[0])):
            for k in range(len(P)):
                M[i][j] += temp[i][k] * P[k][j];
    
    acc_FL1[0][m]=M[0][0];
    acc_FL1[1][m]=M[1][0];
    acc_FL1[2][m]=M[2][0];



plt.figure();
plt.plot(time[pocL:krajL],acc_FL1[0]);
plt.xlabel('t [s]');
plt.ylabel('Ubrzanje [m/s^2]');
plt.title('Leva ubrzanje globalno')
plt.grid(True);
plt.show();
                