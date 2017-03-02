import breakit2
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring
from xml.dom import minidom
import DataStruct



def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")



root = Element('Connections',{'Name':"Connections",
'Export':"False",
'Protected':'wjdPzo1TsEdCfIRkAv0sMZlxRqXcc1QdzIyjJy8Hwg7am6jOL9XzS1wVHfkBu9eB'
,'ConfVersion':"2.5"})

letters=breakit2.breakit("template.csv")

keys=letters.keys()

for key in keys:
    letter=letters[key]
    if letter==None:
        continue
    record=DataStruct.Record
    record['Name']=key
    record['Type']="Container"
    letter_folder = SubElement(root, 'Node', record )  #create letter folder
    for l in letter:
        record=DataStruct.Record
        record['Name']=l.client
        record['Type']="Container"
        client_folder = SubElement(letter_folder, 'Node', record )
        for c in l.clients:
            record=DataStruct.Record
            record['Name']=l.client + " " + c.domain
            record['Type']="Connection"
            record['Hostname']=c.address
            record['UserField']=c.userfield
            connection=SubElement(client_folder, 'Node', record )

            

##document = ElementTree((root))
##document.write('file.xml', encoding='utf-8',xml_declaration=True)

#A hack to get the format of the first line correct. ElementTree.write is hard coded with ' rather than "
data=prettify(root).replace("'",'"')
tmp= data.split('\n')
tmp[0]='<?xml version="1.0" encoding="utf-8"?>'
with open('tmp.xml', 'w') as f:
    for line in tmp:
        f.write(line+'\n')
    
