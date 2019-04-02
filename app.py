import os
import glob
str2=""
def GetFolder1(path,space):
    global str2
    a = glob.glob(path)
    if a==[]:
        return     
    for i in range(len(a)):  
        if(os.path.isdir(a[i])):         
                str1=str(a[i]).replace(" ","%20")
                str1=str1.replace("\\","/")
                if(space=="- "):
                        if a[i][:-1]=="NoUpload":
                                return
                        str2=str2+("## "+a[i][:-1]+"\n")
                        str2=str2+("***\n")
                else:   
                        if "bin" in str(a[i]) or "Properties" in str(a[i]) or "obj" in str(a[i]) or ".idea" in str(a[i]) or "out" in str(a[i]) or "src" in str(a[i]):
                                return
                        str2=str2+(space+"["+str(a[i]).split("\\")[len(str(a[i]).split("\\"))-1]+"]"+"(https://github.com/bsharabi/Advanced-CSharp/tree/master/{})".format(str1)+"\n")
                GetFolder1(str(a[i]+"\\*"),"  "+space)        

def RenameFolder():
    a= glob.glob("APP JS3\\*\\")
    print(a)
    for i in range(len(a)):
        os.rename(a[i], "APP JS3\\APP JS{}".format(i))

GetFolder1("*\\","- ")



file = open("Readme.md","w") 
file.write("# Design-Patterns\n\n") 
file.write(str2)    
file.close()
#RenameFolder()


