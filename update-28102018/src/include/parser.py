from collections import OrderedDict

def gen_html (fname, reps, edges):
    f3 = open (fname, "w")
    print ("<!doctype HTML>", file=f3)
    print ("<html><head><title>validate</title></head>",file=f3)
    print ("<style> th { border: 1px solid #222; min-width: 75px} </style>", file=f3)
    print ("<body>",file=f3)

    for e,v in edges.items():
        matches = v.split(",")
        print ("<hr>", file=f3)

        print ("<table><tr><th>", file=f3)
        print ("<img src=\"../../thumbnails/" +  reps[e] + "\"/>", file=f3)
        print ("</th>", file=f3)
        print ("<th> cluster: ", e ," <br> matches: ", matches, "</th>", file=f3)

        print ("<th>", file=f3)
        for m in matches:
            print ("<img src=\"../../thumbnails/" + reps[m] + "\"/>", file=f3)
        print ("</ht></tr></table>", file=f3)
    print ("</body></html>",file=f3)

def parse_representatives (fname):
    f2 = open (fname, "r")
    reps = {}
    for line in f2:
        reps[line.split(" ")[0]] = line.split(" ")[1].rstrip()
    return reps

def parse_links (fname):
    f = open (fname, "r")
    edges = OrderedDict() 
    for line in f:
        elem = line.split(" ")
        s = elem[0]
        t = elem[1]
        w = elem[2]

        if int(w) > 1:
            if not edges.get(s):
               edges[s] = t
            else:
               edges[s] = edges[s] + "," + t
    return edges
