#break down

class Client:
    def __init__(self):
        self.address=""
        self.domain=""
        self.userfield=""
class Line:
    def __init__(self):
        ##self.num=0 ##Not used yet
        self.client=""
        self.clients=[]
        
    
def breakit(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    header=lines.pop(0)
    letters={}

    for one in range(97,123):
        letters[ str(chr(one)).upper()]=[]

    #print letters
    for i in lines:
        sub=i.split(",")
        line=getclientline(sub)
        letters[line.client[:1]].append(line)
    keys=letters.keys()


    return letters

def getclientline(sub):
    line=Line()
    line.client=sub.pop(0)
##    line.num= len(sub)/3
    for i in range(0,len(sub)/3):
        client=Client()
        con= sub[0:3]   #get data from list
        if(sub[0]==""):
            del sub[0:3]
            continue
        client.address=con[0]
        client.domain=con[1]
        client.userfield=con[2]
        line.clients.append(client)
        del sub[0:3]     # remove data after stored
    return line


