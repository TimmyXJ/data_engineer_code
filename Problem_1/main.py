import json
import random 
import string
import csv

def read_file():
    
    '''read original file and converted to json file'''
    with open('spec.json',encoding='utf-8') as f:
        input_meta = json.loads(f.read())
    
    return input_meta

def file_generator(input_meta,records=10):

    column_length =  input_meta['Offsets']
    
    metadata = [['' for _ in range(len(column_length))] for _ in range(records)]
    
    '''assume there are 10 records in the file.'''
    '''generage data depending on the length of the columns'''
    for i in range(records):
        for j in range(len(column_length)):            
            metadata[i][j] = ''.join(random.choice(string.ascii_lowercase) for k in range(int(column_length[j])))
    
    return metadata
    
def write_file(input_meta,records):
    
    '''write the data'''
    column_name = input_meta['ColumnNames']
    
    with open('spec_final.csv', 'w',encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow(column_name)
        write.writerows(records)
    
    
def main():
    
    input_meta = read_file()
    print("Completed reading file.")
    
    records = file_generator(input_meta,records=10)
    print("Completed generating file.")
    
    write_file(input_meta,records)
    print("Completed writing file.")
    
if __name__ == "__main__":
    main()
