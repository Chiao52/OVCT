import os, sys

import set_init
set_init.init_file_name()
from functions import *

import configparser as cp
inifile_name = "./config.ini"
inifile = cp.ConfigParser()
inifile.read(inifile_name, 'UTF-8')

if __name__ == "__main__":
    set_init.init_file_name()

    All_Source_Path = inifile["File_Path"]["all_resources"]
    Folder_Path = inifile["File_Path"]["resources"]
    Updated_Source = initialize.get_current_list(All_Source_Path)
    menu.choose_operation(Updated_Source, All_Source_Path, Folder_Path)