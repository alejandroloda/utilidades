import os
import re
dir = '.'
reg = "(\d\d:\d\d:\d\d.\d\d\d) --> (\d\d:\d\d:\d\d.\d\d\d)"
pat = re.compile(reg)
allfiles = os.listdir(dir)
files_txt = [ fname for fname in allfiles if fname.endswith('.txt')]

def inc(h,m,s):
    s+=2
    if(s>=60):
        s-=60
        m+=1
        if(m>=60):
            m-=60
            h+=1
    return h,m,s


for file in files_txt:
    with open(file, encoding="utf8") as f:
        lines = f.readlines()
        outfile = open(file[:-3]+"sub",'w', encoding="utf8")
        for line in lines:
            g = pat.match(line)
            if g:
                h,m,s,mm = list(map(int,re.split(':|\.',g.group(2))))
                h,m,s = inc(h,m,s)
                new_g2 =  str(h).zfill(2) +":"+ str(m).zfill(2) +":"+ str(s).zfill(2) +"."+ str(mm).zfill(3)
                line = f"{g.group(1)} --> {new_g2}\n"
            outfile.write(line)
        outfile.close()
                            
                
                
                
            
