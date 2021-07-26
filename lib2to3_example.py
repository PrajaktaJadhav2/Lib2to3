def greet(name):
    print("Hello, {0}!".format(name))
print("What's your name?")
name = input()
greet(name)


dict = {"C" : 8, "C++" : 7.5 , "Java" : 8.2}

for key,val in dict.iteritems():
    print key,val


# 2to3 lib2to3_example.py 
# RefactoringTool: Skipping optional fixer: buffer
# RefactoringTool: Skipping optional fixer: idioms
# RefactoringTool: Skipping optional fixer: set_literal
# RefactoringTool: Skipping optional fixer: ws_comma
# RefactoringTool: Refactored lib2to3_example.py
# --- lib2to3_example.py  (original)
# +++ lib2to3_example.py  (refactored)
# @@ -1,5 +1,5 @@
#  def greet(name):
# -    print "Hello, {0}!".format(name)
# -print "What's your name?"
# -name = raw_input()
# +    print("Hello, {0}!".format(name))
# +print("What's your name?")
# +name = input()
#  greet(name)
# RefactoringTool: Files that need to be modified:
# RefactoringTool: lib2to3_example.py



# 2to3 -w lib2to3_example.py 
# RefactoringTool: Skipping optional fixer: buffer
# RefactoringTool: Skipping optional fixer: idioms
# RefactoringTool: Skipping optional fixer: set_literal
# RefactoringTool: Skipping optional fixer: ws_comma
# RefactoringTool: Refactored lib2to3_example.py
# --- lib2to3_example.py  (original)
# +++ lib2to3_example.py  (refactored)
# @@ -1,5 +1,5 @@
#  def greet(name):
# -    print "Hello, {0}!".format(name)
# -print "What's your name?"
# -name = raw_input()
# +    print("Hello, {0}!".format(name))
# +print("What's your name?")
# +name = input()
#  greet(name)
# RefactoringTool: Files that were modified:
# RefactoringTool: lib2to3_example.py