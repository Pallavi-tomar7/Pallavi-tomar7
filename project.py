import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="contactapp"
)

mycursor = mydb.cursor()



    
print("=================================Contact App===============================================")
    
def printOptions():
        print("1. Sign up")
        print("2. Add contact")
        print("3. See your contacts")
        print("4. Update Contact")
        print("5. Delete")
        print("6. Exit")
        ch = int(input("Enter your choice: "))
        return ch
    
def signup():
    name = input("Enter Username:")    
    email= input("Enter Email:")
    password = input("Make strong Password:")
    sql = ("insert into user(name,email,password) values ( '{}', '{}','{}')".format(name,email,password))
    mycursor.execute(sql)
    mydb.commit()
    print("----------Signup successful----------")
    
def login():
        
     email= input("Enter Email:")
     password = input("Enter your Password:")
     mycursor.execute("SELECT * FROM user where email = '{}'and password = '{}'".format(email,password))   
     user = mycursor.fetchone() #((), ())
     #print(tech_all)
     if user:
        return user
        
     else:
        print("invalid value")
             
     
        
             
def createdetail():
        k = login()
        print("----------login successfull-----------")
        print("------Add your contact detail-------")
        Name = input("Enter your Name: ")
        firstnumber = int(input("Enter your first number:"))
        Secondnumber = int(input("Enter your second number:"))
        email = input("Enter your email: ")
        sql = ("insert into user_contact(Name,firstnumber,Secondnumber,email,u_id) values( '{}', '{}','{}','{}',{})").format(Name,firstnumber,Secondnumber,email,k[0])
        mycursor.execute(sql)
        mydb.commit()       
        print( "-----------contact added---------" )
             
def detaildelete():
      
    s = login()
    print("---------------login successfull---------------") 
    sql =  "DELETE FROM user_contact WHERE u_id ={}".format(s[0])
    mycursor.execute(sql)
    mydb.commit()
    print("--data deleted---")
    
def update():
       
        a = login()
        print("-------------login successfull--------------") 
        na =input("Enter new name:")
        sql = "UPDATE user_contact SET Name = '{}' WHERE u_id = {}".format(na,a[0] )
        
        mycursor.execute(sql)

        mydb.commit()

        print( "---------------contact updated---------------")

def search():
            
        m = login()
        print("----------------login successfull--------------") 
        mycursor.execute("SELECT * FROM user_contact where u_id = {}".format(m[0]))

        data = mycursor.fetchall()

        for i in data:
                print("Name:",i[1])
                print("firstnumber:",i[2])
                print("secondnumber:",i[3])
                print("Email:",i[4])
                print("-----------contact app--------------")
                
        

             




while True:
            choice = printOptions()
            if choice == 1:
                signup()
            elif choice == 2:
                createdetail()
            elif choice == 3:
                search()
            elif choice == 4:
                update()
            elif choice == 5:
                detaildelete()
            elif choice == 6:
               break    
    
    














        
        
