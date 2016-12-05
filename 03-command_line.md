# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `mkdir -p [path]` - creates directory and path if it doesn't exist  
` cd ..` move up one directory  
`touch [file_name]` creates an empty file   
`pushd [path]` push directory, saves current location to list and brings you to directory specified  
`popd` pop directory, brings you to most recent location stored with pushd and removes that location from the list   
`less [file_name]` - display a file one page at a time  
`cat [file_name]` - displays entire contents of a file  
`!!` - repeat last command  
`clear` - clears the terminal  
`man` - read a manual page    

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - lists all files and directories in the working directory  
`ls -a` - includes hidden files and directories starting with a period  
`ls -l` - list shown in long format  
`ls -lh` - size (when printed as in long format) is human readable  
`ls -lah` - lists all files and folders including hidden files, in long format with human readable size  
`ls -t` - sorts files based on timestamp, newest files first    
`ls -Glp` - long format list which ommits group information and appends `/` to directories  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >  `ls -m` - comma separated list  
`ls -1` - list one entry per line  
`ls -r` - reverses list  
`ls -R` - recursive, list subdirectories  
`ls -u ` - sorts list by access time  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs stands for execute arguments. It is used to execute commands based on arguments from standard input.  
` find . -name '*.py' | xargs rm`  
This command finds all python files and removes them.

 

