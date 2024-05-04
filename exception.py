'''try:
    l=[1,2]
    #print(l[2])
    print(l[0])
except:
    print("hella")
finally:
    print("finally") '''
#raise ValueError("abcd")  
'''def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print('value error')
    finally:
        print('end of fun')
l=[1,2,3,4,5]
try:
    fun(l,5)
except IndexError:
    print('Index error')
finally:
    print('end of blocks')  '''                           
    