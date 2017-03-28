
def readCsv():
    with open('data', 'r') as f:
        headers = f.readline()
        headers = headers.split(',')
        print(headers[0])

        for line in f:
            line = line.split(',')
            check(line)

def check(vals):
    if(len(vals) != 18):
        return False
    if(vals[0] < 1 || vals[0] > 5):
        return False
    if(vals[1] < 1 || vals[1] > 2):
        return False
    if((vals[2] != -9 && vals[2] < 1) || vals[2] > 2):
        return False
    if((vals[3] != -9 && vals[3] < 1) || vals[3] > 5):
        return False
    if((vals[4] != -9 ))
