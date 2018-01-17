my_file=open("words.txt")
dict1={}
def read_word(my_file):
    for word in my_file:
        x=word.strip()
        dict1[x]=0
        print(dict1)



read_word(my_file)
