
# What this program does
this is a python daemon that logs tweets corresponding to certain keywords in real time using Twitter Streaming API. You can set your keywords in the config.py file.
Tweets are stored using a DBMS. You can set the DBMS you want to use in the **config.py** file. Currently only MySQL is supported, but it's very easy to bring support for other RDMBS, you just have to provide a different DBConnection interface implementation. (see the docs)
The program only purpose is to store Tweets on the DB, there's no option to visualize them in the program, you will have to write custom SQL or use phpmyadmin to visualize them and eventually extract statistics

# How to setup
- create Twitter account

- create Twitter application at: https://apps.twitter.com/

- install Python3 and MySQL

- install Python dependncies:
  > pip install tweepy

  > pip install mysqlclient

- create db tables. the db tables sql is in file **db.sql**, you can import it with phpmyadmin

- edit **config.py** file adding Tweeter API and MySQL authentication data

- run
  > python3 run.py
  
  once the program is started the only way to stop it is with KeyboardInterrupt (ctrl + c). 
  
  # Documentation
  
  in the folder doc there's a pdf file that explains how the program is structured in case you want to change stuff or add new features.
  For any help or info feel welcome to contact me at:
  ferrariepifanio@gmail.com
