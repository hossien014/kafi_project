import logging
import os

def write_listof_file(_root_path,out_filename):

      
      liste_of_audio =os.listdir(_root_path) # get liste of audio 
      # [logger.info(_root_path+"/"+item) for item in liste_of_audio] # write liste in file
      
      f= open(out_filename,"w",encoding="utf-8")
      for item in liste_of_audio :
            path = _root_path+"/"+item
            f.write(path+"\n")
      f.close()

'''remove line at given index and return its value'''
def reomve_line(path,index:int)->str:
      txtfile=open(path,mode="r+")
      lines= txtfile.readlines() 
      deleted_line=lines[index] 
      lines.pop(index)  
      # clean all text  
      txtfile.seek(0)      
      txtfile.truncate()
      
      txtfile.writelines(lines)      
      txtfile.close()
      
      return deleted_line

def get_unprocessed_video(index:int=0):
      
      f=open("unprocessed_video.txt","r",encoding="utf-8") 
      return f.readlines()[index]


if __name__ == "__main__":
      
      root_path = "E:/kafi"

      write_listof_file(root_path,"unprocessed_video.txt") 


            
      # reomve_line("unprocessed_video.log",0)
