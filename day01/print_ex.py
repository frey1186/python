__author__ = 'yangfeilong'

name = input("name:")
age = input("age:")
job = input("job:")

print("information of " + name + "\nName:" + name + "\nAge:" + age + "\nJob:" + job)

print("information of %s\nName:%s\nAge:%s\nJob:%s" % (name, name, age, job))


msg = '''
Information of %s:
    Name:%s
    Age:%s
    Job:%s
''' % (name, name, age, job)
print(msg)
