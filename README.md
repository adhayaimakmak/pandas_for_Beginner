โจทย์ในโปรเจกตส์ test.py
งานที่ต้องทำ (5 ข้อ)
1
โหลดและสำรวจข้อมูล — โหลดไฟล์ CSV เข้า DataFrame แล้วแสดงขนาด ชนิดข้อมูล และจำนวน missing values ของแต่ละคอลัมน์
2
ทำความสะอาดข้อมูล — กรองเฉพาะ status = completed, แปลงคอลัมน์ date ให้เป็น datetime, เติมค่าที่หายไปอย่างเหมาะสม
3
สร้างคอลัมน์ใหม่ — คำนวณ total_price = quantity × price และสร้างคอลัมน์ month จากคอลัมน์ date
4
สรุปยอดขายรายหมวด — หายอดรวม total_price และจำนวน order แยกตาม category โดยใช้ groupby
5
หาสินค้าขายดี — หา top-3 สินค้าที่มียอด total_price รวมสูงสุด และบันทึกผลเป็นไฟล์ top_products.csv
เงื่อนไขและข้อกำหนด
✅
ต้องใช้ pandas เท่านั้น ห้ามใช้ loop Python วนซ้ำแถวข้อมูล
✅
คอลัมน์ date ต้องแปลงเป็น datetime64 ก่อนดึง month
✅
ผลลัพธ์งาน 4 ต้องมีคอลัมน์: category, total_revenue, order_count
✅
ไฟล์ top_products.csv ต้องไม่มี index column (ใช้ index=False)
🚫
ห้ามลบแถวที่มี missing values ในคอลัมน์ price — ให้เติมด้วยค่า median แทน
🚫
ห้าม hardcode ชื่อสินค้า ต้องใช้ groupby + sort_values + head()
ตัวอย่างเอาท์พุทที่ต้องการ
งาน 4 — ผลลัพธ์ groupby (DataFrame)
category      total_revenue  order_count
Clothing           14940.0           4
Electronics        35250.0           5
ตัวเลขขึ้นอยู่กับข้อมูลจริงใน CSV ที่ใช้ — รูปแบบต้องตรง

งาน 5 — top_products.csv (ไฟล์ output)
product,total_price
แล็ปท็อป ASUS,28000.0
หูฟัง Sony,4500.0
กางเกงยีนส์,1780.0
ทักษะที่ฝึกในโปรเจกต์นี้
read_csv / to_csv
dtypes / info / isnull
fillna / dropna
to_datetime
assign / คอลัมน์ใหม่
groupby + agg
sort_values + head
rename
boolean filtering
🔵 = Data loading/cleaning   🟢 = Analysis/Output