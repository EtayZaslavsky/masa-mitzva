from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from accounts.models import Student
import uuid
import logging

logger = logging.getLogger(__name__)

def user_directory_path(instance, filename):
    extension = filename.split(".")[-1]
    my_uuid = str(uuid.uuid4())
    filename = f'{my_uuid}.{extension}'
    logger.critical(repr(instance))
    # return 'students/{0}/{1}'.format(instance.journey.student.id, filename)
    return 'students/{0}'.format(filename)


class Exhibit(models.Model):   
    def __str__(self):
        return f'{self._meta.verbose_name} {self.id}'
    
    def get_absolute_url(self):
        return reverse('exhibit-detail', kwargs={'pk': self.pk})

class Exhibit0(Exhibit):
    label = " יומן מסע זה שייך ל..."
    quote = """שלושה שמות נקראו לו לאדם: 
אחד מה שקוראים לו אביו ואימו,
ואחד מה שקוראים לו בני אדם,
ואחד מה שקונה הוא לעצמו.
טוב מכולן מה שקונה הוא לעצמו.
( מדרש תנחומא, פרק לה, פרשת ויקהל סימן א)"""
    pre_text = """בני ובנות מצווה יקרים/ות,

הגעתם לגיל שבו אתם מתחילים את המסע הפנימי המרתק בדרככם אל עולם הבוגרים, מסע מורכב וסבוך אשר יעצב את דמותכם ושבמהלכו תהפכו לחכמים ומחושבים יותר.
היום אתם נוטלים על עצמכם עול מצוות, מעתה ואילך, אתם אנשים בוגרים, אחראים על מעשיכם ומודעים אליהם.
אנחנו במועצה מאמינים בכם, ביכולתכם להצליח, ללמוד ולהשתפר כל הזמן ונלווה אתכם לאורך כל הדרך.
אתם פותחים פרק מאד משמעותי, בקרוב תתחילו את לימודיכם בחטיבות הביניים ובתיכונים ביישוב, תרכשו חברים חדשים, ידע, ביטחון וערכים.

בשמי ובשם המועצה המקומית גן יבנה אנחנו מאחלים לכם הצלחה בכל מעשי ידיכם, שלעולם תהיו סקרנים, שמחים ותיהנו מכל הטוב שיש לעולם לתת.

שלכם תמיד,
דרור אהרון, ראש המועצה המקומית גן יבנה, חבריה ועובדיה

תלמידות ותלמידים יקרים,
נתן אלתרמן כתב על חוזקה של הנקודה היהודית ואמר  כי "בנשמת היהודי  כך שמענו תמיד מחכה ליומה הנקודה היהודית. זה עניין של היסטוריה רבה וכבודה, בקיצור זו איננה כך סתם נקודה"  ובעצם הכוונה היא שהנקודה היהודית חבויה בליבו של כל אחד ואחת מאתנו וגם בליבו של מי שלא מודע לכך. 
במסע הערכי של  בני ובנות המצווה שאותו התחלתם  השנה,  עברתם בין תחנות שונות  חלקן אישיות, חלקן כיתתיות,  שכבתיות  וקהילתיות   למדתם את משמעות גיל המצוות, חקרתם  את שורשי המשפחה שלכם, שוחחתם על ערכים של אחריות, ערבות הדדית, מחויבות , התנדבות והתבגרות , חוויתם  רגעים של התרגשות, ומשפחתיות בחיפוש אחר תשובות לשאלות. התחברתם  למסורת היהודית ולזהות היהודית הישראלית, הכרתם דמויות נשים משמעותיות ומעוררות השראה,  חוויתם רגעים של לבד ורגעים של ביחד,  רגעים של שיתוף ורגעים של הסתכלות אל העבר עם ציפייה לעתיד. מסע זה,  שהתקיים בכל היישוב הוא בעצם חיבור בין כל הגורמים במערכת החינוך היישובית: מחלקת החינוך, בתי הספר היסודיים, חטיבות הביניים, תכנית  זיקה, ותנועות הנוער שחברו יחדיו  כדי לקיים את תכנית בני המצווה באופן יישובי.
אני בטוחות שתנצרו את הרגעים הללו בפינה קטנה וחמה בלב של כל אחד ואחת מכם.
זכרו תלמידים יקרים,  לפעול ברגישות בכל צעד שתעשו, להפעיל שיקול דעת בכל בחירה העומדת בפניכם.
זכרו להיות אמפטיים לזולת ולראות את העולם בעיניים פקוחות וטובות.
כל אלה מהווים את מוקד הקיום של היום שלנו, של שעותינו היפות, והוא מעתה גם חובתכם, ילדים יקרים ההופכים לבני מצווה. 
יש בכם כוחות רבים ויכולת ראיית המציאות כשל אדם בוגר. עליכם  לרתום את הנתונים האלה ולהוסיף עליהם הרבה רצון, חום וכוונות טובות ולהשאירם אצלכם כדרך חיים.
יצאתם   למסע מופלא אל הבגרות, אל האחריות, אל העתיד.
כולנו תקווה כי מסע זה שיימשך גם בחטיבת הביניים,  יהיה משמעותי לכם ולבני משפחותיכם. שתבררו ותמצאו את הנקודה היהודית האישית שלכם.  ונסיים בדבריו של הרב קוק מתוך ספרו אורות הקודש:  "בֶּן אָדָם, עֲלֵה לְמַעְלָה עֲלֵה, 
כִּי כֹּחַ עַז לְךָ, יֵשׁ לְךָ כַּנְפֵי רוּחַ, כַּנְפֵי נְשָׁרִים אַבִּירִים, אַל תְּכַחֵשׁ בָּם פֶּן יְכַחֲשׁוּ לְךָ, דְּרוֹשׁ אוֹתָם -
וְיִמָּצְאוּ לְךָ מִיָּד."
מאחלות לכם הצלחה רבה במסע המרגש אל הנקודה היהודית שלכם, גם בשנה הבאה,
אוהבות מנהלות בתי הספר היסודיים: לימור, איריס, דלית, יעל, רינת ומירב.

    בני ובנות מצווה יקרים,
מול עינינו, 
אתם גדלים ומתפתחים
וקונים לעצמכם את השם הייחודי לכם.
בהתפעמות ובאהבה,
אנחנו צופים בכם מפלסים את דרככם האישית
ומפסלים את הדמות הבוגרת שתהפכו להיות.

בלב תפילה,
שנתיב חייכם יזמן לכם קניית דעת וחוכמה,
עיצוב חיים של יושר וערכים
והזדמנויות להוכיח אחריות חברתית וערבות הדדית
בכל אשר תפנו.

מאחלים לכם
מסע אישי מרתק לבחינת זהותכם ושורשיכם
ומסע לאומי משמעותי של הצטרפות לעם יהודי עתיק
ולמדינה ישראלית צעירה ואהובה.

מכל הלב,
חברי צוות זיקה
    """
    my_name = models.CharField("שמי", max_length=100, blank=True)
    name_origin = models.CharField("מקור שמי", max_length=100, blank=True)
    born_date_loazi = models.CharField("נולדתי בתאריך עברי", max_length=100, blank=True)
    born_date_ivri = models.CharField("נולדתי בתאריך לועזי", max_length=100, blank=True)
    parents_names = models.CharField("שמות הוריי", max_length=100, blank=True)
    place_of_birth = models.CharField("מקום הולדתי", max_length=100, blank=True)
    my_photo = models.ImageField("העלה תמונה שלך", upload_to=user_directory_path, blank=True)
    
    class Meta:
        verbose_name = "הקדמה"
        verbose_name_plural = "הקדמות"

