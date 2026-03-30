import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
    def __str__(self):
        return self.data.head().to_string()

def main():
    data = DataProcessor(r'sales.csv')
    print(data)
if __name__ == "__main__":
    main()