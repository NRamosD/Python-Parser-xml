import xml.etree.ElementTree as ET
from xml.dom import minidom

"""mytree = ET.parse('index.xml')
myroot = mytree.getroot()
print(myroot[0].tag)
for x in myroot.findall('country'):
    Name =x.find('name').text
    Female = x.find('female').text
    Male = x.find('male').text
    print('Pais = ', Name,'\nfemale = ', Female,'\nmale = ', Male,'\n')"""

##USANDO MINIDOM

dato = minidom.parse('index.xml')
tagname= dato.getElementsByTagName('country')
print('%d Paices:' %
      tagname.length)

for x in tagname:
        name = x.getElementsByTagName('name')[0]
        female = x.getElementsByTagName('female')[0]
        male = x.getElementsByTagName('male')[0]
        print("\nPais:%s \nfemale:%s \nmale:%s" %
              ( name.firstChild.data, female.firstChild.data, male.firstChild.data))