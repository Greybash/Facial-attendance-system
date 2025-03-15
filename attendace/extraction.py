import pandas as pd
from datetime import datetime

now= datetime.now()
current_date=now.strftime("%Y-%m-%d")
sub=input("Enter the subject name:")
file_path = current_date+'.csv' 
output_file = current_date+'_'+sub+'_final_attendance.csv'  
try:
    df = pd.read_csv(file_path, on_bad_lines='skip')

   
    unique_objects = df.iloc[:, 0].unique()
    unique1 = df.iloc[:, 0].unique()
   

   
    unique_df = pd.DataFrame({
        sub.upper(): unique_objects,
        'ATTENDANCE': 'PRESENT '
    })
   

    unique_df.to_csv(output_file, index=False)

    print(f"Unique objects have been written to '{output_file}'")
except pd.errors.ParserError as e:
    print(f"Error parsing the file: {e}")

