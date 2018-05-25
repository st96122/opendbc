import csv
import cv2
import numpy as np
import thread
def f0x25(j,frame):


    v=int(j[3][4:6],16)
    v=bin(v)
    v=v[2:len(v)].zfill(12)
    print(int(v,2))
def f0x230(j,frame):

    v = (int(j[3], 16))
    v = bin(v)
    v = v[2:len(v)].zfill(56)
    if (v[24] == '1'):
        print(j[3] + ' handcrat')
        cv2.putText(frame, ' handcrat', (50, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    elif (v[29] == '1'):
        print(j[3] + ' brake_H')
        cv2.putText(frame, 'brake_H', (50, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    elif (v[26] == '1'):
        print(j[3] + ' brake_L')
        cv2.putText(frame, 'brake_L', (50, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    else:
        print(j[3] + ' no_brake')

def f0x5b6(j,frame):

    if(j[3][4:5]=='8'):
        print(j[3]+'  lock')
        cv2.putText(frame, 'door lock', (550, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    if (j[3][4:5] == '0'):
        print(j[3] + '  open')
        cv2.putText(frame, 'door open', (550, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)

def f0x57f(j,frame):
    v=(int(j[3],16))
    v=bin(v)
    v=v[2:len(v)].zfill(56)
    if(v[11]=='1'):
        print(j[3]+' high')
        cv2.putText(frame, 'high', (0, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    elif(v[13]=='1'):
        print(j[3]+' big light')
        cv2.putText(frame, 'big light', (0, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    elif(v[12]=='1'):
        print(j[3]+' small light')
        cv2.putText(frame, 'small light', (0, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    else:
        print(j[3]+' light off')
        cv2.putText(frame, 'light off', (0, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)

def f0x120(j,frame):

    {
        '23': lambda:pr('d',j[3][12:14]),
        '20': lambda:pr('p',j[3][12:14]),
        '22': lambda:pr('n',j[3][12:14])
    }.get(j[3][12:14], lambda:pr('',j[3][12:14]))()
def pr(k,j):
    print(j+'  '+k)
    cv2.putText(frame, k, (0, 500), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
def prvideo(frame):

    cv2.putText(frame, lk[kj][1], (0, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    cv2.imshow('frame', frame)
    print('lk=   ' + str(lk[kj]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
def primg(kk):
    img = cv2.imread('car_logger/' + kk)
    cv2.putText(img, lk[kj][1], (0, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 6)
    cv2.imshow('frame', img)
    print('lk=   ' + str(lk[kj]))


    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()

cap=cv2.VideoCapture('0524.avi')
ret,frame=cap.read()
with open('canbus_output2.csv','r') as csvf:
    with open('img_output2.csv','r') as  csvf2:

        k2=csv.reader(csvf2)
        k=csv.reader(csvf)
        lk=[]
        kj=1
        for i in k2:
            lk.append(i)
        np.asanyarray(lk)
        for j in k:

            kji = kj
            if(j[0]!='Time' and kj<1054):
                if(float(j[0])>=float(lk[kj][0])):
                    kj+=1
                '''
                while(float(j[0])>=float(lk[kj][0])):
                    print('kj='+str(kj))
                    kj+=1
                    if(kj>=1053):
                        kj=1053
                        break
                '''
            if(kji!=kj):
                prvideo(frame)
                ret, frame = cap.read()
            {

                '0x25': lambda: f0x25(j,frame),
                '0x230': lambda: f0x230(j,frame),
                '0x5b6': lambda: f0x5b6(j,frame),
                '0x57f': lambda: f0x57f(j,frame),
                '0x120': lambda: f0x120(j,frame)
            }.get(j[2], lambda: None)()

                #primg(lk[kj][1])