class Exhibit1(Exhibit):
    label = "להיות בן / בת מצווה"
    avuri = models.TextField("להיות בן מצווה עבורי...", blank=True)
    egdal = models.CharField("כשאגדל אני רוצה להיות...", max_length=100, blank=True)
    photo_yaldut = models.ImageField("העלה תמונת ילדות", upload_to=user_directory_path, blank=True)
    tsipiot = models.TextField("הציפיות שלי מהמסע הן:", blank=True)
    photo_today = models.ImageField("העלה תמונה שלך היום", upload_to=user_directory_path, blank=True)
    
    class Meta:
        verbose_name = "תחנה א'"
        verbose_name_plural = "תחנות א'"

class Exhibit2(Exhibit):
    label = "מצווה ואחריות"
    quote = """א-ח-ר-י-ו-ת
"המילה אחריות היא מילה מדהימה 
ראשית, היא מתחילה באות- א' ומסתיימת באות- ת', והכוונה היא שכשמישהו לוקח אחריות, היא צריכה להיות כוללת מההתחלה ועד הסוף. שנית, המילה אחריות היא מילה במשמעות מצטברת, כלומר: א - הכוונה היא לאני, קודם כל אני צריך לקחת אחריות על עצמי. אח - לאחר שלקחתי אחריות על עצמי אני יכול לקחת אחריות על אחי הכוונה למעגל הקרוב אלי. אחר - השלב הבא הוא לקיחת אחריות על האחר - והכוונה היא לכל אדם. אחרַי - ברגע שלקחתי אחריות על שלושת המעגלים הראשונים אני יכול להוביל אחרַי. אחריו - אמונה. יש כאלו שיגידו אלוהים, יש כאלו שיגידו הבריאה, אנרגיה קוסמית. ולבסוף – אחריות. מה שעוד לומדים מהמילה המדהימה הזו היא שיש חשיבות לסדר : אדם אינו יכול להיות אחראי על אחר לפני שהוא אחראי על עצמו."
"""
    hitndavti = models.CharField("במהלך כיתה ו' התנדבתי ב...", max_length=100, blank=True)
    litrom = models.TextField("במה ארצה להתנדב /לתרום בשנה הבאה ומדוע?", blank=True)
    rosh = models.TextField("אם הייתי ראש ממשלת ישראל הייתי ...", blank=True)
    
    class Meta:
        verbose_name = "תחנה ב'"
        verbose_name_plural = "תחנות ב'"

