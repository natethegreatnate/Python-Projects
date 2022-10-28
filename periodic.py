lut={
"a":{"Ac","Ag","Al","Am","Ar","As","At","Au"},
"b":{"B","Ba","Be","Bh","Bi","Bk","Br"},
"c":{"C","Ca","Cd","Ce","Cf","Cl","Cm","Cn","Co","Cr","Cs","Cu"},
"d":{"Db","Ds","Dy"},
"e":{"Er","Es","Eu"},
"f":{"F","Fe","Fl","Fm","Fr"},
"g":{"Ga","Gd","Ge"},
"h":{"H","He","Hf","Hg","Ho","Hs"},
"i":{"I","In","Ir"},
"j":{},
"k":{"K","Kr"},
"l":{"La","Li","Lr","Lu","Lv"},
"m":{"Mc","Md","Mg","Mn","Mo","Mt"},
"n":{"N","Na","Nb","Nd","Ne","Nh","Ni","No","Np"},
"o":{"O","Og","Os"},
"p":{"P","Pa","Pb","Pd","Pm","Po","Pr","Pt","Pu"},
"q":{},
"r":{"Ra","Rb","Re","Rf","Rg","Rh","Rn","Ru"},
"s":{"S","Sb","Sc","Se","Sg","Si","Sm","Sn","Sr"},
"t":{"Ta","Tb","Tc","Te","Th","Ti","Tl","Tm","Ts"},
"u":{"U"},
"v":{"V"},
"w":{"W"},
"x":{"Xe"},
"y":{"Y","Yb"},
"z":{"Zn","Zr"},
}
def convert(string):
  string=string.lower()+"  "
  arr=[""]
  out=[]
  while arr:
    for i in lut[string[len(arr[0])]]:
      if len(i)==1 or i[1]==string[len(arr[0])+1]:
        if len(arr[0]+i)==len(string)-2:
          out.append(arr[0]+i)
        else:
          arr.append(arr[0]+i)
    del arr[0]
  return out

print("Done: ",convert(input("String? ")))
