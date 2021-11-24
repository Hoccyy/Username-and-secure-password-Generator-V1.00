import string
import random

#wordbase and num generator
berskies = string.digits
wordBase = ["cats", "unicorn", "bed", "slendy", "ruby", "cherry", \
    "unicorns", "doge", "city", "gurls", "4lifer", "stacks", "aly",\
    "alyssa", "sandra", "tyler", "dave", "danish", "melly", "4kt", \
    "tim", "honest", "hank", "lambo", "nicki", "joe", "baby", "lil", "gang",\
     "otf", "ski", "yessir", "god", "pro", "timmy", "rat", "poop", "jess", \
    "lexi", "conny", "tekashi", "human", "trader", "light", "yagumi", "jay" \
    "muta", "tik", "mal", "boo", "headless"]

#acc maker
def fileMaker():
    #user
    usernm = random.choice(wordBase) + random.choice(wordBase) + ''.join(random.choice(berskies) for i in range(4))
    
    #password
    letters = string.ascii_letters
    pasMkr =  "password : " + ''.join(random.choice(letters) for i in range(14))

    #file
    with open('List_ofNames.txt', 'a') as f:
        f.write(usernm + "\n" + pasMkr + "\n\n")
'''
        add your tag name
        f.write("By disaster999 MAYBE ")
'''
for i in range(15):
    fileMaker()