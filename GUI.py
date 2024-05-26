
import pickle
import cv2
import mediapipe as mp
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageTk
import tkinter as tk


font = ImageFont.truetype("./font/THSarabun.ttf", 50)
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']
cap = cv2.VideoCapture()


# error
# cap.open('VDO/ใบรับรองแพทย์.mp4')                                 #ใบรับรองแพทย์ เทรนใหม่ 
# cap.open('VDO/คัดจมูก.mov')                                        #err
# cap.open('VDO/นอนไม่หลับ.mov')                                     #เทรนใหม่ 084 085 (002 กระพริบ)
# cap.open('VDO/ท้องเสีย1.mp4')                                        #เทรน 095 ใหม่
# cap.open('VDO/หายใจไม่ออก.mov')                                    #มีคำแทรก  เป็นใบ้ ไม่เป็นไร ไม่ขึ้นคำว่า หายใจไม่ออก
# cap.open('VDO/เคล็ดขัดยอก.mp4')                                    #err
# cap.open('VDO/โรงพยาบาล1.mov')                                     #มีคำแทรก หมอ
# cap.open('VDO/มองไม่เห็น.mov')                                      #มีคำแทรก ไม่เป็นไร เป็นใบ้ 
# cap.open('VDO/รถชน.mov')                                     #รันได้แต่มีคำว่าเป็น ใบ้ ไม่เป็นไร แทรกขึ้นมา ไม่ขึ้น รถชน

# cap.open('VDO/โรงพยาบาล2.mov')                    #err
# cap.open('VDO/โรงพยาบาล3.mov')                    #err
# cap.open('VDO/โรงพยาบาล4.mov')                      #err         
# cap.open('VDO/โรงพยาบาล6.mp4')                      #err   รีไซต           


