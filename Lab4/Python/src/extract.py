import pandas as pd

#cuando solo hay un unico archivo
def extract_candidates(path):
    df_candidates = pd.read_csv(path, sep=";")

    df_candidates.columns = [
        "first_name",
        "last_name",
        "email",
        "application_date",
        "country",
        "yoe",
        "seniority",
        "technology",
        "code_challenge_score",
        "technical_interview_score"
    ]

    return df_candidates




''' si se desea escalar se utilizaria asi (cuando hay mas de un archivo)
import glob 
import os
import pandas as pd 

#busca archivos con extension csv
def extract_candidates(path):
    
    csv_pattern = os.path.join(path, '*.csv')  # Builds "path/*.csv" safely across OS types
    csv_files = glob.glob(csv_pattern)
    
    extracted_data_csv = pd.DataFrame(columns=['First Name', 'Last Name', 'Email', 'Application Date', 'YOE', 'Technology', 'Code Challenge Score', 'Technical Interview Score']) 
    for file in csv_files:
        df = pd.read_csv(file)
        extracted_data_csv = pd.concat([extracted_data_csv, df], ignore_index=True)
    
    return extract_candidates
'''
