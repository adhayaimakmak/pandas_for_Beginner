import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        # เพิ่ม error handling กรณีหาไฟล์ไม่เจอ
        try:
            self.data = pd.read_csv(file_path)
            print(f"Successfully loaded {file_path}")
        except FileNotFoundError:
            print("Error: File not found.")
            self.data = pd.DataFrame()

    def __str__(self):
        return self.data.head().to_string()
    
    def check_missing_values(self):
        return self.data.isnull().sum()
    
    def check_data_types(self):
        return self.data.dtypes
    
    def filter_by_category(self, column, value):
        # กรองข้อมูลแบบ Boolean Filtering
        self.data = self.data[self.data[column] == value]
        print(f"Data filtered by {column}: {value}")
    
    def convert_to_datetime(self, column_name):
        self.data[column_name] = pd.to_datetime(self.data[column_name], errors='coerce')
        self.data['month'] = self.data[column_name].dt.month
        print(f"Column '{column_name}' converted to datetime.")

    def manage_missing_values(self, column_name):
        # ตรวจสอบว่าเป็นคอลัมน์ตัวเลขหรือไม่ ถ้าใช่ให้เติมค่าเฉลี่ย
        if self.data[column_name].dtype in ['float64', 'int64']:
            median_val = self.data[column_name].median()
            self.data[column_name] = self.data[column_name].fillna(median_val)
            print(f"Filled missing in {column_name} with mean: {median_val:.2f}")
        else:
            self.data[column_name] = self.data[column_name].fillna('Unknown')
            print(f"Filled missing in {column_name} with 'Unknown'")

    def total_price(self):
        self.data['total_price'] = self.data['quantity'] * self.data['price']
    
    def summary_by_category(self, category_col, value_col):
        return (
    self.data.groupby(category_col).agg(
        total_revenue=(value_col, 'sum'),
        order_count=(value_col, 'count')
    ).reset_index()
)
    
    def find_top_products(self, top_n):
        result = self.data.groupby('product')['total_price'].sum().nlargest(top_n)
        print(result)
        result = result.reset_index().to_csv('top_products.csv',index=False,)
        print(f'Top {top_n} products saved to top_products.csv')
        
def main():
    processor = DataProcessor('sales.csv')
    
    if not processor.data.empty:
        print("--- Initial Data ---")
        print(processor)
        
        print("\n--- Missing Values ---")
        print(processor.check_missing_values())
        
        # 1. แปลงวันที่
        processor.convert_to_datetime('date')
        
        # 2. จัดการค่าว่างในคอลัมน์ price และ quantity 
        processor.manage_missing_values('price')
        processor.manage_missing_values('quantity')
        
        # 3. กรองเฉพาะรายการที่ 'status' เป็น 'completed'
        processor.filter_by_category('status', 'completed')
        
        # 4. คำนวณ total_pricec และสรุปตตาม category
        processor.total_price()
        print("\n--- Summary by Category ---")
        print(processor.summary_by_category('category', 'total_price'))
        
        #5  หา top-3 สินค้าที่มียอด total_price รวมสูงสุด
        processor.find_top_products(3)        
if __name__ == "__main__":
    main()