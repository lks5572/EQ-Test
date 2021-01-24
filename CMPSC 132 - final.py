class EQ:
    def __init__(self, answers, total=0):
        self.answer=answers
        self.total=total
    def totalscore(self):
        for each in self.answer:
            self.total+=each
    @staticmethod
    def start():
        print("Evaluate each statement as you actually are,\n"
              "rather than as you think you should be.\n"
              "Rate 1-Not at all , 2-Rarely , 3-Sometimes , 4-Often , 5-Very Often")
    def results(self):
        print("Your EQ score is: ", self.total)
        if self.total<=34:
            print("You need to work on your emotional intelligence.\n"
                  "You may find that you feel overwhelmed by your emotions,\n"
                  "especially in stressful situations; or,\n"
                  "you may avoid conflict because you think that you'll find it distressing.\n\n"
                  "It's likely, too, that you find it hard to calm down after you've felt upset,\n"
                  "and you may struggle to build strong working relationships.")
        elif self.total<=55:
            print("Your emotional intelligence level is... OK.\n\n"
                  "You probably have good relationships with some of your colleagues,\n"
                  "but others may be more difficult to work with.")
        else:
            print("Great! You're an emotionally intelligent person.\n"
                  "You have great relationships, and you probably find that people approach you for advice.\n\n"
                  "However, when so many people admire your people skills,\n"
                  "it's easy to lose sight of your own needs.")
    def return_total(self):
        raise NotImplementedError("subclass must have a method to return private method")
class SelfAware(EQ):
    def return_total(self):
        return self.__results()
    def __results(self):#1,8,11
        self.total=self.answer[0]+self.answer[7]+self.answer[10]
        print("Your self-awareness score is:", self.total)
class SelfReg(EQ): #2,4,7
    def return_total(self):
        return self.__results()
    def __results(self):
        self.total=self.answer[1]+self.answer[3]+self.answer[6]
        print("Your self-regulation score is:", self.total)
class Motivation(EQ):#6,10,12
    def return_total(self):
        return self.__results()
    def __results(self):
        self.total=self.answer[5]+self.answer[9]+self.answer[11]
        print("Your motivation score is:", self.total)
class Empathy(EQ): #3,13,15
    def return_total(self):
        return self.__results()
    def __results(self):
        self.total=self.answer[2]+self.answer[12]+self.answer[14]
        print("Your empathy score is:", self.total)
class SocSkills(EQ):#5,9,14
    def return_total(self):
        return self.__results()
    def __results(self):
        self.total=self.answer[4]+self.answer[8]+self.answer[13]
        print("Your social skills score is:", self.total)
ans=[]
def QuizAns():
    a=input("Answer:")
    a=int(a)
    ans.append(a)
def questions():
    b=input("If you're ready, type 'YES' followed by the ENTER key: ")
    if b=='YES':
        print("I can recognize my emotions as I experience them")
        QuizAns()
        print("I can control my temper when I feel frustrated")
        QuizAns()
        print("People have told me that I'm a good listener")
        QuizAns()
        print("I know how to calm myself down when I feel anxious or upset")
        QuizAns()
        print("I enjoy organizing groups")
        QuizAns()
        print("I find it easy to focus on something over the long term")
        QuizAns()
        print("I find it easy to move on when I feel frustrated or unhappy.")
        QuizAns()
        print("I know my strengths and weaknesses")
        QuizAns()
        print("I don't avoid conflict and negotiations")
        QuizAns()
        print("I always enjoy my work")
        QuizAns()
        print("I ask people for feedback on what I do well, and how I can improve.")
        QuizAns()
        print("I set long-term goals, and review my progress regularly.")
        QuizAns()
        print("I find it easy to read other people's emotions.")
        QuizAns()
        print("I don't struggle to build rapport with others.")
        QuizAns()
        print("I use active listening skills when people speak to me.")
        QuizAns()
    else:
        pass

answer=EQ(ans)
answer.start()
questions()
print(ans)
SA=SelfAware(ans)
SR=SelfReg(ans)
M=Motivation(ans)
E=Empathy(ans)
SS=SocSkills(ans)
SA.return_total()
SR.return_total()
M.return_total()
E.return_total()
SS.return_total()
answer.totalscore()
answer.results()
#https://www.mindtools.com/pages/article/ei-quiz.htm