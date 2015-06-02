def get_list(p):

    with open(p,'rb') as f:
        s = f.read()
    l = s.split('\n')
    l = map(lambda s:s.strip(),l)
    l = filter(lambda s:not s.startswith('#'),l)
    l = filter(lambda s:len(s),l)
    return l


import sys

if len(sys.argv) !=3:
    print "{} first_file second_file"
    sys.exit(-1)

first = sys.argv[1]
last = sys.argv[2]

print "\n".join(sorted(list(set(get_list(first)) - set(get_list(last)))))
print "-"*80
print "\n".join(sorted(list(set(get_list(last)) - set(get_list(first)))))
