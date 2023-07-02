from XSystemUI import XSystemUI
from experta import *


class LoadsEn(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.xsys_ui = XSystemUI(1)

    @DefFacts()
    def _initial_action(self):
        yield Fact(Problem="urination")
        print(" An Expert System for Diagnosing".center(80, "*"))
        print(" urination problems".center(80, "*"))
        print("".center(80, "*"))
        print("".center(80, "*"))

    # Rule 1
    @Rule(Fact(Problem='urination'), NOT(Fact(Q1=W())))
    def ask_id(self):
        self.declare(
            Fact(Q1=self.xsys_ui.temp))

    # Rule 2
    @Rule(Fact(Problem='urination'), (Fact(Q1='yes')))
    def ask_1(self):
        self.declare(
            Fact(Q2=self.xsys_ui.ask_question("Q2: Is your urine cloudy?: ")))

    # Rule 3
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), (Fact(Q2='yes')))))
    def ask_2(self):
        self.declare(
            Fact(Q3=self.xsys_ui.ask_question("Q3: Do you have a fever and/or backache?")))

    # Rule 4
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'))))
    def ask_3(self):
        self.declare(
            Fact(Q5=self.xsys_ui.ask_question("Q5: Are you a man, and do you have an ache under your scrotum? ")))

    # Rule 5
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'))))
    def ask_4(self):
        self.declare(
            Fact(
                Q6=self.xsys_ui.ask_question(
                    "Q6: Are you a man, and do you have a discharge from the tip of your penis? ")))

    # Rule 6
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'))))
    def ask_5(self):
        self.declare(
            Fact(Q7=self.xsys_ui.ask_question(
                "Q7: Do you have the urge to urinate after just using the restroom, and are you only urinating small amounts at a time? ")))

    # Rule 7
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'))))
    def ask_6(self):
        self.declare(
            Fact(Q8=self.xsys_ui.ask_question("Q8: Are you producing more urine than usual? ")))

    # Rule 8
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='yes'))))
    def ask_7(self):
        self.declare(
            Fact(Q9=self.xsys_ui.ask_question(
                "Q9: Have you been losing weight, drinking lots of fluids and/or have a history of diabetes in the family?")))

    # Rule 9
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'))))
    def ask_8(self):
        self.declare(
            Fact(
                Q10=self.xsys_ui.ask_question("Q10: Are you a woman, and do you leak urine when you cough or sneeze?")))

    # Rule 10
    @Rule(Fact(Problem='urination'), (
            AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'),
                Fact(Q10='no'))))
    def ask_9(self):
        self.declare(
            Fact(Q11=self.xsys_ui.ask_question(
                "Q11: Are you a man, and do you leak or dribble urine after you urinate, or do you have problems starting the urine stream, or do you wake many times at night to urinate? ")))

    # Rule 11
    @Rule(Fact(Problem='urination'), (
            AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'),
                Fact(Q10='no'),
                Fact(Q11='no'))))
    def ask_10(self):
        self.declare(
            Fact(Q12=self.xsys_ui.ask_question("Q12: Do you have blood in your urine?")))

    # Rule 12
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'))))
    def ask_11(self):
        self.declare(
            Fact(Q4=self.xsys_ui.ask_question(
                "Q4: Do you have sharp, knife-like, intense pains in your back or groin?")))

    # Rule 13
    @Rule(Fact(Problem='urination'), (Fact(Q1='no')))
    def ask_12(self):
        self.declare(
            Fact(Q7=self.xsys_ui.ask_question(
                "Q7: Do you have the urge to urinate after just using the restroom, and are you only urinating small amounts at a time?")))

    # Rule 14
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='no'), Fact(Q7='no'))))
    def ask_13(self):
        self.declare(
            Fact(Q8=self.xsys_ui.ask_question("Q8: Are you producing more urine than usual?")))

    # Rule 15
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='yes'))))
    def ask_14(self):
        self.declare(
            Fact(Q9=self.xsys_ui.ask_question(
                "Q9: Have you been losing weight, drinking lots of fluids and/or have a history of diabetes in the family?")))

    # Rule 16
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'))))
    def ask_15(self):
        self.declare(
            Fact(
                Q10=self.xsys_ui.ask_question("Q10: Are you a woman, and do you leak urine when you cough or sneeze?")))

    # Rule 17
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'))))
    def ask_16(self):
        self.declare(
            Fact(Q11=self.xsys_ui.ask_question(
                "Q11: Are you a man, and do you leak or dribble urine after you urinate, or do you have problems starting the urine stream, or do you wake many times at night to urinate?")))

    # Rule 18
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'), Fact(Q11='no'))))
    def ask_17(self):
        self.declare(
            Fact(Q12=self.xsys_ui.ask_question("Q12:Do you have blood in your urine?")))

    # Rule 19
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='yes'))))
    def ask_18(self):
        self.declare(
            Fact(Q13=self.xsys_ui.ask_question("Q13: Do you suffer from chills, nausea and vomiting? ")))

    # Rule 20
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'))))
    def ask_19(self):
        self.declare(
            Fact(Q14=self.xsys_ui.ask_question("Q14:Do you have frequent urinary tract infections? ")))

    # Rule 21
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'))))
    def ask_20(self):
        self.declare(
            Fact(Q17=self.xsys_ui.ask_question(
                "Q9: Have you been losing weight, drinking lots of fluids and/or have a history of diabetes in the family? ")))

    # Rule 22
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'), Fact(Q17='yes'))))
    def ask_21(self):
        self.declare(
            Fact(Q15=self.xsys_ui.ask_question(
                "Q15:Do you suffer from pain in the bones and the presence of swelling in the thighs? ")))

    # Rule 23
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'), Fact(Q17='yes'),
               Fact(Q15='yes'))))
    def ask_22(self):
        self.declare(
            Fact(Q16=self.xsys_ui.ask_question("Are you male and notice high blood pressure? ")))

    # Rule 24
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='yes'))))
    def ask_23(self):
        self.declare(
            Fact(Q18=self.xsys_ui.ask_question("Do you suffer from pain when ejaculation and difficulty in erection? ")))

    ##############################
    # output
    ##############################
    # Rule 19
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='yes'), Fact(Q18='no'))))
    def diagnosis_1(self):
        print(self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                        "You may have PROSTATITIS, an infection of the prostate gland.",
                                        "See your doctor."))

    # Rule 20
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='yes'), Fact(Q13='no'))))
    def diagnosis_2(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "Pain and fever may be caused by an infection of the kidneys called PYELONEPHRITIS.",
                                  "See your doctor right away.")

        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print("Pain and fever may be caused by an infection of the kidneys called PYELONEPHRITIS.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    # Rule 21
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='yes'))))
    def diagnosis_3(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "These may be symptoms of an INFECTION such as URETHRITIS or a SEXUALLY TRANSMITTED INFECTION, such as GONORRHEA.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "These may be symptoms of an INFECTION such as URETHRITIS or a SEXUALLY TRANSMITTED INFECTION, such as GONORRHEA.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    # Rule 22
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='yes'))))
    def diagnosis_4(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "Your symptoms may be caused by an infection in the bladder, called CYSTITIS, or from an irritation of the bladder, called INTERSTITIAL CYSTITIS, or from a KIDNEY STONE stuck in the bladder, or a chemical in the urine.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "Your symptoms may be caused by an infection in the bladder, called CYSTITIS, or from an irritation of the bladder, called INTERSTITIAL CYSTITIS, or from a KIDNEY STONE stuck in the bladder, or a chemical in the urine.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    # Rule 23
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='no'))))
    def diagnosis_5(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have a KIDNEY STONE or another serious problem.",
                                  "See your doctor or go to the emergency room right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(" You may have a KIDNEY STONE or another serious problem.")
        print("SELF CARE".center(20, "*"))
        print("")
        print("EMERGENCY".center(30, "*"))
        print("See your doctor or go to the emergency room right away.")

    # Rule 24
    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='no'))))
    def diagnosis_6(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have a BLADDER INFECTION or a more serious problem with the KIDNEYS.",
                                  "See your doctor right away. Left untreated, problems with your kidneys may cause blood poisoning.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print("You may have a BLADDER INFECTION or a more serious problem with the KIDNEYS.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away. Left untreated, problems with your kidneys may cause blood poisoning.")

    # Rule 25
    @Rule(Fact(Problem='urination'), (
    AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='yes'), Fact(Q9='yes'))))
    def diagnosis_7(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have DIABETES, a condition in which your body lacks insulin or doesn’t use it in the right way.",
                                  "See your doctor.")

        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " You may have DIABETES, a condition in which your body lacks insulin or doesn’t use it in the right way.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor.")

    # Rule 26
    @Rule(Fact(Problem='urination'), (
    AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='yes'), Fact(Q9='no'))))
    def diagnosis_8(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may be taking a medicine that can cause increased urination. Drinking liquids containing caffeine can also cause increased urination.",
                                  "You may want to check with your doctor. If you drink caffeinated beverages, try decreasing the amount you drink.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "You may be taking a medicine that can cause increased urination. Drinking liquids containing caffeine can also cause increased urination.")
        print("SELF CARE".center(20, "*"))
        print(
            "You may want to check with your doctor. If you drink caffeinated beverages, try decreasing the amount you drink.")

    # Rule 27
    @Rule(Fact(Problem='urination'), (
    AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='yes'))))
    def diagnosis_9(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  " Your symptoms may be from a weakness in the bladder due to childbirth or aging. This weakness causes STRESS INCONTINENCE.",
                                  "Absorbent protection may be helpful. Kegel exercises may help strengthen muscles that support the bladder. See your doctor.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " Your symptoms may be from a weakness in the bladder due to childbirth or aging. This weakness causes STRESS INCONTINENCE.")
        print("SELF CARE".center(20, "*"))
        print(
            "Absorbent protection may be helpful. Kegel exercises may help strengthen muscles that support the bladder. See your doctor.")

    # Rule 28
    @Rule(Fact(Problem='urination'), (
    AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'),
        Fact(Q11='yes'))))
    def diagnosis_10(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  " You may have a problem with your PROSTATE GLAND. Your symptoms may be caused by a benign (noncancerous) ENLARGEMENT or a more serious condition such as INFECTION or CANCER.",
                                  "See your doctor.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " You may have a problem with your PROSTATE GLAND. Your symptoms may be caused by a benign (noncancerous) ENLARGEMENT or a more serious condition such as INFECTION or CANCER.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor.")

    # Rule 29
    @Rule(Fact(Problem='urination'), (
    AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'),
        Fact(Q11='no'), Fact(Q12='yes'))))
    def diagnosis_11(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have a KIDNEY STONE, a TUMOR in the kidney or bladder, a BLADDER INFECTION, TRAUMA to your kidney, or possibly a BLEEDING DISORDER.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " You may have a KIDNEY STONE, a TUMOR in the kidney or bladder, a BLADDER INFECTION, TRAUMA to your kidney, or possibly a BLEEDING DISORDER.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    # Rule 30
    @Rule(Fact(Problem='urination'), (
    AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='no'), Fact(Q6='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'),
        Fact(Q11='no'), Fact(Q12='no'))))
    def diagnosis_12(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "For more information, please talk to your doctor. If you think the problem is serious, call your doctor right away.",
                                  "")
        print("")
        print("Possible Causes".center(20, "*"))
        print("".center(80, "*"))
        print("SELF CARE".center(20, "*"))
        print(
            "For more information, please talk to your doctor. If you think the problem is serious, call your doctor right away.")

    # Rule 31
    @Rule(Fact(Problem='urination'),(AND(Fact(Q1='no'), Fact(Q7='yes'))))
    def diagnosis_13(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "Your symptoms may be caused by an infection in the bladder, called CYSTITIS, or from an irritation of the bladder, called INTERSTITIAL CYSTITIS, or from a KIDNEY STONE stuck in the bladder, or a chemical in the urine..",
                                  "See your doctor right away")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "Your symptoms may be caused by an infection in the bladder, called CYSTITIS, or from an irritation of the bladder, called INTERSTITIAL CYSTITIS, or from a KIDNEY STONE stuck in the bladder, or a chemical in the urine.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    # Rule 32
    @Rule(Fact(Problem='urination'),(AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='yes'), Fact(Q9='yes'))))
    def diagnosis_14(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have DIABETES, a condition in which your body lacks insulin or doesn’t use it in the right way..",
                                  "See your doctor")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " You may have DIABETES, a condition in which your body lacks insulin or doesn’t use it in the right way.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor.")

    # Rule 33
    @Rule(Fact(Problem='urination'),(AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='yes'), Fact(Q9='no'))))
    def diagnosis_15(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may be taking a medicine that can cause increased urination. Drinking liquids containing caffeine can also cause increased urination.",
                                  "You may want to check with your doctor. If you drink caffeinated beverages, try decreasing the amount you drink")
        print("".center(80, "*"))
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "You may be taking a medicine that can cause increased urination. Drinking liquids containing caffeine can also cause increased urination.")
        print("SELF CARE".center(20, "*"))
        print(
            "You may want to check with your doctor. If you drink caffeinated beverages, try decreasing the amount you drink.")

    # Rule 34
    @Rule(Fact(Problem='urination'),(AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='yes'))))
    def diagnosis_16(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "Your symptoms may be from a weakness in the bladder due to childbirth or aging. This weakness causes STRESS INCONTINENCE..",
                                  "Absorbent protection may be helpful. Kegel exercises may help strengthen muscles that support the bladder. See your doctor.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " Your symptoms may be from a weakness in the bladder due to childbirth or aging. This weakness causes STRESS INCONTINENCE.")
        print("SELF CARE".center(20, "*"))
        print(
            "Absorbent protection may be helpful. Kegel exercises may help strengthen muscles that support the bladder. See your doctor.")

    # Rule 35
    @Rule(Fact(Problem='urination'),(AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'), Fact(Q11='yes'))))
    def diagnosis_17(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have a problem with your PROSTATE GLAND. Your symptoms may be caused by a benign (noncancerous) ENLARGEMENT or a more serious condition such as INFECTION or CANCER..",
                                  "See your doctor")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "You may have a problem with your PROSTATE GLAND. Your symptoms may be caused by a benign (noncancerous) ENLARGEMENT or a more serious condition such as INFECTION or CANCER.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor.")

    # Rule 36
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'), Fact(Q11='no'), Fact(Q12='yes'))))
    def diagnosis_18(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "You may have a KIDNEY STONE, a TUMOR in the kidney or bladder, a BLADDER INFECTION, TRAUMA to your kidney, or possibly a BLEEDING DISORDER..",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " You may have a KIDNEY STONE, a TUMOR in the kidney or bladder, a BLADDER INFECTION, TRAUMA to your kidney, or possibly a BLEEDING DISORDER.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    # Rule 37
    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='no'), Fact(Q7='no'), Fact(Q8='no'), Fact(Q10='no'), Fact(Q11='no'), Fact(Q12='no'))))
    def diagnosis_19(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "For more information, please talk to your doctor. If you think the problem is serious, call your doctor right away..",
                                  "")
        print("".center(80, "*"))
        print("Possible Causes".center(20, "*"))
        print("".center(80, "*"))
        print("SELF CARE".center(20, "*"))
        print(
            "For more information, please talk to your doctor. If you think the problem is serious, call your doctor right away.")

    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='yes'), Fact(Q13='yes'))))
    def diagnosis_20(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  " It could be a urinary tract infection.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " It could be a urinary tract infection.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'), Fact(Q17='no'))))
    def diagnosis_21(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  " It could be a urinary tract infection.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            " It could be a urinary tract infection.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'), Fact(Q17='yes'),
               Fact(Q15='yes'), Fact(Q16='no'))))
    def diagnosis_22(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "These symptoms may indicate the presence of a serious disease (bladder cancer), and you should see a doctor as soon as possible.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print(
            "These symptoms may indicate the presence of a serious disease (bladder cancer), and you should see a doctor as soon as possible.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    @Rule(Fact(Problem='urination'),
          (AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'), Fact(Q17='yes'),
               Fact(Q15='no'))))
    def diagnosis_23(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "It could be kidney stones.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print("It could be kidney stones.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    @Rule(Fact(Problem='urination'), (
            AND(Fact(Q1='yes'), Fact(Q2='yes'), Fact(Q3='no'), Fact(Q4='yes'), Fact(Q14='yes'), Fact(Q17='yes'),
                Fact(Q15='yes'),
                Fact(Q16='yes'))))
    def diagnosis_24(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "These symptoms may indicate urethral obstruction, please see a doctor immediately.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print("These symptoms may indicate urethral obstruction, please see a doctor immediately.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")

    @Rule(Fact(Problem='urination'), (AND(Fact(Q1='yes'), Fact(Q2='no'), Fact(Q5='yes'), Fact(Q18='yes'))))
    def diagnosis_25(self):
        self.xsys_ui.print_result("Possible Causes" + "\nDIAGNOSIS",
                                  "There may be prostate cancer, please see your doctor as soon as possible.",
                                  "See your doctor right away.")
        print("")
        print("Possible Causes".center(20, "*"))
        print("DIAGNOSIS".center(20, "*"))
        print("There may be prostate cancer, please see your doctor as soon as possible.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor right away.")
