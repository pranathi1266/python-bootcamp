######string##########
#strings are immutable
#the method r len,isupper,islower,toupper,tolower,concat(+),isAlpha,isDigit,
'''str="helloworld"
#print(len(str))##11
#print(str.upper())##HELLO WORLD
#print(str.lower())##hello world
#print(str.capitalize())##Hello world
#print(str.title())##Hello World
#print(str.swapcase())##HELLO WORLD##it will swap upper to lower and lower to upper
#print(str.strip())##   hello world  ###hello World# it will remove spaces at staring and ending but not b/w spaces
#print(str.replace('a','z'))##hello worlda##hello worldz
#print(str.split())##['hello', 'world']
#print(str.split('a'))##hello worlda###['hello world', '']
#rint(str.isalpha())##Falseit will check spaces if spaces r present it will print false
#print(str.isalnum())#True#it will check spaces if spaces r present it will print false'''
'''str="hello world"
#print(str.isascii())#True##given num is ascii value or not
#print(str.isupper())#False
#print(str.islower())#True
#print(str.isnumeric())#False##
#print(str.istitle())#False
#print(str.isdecimal())#False
#print(str.isdigit())#0-9##False
#print(str.isspace())#False#if the str is empty like only space it will print true
#print(str.isprintable())#true#if any thing need to print#false#if nothing thing need to print'''
#######ascii values#############
'''print(ord('a'))
print(ord('A'))
print(ord('o'))
print(ord('O'))
print(ord('p'))'''
#####ascii to string#######
#print(chr('65'))
#######string######
#print(chr(97))
####ascii values###
'''for i in range(32,128):
    print(chr(i),end=" ")'''# ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ 
    #A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~
'''for i in range(65,128):
    print(chr(i),end=" ")'''#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~  
'''for i in range(65,90):
    print(chr(i),end=" ")'''#A B C D E F G H I J K L M N O P Q R S T U V W X Y 
'''for i in range(97,122):
    print(chr(i),end=" ")'''#a b c d e f g h i j k l m n o p q r s t u v w x y'''
'''for i in range(48,58):
    print(chr(i),end=" ")'''#0 1 2 3 4 5 6 7 8 9
'''for i in range(1,32):
    print(chr(i),end=" ")'''#☺ ☻ ♥ ♦ ♣ ♠      
                         #► ◄ ↕ ‼ ¶ § ▬ ↨ ↑ ↓ → ∟↔▲▼
