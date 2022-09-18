"Quiz on Cybersecurity Terms"
a=str(input('''1.What is the term for the attempt to acquire sensitive information:
a Spyware
b Phishing
c Trojan
d None of these
'''))
b=str(input('''2.Full Form of SSL is:
a Secure Socket Layer
b Standard Socket Layer
c Standard Secure Layer
d None of these
'''))
c=str(input('''3.What are the measures to identity if the website is secure or not:
a By checking whether the website of HTTPS connection with SSL Certificate
b By checking whether the website of HTTP connection with SSL Certificate
c By adding an antivirus for internet security
d Both a and c
e Both b and c
f None of the above
'''))
d=str(input('''4.Which among is an ransomware released on 12 May 2017:
a WannaCry
b CryptoLocker
c Code Red
d Trojan
e None of the Above
'''))
e=str(input('''5.Which one of the following can be considered as the class of computer threats?
a Dos Attack
b Phishing
c Soliciting
d Both a and c
'''))
f=str(input('''6.Which of the following is considered as the unsolicited commercial email?
a Virus
b Malware
c Spam
d All of the above
'''))
g=str(input('''7.Which one of the following is a type of antivirus program?
a Kaspersky
b Quick Heal
c Norton
d All of the Above
e None of the Above
'''))
h=str(input('''8.Which of the following are famous and common cyber-attacks used by hackers to infiltrate the user's system?
a DDos and Derive-by Downloads
b Malware & Malvertising
c Phishing and Password attacks
d All of the above
'''))
i=str(input('''9.Hackers usually used the computer virus for ______ purpose:
a To log, monitor each and every user's stroke
b To gain access the sensitive information like user's Id and Passwords
c To corrupt the user's data stored in the computer system
d All of the above
'''))
j=str(input('''10.The response time and transit time is used to measure the ____________ of a network:
a Security
b Longevity
c Reliability
d Performance
'''))
if a == "b" or a =="Phishing":
    print("Correct Answer!")
else:
    print("The answer for the question is Phishing")
if b == "a" or b == "Secure Socket Layer":
    print("Correct Answer!")
else:
    print('''The answer for the question is Secure Socket Layer''')
if c == "d":
    print("Correct Answer!")
else:
    print('''The answer for the question is;
    *By checking whether the website of HTTPS connection with SSL Certificate 
    *By adding an antivirus for internet security ''')
if d == "a" or d == "Wanna Cry" or d == "WannaCry":
    print("Correct Answer!")
else:
    print('''The answer for the question is:
    *WannaCry, an encrypting ransomware computer worm, was initially released on 12 May 2017 ''')
if e == "a" or e =="Dos Attack":
    print("Correct Answer!")
else:
    print('''The answer for the question is Dos Attack;
    *A dos attack refers to the denial of service attack. It is a kind of cyber attack in which one tries to make a machine (or targeted application, website etc.) unavailable for its intended users. It is usually accomplished by disturbing the service temporarily or indefinitely of the target connected to the internet.''')
if f == "c" or f =="Spam":
    print("Correct Answer!")
else:
    print("The answer for the question is Spam")
if g == "d":
    print("Correct Answer!")
else:
    print("The answer for the question is All of the above, as Kaspersky,Quick Heal and Norton are all popular antivirus.") 
if h == "d" or h =="All of the above":
    print("Correct Answer!")
else:
    print('''The answer for the question is;
    DDoS (or denial of service), malware, drive-by downloads, phishing and password attacks are all some common and famous types of cyber-attacks used by hackers.''')
if i == "d" or i =="All of the above":
    print("Correct Answer!")
else:
    print('''The answer for the question is;
    *In general, hackers use computer viruses to perform several different tasks such as to corrupt the user's data stored in his system, to gain access the important information, to monitor or log each user's strokes.''')
if j == "d" or j =="Performance":
    print("Correct Answer!")
else:
    print('''The answer for the question is;
    On the basis of response time and transit time, the performance of a network is measured.''')
