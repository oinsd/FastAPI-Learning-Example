"""yield的演示"""

def fun():
    try:
        print ('1')
        db = 'SessionLocal()' # db也可被赋予变量等
        yield db
    finally:
        print ('3')

for i in fun():
    print(i)
    print('2')

# fun()