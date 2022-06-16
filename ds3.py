class Boss:
    def __init__(self, name, weapon, height, territory, element, fly, armor, alone, hand, puzzle, mask):
        self.point = 0
        self.name = name
        self.weapon = weapon
        self.height = height
        self.territory = territory
        self.element = element
        self.fly = fly
        self.armor = armor
        self.alone = alone
        self.hand = hand
        self.puzzle = puzzle
        self.mask = mask
        


class Question:
    def __init__(self, qnum, question, choice1, choice2, choice3, choice4):
        self.qnum = qnum
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        print(question)
        print('A) ' + choice1)
        print('B) ' + choice2)
        print('C) ' + choice3)
        print('D) ' + choice4)
        self.answer = input()
        if self.answer == 'A':
            self.answer = choice1
        if self.answer == 'B':
            self.answer = choice2
        if self.answer == 'C':
            self.answer = choice3
        if self.answer == 'D':
            self.answer = choice4








boss1 = Boss('Iudex Gundyr', 'Kesmeli', 'Büyük', 'Arena', 'Hiçbirine', 'Havalanmak', 'Ağır', 'Yalnız', 'Tek', 'Olmasın', 'İsterdim')
boss2 = Boss('Vordt of the Boreal Valley', 'Ezmeli', 'Büyük', 'Hiçbiri', 'Buz', 'Uçamamak', 'Ağır', 'Yalnız', 'Tek', 'Olmasın', 'İsterdim')
boss3 = Boss('Dancer of the Boreal Valley', 'Kesmeli', 'Büyük', 'Kilise', 'Ateş', 'Uçamamak', 'Ağır', 'Yalnız', 'Çift', 'Olmasın', 'İsterdim')
boss4 = Boss('Curse rotted Greatwood', 'Hiçbirini', 'Devasa', 'Bahçe,avlu', 'Hiçbirine', 'Uçamamak', 'Zırhsız', 'Grup', 'Boş', 'Olsun', 'Ne yüzü ?')
boss5 = Boss('Crystal Sage', 'Büyülü', 'Normal', 'Bahçe,avlu', 'Kara büyü', 'Uçmak', 'Zırhsız', 'Grup', 'Çift', 'Olmasın', 'İstemezdim')
boss6 = Boss('Abbys Watchers', 'Kesmeli', 'Normal', 'Arena', 'Ateş', 'Havalanmak', 'Hafif', 'Grup', 'Çift', 'Olmasın', 'İsterdim')
boss7 = Boss('High Lord Wolnir', 'Kesmeli', 'Devasa', 'Hiçbiri', 'Kara büyü', 'Uçamamak', 'Zırhsız', 'Grup', 'Tek', 'Olsun', 'İstemezdim')
boss8 = Boss('Old Demon King', 'Ezmeli', 'Büyük', 'Hiçbiri', 'Ateş', 'Uçamamak', 'Zırhsız', 'Yalnız', 'Çift', 'Olmasın', 'İstemezdim')
boss9 = Boss('Pontiff Sulyvahn', 'Kesmeli', 'Normal', 'Kilise', 'Ateş', 'Havalanmak', 'Hafif', 'Grup', 'Çift', 'Olmasın', 'İsterdim')
boss10 = Boss('Yhorm the Giant', 'Kesmeli', 'Devasa', 'Hiçbiri', 'Ateş', 'Uçamamak', 'Ağır', 'Yalnız', 'Tek', 'Olsun', 'İstemezdim')
boss11 = Boss('Deacons of the Deep', 'Büyülü', 'Normal', 'Kilise', 'Kara büyü', 'Uçamamak', 'Zırhsız', 'Grup', 'Çift', 'Olmasın', 'İstemezdim')
boss12 = Boss('Nameless King', 'Kesmeli', 'Normal', 'Hiçbiri', 'Hiçbirine', 'Havalanmak', 'Hafif', 'Yalnız', 'Tek', 'Olmasın', 'İstemezdim')
boss13 = Boss('Dragonslayer Armour', 'Kesmeli', 'Normal', 'Bahçe,avlu', 'Hiçbirine', 'Uçamamak', 'Ağır', 'Yalnız', 'Çift', 'Olmasın', 'İsterdim')
boss14 = Boss('Aldrich,Devourer of the Gods', 'Büyülü', 'Büyük', 'Hiçbiri', 'Kara büyü', 'Uçamamak', 'Zırhsız', 'Yalnız', 'Çift', 'Olmasın', 'İstemezdim')
boss15 = Boss('Oceiros,the Consumed King', 'Ezmeli', 'Büyük', 'Bahçe,avlu', 'Buz', 'Uçmak', 'Zırhsız', 'Yalnız', 'Tek', 'Olmasın', 'İstemezdim')
boss16 = Boss('Lothric and Lorian', 'Kesmeli', 'Büyük', 'Kilise', 'Ateş', 'Uçamamak', 'Hafif', 'Grup', 'Tek', 'Olmasın', 'İstemezdim')
boss17 = Boss('Ancient Wyvern', 'Hiçbirini', 'Devasa', 'Hiçbiri', 'Ateş', 'Uçmak', 'Zırhsız', 'Yalnız', 'Boş', 'Olsun', 'İstemezdim')
boss18 = Boss('Soul of Cinder', 'Kesmeli', 'Normal', 'Hiçbiri', 'Ateş', 'Havalanmak', 'Ağır', 'Yalnız', 'Tek', 'Olmasın', 'İsterdim')
boss19 = Boss('Sister Friede', 'Kesmeli', 'Normal', 'Kilise', 'Buz', 'Havalanmak', 'Zırhsız', 'Yalnız', 'Tek', 'Olmasın', 'İstemezdim')
boss20 = Boss('Champions Gravetender', 'Kesmeli', 'Normal', 'Bahçe,avlu', 'Buz', 'Uçamamak', 'Hafif', 'Grup', 'Çift', 'Olmasın', 'İsterdim')
boss21 = Boss('Demon Prince', 'Hiçbirini', 'Büyük', 'Hiçbiri', 'Ateş', 'Uçmak', 'Zırhsız', 'Yalnız', 'Boş', 'Olmasın', 'İstemezdim')
boss22 = Boss('Darkeater Midir', 'Hiçbirini', 'Devasa', 'Hiçbiri', 'Ateş', 'Uçmak', 'Zırhsız', 'Yalnız', 'Boş', 'Olmasın', 'İstemezdim')
boss23 = Boss('Halflight,Spear of the Church', 'Kesmeli', 'Normal', 'Kilise', 'Kara büyü', 'Uçamamak', 'Zırhsız', 'Grup', 'Çift', 'Olmasın', 'İstemezdim')
boss24 = Boss('Slave Knight Gael', 'Kesmeli', 'Normal', 'Hiçbiri', 'Hiçbirine', 'Havalanmak', 'Ağır', 'Yalnız', 'Tek', 'Olmasın', 'İsterdim')

