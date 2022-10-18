# Lesson 30 XML 

import xml.etree.ElementTree as ET

data = '''<person>
    <name>Tezcatlipoca</name>
    <phone type="intl">555-444-333</phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print(type(tree), tree) # <class 'xml.etree.ElementTree.Element'> <Element 'person' at 0x7f8a87ab28e0>

elName = tree.find('name')
print(elName) # <Element 'name' at 0x7fed9df59da0> 

name = elName.text
print(name) # Tezcatlipoca

attr = tree.find('email').get('hide')
print(attr) # yes

print('------------------')
data2 = '''<persons>
    <person id="1">
        <name>Tez</name>
        <phone type="intl">555-444-333</phone>
        <email hide="yes" />
    </person>
    <person id="2">
        <name>Zet</name>
        <phone>555</phone>
        <email hide="yes" />
    </person>
</persons>'''
tree2 = ET.fromstring(data2)
lst = tree2.findall('person')
for item in lst :
    print('Name:',item.find('name').text)
    print('attr1:',item.get('id'))
    print('attr2:',item.find('email').get('hide'))

lst2 = tree2.findall('person/name')
for item in lst2 :
    print(item.text)