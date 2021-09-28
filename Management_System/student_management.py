from tkinter import *;
from tkinter import ttk;
from tkcalendar import DateEntry;
import pymysql;
class StudentManage:
    def __init__(self,root):
        self.root = root;
        self.root.title('Student Management');
        self.root.geometry("1360x700+0+0");


        self.id_var = StringVar();
        self.name_var = StringVar();
        self.contact_var = StringVar();
        self.email_var = StringVar();
        self.dob_var = StringVar();
        self.gender_var = StringVar();

        title = Label(self.root,text='Student Management System',font=('times new roman',30,'bold'),bg='grey',fg='blue',bd=10,relief=GROOVE);
        title.pack(side=TOP,fill=X);

        Frame1  =Frame(self.root,bd = 4,relief=RIDGE,bg='maroon');
        Frame1.place(x=20,y=100,width=450,height=570);

        Frame2  =Frame(self.root,bd = 4,relief=RIDGE,bg='maroon');
        Frame2.place(x=510,y=100,width=820,height=570);

        #title
        inner_title  = Label(Frame1,text='Student intorduction',font=('times new roman',20,'bold'),bg='maroon',fg='white');
        inner_title.grid(row=0,columnspan=2,pady=20);

        #labels
        name_label = Label(Frame1,text='Student Name',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        name_label.grid(row=1,column=0,pady=10,padx=10,sticky='w');

        enter_name = Entry(Frame1,font=('times new roman',15,'bold'),textvariable=self.name_var,bd = 5,relief=GROOVE);
        enter_name.grid(row=1,column=1,padx=35);

        
        id_label = Label(Frame1,text='Student ID',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        id_label.grid(row=2,column=0,pady=10,padx=10,sticky='w');

        enter_id = Entry(Frame1,font=('times new roman',15,'bold'),textvariable=self.id_var,bd = 5,relief=GROOVE);
        enter_id.grid(row=2,column=1,padx=35);

        email_label = Label(Frame1,text='Email Info',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        email_label.grid(row=3,column=0,pady=10,padx=10,sticky='w');

        enter_email = Entry(Frame1,font=('times new roman',15,'bold'),textvariable=self.email_var,bd = 5,relief=GROOVE);
        enter_email.grid(row=3,column=1,padx=35);

        dob_label = Label(Frame1,text='Birth Date',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        dob_label.grid(row=4,column=0,pady=10,padx=10,sticky='w');

        cal=DateEntry(Frame1,selectmode='day',font=('times new roman',15,'bold'),bd = 5,relief=GROOVE,sticky='w',width=19,textvariable=self.dob_var);
        cal.grid(row=4,column=1,padx=35);

        gender_label = Label(Frame1,text='Gender',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        gender_label.grid(row=5,column=0,pady=10,padx=10,sticky='w');

        combo_gender = ttk.Combobox(Frame1,font=('times new roman',10,'bold'),textvariable=self.gender_var,width=27);
        combo_gender['values']=('Male','Female','Other');
        combo_gender.grid(row=5,column=1);

        contact_label = Label(Frame1,text='Contact Info',font=('times new roman',15,'bold'),textvariable=self.contact_var,bg='maroon',fg='white');
        contact_label.grid(row=6,column=0,pady=10,padx=10,sticky='w');

        enter_contact = Entry(Frame1,font=('times new roman',15,'bold'),bd = 5,relief=GROOVE);
        enter_contact.grid(row=6,column=1,padx=35);


        address_label = Label(Frame1,text='Address',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        address_label.grid(row=7,column=0,pady=10,padx=10,sticky='w');
    
        self.enter_address = Text(Frame1,width=26,height=5);
        self.enter_address.grid(row=7,column=1,pady=10,padx=38,sticky='w');

        #buttons
        btnFrame = Label(Frame1,bd = 4,relief=RIDGE,bg='maroon');
        btnFrame.place(x=10,y =490,width=410);

        addBtn = Button(btnFrame,text='Add',width = 10,command=self.addStudent).grid(row=0,column=1,padx=10,pady=10);
        delBtn = Button(btnFrame,text='Delete',width = 10,command=self.deleteData()).grid(row=0,column=2,padx=10,pady=10);
        updateBtn = Button(btnFrame,text='Update',width = 10,command=self.update).grid(row=0,column=3,padx=10,pady=10);
        clrBtn = Button(btnFrame,text='Clear',width = 10,command=self.clear).grid(row=0,column=4,padx=10,pady=10);


        #search
        search_label = Label(Frame2,text='Search By',font=('times new roman',15,'bold'),bg='maroon',fg='white');
        search_label.grid(row=0,column=1,padx=30,pady=20);

        combo_search = ttk.Combobox(Frame2,font=('times new roman',10,'bold'),width=12);
        combo_search['values']=('ID','Name','Contact');
        combo_search.grid(row=0,column=2);

        enter_text = Entry(Frame2,font=('times new roman',12,'bold'),bd = 5,relief=GROOVE,width=17);
        enter_text.grid(row=0,column=3,padx=60,pady = 20);

        searchBtn = Button(Frame2,text='Search',width = 10).grid(row=0,column=4,padx=10,pady=10);
        showAllBtn = Button(Frame2,text='Show All',width = 10).grid(row=0,column=5,padx=10,pady=10);

        #Table
        tableFrame = Frame(Frame2,bd = 4,relief=RIDGE,bg='maroon');
        tableFrame.place(x=30,y=62,width=710,height=484); 

        scroll_X = Scrollbar(tableFrame,orient=HORIZONTAL);
        scroll_Y = Scrollbar(tableFrame,orient=VERTICAL);

        self.createTable = ttk.Treeview(tableFrame,columns=('Student ID','Name','Email','Date of Birth','Gender','Contact','Address'),xscrollcommand=scroll_X.set,yscrollcommand=scroll_Y.set);
        scroll_X.pack(side=BOTTOM,fill=X);
        scroll_Y.pack(side=RIGHT,fill=Y);

        scroll_X.config(command= self.createTable.xview);
        scroll_Y.config(command=self.createTable.yview);

        #heading
        self.createTable.heading('Student ID',text='Student ID');
        self.createTable.heading('Name',text='Name');
        self.createTable.heading('Email',text='Email');
        self.createTable.heading('Date of Birth',text='Date of Birth');
        self.createTable.heading('Gender',text='Gender');
        self.createTable.heading('Contact',text='Contact');
        self.createTable.heading('Address',text='Address');
        self.createTable['show'] ='headings';
        self.createTable.column('Student ID',width=100); 
        self.createTable.column('Name',width=100);
        self.createTable.column('Email',width=100);
        self.createTable.column('Date of Birth',width=100);
        self.createTable.column('Gender',width=100);
        self.createTable.column('Contact',width=100);
        self.createTable.column('Address',width=100);
        self.createTable.pack(fill=BOTH,expand=1);
        self.createTable.bind('<ButtonRelease-1>',self.focusedSelect);
        self.fetchData();

    def addStudent(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='student_manage');
        cursor = con.cursor();
        cursor.execute('insert into students values(%d,%s,%s,%s,%s,%s,%s)',(self.id_var.get(),
                                                                                  self.name_var.get(),
                                                                                  self.email_var.get(),
                                                                                  self.dob_var.get(),
                                                                                  self.contact_var.get(),
                                                                                  self.gender_var.get(),
                                                                                  self.enter_address.get('1.0',END)))
        con.commit();
        self.fetchData();
        self.clear();
        con.close();
    def fetchData(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='student_manage');
        cursor = con.cursor();
        cursor.execute('select * from students');
        rows = cursor.fetchall();
        if len(rows) !=0:
            self.createTable.delete(*self.createTable.get_children());
            for row in rows:
                self.createTable.insert('',END,values= row);
                con.commit();
        con.close();
    def clear(self):
        self.id_var.set('');
        self.name_var.set('');
        self.email_var.set('');
        self.contact_var('');
        self.gender_var('');
        self.dob_var.set('');
        self.enter_address.delete('1.0',END);
    
    def focusedSelect(self,event):
        cursored_row = self.createTable.focus();
        content = self.createTable.item(cursored_row);
        row = content['value'];

        self.id_var.set(row[0]);
        self.name_var.set(row[1]);
        self.email_var.set(row[2]);
        self.contact_var(row[4]);
        self.gender_var(row[5]);
        self.dob_var.set(row[3]);
        self.enter_address.delete('1.0',END);
        self.enter_address.insert(END,row[6]);
    
    def update(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='student_manage');
        cursor = con.cursor();
        cursor.execute('update students set name=%s,email=%s,dob=%s,contact=%s,gender=%s,address=%s where id_no=%s',(
                                                                                  self.name_var.get(),
                                                                                  self.email_var.get(),
                                                                                  self.dob_var.get(),
                                                                                  self.contact_var.get(),
                                                                                  self.gender_var.get(),
                                                                                  self.enter_address.get('1.0',END),
                                                                                  self.id_var.get()))
        con.commit();
        self.fetchData();
        self.clear();
        con.close();
    def deleteData(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='student_manage');
        cursor = con.cursor();
        cursor.execute('delete from students where id_no=%s',(self.name_var.get()));
        con.commit();
        con.close();

        self.fetchData();
        self.clear();


root = Tk();

stObj = StudentManage(root);
root.mainloop();