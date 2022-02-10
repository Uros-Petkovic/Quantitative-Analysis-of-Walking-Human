import numpy as np
import matplotlib.pyplot as plt



#UCITAVANJE SACUVANIH SIGNALA

time = np.loadtxt("time.txt")
print(time);

fsr_l0=np.loadtxt("fsr_l0.txt")
print(fsr_l0);

fsr_r0=np.loadtxt("fsr_r0.txt")
print(fsr_r0);

gyro_FL0=np.loadtxt("gyro_FL0.txt")
print(gyro_FL0);


gyro_FR0=np.loadtxt("gyro_FR0.txt")
print(gyro_FR0);

acc_FR0=np.loadtxt("acc_FR0.txt")
print(acc_FR0);

acc_FL0=np.loadtxt("acc_FL0.txt")
print(acc_FL0);

tstart=5.1781;
tstop=14.0243;
istart=517;
istop=1401;

#PROBA2 IZ MATLABA

#usrednjen fsr signal Desne
fsr_r0_sr = (fsr_r0[0] + fsr_r0[1] + fsr_r0[2])/ 3


 #odredjivanje koraka preko praga



maxfsrr=max(fsr_r0_sr);
prag=0.2*maxfsrr;
trenuciPi=np.zeros(7);  #indeksi pocetaka 
trenuciKi=np.zeros(6);
trenuciKi[0]=istart;  
trenuciPi[0]=istart;


j=0;  

for i in range(istart+1, istop):
    if(fsr_r0_sr[i-1]<prag and fsr_r0_sr[i]>prag):
        if(j==0):
            j=1;
        trenuciPi[j]=i;
    else:
        if (fsr_r0_sr[i-1]>prag and fsr_r0_sr[i]<prag):  #ispod praga otislo
            if(j!=0): #ignorise se prvi kraj ako se pocetak nije desio
                trenuciKi[j]=i;
                j=j+1;

trenuciKi=trenuciKi.astype(int);
trenuciPi=trenuciPi.astype(int);
#trazenje trenutka udarca pete
minwalk=np.zeros(6); #trenuci udarca pete , pocetak rasta pritiska, vrednost minimuma i indeks tog odbirka

for i in range(0,len(trenuciKi)-1):
    k=trenuciPi[i+1]-1;
    while k>=trenuciKi[i]:
        if (fsr_r0_sr[k]<fsr_r0_sr[k+1] and (fsr_r0_sr[k]<fsr_r0_sr[k-1] or fsr_r0_sr[k]==fsr_r0_sr[k-1])):
            break;
        k=k-1;

    minwalk[i]=k;

    
if(len(trenuciPi)>len(trenuciKi)):
    k=trenuciPi[len(trenuciPi)-1];
    while(k>=trenuciKi[len(trenuciKi)-1]):
        if(fsr_r0_sr[k]<fsr_r0_sr[k+1] and (fsr_r0_sr[k]<fsr_r0_sr[k-1] or fsr_r0_sr[k]==fsr_r0_sr[k-1])):
            break;
        k=k-1;
    minwalk[len(trenuciKi)-1]=k;
else:
    k=istop;
    while(k>=trenuciKi[len(trenuciKi)-1]):
        if(fsr_r0_sr[k]<fsr_r0_sr[k+1] and (fsr_r0_sr[k]<fsr_r0_sr[k-1] or fsr_r0_sr[k]==fsr_r0_sr[k-1])):
            break;
        k=k-1;
    minwalk[len(trenuciKi)-1]=k;

    
minwalk=minwalk.astype(int);

 #usrednjen fsr signal sa oznakama koraka

plt.figure(3)
#plt.plot(time[minwalk(0):minwalk(len(minwalk))], fsr_r0_sr([minwalk(0):minwalk(len(minwalk))]));
plt.plot(time,fsr_r0_sr);
plt.plot(tstart,0,color='green',marker='^',markerfacecolor='green', markersize=8)
plt.plot(tstop, 0, color='red', marker='^', markerfacecolor='red',  markersize=8)

for i in range(0,len(minwalk)):
    
    plt.plot(time[minwalk[i]], 0, color='green',marker='^',markerfacecolor='green', markersize=8)
    
plt.xlabel('t [s]');
plt.ylabel('FSR signali [a.u.]');
plt.title('Usrednjeni kalibrisani FSR sa oznakama koraka DESNO');
plt.grid(True);
plt.show()

 #merenje vremena potrebnog za korak
timewalk=0;  #sr vreme trajanja koraka
imaxwalk=0;  #max vreme trajanja koraka u indeksima
maxtimewalk=0;  #max vreme trajana koraka u sekundama
dt=0;
di=0;
for i in range(0, len(minwalk)-1):
    dt=time[minwalk[i+1]]-time[minwalk[i]];
    di=minwalk[i+1]-minwalk[i];
   
    timewalk=timewalk+dt;
    if(imaxwalk<di):
        maxtimewalk=dt;
        imaxwalk=di;
        
        
timewalk=timewalk/5;
print(imaxwalk)

plt.figure(4)

