result = input().strip()
target = int(input())
i = 0 # เตรียมตัวแปรที่คอยเก็บ index เริ่มต้นของเฟรม
total_score = 0 # เตรียมตัวแปรเก็บคะแนนรวม
for f in range(1,11) : # บังคับให้ท ำตั้งแต่เฟรม 1,2,...,10
 # ต้องให้ i เกบ็ ตำ แหน่งเริ่มต้นของเฟรม f ใน result
 เขียนแบบตรงไปตรงมำ
 ก็แยกเป็ น 7 กรณี XXX, XX?, X?/, X??, ?/X, ?/?, ??
 เพื่อค ำนวณคะแนนของเฟรม f เก็บใส่ตัวแปร score_in_frame_f
 แต่ละกรณีอำจมีรูปแบบกำรค ำนวณคะแนน และปรับค่ำของ i ต่ำงกัน
 if ..... :
 ...
 elif ... :
 ...
 elif ... :
 ...
 elif ... :
 ...
 elif ... :
 ...
 elif ... :
 ...
 else :
 ...

 total_score += score_in_frame_f
 if f == target :
 ???
???