class Exhibit3(Exhibit):
    label = "ציר הזמן שלי"
    gil1 = models.CharField("תקופה א'", max_length=100, blank=True)
    gil2 = models.CharField("תקופה ב'", max_length=100, blank=True)
    gil3 = models.CharField("תקופה ג'", max_length=100, blank=True)
    gil4 = models.CharField("תקופה ד'", max_length=100, blank=True)
    avakesh1 = models.TextField("תחנה משמעותיות שאבקש לי בעתיד א'", blank=True)
    avakesh2 = models.TextField("תחנה משמעותיות שאבקש לי בעתיד ב'", blank=True)
    
    class Meta:
        verbose_name = "תחנה ג'"
        verbose_name_plural = "תחנות ג'"
        
class Exhibit4(Exhibit):
    label = "פעילות חוץ בית ספרית"
    quote = '"קום והתהלך בארץ בתרמיל ובמקל וודאי תפגוש בדרך שוב את ארץ ישראל" (יורם טהר לב)'
    htsaga = models.TextField("מה אזכור מהטיולים וההצגות", blank=True)
    arachim = models.CharField("אילו ערכים באו לידי ביטוי?", max_length=100, blank=True)
    
    class Meta:
        verbose_name = "תחנה ד'"
        verbose_name_plural = "תחנות ד'"

class Exhibit5(Exhibit):
    label = "הדרשה שלי"
    darsha_upload = models.FileField("העלה / העלי את הדרשה שלך", upload_to=user_directory_path, blank=True)
    
    class Meta:
        verbose_name = "תחנה ה'"
        verbose_name_plural = "תחנות ה'"
             
