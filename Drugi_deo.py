
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.interpolate import interp1d





#INTEGRAL IZ MATLABA
#DESNA

poc=minwalk[0]; #od pocetka prvog koraka do kraja poslednjeg
kraj=minwalk[len(minwalk)-1];
TetR=[];
for i in range(3):
    row=[];
    for j in range((poc-1),kraj):
        row.append(0);
    TetR.append(row);

TetR[0]=integrate.cumtrapz(gyro_FR0[0,(poc):kraj+1],time[poc:kraj+1]);  #ugaoni pomeraji za x,y,z ziroskopa osu kroz vreme
TetR[1]=integrate.cumtrapz(gyro_FR0[1,(poc):kraj+1],time[poc:kraj+1]);
TetR[2]=integrate.cumtrapz(gyro_FR0[2,(poc):kraj+1],time[(poc):kraj+1]);

tackeR=[]; #tacke za interpolaciju kao max FSR pete desne noge
for i in range(4):
    row=[] 
    for j in range(len(trenuciKi)-1): 
        row.append(0) 
    tackeR.append(row)    



for i in range(0,len(trenuciKi)-1):
    tackeR[0][i]=np.argmax(fsr_r0[2,trenuciPi[i+1]:trenuciKi[i+1]]);
    tackeR[0][i]=tackeR[0][i]+trenuciPi[i+1];
    tackeR[1][i]=TetR[0][tackeR[0][i]-poc+1]; #za x
    tackeR[2][i]=TetR[1][tackeR[0][i]-poc+1];  #za y
    tackeR[3][i]=TetR[2][tackeR[0][i]-poc+1];  #za z


osa=np.arange(poc, kraj-1, 1) ;

baznaR=[];
for i in range(3):
    row=[] 
    for j in range(len(osa)): 
        row.append(0) 
    baznaR.append(row)
 
tackeRR=[[poc,tackeR[0][0],tackeR[0][1],tackeR[0][2],tackeR[0][3],tackeR[0][4],kraj]];
       

tackeR[0][0]=poc;
tackeR[0][4]=kraj-2;


baznaR[0]=interp1d(tackeR[0],tackeR[1])(osa);
baznaR[1]=interp1d(tackeR[0],tackeR[2])(osa);
baznaR[2]=interp1d(tackeR[0],tackeR[3])(osa);

TetRb=[];
for i in range(3):
    row=[];
    for j in range(poc,kraj):
        row.append(0);
    TetRb.append(row);
    

for i in range(0,len(osa)):
    TetRb[0][i]=TetR[0][i] - baznaR[0][i];
    TetRb[1][i]=TetR[1][i] - baznaR[1][i];
    TetRb[2][i]=TetR[2][i] - baznaR[2][i];
    
osa1=np.arange(poc,kraj,1);


plt.figure()
plt.plot(time[poc:(kraj)],TetR[0]);
plt.plot(time[poc:(kraj)],TetR[1]);
plt.plot(time[poc:(kraj)],TetR[2]);
plt.xlabel('t [s]')
plt.ylabel('Ugao [rad]')
plt.title('Ugao sa baznom desno u lokalnom')
plt.grid(True);
plt.show()

plt.figure()
plt.plot(time[poc:kraj],TetRb[0]);
plt.plot(time[poc:kraj],TetRb[1]);
plt.plot(time[poc:kraj],TetRb[2]);
plt.xlabel('t [s]')
plt.ylabel('Ugao [rad]')
plt.title('Ugao bez bazne desno u lokalnom')
plt.grid(True);
plt.show()

 
#LEVA

pocL=minwalkL[0]; #od pocetka prvog koraka do kraja poslednjeg
krajL=minwalkL[len(minwalkL)-1];
TetL=[];
for i in range(3):
    row=[];
    for j in range(pocL-1,krajL):
        row.append(0);
    TetL.append(row);

TetL[0]=integrate.cumtrapz(gyro_FL0[0,pocL:krajL+1],time[pocL:krajL+1]);  #ugaoni pomeraji za x,y,z ziroskopa osu kroz vreme
TetL[1]=integrate.cumtrapz(gyro_FL0[1,pocL:krajL+1],time[pocL:krajL+1]);
TetL[2]=integrate.cumtrapz(gyro_FL0[2,pocL:krajL+1],time[pocL:krajL+1]);

tackeL=[]; #tacke za interpolaciju kao max FSR pete desne noge
for i in range(4):
    row=[] 
    for j in range(len(trenuciKiL)-1): 
        row.append(0) 
    tackeL.append(row)    

for i in range(0,len(trenuciKiL)-1):
    tackeL[0][i]=np.argmax(fsr_l0[2,trenuciPiL[i+1]:trenuciKiL[i+1]]);
    tackeL[0][i]=tackeL[0][i]+trenuciPiL[i+1];
    tackeL[1][i]=TetL[0][tackeL[0][i]-pocL+1]; #za x
    tackeL[2][i]=TetL[1][tackeL[0][i]-pocL+1];  #za y
    tackeL[3][i]=TetL[2][tackeL[0][i]-pocL+1];  #za z


osaL=np.arange(pocL, krajL-1, 1) ;
baznaL=[];
for i in range(3):
    row=[] 
    for j in range(len(osaL)): 
        row.append(0) 
    baznaL.append(row)

tackeLL=[[pocL,tackeL[0][0],tackeL[0][1],tackeL[0][2],tackeL[0][3],tackeL[0][4],krajL]];


tackeL[0][0]=pocL;
tackeL[0][4]=krajL-2;
baznaL[0]=interp1d(tackeL[0],tackeL[1])(osaL)
baznaL[1]=interp1d(tackeL[0],tackeL[2])(osaL)
baznaL[2]=interp1d(tackeL[0],tackeL[3])(osaL)

TetLb=[];
for i in range(3):
    row=[];
    for j in range(pocL,krajL):
        row.append(0);
    TetLb.append(row);
    

for i in range(0,len(osaL)):
    TetLb[0][i]=TetL[0][i] - baznaL[0][i];
    TetLb[1][i]=TetL[1][i] - baznaL[1][i];
    TetLb[2][i]=TetL[2][i] - baznaL[2][i];
osaL1=np.arange(pocL,krajL,1);


plt.figure()
plt.plot(time[pocL:(krajL)],TetL[0]);
plt.plot(time[pocL:(krajL)],TetL[1]);
plt.plot(time[pocL:(krajL)],TetL[2]);
plt.xlabel('t [s]')
plt.ylabel('Ugao [rad]')
plt.title('Ugao sa baznom levo u lokalnom')
plt.grid(True);
plt.show()

plt.figure()
plt.plot(time[pocL:krajL],TetLb[0]);
plt.plot(time[pocL:krajL],TetLb[1]);
plt.plot(time[pocL:krajL],TetLb[2]);
plt.xlabel('t [s]')
plt.ylabel('Ugao [rad]')
plt.title('Ugao bez bazne levo u lokalnom')
plt.grid(True);
plt.show()