bossList = [boss1, boss2, boss3, boss4, boss5, boss6, boss7, boss8, boss9, boss10, boss11, boss12, boss13, boss14, boss15, boss16, boss17, boss18, boss19, boss20, boss21, boss22, boss23, boss24]

def compare(ans, qnum):
    for i in bossList:
        if qnum == 1:
            if i.weapon == ans:
                i.point += 1
        if qnum == 2:
            if i.height == ans:
                i.point += 1
        if qnum == 3:
            if i.territory == ans:
                i.point += 1
        if qnum == 4:
            if i.element == ans:
                i.point += 1
        if qnum == 5:
            if i.fly == ans:
                i.point += 1
        if qnum == 6:
            if i.armor == ans:
                i.point += 1
        if qnum == 7:
            if i.alone == ans:
                i.point += 1
        if qnum == 8:
            if i.hand == ans:
                i.point += 1
        if qnum == 9:
            if i.puzzle == ans:
                i.point += 1
        if qnum == 10:
            if i.mask == ans:
                i.point += 1





q1 = Question(1, "Ne tür silah kullanmayı tercih ederdin ?", 'Kesmeli', 'Büyülü', 'Ezmeli', 'Hiçbirini')
q2 = Question(2, "Kavgaya girecek olsan hangi boyutlarda olmayı seçerdin ?", 'Normal', 'Büyük', 'Devasa', '-')
q3 = Question(3, "Neresi sana cazip geldi ?", 'Arena', 'Kilise', 'Bahçe,avlu', 'Hiçbiri')
q4 = Question(4, "Hükmetsen hangi büyü çeşidine hükmederdin ?", 'Buz', 'Ateş', 'Kara büyü', 'Hiçbirine')
q5 = Question(5, "Savaşırken havada olmak mı,yükselebilmek mi yoksa karada sağlamca durmak mı daha mantıklı ?", 'Uçmak', 'Havalanmak', 'Uçamamak', '-')
q6 = Question(6, "Ne tarz zırhla savaşmak isterdin,dayanıklı mı çevik mi ?", 'Ağır', 'Hafif', 'Zırhsız', '-')
q7 = Question(7, "Tek başına mı savaşmak isterdin grup halinde mi ?", 'Yalnız', 'Grup', '-', '-')
q8 = Question(8, "Savaşırken ellerini kullanma durumun ne olurdu ?", 'Tek', 'Çift', 'Boş', '-')
q9 = Question(9, "Hangisini seçerdin,zayıf bir noktan olmadan ama biraz daha güçsüz olmayı mı yoksa daha sağlam olup zayıf bir noktanın olmasını mı ?", 'Olsun', 'Olmasın', '-', '-')
q10 = Question(10, "Bütün yüzünü maske vb. ile saklamayı ister miydin ?", 'İsterdim', 'İstemezdim', 'Ne yüzü ?', '-')

questionList = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]


for i in questionList:
    compare(i.answer, i.qnum)

max = 0
maxboss = None
for i in bossList:
    if i.point > max:
        max = i.point
        maxboss = i

print(maxboss.name)
