with open("list2.dat") as f:
    for line in f:
        t = line.split()
        print str(t[0])+','+str(t[1])+','+str(t[2])
