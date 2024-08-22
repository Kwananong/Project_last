import os
import cv2


# เอาไว้ใช้เก็บท่าจากกล้องโน๊ตบุ๊คเรา

DATA_DIR = './data_capRT'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 20          # จำนวนครั้งที่ถ่าย
dataset_size = 100              # จำนวนภาพที่ถ่ายในแต่ละครั้ง

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.                  path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False

    while True:         #### กด q เพื่อออก ####
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
