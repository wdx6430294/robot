# -*- coding: utf-8 -*-
import os

"""firefox : firefox.exe,geckodriver.exe """
"""Chrome : chromedriver.exe , IEDriverServer.exe """

def Cleanbrowser (process_name_1,process_name_2):

  try :
    
      os.system("taskkill /f /im " + process_name_1)
  
      os.system("taskkill /f /im " + process_name_2)
      
  except Exception as e:
    
   print('Error:',e)

if __name__ == "__main__":

    Cleanbrowser("firefox.exe","geckodriver.exe")

