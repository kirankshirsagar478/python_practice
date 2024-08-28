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
print(a) #{'kiran': 'ray', 'surya': 'sun', 'ful': 'flower', 'shala': 'collage'}

#get value by key:
print(a.get("kiran")) #ray