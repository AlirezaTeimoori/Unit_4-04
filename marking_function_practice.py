#Created by: Alireza Teimoori
#Created on: 6 Nov 2017
#Created for: ICS3UR-1
#Lesson: Unit 4-04
#This program gets the mark from user and passes percentage back to them


import ui


def calculate_percentage(mark):
    
    if mark == "4+":
        return "95%"
    elif mark == "4":
        return "90%"
    elif mark == "4-":
        return "85%"
    elif mark == "3+":
        return "80%"
    elif mark == "3":
        return "75%"
    elif mark == "3-":
        return "70%"
    elif mark == "2+":
        return "65%"
    elif mark == "2":
        return "60%"
    elif mark == "2-":
        return "55%"
    elif mark == "1+":
        return "50%"
    elif mark == "1":
        return "45%"
    elif mark == "1-":
        return "40%"
    elif mark == "R":
        return "30%"
    elif mark == "NE":
        return "0%"
    else :
        return "-1"
    
    

def confirm_button_touch_up_inside(sender):

    mark = view['mark_textfield'].text
    percentage = calculate_percentage(mark)
    view['percentage_label'].text = percentage


view = ui.load_view()
view.present('sheet')

