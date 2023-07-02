from XSystemUI import XSystemUI
from experta import *


class LoadsAr(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.xsys_ui = XSystemUI(2)

    @DefFacts()
    def _initial_action(self):
        yield Fact(Problem="التبول")
        print(" نظام خبير للتشخيص".center(80, "*"))
        print(" مشاكل التبول".center(80, "*"))
        print("".center(80, "*"))
        print("".center(80, "*"))

    # Rule 1
    @Rule(Fact(Problem='التبول'), NOT(Fact(Q1=W())))
    def ask_id(self):
        self.declare(
            Fact(Q1=self.xsys_ui.temp))

    # Rule 2
    @Rule(Fact(Problem='التبول'), (Fact(Q1='نعم')))
    def ask_1(self):
        self.declare(
            Fact(Q2=self.xsys_ui.ask_question("س2: هل بولك عكر؟")))

    # Rule 3
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), (Fact(Q2='نعم')))))
    def ask_2(self):
        self.declare(
            Fact(Q3=self.xsys_ui.ask_question("س3: هل تعاني من الحرارة  / أو آلام في الظهر؟ ")))

    # Rule 4
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'))))
    def ask_3(self):
        self.declare(
            Fact(Q5=self.xsys_ui.ask_question("س 5: هل أنت رجل وهل لديك وجع تحت كيس الصفن؟ ")))

    # Rule 5
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'))))
    def ask_4(self):
        self.declare(
            Fact(Q6=self.xsys_ui.ask_question(
                "س 6: هل أنت رجل ولديك إفرازات من رأس قضيبك؟ ")))

    # Rule 6
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'))))
    def ask_5(self):
        self.declare(
            Fact(Q7=self.xsys_ui.ask_question(
                "س 7: هل لديك الرغبة في التبول بعد دخول الحمام فقط ، وهل تتبول بكميات قليلة في المرة الواحدة؟  ")))

    # Rule 7
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'))))
    def ask_6(self):
        self.declare(
            Fact(Q8=self.xsys_ui.ask_question("س 8: هل ينتج بول أكثر من المعتاد؟ ")))

    # Rule 8
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='نعم'))))
    def ask_7(self):
        self.declare(
            Fact(Q9=self.xsys_ui.ask_question(
                "س 9: هل كنت تفقد الوزن ، وشربت الكثير من السوائل  أو لديك تاريخ مرضي في الأسرة؟  ")))

    # Rule 9
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'))))
    def ask_8(self):
        self.declare(
            Fact(Q10=self.xsys_ui.ask_question("س 10: هل أنت امرأة وهل يتسرب البول عند السعال أو العطس ؟")))

    # Rule 10
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'),
                Fact(Q10='لا'))))
    def ask_9(self):
        self.declare(
            Fact(Q11=self.xsys_ui.ask_question(
                "س 11: هل أنت رجل وهل يتسرب البول أو يقطر منه بعد التبول ، أو لديك مشاكل في بدء مجرى البول ، أو هل تستيقظ عدة مرات ليلاً للتبول؟ ")))

    # Rule 11
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'),
                Fact(Q10='لا'),
                Fact(Q11='لا'))))
    def ask_10(self):
        self.declare(
            Fact(Q12=self.xsys_ui.ask_question("س 12: هل يوجد دم في بولك؟")))

    # Rule 12
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'))))
    def ask_11(self):
        self.declare(
            Fact(Q4=self.xsys_ui.ask_question(
                "س 4: هل تعانين من آلام حادة تشبه السكين في ظهرك أو فخذك؟ ")))

    # Rule 13
    @Rule(Fact(Problem='التبول'), (Fact(Q1='لا')))
    def ask_12(self):
        self.declare(
            Fact(Q7=self.xsys_ui.ask_question(
                "س 7: هل لديك الرغبة في التبول بعد استخدام الحمام فقط ، وهل تتبول بكميات قليلة فقط في المرة الواحدة؟")))

    # Rule 14
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'))))
    def ask_13(self):
        self.declare(
            Fact(Q8=self.xsys_ui.ask_question("س 8: هل ينتج بول أكثر من المعتاد؟  ")))

    # Rule 15
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='نعم'))))
    def ask_14(self):
        self.declare(
            Fact(Q9=self.xsys_ui.ask_question(
                "س 9: هل كنت تفقد الوزن ، وشربت الكثير من السوائل و / أو لديك تاريخ مرضي في الأسرة؟ ")))

    # Rule 16
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'))))
    def ask_15(self):
        self.declare(
            Fact(Q10=self.xsys_ui.ask_question(
                "س 10: هل أنت امرأة وهل يتسرب البول عند السعال أو العطس؟ ")))

    # Rule 17
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'), Fact(Q10='لا'))))
    def ask_16(self):
        self.declare(
            Fact(Q11=self.xsys_ui.ask_question(
                "س 11: هل أنت رجل وهل يتسرب البول أو يقطر منه بعد التبول ، أو لديك مشاكل في بدء مجرى البول ، أو هل تستيقظ عدة مرات ليلاً للتبول؟ ")))

    # Rule 18
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'), Fact(Q10='لا'), Fact(Q11='لا'))))
    def ask_17(self):
        self.declare(
            Fact(Q12=self.xsys_ui.ask_question("س 12: هل يوجد دم في بولك؟")))

    # Rule 19
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='نعم'))))
    def ask_18(self):
        self.declare(
            Fact(Q13=self.xsys_ui.ask_question("س 13: هل تعاني من قشعريرة وغثيان وتقيؤ ؟ ")))

    # Rule 20
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'))))
    def ask_19(self):
        self.declare(
            Fact(Q14=self.xsys_ui.ask_question("س 14: هل لديك التهابات مسالك بولية متكررة ؟ ")))

    # Rule 21
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'), Fact(Q14='نعم'))))
    def ask_20(self):
        self.declare(
            Fact(Q17=self.xsys_ui.ask_question(
                "س9: هل كنت تفقد الوزن ، وشربت الكثير من السوائل و / أو لديك تاريخ مرضي في الأسرة؟")))

    # Rule 22
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'), Fact(Q14='نعم'), Fact(Q17='نعم'))))
    def ask_21(self):
        self.declare(
            Fact(Q15=self.xsys_ui.ask_question("س 15:هل تعاني من ألم في العظام ووجود تورم في الفخذين ؟")))

    # Rule 23
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'), Fact(Q14='نعم'), Fact(Q17='نعم'),
               Fact(Q15='نعم'))))
    def ask_22(self):
        self.declare(
            Fact(Q16=self.xsys_ui.ask_question("س16: هل انت ذكر و تلاحظ وجود ارتفاع في ضغط الدم؟ ")))

    # Rule 24
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='نعم'))))
    def ask_23(self):
        self.declare(
            Fact(Q18=self.xsys_ui.ask_question("س17:  هل تعاني من ألم عند القذف وصعوبة في الانتصاب ؟")))

    ##############################
    # output
    ##############################

    # Rule 19
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='نعم'),Fact(Q18='لا'))))
    def diagnosis_1(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك التهاب البروستاتا ، وهو التهاب في غدة البروستاتا",
                                  "راجع طبيبك.")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد يكون لديك التهاب البروستاتا ، وهو التهاب في غدة البروستاتا")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك.")

    # Rule 20
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='نعم'), Fact(Q13='لا'))))
    def diagnosis_2(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد ينجم الألم وارتفاع الحرارة عن عدوى في الكلى تسمى PYELONEPHRITIS.",
                                  "راجع طبيبك على الفور")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد ينجم الألم وارتفاع الحرارة عن عدوى في الكلى تسمى PYELONEPHRITIS.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور")

    # Rule 21
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='نعم'))))
    def diagnosis_3(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون هذه أعراض عدوى مثل التهاب الإحليل أو عدوى منقولة جنسيًا ، مثل مرض السيلان.",
                                  "راجع طبيبك على الفور.")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تكون هذه أعراض عدوى مثل التهاب الإحليل أو عدوى منقولة جنسيًا ، مثل مرض السيلان.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور.")

    # Rule 22
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='نعم'))))
    def diagnosis_4(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون أعراضك ناتجة عن عدوى في المثانة ، تسمى التهاب المثانة ، أو بسبب تهيج المثانة ، الذي يسمى التهاب المثانة البيني ، أو من حصى الكلى العالق في المثانة ، أو بسبب مادة كيميائية في البول.",
                                  "راجع طبيبك على الفور.")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تكون أعراضك ناتجة عن عدوى في المثانة ، تسمى التهاب المثانة ، أو بسبب تهيج المثانة ، الذي يسمى التهاب المثانة البيني ، أو من حصى الكلى العالق في المثانة ، أو بسبب مادة كيميائية في البول.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور.")

    # Rule 23
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'),Fact(Q14='لا'))))
    def diagnosis_5(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك حصى في الكلى أو مشكلة خطيرة أخرى.",
                                  "حالة اسعافية,راجع طبيبك أو اذهب إلى الاسعاف على الفور")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد يكون لديك حصى في الكلى أو مشكلة خطيرة أخرى.")
        print("رعاية ذاتية".center(20, "*"))
        print("")
        print("حالة اسعافية".center(30, "*"))
        print("راجع طبيبك أو اذهب إلى الاسعاف على الفور")

    # Rule 24
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='لا'))))
    def diagnosis_6(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك التهاب المثانة أو مشكلة أكثر خطورة في الكلى.",
                                  "راجع طبيبك على الفور. إذا تُركت دون علاج ، فقد تؤدي مشاكل الكلى إلى تسمم الدم.")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد يكون لديك التهاب المثانة أو مشكلة أكثر خطورة في الكلى.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور. إذا تُركت دون علاج ، فقد تؤدي مشاكل الكلى إلى تسمم الدم.")

    # Rule 25
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='نعم'),
                Fact(Q9='نعم'))))
    def diagnosis_7(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون مصابًا بمرض السكري ، وهي حالة يفتقر فيها جسمك إلى الأنسولين أو لا يستخدمه بالطريقة الصحيحة.",
                                  "راجع طبيبك.")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            " قد تكون مصابًا بمرض السكري ، وهي حالة يفتقر فيها جسمك إلى الأنسولين أو لا يستخدمه بالطريقة الصحيحة.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك.")

    # Rule 26
    @Rule(Fact(Problem='التبول'), (
    AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='نعم'), Fact(Q9='لا'))))
    def diagnosis_8(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تتناولين دواء يمكن أن يسبب زيادة التبول. شرب السوائل المحتوية على الكافيين يمكن أن يسبب أيضًا زيادة التبول..",
                                  "قد ترغب في مراجعة طبيبك. إذا كنت تشرب المشروبات التي تحتوي على الكافيين ، فحاول تقليل الكمية التي تتناولها..")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تتناولين دواء يمكن أن يسبب زيادة التبول. شرب السوائل المحتوية على الكافيين يمكن أن يسبب أيضًا زيادة التبول..")
        print("رعاية ذاتية".center(20, "*"))
        print(
            "قد ترغب في مراجعة طبيبك. إذا كنت تشرب المشروبات التي تحتوي على الكافيين ، فحاول تقليل الكمية التي تتناولها..")

    # Rule 27
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'),
                Fact(Q10='نعم'))))
    def diagnosis_9(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون أعراضك من ضعف في المثانة بسبب الولادة أو الشيخوخة. هذا الضعف يسبب سلس البول.",
                                  "قد تكون الفوط الماصة مفيدة. قد تساعد تمارين كيجل في تقوية العضلات التي تدعم المثانة. راجع طبيبك")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            " قد تكون أعراضك من ضعف في المثانة بسبب الولادة أو الشيخوخة. هذا الضعف يسبب سلس البول.")
        print("رعاية ذاتية".center(20, "*"))
        print(
            "قد تكون الفوط الماصة مفيدة. قد تساعد تمارين كيجل في تقوية العضلات التي تدعم المثانة. راجع طبيبك.")

    # Rule 28
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'),
                Fact(Q10='لا'), Fact(Q11='نعم'))))
    def diagnosis_10(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك مشكلة مع غدة البروستات الخاصة بك. قد تكون أعراضك ناتجة عن تضخم حميد (غير سرطاني) أو حالة أكثر خطورة مثل العدوى أو السرطان",
                                  "راجع طبيبك")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد يكون لديك مشكلة مع غدة البروستات الخاصة بك. قد تكون أعراضك ناتجة عن تضخم حميد (غير سرطاني) أو حالة أكثر خطورة مثل العدوى أو السرطان.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك.")

    # Rule 29
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'),
                Fact(Q10='لا'),
                Fact(Q11='لا'), Fact(Q12='نعم'))))
    def diagnosis_11(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك حصوة في الكلى ، أو ورم في الكلى أو المثانة ، أو التهاب المثانة ، أو صدمة في كليتك ، أو من المحتمل أن يكون لديك الهيموفيليا ..",
                                  "راجع طبيبك على الفور.")
        print("")

        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد يكون لديك حصوة في الكلى ، أو ورم في الكلى أو المثانة ، أو التهاب المثانة ، أو صدمة في كليتك ، أو من المحتمل أن يكون لديك الهيموفيليا .")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور.")

    # Rule 30
    @Rule(Fact(Problem='التبول'), (
            AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='لا'), Fact(Q6='لا'), Fact(Q7='لا'), Fact(Q8='لا'),
                Fact(Q10='لا'),
                Fact(Q11='لا'), Fact(Q12='لا'))))
    def diagnosis_12(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "لمزيد من المعلومات ، يرجى التحدث مع طبيبك. إذا كنت تعتقد أن المشكلة خطيرة ، فاتصل بطبيبك على الفور.",
                                  "")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("".center(80, "*"))
        print("SELF CARE".center(20, "*"))
        print(
            "لمزيد من المعلومات ، يرجى التحدث مع طبيبك. إذا كنت تعتقد أن المشكلة خطيرة ، فاتصل بطبيبك على الفور.")

    # Rule 31
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='نعم'))))
    def diagnosis_13(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون أعراضك ناتجة عن عدوى في المثانة ، تسمى التهاب المثانة ، أو بسبب تهيج المثانة ، الذي يسمى التهاب المثانة البيني ، أو من حصى الكلى العالق في المثانة ، أو بسبب مادة كيميائية في البول.",
                                  "راجع طبيبك على الفور.")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تكون أعراضنا ناجمة عن عدوى في المثانة ، تسمى CYSTITIS ، أو من تهيج المثانة ، يسمى التهاب المثانة الخلالي ، أو من حصى الكلى العالق في المثانة ، أو بسبب مادة كيميائية في البول.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور.")

    # Rule 32
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='نعم'), Fact(Q9='نعم'))))
    def diagnosis_14(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون مصابًا بمرض السكري ، وهي حالة يفتقر فيها جسمك إلى الأنسولين أو لا يستخدمه بالطريقة الصحيحة.",
                                  "راجع طبيبك.")
        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            " قد تكون مصابًا بمرض السكري ، وهي حالة يفتقر فيها جسمك إلى الأنسولين أو لا يستخدمه بالطريقة الصحيحة.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك .")

    # Rule 33
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='نعم'), Fact(Q9='لا'))))
    def diagnosis_15(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تتناولين دواء يمكن أن يسبب زيادة التبول. شرب السوائل المحتوية على الكافيين يمكن أن يسبب أيضًا زيادة التبول..",
                                  "قد ترغب في مراجعة طبيبك. إذا كنت تشرب المشروبات التي تحتوي على الكافيين ، فحاول تقليل الكمية التي تتناولها..")
        print("")
        print("".center(80, "*"))
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تتناولين دواء يمكن أن يسبب زيادة التبول. شرب السوائل المحتوية على الكافيين يمكن أن يسبب أيضًا زيادة التبول.")
        print("رعاية ذاتية".center(20, "*"))
        print(
            "قد ترغب في مراجعة طبيبك. إذا كنت تشرب المشروبات التي تحتوي على الكافيين ، فحاول تقليل الكمية التي تتناولها.")

    # Rule 34
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'), Fact(Q10='نعم'))))
    def diagnosis_16(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون أعراضك من ضعف في المثانة بسبب الولادة أو الشيخوخة. هذا الضعف يسبب سلس البول.",
                                  "قد تكون الفوط الماصة مفيدة. قد تساعد تمارين كيجل في تقوية العضلات التي تدعم المثانة. راجع طبيبك")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            " قد تكون أعراضك من ضعف في المثانة بسبب الولادة أو الشيخوخة. هذا الضعف يسبب سلس البول.")
        print("SELF CARE".center(20, "*"))
        print(
            "قد تكون الفوط الماصة مفيدة. قد تساعد تمارين كيجل في تقوية العضلات التي تدعم المثانة. راجع طبيبك.")

    # Rule 35
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'), Fact(Q10='لا'), Fact(Q11='نعم'))))
    def diagnosis_17(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك مشكلة مع غدة البروستات الخاصة بك. قد تكون أعراضك ناتجة عن تضخم حميد (غير سرطاني) أو حالة أكثر خطورة مثل العدوى أو السرطان",
                                  "راجع طبيبك")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد يكون لديك مشكلة مع غدة البروستات الخاصة بك. قد تكون أعراضك ناتجة عن تضخم حميد (غير سرطاني) أو حالة أكثر خطورة مثل العدوى أو السرطان.")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك.")

    # Rule 36
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'), Fact(Q10='لا'), Fact(Q11='لا'), Fact(Q12='نعم'))))
    def diagnosis_18(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكون لديك حصوة في الكلى ، أو ورم في الكلى أو المثانة ، أو التهاب المثانة ، أو صدمة في كليتك ، أو من المحتمل أن يكون لديك الهيموفيليا ..",
                                  "راجع طبيبك على الفور.")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد يكون لديك حصوة في الكلى ، أو ورم في الكلى أو المثانة ، أو التهاب المثانة ، أو صدمة في كليتك ، أو من المحتمل أن يكون لديك الهيموفيليا .")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور.")

    # Rule 37
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='لا'), Fact(Q7='لا'), Fact(Q8='لا'), Fact(Q10='لا'), Fact(Q11='لا'), Fact(Q12='لا'))))
    def diagnosis_19(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "لمزيد من المعلومات ، يرجى التحدث مع طبيبك. إذا كنت تعتقد أن المشكلة خطيرة ، فاتصل بطبيبك على الفور.",
                                  "")
        print("".center(80, "*"))
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("".center(80, "*"))
        print("SELF CARE".center(20, "*"))
        print(
            "لمزيد من المعلومات ، يرجى التحدث مع طبيبك. إذا كنت تعتقد أن المشكلة خطيرة ، فاتصل بطبيبك على الفور.")

    # Rule 38
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='نعم'), Fact(Q13='نعم'))))
    def diagnosis_20(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكوت التهاب في المسالك البولية",
                                  "راجع طبيبك على الفور")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد يكوت التهاب في المسالك البولية ")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور")

    # Rule 39
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'),Fact(Q4='نعم'), Fact(Q14='نعم'),Fact(Q17='لا'))))
    def diagnosis_21(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يكوت التهاب في المسالك البولية",
                                  "راجع طبيبك على الفور")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد يكوت التهاب في المسالك البولية ")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك على الفور")

    # Rule 40
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'),Fact(Q14='نعم'), Fact(Q17='نعم'),Fact(Q15='نعم'),Fact(Q16='لا'))))
    def diagnosis_22(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون هذه الاعراض تدل على وجود مرض خطير (سرطان المثانة)",
                                  "راجع طبيبك على الفور")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تكون هذه الاعراض تدل على وجود مرض خطير (سرطان المثانة) , يجب مراجعة الطبيب في اسرع وقت .")
        print("راجع طبيبك.")

    # Rule 41
    @Rule(Fact(Problem='التبول'),
          (AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'),Fact(Q4='نعم'), Fact(Q14='نعم'), Fact(Q17='نعم'), Fact(Q15='لا'))))
    def diagnosis_23(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  " قد تكون حصى في الكلية ",
                                  "راجع طبيبك على الفور")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            " قد تكون حصى في الكلية ")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك .")

    # Rule 42
    @Rule(Fact(Problem='التبول'), (
    AND(Fact(Q1='نعم'), Fact(Q2='نعم'), Fact(Q3='لا'), Fact(Q4='نعم'), Fact(Q14='نعم'), Fact(Q17='نعم'), Fact(Q15='نعم'),
        Fact(Q16='نعم'))))
    def diagnosis_24(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد تكون هذه الاعراض تدل على انسداد الاحليل ",
                                  "راجع طبيبك على الفور")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print(
            "قد تكون هذه الاعراض تدل على انسداد الاحليل يرجى مراجعة الطبيب على الفور .")
        print("راجع طبيبك.")

    # Rule 43
    @Rule(Fact(Problem='التبول'), (AND(Fact(Q1='نعم'), Fact(Q2='لا'), Fact(Q5='نعم'),Fact(Q18='نعم'))))
    def diagnosis_25(self):
        self.xsys_ui.print_result("الأسباب المحتملة" + "\nالتشخيص",
                                  "قد يوجد سرطان في البروستاتا الرجاء مراجعة طبيبك في السرعة القصوى",
                                  "راجع طبيبك على الفور")

        print("")
        print("الأسباب المحتملة".center(20, "*"))
        print("التشخيص".center(20, "*"))
        print("قد يوجد سرطان في البروستاتا الرجاء مراجعة طبيبك في السرعة القصوى ")
        print("رعاية ذاتية".center(20, "*"))
        print("راجع طبيبك.")