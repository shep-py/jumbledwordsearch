from nltk.corpus import words
jw=input("enter the jumbled word:")
print("*****************************************************")
print("       the jumbled word entered:",jw)
sli=list(jw)
sle=len(sli) 
wl=words.words()
d=0
l0=[]
ll=[]
l1=[0,1]
for a in range(0,sle):
   for b in range(0,sle):
       if sli[a]==sli[b] and sli[a] not in ll :
           d+=1
   l0.append(d)           
   ll.append(sli[a])
   d=0
l0=[e for e in l0 if e not in l1]
fc=1
f=1
while f<=sle:
    
        fc*=f
        f+=1
if l0!=[]:
    fc1=1
    f1=1
    fct=0
    lf=[]
    pr=1
    for ele in l0:
        while f1<=ele:
            fc1*=f1
            f1+=1
        lf.append(fc1)
    for c in range(0,len(lf)):
        pr*=lf[c]
    fct=fc/pr
    print(jw," has repeated letters....")        
else:
    fct=fc
    print(jw,"has no repeated letters...")
x=sle
no=0
lno=[]
while x>=0:
    no=no+(10**x)*x
    lno.append(x)
    x-=1    
rev=0
rem=0
z=no
while z>0:
    rem=z%10
    rev=rev*10+rem
    z=z//10  
rc=rev
ct=0
slrc=[]
q=0
for j in range(rev,no+1):
    rem1=0
    lrc=[]
    y=rc
    while y>0:
        rem1=y%10
        lrc.append(rem1)
        y=y//10   
    clrc=[]
    for t in range(0,len(lrc)):
        clrc.append(lrc[t])
        clrc.sort(reverse=True) 
    if clrc==lno:
        slrc.append(lrc)
        slrc[q].remove(max(slrc[q]))
        q=q+1
    rc+=1
lpw=[]
ls_slrc=[list(t) for t in set(tuple(element) for element in slrc)]
for e1 in range(0,len(ls_slrc)):
    pw=""
    for e2 in range(0,len(ls_slrc[0])):
        pw=pw+jw[ls_slrc[e1][e2]]
    if pw not in lpw:
        lpw.append(pw)
fl=[]
for  lo in range(0,len(lpw)):
    if lpw[lo] in wl:
        fl.append(lpw[lo])
print("*****************************************************")        
print("         TOTAL NUMBER OF COMBINATIONS:",fct)
print("*****************************************************")
for pwe in fl:
    print("THE WORD COULD BE:",pwe)
         
     
      
      
        
        
    
   
    
   
        
        
       
       
       
    
    
    
    


    
    

        

        

    
    
    
    


   
   
          
       
    
    
