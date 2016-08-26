# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd --- print working directory, tells you where you are
cd --- change directory
ls --- list contents of working directory
touch  fileName --- creats a new file
mkdir directoryName(s)(path) -- create directory use -p to create a whole path at once
cd .. -- moves up one level in the directory tree
pushd pathName -- moves you to the final directory in the specified path leaving a placeholder at the origin
popd --  returns you to the origin that you pushed from
~  -- shorthand to reference your home folder instead of cd /Users/kylemix/directoryName use cd ~/directoryName
mv file or directory -- move an item between directories, rename a file or directory
less fileName -- page through a file, more controlled way of viewing file contents, best for large files
cat fileName(s) -- print file contents directly to the terminal, input multiple file names and it prints them both one after the other
rmdir directoryName(s) -- remove directory directory must be empty or this will error
rm -rf directoryName(s) -- recursive delete directory -- remove directory and all of the files/directories it contains 
man + command -- pull up documentation for the command- exit documentation with q




---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  list contents of working directory
`ls -a`  include dotfiles in list
`ls -l`  long format list which displays mode, last modified, size in number of 512 byte blocks, pathname, # of links, and more
`ls -lh` displays longform list, but with sizes listed in Byte Kilobyte Megabyte etc.  
`ls -lah`  h version of longform but dotfiles are included
`ls -t`  sorts list by datetime modified
`ls -Glp` colorizes list output based on file type in the longform and adds a "/" after each filename if it is a directory
---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-d --- displays only directories
-R --- also displays subdirectories, goes nuts if called on home folder... wow. helpful in more controlled settings
-1 --- puts everything on a single line,  makes it easier to read
-oh --- h version of longform without the groupname 
-F --- flags the filename ith an identifier * for executable, / for directory etc.
---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is used to process input from another unix command. It takes input from one command and passes it to another.  Say you had a list of student names in a text file called students.txt, and you needed a directory for each created in a folder on your desktop.  You would enter the command cat students.txt | xargs -I {} mkdir -p ~/Desktop/Students/{} and xargs would take the names listed in the file and pass them one by one to mkdir which would first create the path Desktop/students, and within the students directory create a directory for each name in the list.  
 

