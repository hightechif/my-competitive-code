list = {'george':16,'amber':19}
search_age = input("Provide age : ")
for name, age in list.iteritems():
    if age == search_age:
        print(name)
