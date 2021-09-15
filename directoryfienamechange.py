import os

def sai():
    i,j,k,l=0,0,0,0
    path= input("enter path of the directory: ")
    path=path.replace('\\','/')
    path=path+'/'
    for filename in os.listdir(path):
        type_file,ext= filename.split('.')
        if ext=='png':
            destiny = 'image'+str(i)+'.png'
            i+=1
        elif ext=='jpg':
            destiny = 'img' + str(k) + '.jpg'
            k+=1
        elif ext == 'docx':
            destiny = 'word' + str(j) + '.doc'
            j+=1
        elif ext == 'pdf':
            destiny = 'pdffile'+str(l)+'.pdf'
            l+=1
        my_source = path + filename
        my_destiny = path+ destiny
        os.rename(my_source,my_destiny)
if __name__ == '__main__':
    sai()