#เทสแล้ว 
# cap.open('VDO/ฉัน1.mov')           #คลิปเบส
# cap.open('VDO/ฉัน2.mp4')                                           
# cap.open('VDO/ฉัน3.mp4')                                   #มีคำว่า จาม แทรก แก้ไม่ได้*
# cap.open('VDO/เธอ1.mov')           #คลิปเบส  
# cap.open('VDO/เธอ2.mp4')                                  #err
# cap.open('VDO/เพื่อน1.mp4')          #คลิปเบส                #มีคำว่า เจ็บ แทรกขึ้นมา แก้แล้ว*
# cap.open('VDO/เพื่อน2.mp4')                                 #มีคำว่า รถชน แทรกขึ้นมา แก้ไม่ได้      
# cap.open('VDO/เพื่อน3.mov')                                 #มีคำว่า เจ็บ แทรกขึ้นมา แก้แล้ว*
# cap.open('VDO/สบายดี1.mov')                                 #มีคำว่า ไม่เป็นไร แทรกขึ้นมา แก้แล้ว*
# cap.open('VDO/สบายดี2.mp4')                                         
# cap.open('VDO/สบายดี3.mp4')           #คลิปเบส                                 
# cap.open('VDO/สบายดี4.mp4')                                       
# cap.open('VDO/สบายดี5.mp4')                                       
# cap.open('VDO/ชื่อ1.mov')            #คลิปเบส                #มีคำแทรก เจ็บ นามสกุล ชื่อ ไม่เข้าใจ
# cap.open('VDO/ชื่อ2.mp4')                                   #err
# cap.open('VDO/นามสกุล1.mov')        #คลิปเบส  
# cap.open('VDO/นามสกุล2.mov')                               #มีคำว่า เจ็บ แทรก แก้แล้ว*
# cap.open('VDO/นามสกุล3.mp4')                               #err
# cap.open('VDO/พ่อ1.mov')                                   #มีคำ ไม่ใช่ แทรก แก้ไม่ได้
# cap.open('VDO/พ่อ2.mov')             #คลิปเบส                          
# cap.open('VDO/พ่อ3.mp4')                                   #err
# cap.open('VDO/พ่อ4.mp4')                                   #มีคำ ไม่ใช่ แทรก แก้ไม่ได้
# cap.open('VDO/พ่อ5.mov')                                   #มีคำ ใช่ แทรก แก้ไม่ได้
# cap.open('VDO/แม่1.mov')             #คลิปเบส               #มีคำว่า เข้าใจ แทรก แก้ไม่ได้
# cap.open('VDO/แม่2.mp4')                                   #err
# cap.open('VDO/แม่3.mp4')                                   #มีคำว่า ที่ไหน แทรก แก้ไม่ได้
# cap.open('VDO/แม่4.mov')                                   #มีคำว่า ใช่ แทรก แก้ไม่ได้
# cap.open('VDO/แม่5.mov')                                   #err 
# cap.open('VDO/ไม่ใช่.mov')             #คลิปเบส
# cap.open('VDO/ไม่เป็นไร1.mov')         #คลิปเบส
# cap.open('VDO/ไม่เป็นไร2.mov')                              #มีคำว่า คลอดบุตร เป็นใบ้ 
# cap.open('VDO/ไม่เป็นไร3.mov') 
# cap.open('VDO/ไม่เข้าใจ.mov')          #คลิปเบส
# cap.open('VDO/หิว1.mov')              #คลิปเบส                                        
# cap.open('VDO/หิว2.mov')                                   #มีคำว่า ไอ แทรก แก้ไม่ได้                               
# cap.open('VDO/หิว3.mp4')                                   #err   
# cap.open('VDO/ไม่สบาย1.mov')          #คลิปเบส                                                 
# cap.open('VDO/ไม่สบาย2.mov')  
# cap.open('VDO/ใช่1.mp4')                                    #err 
# cap.open('VDO/ใช่2.mp4')              #คลิปเบส       
# cap.open('VDO/ที่ไหน1.mov')            #คลิปเบส  
# cap.open('VDO/ที่ไหน2.mov')            
# cap.open('VDO/อย่างไร1.mov')           #คลิปเบส    
# cap.open('VDO/แต่งงาน1.mov')           #คลิปเบส       
# cap.open('VDO/แต่งงาน2.mp4')                                #err 
# cap.open('VDO/แต่งงาน3.mov') 
# cap.open('VDO/หย่า1.mov')                                   #มีคำว่า ไม่เป็นไร สบายดี แทรก
# cap.open('VDO/หย่า2.mp4')                                    #มีคำแทรก ไม่เป็นไร เภสัช     
# cap.open('VDO/หย่า3.mov')                                  #มีคำว่า ไม่เป็นไร แทรก 
# cap.open('VDO/หย่า4.mov')              #คลิปเบส             #มีคำว่า สบายดี แทรก แก้ไม่ได้
# cap.open('VDO/ถอดเสื้อ1.mp4')           #คลิปเบส  
# cap.open('VDO/ถอดเสื้อ2.mov')                                #มีคำแทรก คลอดบุตร หนาว 
# cap.open('VDO/ฉีดยา1.mp4')    
# cap.open('VDO/ฉีดยา2.mp4')    
# cap.open('VDO/หมอ1.mov')                                   #err
# cap.open('VDO/หมอ2.mov')               #คลิปเบส
# cap.open('VDO/01พยาบาล_Test.mp4')                            #น่าจะเพราะมีคำว่าฉีดยาแทรก err
# cap.open('VDO/พยาบาล1.mov')            #คลิปเบส              #มีแทรก  ไม่เข้าใจ  ไม่เห็นคำว่าพยาบาลขึ้น ในเล่มเขียนไปว่าถูก **      
# cap.open('VDO/พยาบาล2.mp4')                                    #ไม่ได้คิดในผล   err
# cap.open('VDO/05เภสัช_Test.mp4')          #คลิปเบส                #มีคำว่า จาม แทรกมา
# cap.open('VDO/คนไข้.mov')                 #คลิปเบส              #กระพริบ  
# cap.open('VDO/หูหนวก1.mp4')                                   #มีคำว่า น้ำมูกไหล แทรกเข้ามา 
# cap.open('VDO/หูหนวก2.mov')                                   #มีเป็นใบ้แทรกเข้ามา err
# cap.open('VDO/หูหนวก3.mp4')              #คลิปเบส               #มีคำว่า หิว สบายดี แทรกเข้ามา 
# cap.open('VDO/เป็นใบ้.mov')                #คลิปเบส 
# cap.open('VDO/รักษารากฟัน1.mp4')           #คลิปเบส
# cap.open('VDO/รักษารากฟัน2.mp4')                                 #err  มีคำว่า เป็นใบ้ แทรก
# cap.open('VDO/03คลอดบุตร_Test.mp4')       #คลิปเบส
# cap.open('VDO/คลื่นไส้.mov')                #คลิปเบส
# cap.open('VDO/อาเจียน.mov')                #คลิปเบส              #มีคำแทรก จาม แก้ไม่ได้
# cap.open('VDO/แพ้ยา1.mov')                                     มีคำว่าหนาวแทรก
# cap.open('VDO/แพ้ยา2.mov')                    #คลิปเบส  
# cap.open('VDO/แพ้อาหาร1.mov')                                  #มีคำว่า หนาว แทรก
# cap.open('VDO/แพ้อาหาร2.mov')                                    #err + มีคำแทรก
# cap.open('VDO/ไอ.mov')                    #คลิปเบส                #มีคำแทรก  หิว น้ำมูกไหล    
# cap.open('VDO/จาม.mov')                   #คลิปเบส 
# cap.open('VDO/เจ็บ1.mov')                    #คลิปเบส
# cap.open('VDO/เจ็บ2.mov')                                          #err       
# cap.open('VDO/อาหารติดคอ1.mov')              #คลิปเบส               #รันได้แต่กระพริบ มีคำว่า ไม่เป็นไร แทรก
# cap.open('VDO/อาหารติดคอ2.mov')                                      #err
# cap.open('VDO/หนาว1.mov')                    #คลิปเบส 
# cap.open('VDO/หนาว2.mov')                             
# cap.open('VDO/คัน1.mov')                      #คลิปเบส 
# cap.open('VDO/คัน2.mov')            
# cap.open('VDO/ตาย1.mov')                     #คลิปเบส   
# cap.open('VDO/ตาย2.mov')                                          #err      
# cap.open('VDO/อมยา.mov')                       #คลิปเบส              #มีคำว่า สบายดี แทรก
# cap.open('VDO/น้ำมูกไหล.mp4')                                       #มีคำว่า ไม่เป็นไร แทรก ไม่ขึ้นคำว่า น้ำมูกไหล แก้แล้ว*

