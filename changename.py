last = 36
import os
dir = '.'
allfiles = os.listdir(dir)
files_mp4 = [ fname for fname in allfiles if fname.endswith('.mp4')]
files_txt = [ fname for fname in allfiles if fname.endswith('.txt')]
print("mp4:",files_mp4)
print("txt:",files_txt)
date = input("Fecha: ")
temario = input("Temario: ")
st = f"{last+1} - {date} {temario}"
os.rename(files_mp4[0], st+".mp4")
os.rename(files_txt[0], st+".txt")

print(st)
with open("changename.py") as f:
    lines = f.readlines()

st = lines[0]
number = [int(s) for s in st.split() if s.isdigit()]
number = number[0]

lines[0] = f"last = {number+1}"+"\n"

with open("changename.py", "w") as f:
    f.writelines(lines)
