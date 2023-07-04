f = open("english_new.txt", "r")
contents = f.read().replace('\n',' ')
print(contents)

f.close()



'''
with open('csv_demo.csv', 'a') as f:
    f.write('name,grade\n')
    f.write('isaac,60\n')
    f.write('andy,50\n')
'''