# cap.open('VDO/รวม1.mov')                       #คลิปรวมอันที่ถูกต้อง
# cap.open('VDO/ผิดพลาด.mov')


   

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

labels_dict = {1: '001', 2: '002', 3: '003',4:'004',5:'005',6:'006',7:'007',8:'008',9:'009',
               10:'010',11:'011',12:'012',13:'013',14:'014',15:'015',16:'016',17:'017',18:'018',19:'019',
               20:'020',21:'021',22:'022',23:'023',24:'024',25:'025',26:'026',27:'027',28:'028',29:'029',
               30:'030',31:'031',32:'032',33:'033',34:'034',35:'035',36:'036',37:'037',38:'038',39:'039',
               40:'040',41:'041',42:'042',43:'043',44:'044',45:'045',46:'046',47:'047',48:'048',49:'049',
               50:'050',51:'051',52:'052',53:'053',54:'054',55:'055',56:'056',57:'057',58:'058',59:'059',
                60:'060',61:'061',62:'062',63:'063',64:'064',65:'065',66:'066',67:'067',68:'068',69:'069',
                70:'070',71:'071',72:'072',73:'073',74:'074',75:'075',76:'076',77:'077',78:'078',79:'079',
                80:'080',81:'081',82:'082',83:'083',84:'084',85:'085',86:'086',87:'087',88:'088',89:'089',
                90:'090',91:'091',92:'092',93:'093',94:'094',95:'095',96:'096',97:'097',98:'098',99:'099',
                100:'100',101:'101'}

data__ = []
joined_data = ''
data_ = []
massage = ''
massage2 = ''
predicted_character = ''

