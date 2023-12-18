import csv
import pickle
import os

def loadTablePKL(filename):
    _, ext = os.path.splitext(filename)
    if ext == '.pkl':
        with open(filename, 'rb') as f:
            table = pickle.load(f)
            attributes = {'format': 'pickle'}
    else:
        raise ValueError('Unsupported file format.')

    return {'attributes': attributes, 'data': table}

def loadTableCSV(filename):
    _, ext = os.path.splitext(filename)
    if ext == '.csv':
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            table = list(reader)
            attributes = {'delimiter': ','}
    else:
        raise ValueError('Unsupported file format.')

    return {'attributes': attributes, 'data': table}

def saveTableCSV(table, filename):
    _, ext = os.path.splitext(filename)
    if ext == '.csv':
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(table['data'])
    else:
        raise ValueError('Unsupported file format.')
    
def saveTablePKL(table, filename):
    _, ext = os.path.splitext(filename)
    if ext == '.pkl':
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(table['data'])
    else:
        raise ValueError('Unsupported file format.')
    
def saveTableTXT(table, filename):
    _, ext = os.path.splitext(filename)
    if ext == '.txt':
        with open(filename, 'w') as f:
            for row in table['data']:
                f.write(' '.join(map(str, row)))
                f.write('\n')
    else:
        raise ValueError('Unsupported file format.')   
