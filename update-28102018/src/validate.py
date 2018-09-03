from include.parser import *
from include.joiner import *

def main():
    reps = parse_representatives("../data/representatives.tsv")
    edges = parse_links("../data/intercluster-links.abc")
    e = wrapper(edges)
    gen_html ("../html/cluster-links.html", reps, e)

    ofile= open("../html/Matches.csv","w")
    print ("Cluster id, Similar Clusters", file=ofile)
    for k,v in e.items():
        print (k + "," + v, file=ofile)

if __name__=="__main__":
    main()



