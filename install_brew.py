with open('brew_requirement.txt','rb') as f:
    s = f.read()
l = s.split('\n')
l = map(lambda s:s.strip(),l)
l = filter(lambda s:len(s),l)


print "export "

"""
brew tap phinze/homebrew-cask
brew install brew-cask

"""

print "brew cask audit {} --download".format(' '.join(l))

print ""

print "brew cask install {}".format(' '.join(l))

#for i in l:
#    brew cask audit ${PACKAGENAME} --download