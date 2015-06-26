import os


#os.system("brew install caskroom/cask/brew-cask")

p = os.path.join(os.path.dirname(__file__), 'brew_requirement.txt')

with open(p,'rb') as f:
    s = f.read()
l = s.split('\n')
l = map(lambda s:s.strip(),l)
l = filter(lambda s:not s.startswith('#'),l)
l = filter(lambda s:len(s),l)
commands = ["brew audit {} --download".format(i) for i in l]


from functools import partial
from multiprocessing import Pool
from subprocess import call

pool = Pool(30) # two concurrent commands at a time
for i, returncode in enumerate(pool.imap(partial(call, shell=True), commands)):
    if returncode != 0:
       print("%d command failed: %d" % (i, returncode))


#print("-"*80)
#raw_input("enter_to_start_install")

#for i in l:
#    os.system("brew cask install {}".format(i))



#print "brew cask install {}".format(' '.join(l))

#for i in l:
#    brew cask audit ${PACKAGENAME} --download
