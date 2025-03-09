for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += ('\t%3d' % (x*y))
    print(line)