from configparser import ConfigParser, ExtendedInterpolation

# c=ConfigParser()
# c["settings"]={
#     'debug':"true",
#     'secret_key':"abc123",
#     'log_path':"D:\Pythonprograms"
#     }
# c["DB"]={
#     'db_name':"Mysql",
#     'db_drive':"RDBMS",
#     'db_port':8888
#     }
# f=open("D:\Pythonprograms\\sample2.ini","w")
# c.write(f)
# f.close()


#read a config file
c=ConfigParser(interpolation=ExtendedInterpolation())
c.read("D:\Pythonprograms\\sample2.ini")
print(c.sections()) #how many blocks in the file
print(c.get("settings",'secret_key'))
print(c.options("settings")) #to get the options in settings
print("DB"in c)
print(c.get('DB','db_port'))
print(c.getint('DB','db_defalult_port',fallback=3306)) #instead of typecasting we use getint method
print(c.getboolean("settings",'debug'))