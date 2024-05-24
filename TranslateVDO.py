import pickle
import cv2
import mediapipe as mp
import time
import numpy as np
from PIL import ImageFont, ImageDraw, Image

font = ImageFont.truetype("./font/THSarabun.ttf", 50)

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture()
cap.open('VDO/03คลอดบุตร_Test.mp4') #1,6

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

holistic = mp_holistic.Holistic(
    static_image_mode=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)
def draw_text_on_frame(frame, text, position=(70, 5), font_path="./font/THSarabun.ttf", font_size=40):
    font = ImageFont.truetype(font_path, font_size)
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)
    draw.text(position, text, font=font, fill=(255, 255, 255))
    frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
    return frame


def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle
    return angle 
    
labels_dict = {0: '000', 1: '001', 2: '002', 3: '003',4:'004',5:'005',6:'006',7:'007',8:'008',9:'009',
               10:'010',11:'011',12:'012',13:'013',14:'014',15:'015',16:'016',17:'017',18:'018',19:'019',
               20:'020',21:'021',22:'022',23:'023',24:'024',25:'025',26:'026',27:'027',28:'028',29:'029',
               30:'030',31:'031',32:'032',33:'033',34:'034',35:'035',36:'036',37:'037',38:'038',39:'039',
               40:'040',41:'041',42:'042',43:'043',44:'044',45:'045',46:'046',47:'047',48:'048',49:'049',
               50:'050',51:'051',52:'052',53:'053',54:'054',55:'055',56:'056',57:'057',58:'058',59:'059',
                60:'060',61:'061',62:'062',63:'063',64:'064',65:'065',66:'066',67:'067',68:'068',69:'069',
                70:'070',71:'071',72:'072',73:'073',74:'074',75:'075',76:'076',77:'077',78:'078',79:'079',
                80:'080',81:'081',82:'082',83:'083',84:'084',85:'085',86:'086',87:'087',88:'088',89:'089',
                90:'090',91:'091',92:'092',93:'093',94:'094',95:'095',96:'096',97:'097',98:'098',99:'099',}

data__ = []
joined_data = ''
data_ = []
massage = ''

while True:

    data_aux = []
    x_left = []
    y_left = []
    x_right = []
    y_right = []
   


    ret, frame = cap.read()
 
    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = holistic.process(frame_rgb)

    if results.left_hand_landmarks is not None:
            left_hand_landmarks = results.left_hand_landmarks.landmark

            # Find the minimum x and y values
            min_x = min([landmark.x for landmark in left_hand_landmarks])
            min_y = min([landmark.y for landmark in left_hand_landmarks])

            for landmark in left_hand_landmarks:
                # Subtract the minimum x and y values from each landmark coordinate
                data_aux.append(landmark.x - min_x)
                data_aux.append(landmark.y - min_y)

             #point
            mcp_xl = int(left_hand_landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP].x * W)
            mcp_yl = int(left_hand_landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP].y * H)

            cv2.circle(frame, (mcp_xl, mcp_yl), 5, (0, 255, 0), -1)

                # Draw hand landmarks
            # mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    else:
            # If no left hand landmarks are detected, fill the data_aux list with 0.999
            data_aux.extend([1] * 42)

    if results.right_hand_landmarks is not None:
            right_hand_landmarks = results.right_hand_landmarks.landmark

            # ค้นหาค่า x และ y ที่ต่ำที่สุด
            min_x = min([landmark.x for landmark in right_hand_landmarks])
            min_y = min([landmark.y for landmark in right_hand_landmarks])

            for landmark in right_hand_landmarks:
                # ลบค่า x และ y ที่ต่ำที่สุดออกจากทุกๆ จุดตำแหน่ง
                data_aux.append(landmark.x - min_x)
                data_aux.append(landmark.y - min_y)

            #point
            mcp_xr = int(right_hand_landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP].x * W)
            mcp_yr = int(right_hand_landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP].y * H)
            
            cv2.circle(frame, (mcp_xr, mcp_yr), 5, (0, 255, 0), -1)
    else:
            # หากไม่พบจุดที่มือขวาตรวจจับได้ ให้เติมรายการ data_aux 
            data_aux.extend([1] * 42)


    if results.pose_landmarks is not None:
            pose_landmarks = results.pose_landmarks.landmark
            
            # left 
            shoulder_left = [pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_left = [pose_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_left = [pose_landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y]

            # right
            shoulder_right = [pose_landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_right = [pose_landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_right = [pose_landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y]

            left_arm_angle1 = calculate_angle(shoulder_left, elbow_left, wrist_left)
            right_arm_angle1 = calculate_angle(shoulder_right, elbow_right, wrist_right)

            under_angle = [left_arm_angle1, right_arm_angle1]
            data_aux.extend(under_angle)

    else:
            data_aux.extend([1] * 2)

    # data_aux.extend(under_angle)

    if results.pose_landmarks is not None:
                    pose_landmarks = results.pose_landmarks.landmark
                    # left 
                    hip_left = [pose_landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y]
                    elbow_left = [pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
                    wrist_left = [pose_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]

                    # right
                    hip_right = [pose_landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y]
                    elbow_right = [pose_landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
                    wrist_right = [pose_landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].x, pose_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]

                    left_arm_angle2 = calculate_angle(hip_left, elbow_left, wrist_left)
                    right_arm_angle2 = calculate_angle(hip_right, elbow_right, wrist_right)

                    bottom_angle = [left_arm_angle2, right_arm_angle2]
                    data_aux.extend(bottom_angle)

                     # right
                    shld_rx = int(pose_landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x * W)
                    shld_ry = int(pose_landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].y * H)
                    # left 
                    shld_lx = int(pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y * W)
                    shld_ly = int(pose_landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y * H)
    else:
                    data_aux.extend([1] * 2)


    if results.left_hand_landmarks is not None and results.right_hand_landmarks is not None and results == 1:
        pass
    else:
        if results.left_hand_landmarks is not None or results.right_hand_landmarks is not None:
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]
            data_.append(predicted_character)
            
            # รวมรหัสและลบรหัสที่ซ้ำเฉพาะที่ติดกัน
            unique_labels = [data_[0]]  # ใส่รหัสแรกไว้ก่อน
            for i in range(1, len(data_)):
                if data_[i] != data_[i-1]:  # ตรวจสอบว่ารหัสปัจจุบันไม่ซ้ำกับก่อนหน้า
                    unique_labels.append(data_[i])
            
            # แปลงเป็นข้อความ
            massage = ''.join(unique_labels)
            joined_data = massage[-18:] #3* จำนวนรหัส เอา 6 รหัส
    
            # print('data', data_)
            print('m',massage)  # ผลลัพธ์: 045046044046044027
            print('j',joined_data)  # ผลลัพธ์: 460460

             # กำหนดพิกัดของข้อความ
            text_x = 0
            text_y = 50  # ปรับตำแหน่งข้อความตามต้องการ

            # แสดงข้อความที่มุมบนซ้ายบนของเฟรม
            cv2.putText(frame, predicted_character, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)

    # ตรวจสอบและแสดงข้อความตามเงื่อนไข
        # if '001' in joined_data:
        #     frame = draw_text_on_frame(frame, "ฉัน")
        # if '002' in joined_data:
        #     frame = draw_text_on_frame(frame, "เธอ")
        # if '017018' in joined_data and '018002' in joined_data:
        #     frame = draw_text_on_frame(frame, "ไม่เข้าใจ")
        # เงื่อนไขในการแปลคำ
        if "045" in joined_data and "046" in joined_data:
            frame = draw_text_on_frame(frame, "คลอดบุตร")
             
            
        cv2.imshow('fram', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()