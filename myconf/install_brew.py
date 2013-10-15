import os

p = os.path.join(os.path.dirname(__file__), 'brew_requirement.txt')

with open(p,'rb') as f:
    s = f.read()
l = s.split('\n')
l = map(lambda s:s.strip(),l)
l = filter(lambda s:not s.startswith('#'),l)
l = filter(lambda s:len(s),l)

for i in l:
    os.system("brew install {}".format(i))
