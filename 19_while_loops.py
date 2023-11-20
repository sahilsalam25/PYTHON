# While loops in python
'''
# print 1 to 45 number :
a=0
while a<=45:
    # print("SAHIL : " + str(a))
    print(a) 
    a=a+1 '''
# prg to print fruits from a list
''' fruits=['apple','guava','mango','grape','papaya','kiwi','banana']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+2    '''
    
### Game-1...WAP to guess a word :
''' secret_word= "Secret"
guess= " "   
while guess!=secret_word:
    guess=input("Enter the Word : ")
    
print("Congrats, You Win !") '''
### Game-1...WAP to guess a word with a limit of 3:
secret_word= "Secret"
guess_count=0
guess_limit=3
out_of_guesses=False
guess= " "   
while guess!=secret_word and not(out_of_guesses):
      if guess_count<guess_limit:
         guess=input("Enter the Word : ")
         guess_count +=1
      else:
          out_of_guesses=True  
         
if out_of_guesses:
          print("Out of Guesses ," "You Lose !")
else:        
          print("Congrats, You Win !")
    
    