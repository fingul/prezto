import os

p = os.path.join(os.path.dirname(__file__),'brew_requirement.txt')

with open(p,'rb') as f:
    s = f.read()
l = s.split('\n')
l = map(lambda s:s.strip(),l)
l = filter(lambda s:len(s),l)



print """
brew tap phinze/homebrew-cask
brew install brew-cask

"""

print "brew cask audit {} --download".format(' '.join(l))

print ""

print "brew cask install {}".format(' '.join(l))

#for i in l:
#    brew cask audit ${PACKAGENAME} --download