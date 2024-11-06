students=[{'pid':1,'name':'rajesh'},{'pid':2,'name':'rahul'},{'pid':3,'name':'sruthi'}]

usinp=int(input('Give id number: '))

if usinp in range(0,len(students)+1):
    print(students[usinp-1]['name'])
else:
    print('Give valid id')