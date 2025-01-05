#RULES
# If the number is even, divide it by two.
# If the number is odd, triple it and add one.

import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from dotenv import load_dotenv
import os
import uuid
import json as js

load_dotenv()

if(not os.path.exists('.env')):
    print('Creating config file...')
    try:
        f = open('.env','w')
        f.write('PLT_GRAPH=1 #Creates MatplotLib window\nOUT_CONSOLE=0 #Outputs result on console\nOUT_JSON=0 #Outputs result on json')
        print('[+] Config file created.')
    except Exception as e:
        print('[x]Could not create config file. Please create it manually.')
        print('File name: .env\nContent: PLT_GRAPH=1 #Creates MatplotLib window\n\t OUT_CONSOLE=0 #Outputs result on console\n\t OUT_JSON=0 #Outputs result on json')

def mtplt_graph(initnum,store):
    print("Generating Graph...")

    fig, ax = plt.subplots(figsize=(10, 6))
    
    axis = plt.gca()
    x_axis = axis.axes.get_xaxis()
    x_axis = x_axis.set_visible(False)
    
    
    plt.plot(range(len(store)), store, '-o', label=f'Collatz Sequence for {initnum}')
    plt.title("Collatz Conjecture Graph")

    for i, num in enumerate(store):
        ax.annotate(
            str(num),  
            (i, num),  
            textcoords="offset points", 
            xytext=(0, 8),
            ha='center',  
            fontsize=8,
        )
        
        
    
    plt.ylabel(f'Iterations of {initnum}', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def console_out(initnum,store):
    print(f'Init:{initnum}\nIterations: {store}\nLength: {len(store)}')

def out_json(initnum,store):
    try:
        content = {
            'init': initnum,              
            'iterations': store,
            'length':len(store)       
        }
        
        for index, value in enumerate(store):
            content[index] = value
        
        
        filename = f'{initnum}_{uuid.uuid4()}.json'
        
        with open(filename, 'w') as f:
            js.dump(content,f)
        
        print(f'[+] Successfully exported results to {filename}')
            
    except Exception as e:
        print(f'[x] Error: {e}')
        print('[x] Could not export results as json.')
        
try:
    args = sys.argv 
    # Checking for param errors
    if(len(args) > 2):
        print('USAGE:\tpython main.py <value>\n\tpython main.py 3')
        exit()
    if(len(args) < 2):
        print('USAGE:\tpython main.py <value>\n\tpython main.py 3')
        exit()
    
    #set value & check if it is positive
    value = int(args[1])
    initnum = value
    store = [value]

    if(value < 0 or value == 0):
        print('[x] Value must be positive')
        print('USAGE:\tpython main.py <value>\n\tpython main.py 3')
        exit()

    while(value != 0):
        if(value & 1):
            value = value * 3 + 1
        else:
            value = round(value / 2)
            
        store.append(value)
        if(len(store) > 3 and store[-3] == 4 and store[-2] == 2 and store[-1] == 1):
            break
    
    

    mtplt = int(os.getenv("PLT_GRAPH"))
    console = int(os.getenv("OUT_CONSOLE"))
    json = int(os.getenv("OUT_JSON"))

    if(console == 1):
        console_out(initnum,store)
    
    if(json == 1):
        out_json(initnum,store)

    if(mtplt == 1):
        mtplt_graph(initnum,store)
    
    

except Exception as e:
    print(e)
    print('USAGE:\tpython main.py <value:Integer>\n\tpython main.py 3')
    exit()
    

