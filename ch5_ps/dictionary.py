a={
    "kiran":"ray",
    "surya":"sun",
    "ful":"flower",
    "shala":"school"
}
print(a) #{'kiran': 'ray', 'surya': 'sun', 'ful': 'flower', 'shala': 'school'}
print(a.items()) #dict_items([('kiran', 'ray'), ('surya', 'sun'), ('ful', 'flower'), ('shala', 'school')])
print(a.keys()) #dict_keys(['kiran', 'surya', 'ful', 'shala'])

#updating list:
a.update({"shala":"collage"})
a.update({"pankha":"fan"})
print(a) #{'kiran': 'ray', 'surya': 'sun', 'ful': 'flower', 'shala': 'collage', 'pankha': 'fan'}  

#get value by key:
print(a.get("kiran")) #ray