s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

#answer:

print(s) #{20, '20'}
print(len(s)) #2

#05 s={} type?
s1={}
print(type(s1)) #dict

s2 =()
print(type(s2)) #tuple

s3 = set()
print(type(s3)) #set