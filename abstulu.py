# import operator
# import speech_recognition as s_r
# import pyttsx3
# r = s_r.Recognizer()
# my_mic_device = s_r.Microphone(device_index=1)
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
# with my_mic_device as source:
#     r.adjust_for_ambient_noise(source)  #reduce noise
#     audio = r.listen(source)
# my_string=r.recognize_google(audio)
# print(my_string)
#
# def get_operator_fn(op):
#     return {
#         '+' : operator.add,
#         '-' : operator.sub,
#         'x' : operator.mul,
#         'Mod' : operator.mod,
#         'mod' : operator.mod,
#         '^' : operator.xor,
#         }[op]
# def calculateAbs(op1, oper, op2):
#     op1,op2 = int(op1), int(op2)
#     return get_operator_fn(oper)(op1, op2)
# a1=calculateAbs(*(my_string.split()))
# talk(a1)