timeK=time[1:imaxwalk];  #time osa samo za 1 korak
odbK=np.arange(0, imaxwalk, 1)  #osa po odbircima za 1 korak

for i in range(0,len(minwalk)-1):
    gr=fsr_r0_sr[minwalk[i]:minwalk[i+1]-1];
    n=np.max(np.nonzero(gr));
    plt.plot(odbK[0:n+1],gr);

plt.title('Profili pritiska desno')
plt.grid('True')
plt.show();    

    


#usrednjen fsr signal Leve
fsr_l0_sr = (fsr_l0[0] + fsr_l0[1] + fsr_l0[2])/ 3



 #odredjivanje koraka preko praga



maxfsrl=max(fsr_l0_sr);
pragL=0.2*maxfsrl;
trenuciPiL=np.zeros(7);  #indeksi pocetaka 
trenuciKiL=np.zeros(6);
trenuciKiL[0]=istart;  
trenuciPiL[0]=istart;


j=0;  

for i in range(istart+1, istop):
    if(fsr_l0_sr[i-1]<pragL and fsr_l0_sr[i]>pragL):
        if(j==0):
            j=1;
        trenuciPiL[j]=i;
    else:
        if (fsr_l0_sr[i-1]>pragL and fsr_l0_sr[i]<pragL):  #ispod praga otislo
            if(j!=0): #ignorise se prvi kraj ako se pocetak nije desio
                trenuciKiL[j]=i;
                j=j+1;

trenuciKiL=trenuciKiL.astype(int);
trenuciPiL=trenuciPiL.astype(int);
#trazenje trenutka udarca pete
minwalkL=np.zeros(6); #trenuci udarca pete , pocetak rasta pritiska, vrednost minimuma i indeks tog odbirka

for i in range(0,len(trenuciKiL)-1):
    k=trenuciPiL[i+1]-1;
    while k>=trenuciKiL[i]:
        if (fsr_l0_sr[k]<fsr_l0_sr[k+1] and (fsr_l0_sr[k]<fsr_l0_sr[k-1] or fsr_l0_sr[k]==fsr_l0_sr[k-1])):
            break;
        k=k-1;

    minwalkL[i]=k;

    
if(len(trenuciPiL)>len(trenuciKiL)):
    k=trenuciPiL[len(trenuciPiL)-1];
    while(k>=trenuciKiL[len(trenuciKiL)-1]):
        if(fsr_l0_sr[k]<fsr_l0_sr[k+1] and (fsr_l0_sr[k]<fsr_l0_sr[k-1] or fsr_l0_sr[k]==fsr_l0_sr[k-1])):
            break;
        k=k-1;
    minwalkL[len(trenuciKiL)-1]=k;
else:
    k=istop;
    while(k>=trenuciKiL[len(trenuciKiL)-1]):
        if(fsr_l0_sr[k]<fsr_l0_sr[k+1] and (fsr_l0_sr[k]<fsr_l0_sr[k-1] or fsr_l0_sr[k]==fsr_l0_sr[k-1])):
            break;
        k=k-1;
    minwalkL[len(trenuciKiL)-1]=k;

    
minwalkL=minwalkL.astype(int);

 #usrednjen fsr signal sa oznakama koraka

plt.figure(3)
#plt.plot(time[minwalk(0):minwalk(len(minwalk))-2], fsr_l0_sr[minwalk(0):minwalk(len(minwalk))-2]);
plt.plot(time,fsr_l0_sr)
#plt.plot(tstart,0,color='green',marker='^',markerfacecolor='red', markersize=8)
#plt.plot(tstop, 0, color='red', marker='^', markerfacecolor='red',  markersize=8)

for i in range(0,len(minwalkL)):
    
    plt.plot(time[minwalkL[i]], 0, color='green',marker='^',markerfacecolor='green', markersize=8)
    
plt.xlabel('t [s]');
plt.ylabel('FSR signali [a.u.]');
plt.title('Usrednjeni kalibrisani FSR sa oznakama koraka LEVO');
plt.grid(True);
plt.show()

 #merenje vremena potrebnog za korak
timewalkL=0;  #sr vreme trajanja koraka
imaxwalkL=0;  #max vreme trajanja koraka u indeksima
maxtimewalkL=0;  #max vreme trajana koraka u sekundama
dt=0;
di=0;
for i in range(0, len(minwalkL)-1):
    dt=time[minwalkL[i+1]]-time[minwalkL[i]];
    di=minwalkL[i+1]-minwalkL[i];
    timewalkL=timewalkL+dt;
    if(imaxwalkL<di):
        maxtimewalkL=dt;
        imaxwalkL=di;
timewalkL=timewalkL/5;

plt.figure(4)

timeKL=time[1:imaxwalkL];  #time osa samo za 1 korak
odbKL=np.arange(0, imaxwalkL, 1)  #osa po odbircima za 1 korak

for i in range(0,len(minwalkL)-1):
    gr=fsr_l0_sr[minwalkL[i]:minwalkL[i+1]-1];
    n=np.max(np.nonzero(gr));
    plt.plot(odbKL[0:n+1],gr);

plt.title('Profili pitiska levo')
plt.grid('True')
plt.show();    