class Exhibit6(Exhibit):
    label = "מעמקי ליבי- סליחה..."
    quote = "ואהבת לרעך כמוך.."
    pre_text = """בתרבות צפון אפריקה היה נהוג: חמישה ימים לפני בר המצווה נהגו לספר את שיער ראשו של הבן. בדרכו לבית הכנסת היו מלווים אותו בני הקהילה בשירה וריקודים ואף נהגו לזרוק עליו סוכריות ואגוזים. בבוקר האם יצקה מים על ידי בנה והוא ביקש ממנה סליחה על כל פגיעה שפגע בה מאז ימי ילדותו."""
    sliha = models.TextField("אני שמחה שהצלחתי לבקש סליחה מ…", blank=True)
    salahti = models.TextField("אני גאה בעצמי שסלחתי ל…", blank=True)
    
    class Meta:
        verbose_name = "תחנה ו'"
        verbose_name_plural = "תחנות ו'"
        
class Exhibit7(Exhibit):
    label = "גיבורה/ מנהיגה"
    quote = '"   רבות בנות עשו חיל ואת עלית על כלנה    " משלי לא כט'
    post_text = """"""
    dmut1 = models.TextField("דמות נשית משמעותית בחיי", blank=True)
    dmut2 = models.TextField("דמות נשית המהווה השראה עבורי", blank=True)
    
    class Meta:
        verbose_name = "תחנה ז'"
        verbose_name_plural = "תחנות ז'"

class Exhibit8(Exhibit):
    label = '" תיקון עולם"'
    quote = '"צאו וראו איזוהי דרך ישרה שידבק בה האדם" (משנה מסכת אבות ב ח-ט)'
    hitnadvti = models.TextField("במהלך כיתה ז' התנדבתי ב....", blank=True)
    lamadti = models.TextField("מה למדתי מהתנדבות זו?", blank=True)
    shana = models.TextField("במה ארצה להתנדב / לתרום בשנה הבאה ומדוע?", blank=True)
    
    class Meta:
        verbose_name = "תחנה ח'"
        verbose_name_plural = "תחנות ח'"
        
class Exhibit9(Exhibit):
    label = "פעילות חווייתית עם תנועות הנוער של גן יבנה"
    quote = "אִישׁ, כְּמַתְּנַת יָדוֹ, כְּבִרְכַּת ה' אֱלֹהֶיךָ, אֲשֶׁר נָתַן-לָךְ (דברים טז)"
    giliti = models.TextField("בפעילות גיליתי שאני...", blank=True)
    erganno = models.TextField("מה אהבתי בפעילות שתנועות הנוער ארגנו לנו?", blank=True)
    
    class Meta:
        verbose_name = "תחנה ט'"
        verbose_name_plural = "תחנות ט'"
        
class Exhibit10(Exhibit):
    label = '"יצירה עם ערך"'
    erech_gallery = models.ImageField("העלו תמונות מתוך היצירה", upload_to=user_directory_path, blank=True)
    erech = models.TextField("מה למדתי מן התהליך ומדוע חשוב לקיים פעילות מסוג זה?", blank=True)
    
    class Meta:
        verbose_name = "תחנה י'"
        verbose_name_plural = "תחנות י'"
        
class Exhibit11(Exhibit):
    label = '"דע מאין באת ולאן אתה הולך"'
    quote = "לזכור את העבר, לחיות את ההווה, להאמין בעתיד (אבא קובנר)"
    reflacion = models.FileField("צרפו את הרפלקציה מתוך עבודת השורשים", upload_to=user_directory_path, blank=True)
    etgarim = models.TextField("ברפלקציה התייחסו לאתגרים בעבודתכם וגילויים חדשים", blank=True)
    
    class Meta:
        verbose_name = "תחנה יא'"
        verbose_name_plural = "תחנות יא'"
        
class Exhibit12(Exhibit):
    label = 'הצגת עבודת השורשים להורים'
    sium_gallery = models.ImageField("העלו תמונות מפעילות הסיום עם ההורים", upload_to=user_directory_path, blank=True)
    sium = models.TextField("בפעילות הסיום התרגשתי מ.... ", blank=True)
    
    class Meta:
        verbose_name = "תחנה יב'"
        verbose_name_plural = "תחנות יב'"
        
