print("Welcome to personality test")
#input("Please enter your name:")
#email = input("Please enter your email:")
print("1.Strongly Disagree")
print("2.Agree")
print("3.Neutral")
print("4.Agree")
print("5.Strongly Agree")
print("Type your answer from 1 to 5")
print()
#Extraversion (E)
#Introversion (I)
#Sensing (S)
#Intuition (N)
#Thinking (T)
#Feeling (F)
#Judging (J)
#Perceivign (P)


class Person:
    def __init__(self, EI, SN, TF, JP):
        self.EI = EI
        self.SN = SN
        self.TF = TF
        self.JP = JP
    def add_point(self, point):
        self.EI += point
    def add_point2(self, point2):
        self.SN += point2
    def add_point3(self, point3):
        self.TF += point3
    def add_point4(self, point4):
        self.JP += point4

def get_valid_input():
    while True:
        try:
            ans = int(input("Answer from 1 to 5: "))
            if 1 <= ans <= 5:
                return ans
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

personality = Person(0, 0, 0, 0)

print("1.You enjoy being the center of attention.")
ei1 = get_valid_input()
personality.add_point(ei1)
print()
print("2.You prefer spending weekends out with a big group of friends even though you are not close to them.")
ei2 = get_valid_input()
personality.add_point(ei2)
print()
print("3.You often speak before thinking things through.")
ei3 = get_valid_input()
personality.add_point(ei3)
print()
print("4.You feel bored or lonely when you're by yourself for too long")
ei4 = get_valid_input()
personality.add_point(ei4)
print()
print("5.You often find yourself starting conversations with strangers.")
ei5 = get_valid_input()
personality.add_point(ei5)
print()

print("6.You focus more on future possibilities than present details..")
sn1 = get_valid_input()
personality.add_point2(sn1)
print()
print("7.You enjoy discussing abstract or theoretical ideas.")
sn2 = get_valid_input()
personality.add_point2(sn2)
print()
print("8.You prefer exploring new ideas rather than following proven methods.")
sn3 = get_valid_input()
personality.add_point2(sn3)
print()
print("9.You trust your gut feelings more than hard facts.")
sn4 = get_valid_input()
personality.add_point2(sn4)
print()
print("10.You like thinking about what could be rather than what is?")
sn5 = get_valid_input()
personality.add_point2(sn5)
print()

print("11.You make decisions based more on logic than emotions.")
tf1 = get_valid_input()
personality.add_point3(tf1)
print()
print("12.You believe fairness is more important than kindness.")
tf2 = get_valid_input()
personality.add_point3(tf2)
print()
print("13.You value being right over keeping the peace.")
tf3 = get_valid_input()
personality.add_point3(tf3)
print()
print("14.You find it easy to separate feelings from facts..")
tf4 = get_valid_input()
personality.add_point3(tf4)
print()
print("15.You focus more on tasks than on how people feel about them.")
tf5 = get_valid_input()
personality.add_point3(tf5)
print()

print("16.You prefer having a detailed plan rather than going with the flow.")
jp1 = get_valid_input()
personality.add_point4(jp1)
print()
print("17.You feel stressed when things are left unfinished.")
jp2 = get_valid_input()
personality.add_point4(jp2)
print()
print("18.You like sticking to schedules and routines..")
jp3 = get_valid_input()
personality.add_point4(jp3)
print()
print("19.You often make decisions quickly and confidently..")
jp4 = get_valid_input()
personality.add_point4(jp4)
print()
print("20.You dislike last-minute changes to your plans.")
jp5 = get_valid_input()
personality.add_point4(jp5)
print()

print(f'Score of EI: {personality.EI}')
print(f'Score of SN: {personality.SN}')
print(f'Score of TF: {personality.TF}')
print(f'Score of JP: {personality.JP}')


def get_personality_type(p):
    if p.EI >= 15:
        ei_letter = 'E'
    else:
        ei_letter = 'I'
    if p.SN >= 15:
        sn_letter = 'S'
    else:
        sn_letter = 'N'
    if p.TF >= 15:
        tf_letter = 'T'
    else:
        tf_letter = 'F'
    if p.JP >= 15:
        jp_letter = 'J'
    else:
        jp_letter = 'P'

    return ei_letter + sn_letter + tf_letter + jp_letter


def print_personality_description(type_code):
    descriptions = {
        "ISTJ": "ISTJ - The Inspector: Responsible, serious, and loyal. You value traditions and prefer facts over theories.",
        "ISFJ": "ISFJ - The Defender: Warm, considerate, and quiet. You enjoy helping others and keeping harmony.",
        "INFJ": "INFJ - The Advocate: Insightful, creative, and deeply caring. You’re driven by your values.",
        "INTJ": "INTJ - The Mastermind: Strategic and logical. You love long-term planning and solving complex problems.",
        "ISTP": "ISTP - The Virtuoso: Practical and hands-on. You love figuring out how things work.",
        "ISFP": "ISFP - The Adventurer: Gentle, sensitive, and quiet. You enjoy living in the moment and expressing creativity.",
        "INFP": "INFP - The Mediator: Idealistic and empathetic. You strive to understand yourself and others.",
        "INTP": "INTP - The Logician: Curious and analytical. You love ideas and theories more than social interaction.",
        "ESTP": "ESTP - The Dynamo: Energetic and action-oriented. You enjoy taking risks and being spontaneous.",
        "ESFP": "ESFP - The Performer: Fun-loving, outgoing, and spontaneous. You bring energy to every room.",
        "ENFP": "ENFP - The Campaigner: Enthusiastic and imaginative. You see potential everywhere.",
        "ENTP": "ENTP - The Debater: Quick-witted and curious. You love discussions and intellectual challenges.",
        "ESTJ": "ESTJ - The Supervisor: Organized, honest, and dedicated. You value order and tradition.",
        "ESFJ": "ESFJ - The Provider: Caring and social. You enjoy helping others and feeling appreciated.",
        "ENFJ": "ENFJ - The Protagonist: Charismatic and inspiring. You love leading people toward a common goal.",
        "ENTJ": "ENTJ - The Commander: Bold and confident. You enjoy leadership and making strategic decisions."
    }
    print()
    print(f"Your personality type is: {type_code}")
    print(descriptions.get(type_code, "No description available for this type."))

# Get type and show result
initialize = get_personality_type(personality)
print_personality_description(initialize)