def update_data():
    global joined_data, data__,massage2

    if "034" in massage2 and "035" in massage2 and "026" in massage2 :
        return "เภสัช"
    if "059" in joined_data and "060" in joined_data:
          return "ฉีดยา"
    if "040" in joined_data and "001" in joined_data:
          return "เป็นใบ้"
    if "057" in joined_data and "058" in joined_data:
          return "ถอดเสื้อ"
    if "004" in joined_data and "029" in joined_data:
        return "หย่า" 
    if "004" in joined_data and "005" in joined_data :
        return "สบายดี" 
    if "004004005" in joined_data:
        return "สบายดี"
    if "004004004004004004004004004004004004004004004004004004004004004004" in massage2 :
        return "ไม่เป็นไร" 
    # Check for "004" and count the next 3 characters only
    # if "004" in joined_data:
    #     position = joined_data.find("004")
    #     if position != -1:
    #         # Calculate the length of the substring after "004"
    #         length_after_004 = len(joined_data[position + 3:])
    #         if length_after_004 >= 3:
    #             next_three_chars = joined_data[position + 3:position + 6]
    #             # Check if the next three characters are not "005"
    #             if next_three_chars != "005":
    #                 return "ไม่เป็นไร"

    if "015" in joined_data and "016" in joined_data:
        return "เพื่อน" 
    if "006" in joined_data and "007" in joined_data:
        return "ชื่อ"
    
    if "006" in joined_data and "008" in joined_data:
        return "นามสกุล"
    # if "006" in joined_data and "008" in joined_data:
    #     position = joined_data.find("008")
    #     if position != -1:
    #         length_after_008 = len(joined_data[position + 3:])
    #         if length_after_008 >= 3:
    #             next_three_chars = joined_data[position + 3:position + 6]
    #             if next_three_chars != "007":
    #                 return "นามสกุล"

    if "009009" in massage2 and "099" in massage2:
        return "พ่อ"
    if "011" in joined_data and "099" in joined_data:
        return "แม่"
    if "099" in massage2 and "007" in massage2 and "002" in massage2:
        return "ไม่เข้าใจ"
    if "023" in joined_data and "024" in joined_data:
        return "ใช่"
    if "042" in joined_data and "001" in joined_data :
        return "เป็นใบ้"
    if "039" in massage and "040" in massage:
        return "หูหนวก"
    
     # in massage
    if "001001001001001001001001001001001001001" in massage2:
        return "ฉัน"
    if "002002002002002002002002002002002002002" in massage2:
        return "เธอ"
    if "083083083083" in massage2:
        return "อาหารติดคอ"
    
 
    if "032" in massage2 and "033" in massage2  and "030" in massage2  and "031" in massage2 :
        return "พยาบาล" 
    
    #สร้างเงื่อนไขเพิ่ม
    if "038038038038038038038038038038038038038" in massage2:
        return "คนไข้/ผู้ป่วย" #สร้างเงื่อนไขเพิ่ม
    
    if "030" in joined_data and "031" in joined_data and "089" in joined_data :
        return "โรงพยาบาล"  #สร้างเงื่อนไขเพิ่ม
    if "030" in massage2 and "031" in massage2 :
            return "หมอ/แพทย์"
  
    if "045" in joined_data and "046" in joined_data:
          return "คลอดบุตร"
    if "051" in joined_data and "052" in joined_data and "053" in joined_data :
        return "แพ้ยา"
    
    if "045" in joined_data and "046" in joined_data :
        return "คลอดบุตร"
    if "020" in joined_data and "021" in joined_data :
        return "หิว"
    if "006" in joined_data and "027" in joined_data :
        return "อย่างไร"
    if "040" in massage and "001" in massage :
        return "มองไม่เห็น"
    if "090" in joined_data and "091" in joined_data :
        return "รถชน"
    # if "001" in joined_data and "047" in joined_data :
    #     return "แน่นหน้าอก"
    if "004" in joined_data and "029" in joined_data :
        return "หย่า"


    # if '052052' in massage2 :  #อันนี้ใช้ได้กับทั้ง 2 คลิป 
    #     return "หนาว"
    if '052052052052052052' in massage2 :
        return "หนาว"
    
    # -------------------------------------------------------------------------------------------------------- #
    
    if "038038038" in massage2 :
        return "คนไข้/ผู้ป่วย" 
    if "039" in joined_data and "040" in joined_data :
        return "หูหนวก"
    if "040" in joined_data and "081" in joined_data :
        return "น้ำมูกไหล"
    if "047047047047047047047047047047047047047047047047047047047047047047047047047" in massage2 :
        return "คลื่นไส้"
    if "056" in joined_data and "049" in joined_data :
        return "อาเจียน" 
    if "092" in joined_data and "094" in joined_data :
        return "รักษารากฟัน" 
    if "099" in joined_data and "052" in joined_data and "053" in joined_data :
        return "แพ้อาหาร"
    if "084" in massage and "085" in massage and "002" in massage :
        return "นอนไม่หลับ"
    if "040040040040040040040040040" in massage2 and "001001001001001001001001" in massage2 :
        return "หายใจไม่ออก" 
    if "042042" in massage2 and "088088" in massage2 :
        return "ตาย/เสียชีวิต" 
    if "021021021021021021021021" in massage2:
        return "ไอ" 
    if "056056056" in massage2 :
        return "จาม" 
    
    if "006006006006006006006006006006006006006006006006006006006006006006006006006006006006006006006" in massage2 :
        return "เจ็บ" 
    # if "006" in joined_data:
    #     position = joined_data.find("006")
    #     if position != -1:
    #         length_after_006 = len(joined_data[position + 3:])
    #         if length_after_006 >= 3:
    #             next_three_chars = joined_data[position + 3:position + 6]
    #             if next_three_chars != "008":
    #                 return "เจ็บ"
    if "087087087087087087087087087087087" in massage2 :
        return "คัน" 

    if "022022022022022022022022022022022022022022022" in massage2 :
        return "ไม่สบาย/ป่วย" 
    if "009009009009009009009009009009009009009009009009009" in massage2 :
        return "ไม่/ไม่ใช่"    
    if "007007007007007007007007007" in massage2 :
        return "ที่ไหน"  
    if "028028028028028028028028028028028028028028028" in massage2 :
        return "แต่งงาน/สมรส"  
    if "062062062062062062062062062" in massage2 :
        return "อมยา" 
    else:
        return "----------"