class Exhibit13(Exhibit):
    label = 'סוף המסע'
    hergashti = models.TextField("במבט לאחור על המסע הרגשתי/ למדתי ש.....", blank=True)
    
    class Meta:
        verbose_name = "תחנת סיום"
        verbose_name_plural = "תחנות סיום"
        
class Journey(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    current_exhibit = models.PositiveSmallIntegerField(default=0)
    exhibit_0 = models.OneToOneField(Exhibit0, on_delete=models.CASCADE, null=True)
    exhibit_1 = models.OneToOneField(Exhibit1, on_delete=models.CASCADE, null=True)
    exhibit_2 = models.OneToOneField(Exhibit2, on_delete=models.CASCADE, null=True)
    exhibit_3 = models.OneToOneField(Exhibit3, on_delete=models.CASCADE, null=True)
    exhibit_4 = models.OneToOneField(Exhibit4, on_delete=models.CASCADE, null=True)
    exhibit_5 = models.OneToOneField(Exhibit5, on_delete=models.CASCADE, null=True)
    exhibit_6 = models.OneToOneField(Exhibit6, on_delete=models.CASCADE, null=True)
    exhibit_7 = models.OneToOneField(Exhibit7, on_delete=models.CASCADE, null=True)
    exhibit_8 = models.OneToOneField(Exhibit8, on_delete=models.CASCADE, null=True)
    exhibit_9 = models.OneToOneField(Exhibit9, on_delete=models.CASCADE, null=True)
    exhibit_10 = models.OneToOneField(Exhibit10, on_delete=models.CASCADE, null=True)
    exhibit_11 = models.OneToOneField(Exhibit11, on_delete=models.CASCADE, null=True)
    exhibit_12 = models.OneToOneField(Exhibit12, on_delete=models.CASCADE, null=True)
    exhibit_13 = models.OneToOneField(Exhibit13, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'המסע של {self.student.first_name} {self.student.last_name}'
    
    def get_absolute_url(self):
        return reverse('journey-id', kwargs={'id' : self.id})
        
    class Meta:
        verbose_name = "מסע"
        verbose_name_plural = "מסעות"
        
@receiver(post_save, sender=Student)
def created_student(sender, instance, created, **kwargs):
    if created:
        Journey.objects.create(student=instance)

@receiver(post_save, sender=Student)
def saved_student(sender, instance, **kwargs):
    instance.journey.save()
    
@receiver(post_save, sender=Journey)
def created_journey(sender, instance, created, **kwargs):
    if created:
        instance.exhibit_0 = Exhibit0.objects.create()
        instance.exhibit_1 = Exhibit1.objects.create()
        instance.exhibit_2 = Exhibit2.objects.create()
        instance.exhibit_3 = Exhibit3.objects.create()
        instance.exhibit_4 = Exhibit4.objects.create()
        instance.exhibit_5 = Exhibit5.objects.create()
        instance.exhibit_6 = Exhibit6.objects.create()
        instance.exhibit_7 = Exhibit7.objects.create()
        instance.exhibit_8 = Exhibit8.objects.create()
        instance.exhibit_9 = Exhibit9.objects.create()
        instance.exhibit_10 = Exhibit10.objects.create()
        instance.exhibit_11 = Exhibit11.objects.create()
        instance.exhibit_12 = Exhibit12.objects.create()
        instance.exhibit_13 = Exhibit13.objects.create()
    
@receiver(post_delete, sender=Journey)
def deleted_journey(sender, instance, **kwargs):
    instance.exhibit_0.delete()
    instance.exhibit_1.delete()
    instance.exhibit_2.delete()
    instance.exhibit_3.delete()
    instance.exhibit_4.delete()
    instance.exhibit_5.delete()
    instance.exhibit_6.delete()
    instance.exhibit_7.delete()
    instance.exhibit_8.delete()
    instance.exhibit_9.delete()
    instance.exhibit_10.delete()
    instance.exhibit_11.delete()
    instance.exhibit_12.delete()
    instance.exhibit_13.delete()
    