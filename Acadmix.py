import random

class Course:
    '''
    Represents a course with a course ID, name, and credits.

    Example:
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def __str__(self):
        return "{}({}): {}".format(self.cid, self.credits, self.cname)

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.cid == other.cid
        else:
            return False

class Catalog:
    ''' 
    Represents a catalog of courses.

    Example:
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        if cid not in self.courseOfferings:
            cnm = Course(cid, cname, credits)
            self.courseOfferings[cid] = cnm
            return "Course added successfully"
        else:
            return "Course already added"
        
    def removeCourse(self, cid):
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        else:
            return "Course not found"
        
    def _loadCatalog(self, file):
        with open(file, 'r') as f: 
            course_info = f.read()  
        
        spl1 = course_info.split('\n')  
        for spl2 in spl1:                       
            data = spl2.split(',')              
            if len(data) == 3:                  
                cid, cname, credits = data     
                self.addCourse(cid, cname, credits) 

class Semester:
    '''
    Represents a semester with courses.

    Example:
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        self.courses = {}

    def __str__(self):          
        if not self.courses:    
            return "No courses"
        else:
            return '; '.join(map(str, self.courses.keys())) 
 
    __repr__ = __str__

    def addCourse(self, course):
        if course.cid not in self.courses:              
            self.courses[course.cid] = course     
        else:
            return "Course already added"
        
    def dropCourse(self, course):                   
        if course.cid in self.courses:
            del self.courses[course.cid]
        else:
            return "No such course"
        

    @property
    def totalCredits(self):
        ctotal = 0
        for x in self.courses.values():         
            ctotal += int(x.credits)              
        return ctotal
    
    @property
    def isFullTime(self):
        return self.totalCredits >= 12

class Loan:
    '''
    Represents a loan with an amount and a unique loan ID.

    Example:
        >>> import random
        >>> random.seed(2)  
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    
    def __init__(self, amount):
        self.amount = amount
        self.loan_id = self.__getloanID 

    def __str__(self):
        return "Balance: ${}".format(self.amount)

    __repr__ = __str__


    @property
    def __getloanID(self):
        x = random.randint(10000,99999)    
        return x
        
class Person:
    '''
    Represents a person with a name and a social security number (SSN).

    Example:
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name = name          
        self.__ssn = ssn        

    def __str__(self):
        last = self.__ssn[7:]       
        return "Person({}, ***-**-{})".format(self.name, last)
    __repr__ = __str__

    def get_ssn(self):      
        return self.__ssn
        

    def __eq__(self, other):
        if isinstance(other, Person):
            x = other.get_ssn()
            if self.__ssn == x:     
                return True
            else:
                return False
        else:
            return False

class Staff(Person):
    '''
    Represents a staff member.

    Example:
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name, ssn)    
        self.__supervisor = supervisor    
        

    def __str__(self):
        return "Staff({}, {})".format(self.name,self.id)

    __repr__ = __str__


    @property
    def id(self):         
        y = self.get_ssn()[7:]  
        words = self.name.lower()
        words = words.split()
        initials = ""              
        for i in words:             
            initials += i[0]        
    
        return "905{}{}".format(initials, y)

    @property   
    def getSupervisor(self):            
        return self.__supervisor

    def setSupervisor(self, new_supervisor):    
        if isinstance(new_supervisor, Staff):
            self.__supervisor = new_supervisor

    def applyHold(self, student):
        if isinstance(student, Student):       
            student.hold = True                   
            return "Completed!"
        else:
            return None

    def removeHold(self, student):
        if isinstance(student, Student):
            student.hold = False              
            return "Completed!"
        else:
            return None

    def unenrollStudent(self, student):
        if isinstance(student, Student):
            student.active = False           
            return "Completed!"
        else:
            return None

    def createStudent(self, person):
        if isinstance(person, Person):      
            std = Student(person.name, person.get_ssn(), "Freshman")
            return std

