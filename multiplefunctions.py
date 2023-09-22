class multipleFuntions():
    def listAISubFields():
        aiSubFieldList = ["Machine Learning","Neural Networks","Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for aiSubFieldItem in aiSubFieldList:
            print(aiSubFieldItem)

    def findOddEven():
        num=int(input("Enter the number:"))
        if((num%2) == 1):
            message = str(num) + " is a odd Number"
        else:
            message = str(num) + " is a even number"
        return message;
    
    def check_eligibility(gender, age):
        if gender.lower() == "male":
            if age >= 21:
                return f"Your gender {gender},Your age {age} ELIGIBLE"
            else:
                return f"Your gender {gender}, Your age {age}, NOT ELIGIBLE"
        elif gender.lower() == "female":
            if age >= 18:
                 return f"Your gender {gender}, Your age {age}, ELIGIBLE"
            else:
                return f"Your gender {gender}, Your age {age}, NOT ELIGIBLE"
        else:
            return f"Invalid input."

    def findTotalAndPercentage():
                subject1 = int(input(f"Enter the subject1 mark:"))  
                subject2 = int(input(f"Enter the subject2 mark:")) 
                subject3 = int(input(f"Enter the subject3 mark:"))
                subject4 = int(input(f"Enter the subject4 mark:"))
                subject5 = int(input(f"Enter the subject5 mark:"))
                subjectTotal = subject1 + subject2 + subject3 + subject4 + subject5
                percentage = subjectTotal/5
                print(f"Subject 1:{subject1}")
                print(f"Subject 2:{subject2}")
                print(f"Subject 3:{subject3}")
                print(f"Subject 4:{subject4}")
                print(f"Subject 5:{subject5}")
                print(f"Total : {subjectTotal}")
                print(f"Percentage : {percentage}")
                
    def calculate_area(height,breath):
        return (height*breath)/2

    def calculate_perimeter(height1, height2, breath):
        return height1 + height2 + breath