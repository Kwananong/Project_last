import random
import time

count = 0
max_count = 10  # เลขสุ่มที่ต้องการให้สร้าง

while count < max_count:
    # สร้างเลขสุ่ม 3 ตัว
    random_numbers = [random.randint(0, 9) for _ in range(3)]
    
    # แปลงเลขสุ่มให้เป็นรูปแบบ "001", "002", "003", ...
    formatted_numbers = "".join(["{:03d}".format(num) for num in random_numbers])
    
    # พิมพ์เลขที่สร้างขึ้น
    print("".join(formatted_numbers), end="")
    
    # เพิ่มจำนวนครั้งที่สร้างขึ้นไป
    count += 1
    
    # หยุดเพื่อรอเวลา 2 วินาที
    time.sleep(2)

# สิ้นสุดลูป while ที่นี่
print("\nเสร็จสิ้นการสร้างเลขสุ่ม")
