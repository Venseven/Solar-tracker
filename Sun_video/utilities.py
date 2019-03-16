
import cv2
import os
import sqlite3
import sys
from tqdm import tqdm
import time
import shutil
def _input_():
    video=str(input("Enter the video name :-"))
    path1=str(input("Enter the path of the folder you want to store :-"))
    return video,path1
def cloud():
    data=robust_cloud.retrieve()
    count=data[len(data)-1][1]
    count +=1
    database=Db(count)
    database.store()
def greetings():        
    columns = shutil.get_terminal_size().columns
    print("\n\n")
    print(" ====================".center(columns))
    print("||  ROBUST TECH INC ||".center(columns))
    print(" ====================".center(columns))
def welcome(count,path1):
    columns = shutil.get_terminal_size().columns
    print("\n\n\n")
    print("\nYour images has been stored in 'Robust_idno_{}' file and.. in path:{}\n".format(count,path1))
    print("Thank you for your Contribution..!".center(columns))