def update_frame(frame, predicted_text):
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)
    draw.text((70, 5), predicted_text, font=font, fill=(255, 255, 255))
    return cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

def update_gui_text(label, prefix, text):
    full_text = f"{prefix} {text}"
    label.config(text=full_text)
    label.update_idletasks()  

def update_gui():
    global prev_hand_state, joined_data, data__, massage2, data_, massage
    predicted_character = ''

    # เพิ่มตรงนี้เพื่อกำหนดค่าเริ่มต้นให้กับ prev_hand_state
    if 'prev_hand_state' not in globals():
        prev_hand_state = ""

    ret, frame = cap.read()
 
    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = holistic.process(frame_rgb)

    hand_state = "OPEN" if results.left_hand_landmarks or results.right_hand_landmarks else "CLOSED"
    if hand_state != prev_hand_state:
        data_ = []
        data__ = []
        massage = ''
        joined_data = ''
        massage2 = ''
        update_gui_text(value_label2, "", "")  # Clear the GUI text as well
        update_gui_text(value_label4, "", "")
        update_gui_text(value_label3, "Vocabulary :", "")
        update_gui_text(value_label1, "Code :", "")
    prev_hand_state = hand_state

    data_aux = []

    x_left = []
    y_left = []
    x_right = []
    y_right = []

    if results.left_hand_landmarks is not None:
        
        left_hand_landmarks = results.left_hand_landmarks.landmark

        min_x = min([landmark.x for landmark in left_hand_landmarks])
        min_y = min([landmark.y for landmark in left_hand_landmarks])
        
        for landmark in left_hand_landmarks:
            x_left.append(landmark.x)
            y_left.append(landmark.y)

            data_aux.append(landmark.x - min_x)
            data_aux.append(landmark.y - min_y)

        
            # Draw hand 
            mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        

    else:
        data_aux.extend([1] * 42)

    if results.right_hand_landmarks is not None:

        right_hand_landmarks = results.right_hand_landmarks.landmark

        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        min_x = min([landmark.x for landmark in right_hand_landmarks])
        min_y = min([landmark.y for landmark in right_hand_landmarks])
       
        for landmark in right_hand_landmarks:
            x_right.append(landmark.x)
            y_right.append(landmark.y)

            data_aux.append(landmark.x - min_x)
            data_aux.append(landmark.y - min_y)
  
    else:
        data_aux.extend([1] * 42)


    if results.pose_landmarks is not None:
        pose_landmarks = results.pose_landmarks.landmark
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

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

    else:
        data_aux.extend([1] * 2)
 
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
        massage2 = ''.join(data_)
        print(massage2)
        massage = ''.join(unique_labels)
        print('massage',massage)
        joined_data = massage[-18:] #3* จำนวนรหัส เอา6 รหัส
        print('joined_data',joined_data)

            # กำหนดพิกัดของข้อความ
        # text_x = 0
        # text_y = 50  # ปรับตำแหน่งข้อความตามต้องการ

        # แสดงข้อความที่มุมบนซ้ายบนของเฟรม
        # cv2.putText(frame, predicted_character, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)

    # Update GUI
    predicted_text = update_data()
    update_gui_text(value_label2, "", predicted_character)
    update_gui_text(value_label4, "", predicted_text)
    update_gui_text(value_label3, "Vocabulary :", "")
    update_gui_text(value_label1, "Code :", "")

    # if predicted_text:
    #     frame = update_frame(frame, predicted_text)

    # Update video frame
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    img = ImageTk.PhotoImage(image=img)
    video_box.img = img
    video_box.config(image=img)

    window.after(10, update_gui)

# Create GUI
window = tk.Tk()
window.title("Sign language translate")

video_box = tk.Label(window)
video_box.pack(padx=10, pady=10)

value_label1 = tk.Label(window, text="", font=("Arial", 20), fg="green")
value_label1.pack(padx=35, pady=25, side=tk.LEFT)

value_label2 = tk.Label(window, text="", font=("Arial", 30),fg='green')
value_label2.pack(padx=10, pady=25, side=tk.LEFT)

value_label4 = tk.Label(window, text="", font=("Arial", 30),fg="blue")
value_label4.pack(padx=15, pady=25, side=tk.RIGHT)

value_label3 = tk.Label(window, text="", font=("Arial", 20), fg="blue")
value_label3.pack(padx=0, pady=25, side=tk.RIGHT)


update_gui()
window.mainloop()
