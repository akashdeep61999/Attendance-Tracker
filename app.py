import pandas as pd
import re,datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)



Java_Theory='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
Java_Lab_A="1Ik4guLKNHQz7ZC0LwTeCGl23G66vm9xWEwzhgcwrzJA"
Java_Lab_B="1--xishZY_sgONYzStNwhgkoFf3Pj7yn_CDAiDlJnhUg"
mst_java='Award_list_Java.xlsx'
sub_java='Submission_list_Java.xlsx'

@app.route("/")
def home():
    return render_template("startpage.html")

@app.route("/studentpanel")
def studentpanel():
    return render_template("First_page.html")

@app.route("/checksora", methods=['POST'])
def checksora():
    if request.method == 'POST':
        teacher = request.form['language']
        return render_template("teacher.html", teacher=teacher)
    else:
        return "Error: Invalid request method"

@app.route("/admin",methods=['POST'])
def admin():
    if request.method == 'POST':
        teacher = request.form['language']
        return render_template("admin.html",teacher=teacher)
    else:
        return render_template("loginerror.html")


@app.route('/adminpage')
def adminpage():
    return render_template('adminpage.html')

@app.route('/login', methods=['POST'])
def login():
    admin=1
    a=0
    if request.method == 'POST':
        teacher = request.form['language']
        if teacher == "Shivamsir":
            username = request.form['username']
            password = request.form['password']
            # Check if username and password are correct
            if username == '11111' and password == '11111':
                return render_template("subject.html",teacher=teacher,admin=admin)
            else:
                return render_template("founderror.html",a=a)
        else:
            username = request.form['username']
            password = request.form['password']
            # Check if username and password are correct
            if username == '22222' and password == '22222':
                return render_template("subject.html",teacher=teacher)
            else:
             return render_template("founderror.html")
    else:
        return render_template("loginerror.html",a=a)

@app.route('/adminsub',methods=['POST'])
def adminsub():
    if request.method == 'POST':
        subject = request.form['language']
    return render_template('adminpage.html',subject=subject)

# @app.route("/checkteacher")
# def checkteacher():
#     if request.method == 'POST':
#         teacher = request.form['language']
#         return render_template("teacher.html",teacher=teacher)

@app.route("/checksub",methods=['POST'])
def checksub():
    admin=0
    if request.method == 'POST':
        teacher = request.form['language']
    return render_template("subject.html",teacher=teacher,admin=admin)



@app.route('/subject', methods=['POST'])
def subject():
    if request.method == 'POST':
        subject = request.form['language']
        return render_template('first_page.html', subject=subject)

@app.route('/attbydate',methods=['POST'])
def attbydate():
    if request.method == 'POST':
        date = request.form['date']
        gsheetid=request.form['gsheetid']
        sheet_name = "Data"
        gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
        df = pd.read_csv(gsheet_url)
        df = df.drop(['Timestamp'], axis=1)

        def clean_column(col):
            col = re.sub(r'[^\w\s]+', ' ', col)
            col = re.sub(r'\s+', ' ', col)
            col = col.strip()
            return col
        for col in df.columns:
            df.rename(columns={col: clean_column(col)}, inplace=True)
        

        filtered_df = df[df['Date'] == date]

        # Save the columns of the matching rows to a single list
        lis = filtered_df.values.flatten().tolist()

        roll_no = df.columns.tolist()



        recent_Att = [(roll_no, value) for roll_no, value in zip(roll_no, lis)]
        p_count = 0
        a_count = 0
        try:
            for key, value in recent_Att[1:]:
               p_count += value.count('P')
               a_count += value.count('A')
            Total = p_count + a_count
            Sr_no = [i + 1 for i in range(len(recent_Att)-1)]
            
            return render_template("attbydate.html",recent_Att=recent_Att,Sr_no=Sr_no,p_count=p_count, a_count=a_count, Total=Total)

        except Exception as e:
            return f"Java Theory Register Error"
        
    else:
        return render_template('Register.html')
        
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        submit_value = request.form['submit']
        if submit_value == 'Java_Theory':
            gsheetid = Java_Theory
        elif submit_value == 'Java_Lab_A':
            gsheetid = Java_Lab_A
        elif submit_value == 'Java_Lab_B':
            gsheetid = Java_Lab_B

        elif submit_value == 'Python_Theory':
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        elif submit_value == 'Python_Lab_A':
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        elif submit_value=="Python_Lab_B":
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

        elif submit_value == 'CC_Theory':
            gsheetid = Java_Theory
        elif submit_value == 'CC_Lab_A':
            gsheetid = Java_Lab_A
        elif submit_value == 'CC_Lab_B':
            gsheetid = Java_Lab_B

        elif submit_value == 'DBMS_Theory':
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        elif submit_value == 'DBMS_Lab_A':
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        elif submit_value == 'SCAshivamsir':
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        elif submit_value == 'SCAakashsir':
            gsheetid = '1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
        else:
            gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

        sheet_name = "Data"
        gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
        df = pd.read_csv(gsheet_url)
        df = df.drop(['Timestamp'], axis=1)
        try:
            def clean_column(col):
                col = re.sub(r'[^\w\s]+', ' ', col)
                col = re.sub(r'\s+', ' ', col)
                col = col.strip()
                return col

            for col in df.columns:
                df.rename(columns={col: clean_column(col)}, inplace=True)

            counts = []
            # loop through each column (except the first) and count the number of 'P's
            for col in df.columns[1:]:
                counts.append((df[col] == 'P').sum())

            lis = ['Total Presents']
            Sum_of_P = lis + counts
            df.loc[len(df)] = Sum_of_P
            table_html = df.to_html(index=False)
            a = "Theory"
            return render_template('Register.html', table=table_html, a=a)
        except Exception as e:
            return f"Java Theory Register Error"
    else:
        return render_template('Register.html')

@app.route("/sessional",methods=['POST'])
def sessional():
    if request.method == 'POST':
        submit_value = request.form['submit']
        Best_one=request.form['username']

        if submit_value == 'Java':
            gsheetid = Java_Theory
            gsheetid1=Java_Lab_A
            gsheetid2=Java_Lab_B
            mst_df = pd.read_excel(mst_java)
            sub_df=pd.read_excel(sub_java)
        elif submit_value == 'Python':
            gsheetid = Java_Theory
            gsheetid1=Java_Lab_A
            gsheetid2=Java_Lab_B
            mst_df = pd.read_excel(mst_java)
            sub_df=pd.read_excel(sub_java)
        elif submit_value == 'DBMS':
            gsheetid =  Java_Theory
            gsheetid1=Java_Lab_A
            gsheetid2=Java_Lab_B
            sub_df=pd.read_excel(sub_java)
            mst_df = pd.read_excel(mst_java)
        elif submit_value == 'Cloud Computing':
            gsheetid = Java_Theory
            mst_df = pd.read_excel(mst_java)
            gsheetid1=Java_Lab_A
            gsheetid2=Java_Lab_B
            sub_df=pd.read_excel(sub_java)

        sheet_name = "Data"
        gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
        df = pd.read_csv(gsheet_url)

        sheet_name1 = "Data"
        gsheet_url1 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid1, sheet_name1)
        df1 = pd.read_csv(gsheet_url1)
        counts = []
        for col in df1.columns[2:]:
            counts.append((df1[col] == 'P').sum())
        Total_lec=len(df1['Date'])
        counts = [int((value / Total_lec) * 100) for value in counts]
        attendanceLabA = []
        for count in counts:
            if count >= 80:
                attendanceLabA.append(4.5)
            elif count >= 70:
                attendanceLabA.append(4.0)
            elif count >= 60:
                attendanceLabA.append(3.5)
            elif count >= 50:
                attendanceLabA.append(3.0)
            else:
                attendanceLabA.append(2.5)
        attPercLabA=counts

        sheet_name2 = "Data"
        gsheet_url2 = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid2, sheet_name2)
        df2 = pd.read_csv(gsheet_url2)
        counts = []
        for col in df2.columns[2:]:
            counts.append((df2[col] == 'P').sum())
        Total_lec=len(df2['Date'])
        counts = [int((value / Total_lec) * 100) for value in counts]
        attendanceLabB = []
        for count in counts:
            if count >= 80:
                attendanceLabB.append(4.5)
            elif count >= 70:
                attendanceLabB.append(4.0)
            elif count >= 60:
                attendanceLabB.append(3.5)
            elif count >= 50:
                attendanceLabB.append(3.0)
            else:
                attendanceLabB.append(2.5)
        attPercLabB=counts
        attendanceLab=attendanceLabA+attendanceLabB
        attPercLab=attPercLabA+attPercLabB
        


        df = df.drop(['Timestamp'], axis=1)
        def clean_column(col):
            col = re.sub(r'[^\w\s]+', ' ', col)
            col = re.sub(r'\s+', ' ', col)
            col = col.strip()
            return col
        for col in df.columns:
            df.rename(columns={col: clean_column(col)}, inplace=True)
        counts = []
        for col in df.columns[1:]:
            counts.append((df[col] == 'P').sum())
        Total_lec=len(df['Date'])
        counts = [int((value / Total_lec) * 100) for value in counts]
        attendanceTh = []
        for count in counts:
            if count >= 80:
                attendanceTh.append(4.5)
            elif count >= 70:
                attendanceTh.append(4.0)
            elif count >= 60:
                attendanceTh.append(3.5)
            elif count >= 50:
                attendanceTh.append(3.0)
            else:
                attendanceTh.append(2.5)
        attendancePerTh=counts

        Roll_no=[]
        mst1=[]
        mst2=[]
        mst3=[]

        n=len(mst_df['Roll no'])
        for i in range(n):
            Roll_no.append(mst_df['Roll no'][i])
            mst1.append(mst_df['MST1'][i])
            mst2.append(mst_df['MST2'][i])
            mst3.append(mst_df['MST3'][i])


        n=len(sub_df)
        sub_marks=[]
        for i in range(n):
            sub_marks.append(sub_df['SUB1'][i]+sub_df['SUB2'][i]+sub_df['SUB3'][i])
   


        value_list = [int(value) for value in Best_one.split(',')]
        Best_one=[]
        for i in range(n):
            if i<len(value_list) and value_list[i]!='':
             Best_one.append(value_list[i])
            else:
                Best_one.append(0)

        marks=[]
        for i in range (n):
            if mst_df['Roll no'][i] in value_list:
                if mst_df['MST1'][i]=='AB' and mst_df['MST2'][i]=='AB' and mst_df['MST3'][i]=='AB':
                  marks.append(0)
                elif mst_df['MST1'][i]=='AB' and mst_df['MST2'][i]=='AB':
                    marks.append(mst_df['MST3'][i]*2)
                elif mst_df['MST2'][i]=='AB' and mst_df['MST3'][i]=='AB':
                    marks.append(mst_df['MST1'][i]*2)
                elif mst_df['MST3'][i]=='AB' and mst_df['MST1'][i]=='AB':
                    marks.append(mst_df['MST2'][i]*2)
                elif mst_df['MST1'][i]=='AB':
                    if mst_df['MST2'][i]>mst_df['MST3'][i]:
                        marks.append(mst_df['MST2'][i]*2)
                    else:
                        marks.append(mst_df['MST3'][i]*2)
                elif mst_df['MST2'][i]=='AB':
                    if mst_df['MST1'][i]>mst_df['MST3'][i]:
                        marks.append(mst_df['MST1'][i]*2)
                    else:
                        marks.append(mst_df['MST3'][i]*2)
                elif mst_df['MST3'][i]=='AB':
                    if mst_df['MST2'][i]>mst_df['MST1'][i]:
                        marks.append(mst_df['MST2'][i]*2)
                    else:
                        marks.append(mst_df['MST1'][i]*2)
                elif mst_df['MST1'][i]>=mst_df['MST2'][i] and mst_df['MST1'][i]>=mst_df['MST3'][i]:
                        marks.append(mst_df['MST1'][i]*2)
                elif mst_df['MST2'][i]>=mst_df['MST3'][i] and mst_df['MST2'][i]>=mst_df['MST1'][i]:
                        marks.append(mst_df['MST2'][i]*2)
                else:
                    marks.append(mst_df['MST3'][i]*2)
            
            
            else:
                if mst_df['MST1'][i]=='AB' and mst_df['MST2'][i]=='AB' and mst_df['MST3'][i]=='AB':
                    marks.append(0)
                elif mst_df['MST1'][i]=='AB' and mst_df['MST2'][i]=='AB':
                    marks.append(mst_df['MST3'][i])
                elif mst_df['MST2'][i]=='AB' and mst_df['MST3'][i]=='AB':
                    marks.append(mst_df['MST1'][i])
                elif mst_df['MST3'][i]=='AB' and mst_df['MST1'][i]=='AB':
                    marks.append(mst_df['MST2'][i])
                elif mst_df['MST1'][i]=='AB':
                        marks.append(mst_df['MST2'][i]+mst_df['MST3'][i])
                elif mst_df['MST2'][i]=='AB':
                        marks.append(mst_df['MST1'][i]+mst_df['MST3'][i])
                elif mst_df['MST3'][i]=='AB':
                        marks.append(mst_df['MST1'][i]+mst_df['MST2'][i])
                
                elif mst_df['MST1'][i]<=mst_df['MST2'][i] and mst_df['MST1'][i]<=mst_df['MST3'][i]:
                        marks.append(mst_df['MST2'][i]+mst_df['MST3'][i])
                elif mst_df['MST2'][i]<=mst_df['MST1'][i] and mst_df['MST2'][i]<=mst_df['MST3'][i]:
                        marks.append(mst_df['MST1'][i]+mst_df['MST3'][i])
                else:
                    marks.append(mst_df['MST1'][i]+mst_df['MST2'][i])

        for i in range(len(marks)):
            marksfifteenpercent = [round(mark * 0.15, 1) for mark in marks]

        marksroundoff = []
        for i in range(n):
            decimal_part = round(marksfifteenpercent[i] - int(marksfifteenpercent[i]), 1)
            if decimal_part <= 0.2 or decimal_part == 0:
                marksroundoff.append(int(marksfifteenpercent[i]))
            elif decimal_part <= 0.7 and decimal_part >= 0.3:
                marksroundoff.append(int(marksfifteenpercent[i]) + 0.5)
            else:
                marksroundoff.append(int(marksfifteenpercent[i]) + 1)

        submission_marks=[]
        for i in range(n):
            if sub_marks[i]>=25:
                submission_marks.append(4.5)
            elif sub_marks[i]>=20:
                submission_marks.append(4.0)
            elif sub_marks[i]>=15:
                submission_marks.append(3.5)
            elif sub_marks[i]>0:
                submission_marks.append(2.5)
            else:
                submission_marks.append(0)

        data = {
    'Roll_no': Roll_no,
    'mst1': mst1,
    'mst2': mst2,
    'mst3': mst3,
    'marks':marks,
    'marksfifteenpercent': marksfifteenpercent,
    'marksroundoff': marksroundoff,
    'Submission_marks':submission_marks,
    'attendanceTh': attendanceTh,
    'attendanceLab':attendanceLab,
    'Best one':Best_one,
    'attPercLab':attPercLab,
    'attendancePerTh':attendancePerTh
                }
        df3 = pd.DataFrame(data)
        return render_template('sessional.html',dataframe=df3,submit_value =submit_value )
# @app.route("/labaregister")
# def labaregister():
#     gsheetid = Java_Lab_A
#     sheet_name = "Data"
#     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
#     df = pd.read_csv(gsheet_url)
#     df=df.drop(['Timestamp'], axis=1)
#     try:
#         def clean_column(col):
#             col = re.sub(r'[^\w\s]+', ' ', col)
#             col = re.sub(r'\s+', ' ', col)
#             col = col.strip()
#             return col
#         for col in df.columns:
#             df.rename(columns={col:clean_column(col)}, inplace=True)
#         counts = []
#         # loop through each column (except the first) and count the number of 'P's
#         for col in df.columns[1:]:
#             counts.append((df[col] == 'P').sum())
#         lis=['Total Presents']
#         Sum_of_P=lis+counts
#         df.loc[len(df)] = Sum_of_P
#         table_html = df.to_html(index=False)
#         a="Lab A"
#         return render_template('Register.html', table=table_html,a=a)
#     except Exception as e:
#         return f"Java Lab A Register Error"

# @app.route("/labbregister")
# def labbregister():
#     gsheetid = Java_Lab_B
#     sheet_name = "Data"
#     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
#     df = pd.read_csv(gsheet_url)
#     df=df.drop(['Timestamp'], axis=1)
#     try:
#         def clean_column(col):
#             col = re.sub(r'[^\w\s]+', ' ', col)
#             col = re.sub(r'\s+', ' ', col)
#             col = col.strip()
#             return col
#         for col in df.columns:
#             df.rename(columns={col:clean_column(col)}, inplace=True)
#         counts = []
#         # loop through each column (except the first) and count the number of 'P's
#         for col in df.columns[1:]:
#             counts.append((df[col] == 'P').sum())
#         lis=['Total Presents']
#         Sum_of_P=lis+counts
#         df.loc[len(df)] = Sum_of_P
#         table_html = df.to_html(index=False)
#         a="lab B"
#         return render_template('Register.html', table=table_html,a=a)
#     except Exception as e:
#         return f"Java Lab B Register Error"

@app.route("/recentatt",methods=['POST'])
def recentatt():
    submit_value = request.form['submit']
    if submit_value == 'Java_Theory':
        gsheetid = Java_Theory
    elif submit_value == 'Java_Lab_A':
        gsheetid = Java_Lab_A
    elif submit_value == 'Java_Lab_B':
        gsheetid = Java_Lab_B

    elif submit_value == 'Python_Theory':
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'Python_Lab_A':
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value=="Python_Lab_B":
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

    elif submit_value == 'CC_Theory':
        gsheetid = Java_Theory
    elif submit_value == 'CC_Lab_A':
        gsheetid = Java_Lab_A
    elif submit_value == 'CC_Lab_B':
        gsheetid = Java_Lab_B

    elif submit_value == 'DBMS_Theory':
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'DBMS_Lab_A':
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'DBMS_Lab_B':
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    
    elif submit_value == 'SCAshivamsir':
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'SCAakashsir':
        gsheetid = '1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'

    else:
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

    sheet_name = "Data"
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    df = pd.read_csv(gsheet_url)
    df = df.drop(['Timestamp'], axis=1)

    date_list = df['Date'].tolist() # List of Dates

    def clean_column(col):
        col = re.sub(r'[^\w\s]+', ' ', col)
        col = re.sub(r'\s+', ' ', col)
        col = col.strip()
        return col

    try:
        for col in df.columns:
            df.rename(columns={col: clean_column(col)}, inplace=True)
        columns_recent_Att = list(df.columns)
        last_row = list(df.iloc[-1])
        recent_Att = [(columns_recent_Att, value) for columns_recent_Att, value in zip(columns_recent_Att, last_row)]
        p_count = 0
        a_count = 0
        for key, value in recent_Att[1:]:
            p_count += value.count('P')
            a_count += value.count('A')
        Total = p_count + a_count
        Sr_no = [i + 1 for i in range(len(recent_Att) - 1)]
        return render_template('recentatt.html', gsheetid=gsheetid,recent_Att=recent_Att,date_list=date_list, submit_value=submit_value, p_count=p_count, a_count=a_count, Total=Total, Sr_no=Sr_no)
    except Exception as e:
        return "Recent att Error: " + str(e)



# @app.route("/recentatta",methods=['POST'])
# def recentatta():
#     submit_value = request.form['submit']
#     if submit_value == 'Java_Lab_A':
#         gsheetid = Java_Lab_A
#     sheet_name = "Data"
#     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
#     df = pd.read_csv(gsheet_url)
#     df=df.drop(['Timestamp'], axis=1)
#     def clean_column(col):
#         col = re.sub(r'[^\w\s]+', ' ', col)
#         col = re.sub(r'\s+', ' ', col)
#         col = col.strip()
#         return col

#     try:
#         a=1
#         for col in df.columns:
#             df.rename(columns={col:clean_column(col)}, inplace=True)
#         columns_recent_Att = list(df.columns)
#         last_row = list(df.iloc[-1])
#         recent_Att = [(columns_recent_Att, value) for columns_recent_Att, value in zip(columns_recent_Att, last_row)]
#         p_count = 0
#         a_count = 0
#         for key, value in recent_Att[1:]:
#             p_count += value.count('P')
#             a_count += value.count('A')
#         Total=p_count+a_count
#         Sr_no = [i+1 for i in range(len(recent_Att)-1)]
#         return render_template('recentatt.html', recent_Att=recent_Att,a=a,p_count=p_count,a_count=a_count,Total=Total,Sr_no=Sr_no)

#     except Exception as e:
#         return f"Recent att at b Error"

# @app.route("/recentattb",methods=['POST'])
# def recentattb():
#     submit_value = request.form['submit']
#     if submit_value == 'Java_Lab_B':
#         gsheetid = Java_Lab_B
#     sheet_name = "Data"
#     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
#     df = pd.read_csv(gsheet_url)
#     df=df.drop(['Timestamp'], axis=1)
#     def clean_column(col):
#         col = re.sub(r'[^\w\s]+', ' ', col)
#         col = re.sub(r'\s+', ' ', col)
#         col = col.strip()
#         return col

#     try:
#         a=2
#         for col in df.columns:
#             df.rename(columns={col:clean_column(col)}, inplace=True)
#         columns_recent_Att = list(df.columns)
#         last_row = list(df.iloc[-1])
#         recent_Att = [(columns_recent_Att, value) for columns_recent_Att, value in zip(columns_recent_Att, last_row)]
#         p_count = 0
#         a_count = 0
#         for key, value in recent_Att[1:]:
#             p_count += value.count('P')
#             a_count += value.count('A')
#         Total=p_count+a_count
#         Sr_no = [i+1 for i in range(len(recent_Att)-1)]
#         return render_template('recentatt.html', recent_Att=recent_Att,a=a,p_count=p_count,a_count=a_count,Total=Total,Sr_no=Sr_no)

#     except Exception as e:
#         return f"Recent att at a Error"

@app.route("/search", methods=["POST"])
def search():
    a=1
    submit_value = request.form['submit']
    if submit_value == 'Java_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Theory
    elif submit_value == 'Java_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Lab_A
    elif submit_value == 'Java_Lab_B':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Lab_B

    elif submit_value == 'Python_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'Python_Lab_A':
        mst_df = pd.read_excel(mst_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value=="Python_Lab_B":
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

    elif submit_value == 'CC_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Theory
    elif submit_value == 'CC_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Lab_A
    elif submit_value == 'CC_Lab_B':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Lab_B

    elif submit_value == 'DBMS_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'DBMS_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    elif submit_value == 'DBMS_Lab_B':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

    elif submit_value == 'SCAakashsir':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
    elif submit_value == 'SCAshivamsir':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    else:
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)



    sheet_name = "Data"
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    df = pd.read_csv(gsheet_url)
    name1 = request.form['username']
        
    #for MST marks display
    
    lis = []

    for index, row in mst_df.iterrows():
        if name1!='':
            if row['Roll no'] == int(name1):
                lis.append(row.tolist())
                mst1=lis[0][1]
                mst2=lis[0][2]
                mst3=lis[0][3]

     #for Submission marks display
    
    lis1= []

    for index, row in sub_df.iterrows():
        if name1!='':
            if row['Roll no'] == int(name1):
                lis1.append(row.tolist())
                sub1=lis1[0][1]
                sub2=lis1[0][2]
                sub3=lis1[0][3]
        
    try:
        def clean_column(col):

            col = re.sub(r'[^\w\s]+', ' ', col)
            col = re.sub(r'\s+', ' ', col)
            col = col.strip()
            return col
        for col in df.columns:
            df.rename(columns={col:clean_column(col)}, inplace=True)

        if name1 in df.columns:
            att = df[name1]
            att = list(att)
            date = list(df["Date"])
            result = list(zip(date,att))

            result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
            sorted_list = sorted(result, key=lambda x: x[0])
            sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]

            counts = {'P': 0, 'A': 0}

            for _, value in sorted_list:
                counts[value] += 1

            p_count = counts['P']
            a_count = counts['A']
            n=len(sorted_list)
            generate_list = lambda n: list(range(1, n+1))
            return render_template('home.html',submit_value=submit_value, sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,lis=lis,mst1=mst1,mst2=mst2,mst3=mst3,sub1=sub1,sub2=sub2,sub3=sub3)
        else:
            return render_template('founderror.html',a=a)
    except Exception as e:
        return f"Java Theory Error"


    # elif submit_value=='Python_Theory':
    #     gsheetid ='1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

    #     gsheetid = Java_Theory
    #     sheet_name = "Data"
    #     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    #     df = pd.read_csv(gsheet_url)
    #     name1 = request.form['username']
        
    #     #for MST marks display
    #     mst_df = pd.read_excel(mst_java)
    #     lis = []

    #     for index, row in mst_df.iterrows():
    #         if name1!='':
    #             if row['Roll no'] == int(name1):
    #                 lis.append(row.tolist())
    #                 mst1=lis[0][1]
    #                 mst2=lis[0][2]
    #                 mst3=lis[0][3]

        
    #     try:
    #         def clean_column(col):

    #             col = re.sub(r'[^\w\s]+', ' ', col)
    #             col = re.sub(r'\s+', ' ', col)
    #             col = col.strip()
    #             return col
    #         for col in df.columns:
    #             df.rename(columns={col:clean_column(col)}, inplace=True)

    #         if name1 in df.columns:
    #             att = df[name1]
    #             att = list(att)
    #             date = list(df["Date"])
    #             result = list(zip(date,att))

    #             result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
    #             sorted_list = sorted(result, key=lambda x: x[0])
    #             sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]

    #             counts = {'P': 0, 'A': 0}

    #             for _, value in sorted_list:
    #                 counts[value] += 1

    #             p_count = counts['P']
    #             a_count = counts['A']
    #             n=len(sorted_list)
    #             generate_list = lambda n: list(range(1, n+1))
    #             return render_template('home.html', sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,lis=lis,mst1=mst1,mst2=mst2,mst3=mst3)
    #         else:
    #             return render_template('founderror.html')
    #     except Exception as e:
    #         return f"Java Theory Error"


    # elif submit_value == 'Java_Lab_A':
    #     gsheetid = Java_Lab_A
    #     sheet_name = "Data"
    #     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    #     df = pd.read_csv(gsheet_url)
    #     name1 = request.form['username']
        
    #     #for MST marks display
    #     mst_df = pd.read_excel(mst_java)
    #     lis = []
    #     for index, row in mst_df.iterrows():
    #         if name1!='':
    #             if row['Roll no'] == int(name1):
    #                 lis.append(row.tolist())
    #                 mst1=lis[0][1]
    #                 mst2=lis[0][2]
    #                 mst3=lis[0][3]
        
    #     try:
    #         def clean_column(col):

    #             col = re.sub(r'[^\w\s]+', ' ', col)
    #             col = re.sub(r'\s+', ' ', col)
    #             col = col.strip()
    #             return col
    #         for col in df.columns:
    #             df.rename(columns={col:clean_column(col)}, inplace=True)

    #         if name1 in df.columns:
    #             att = df[name1]
    #             att = list(att)
    #             date = list(df["Date"])
    #             result = list(zip(date,att))

    #             result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
    #             sorted_list = sorted(result, key=lambda x: x[0])
    #             sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]

    #             counts = {'P': 0, 'A': 0}

    #             for _, value in sorted_list:
    #                 counts[value] += 1

    #             p_count = counts['P']
    #             a_count = counts['A']
    #             n=len(sorted_list)
    #             generate_list = lambda n: list(range(1, n+1))
    #             return render_template('home.html', sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,lis=lis,mst1=mst1,mst2=mst2,mst3=mst3)
    #         else:
    #             return render_template('founderror.html')
    #     except Exception as e:
    #         return f"Java Theory Error"

    # elif submit_value=='Python_Lab_A':
    #     gsheetid ='1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    #     sheet_name = "Data"
    #     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    #     df = pd.read_csv(gsheet_url)
    #     name1 = request.form['username']
    #      #for MST marks display
    #     mst_df = pd.read_excel(mst_java)
    #     lis = []
    #     for index, row in mst_df.iterrows():
    #         if name1!='':
    #             if row['Roll no'] == int(name1):
    #                 lis.append(row.tolist())
    #                 mst1=lis[0][1]
    #                 mst2=lis[0][2]
    #                 mst3=lis[0][3]
    #     try:
    #         def clean_column(col):
    #             col = re.sub(r'[^\w\s]+', ' ', col)
    #             col = re.sub(r'\s+', ' ', col)
    #             col = col.strip()
    #             return col
    #         for col in df.columns:
    #             df.rename(columns={col:clean_column(col)}, inplace=True)

    #         if name1 in df.columns:
    #             att = df[name1]
    #             att = list(att)
    #             date = list(df["Date"])
    #             result = list(zip(date,att))
    #             result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
    #             sorted_list = sorted(result, key=lambda x: x[0])
    #             sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]
    #             counts = {'P': 0, 'A': 0}

    #             for _, value in sorted_list:
    #                 counts[value] += 1

    #             p_count = counts['P']
    #             a_count = counts['A']
    #             n=len(sorted_list)
    #             generate_list = lambda n: list(range(1, n+1))
    #             return render_template('home.html', sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,mst1=mst1,mst2=mst2,mst3=mst3)
    #         else:
    #             return render_template('founderror.html')
    #     except Exception as e:
    #         return f"Java Lab A Error"


    # elif submit_value == 'Java_Lab_B':
    #     gsheetid = Java_Lab_B
        
    #     sheet_name = "Data"
    #     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    #     df = pd.read_csv(gsheet_url)
    #     name1 = request.form['username']
    #      #for MST marks display
    #     mst_df = pd.read_excel(mst_java)
    #     lis = []
    #     for index, row in mst_df.iterrows():
    #         if name1!='':
    #             if row['Roll no'] == int(name1):
    #                 lis.append(row.tolist())
    #                 mst1=lis[0][1]
    #                 mst2=lis[0][2]
    #                 mst3=lis[0][3]
    #     try:
    #         def clean_column(col):
    #             col = re.sub(r'[^\w\s]+', ' ', col)
    #             col = re.sub(r'\s+', ' ', col)
    #             col = col.strip()
    #             return col
    #         for col in df.columns:
    #             df.rename(columns={col:clean_column(col)}, inplace=True)

    #         if name1 in df.columns:
    #             att = df[name1]
    #             att = list(att)
    #             date = list(df["Date"])
    #             result = list(zip(date,att))

    #             result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
    #             sorted_list = sorted(result, key=lambda x: x[0])
    #             sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]

    #             counts = {'P': 0, 'A': 0}

    #             for _, value in sorted_list:
    #                 counts[value] += 1

    #             p_count = counts['P']
    #             a_count = counts['A']
    #             n=len(sorted_list)
    #             generate_list = lambda n: list(range(1, n+1))
    #             return render_template('home.html', sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,mst1=mst1,mst2=mst2,mst3=mst3)
    #         else:
    #             return render_template('founderror.html')
    #     except Exception as e:
    #         return f"Java Lab B Error"


    # elif submit_value=='Python_Lab_B':
    #     gsheetid ='1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
    #     sheet_name = "Data"
    #     gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    #     df = pd.read_csv(gsheet_url)
    #     name1 = request.form['username']
    #      #for MST marks display
    #     mst_df = pd.read_excel(mst_java)
    #     lis = []
    #     for index, row in mst_df.iterrows():
    #         if name1!='':
    #             if row['Roll no'] == int(name1):
    #                 lis.append(row.tolist())
    #                 mst1=lis[0][1]
    #                 mst2=lis[0][2]
    #                 mst3=lis[0][3]
    #     try:
    #         def clean_column(col):
    #             col = re.sub(r'[^\w\s]+', ' ', col)
    #             col = re.sub(r'\s+', ' ', col)
    #             col = col.strip()
    #             return col
    #         for col in df.columns:
    #             df.rename(columns={col:clean_column(col)}, inplace=True)

    #         if name1 in df.columns:
    #             att = df[name1]
    #             att = list(att)
    #             date = list(df["Date"])
    #             result = list(zip(date,att))

    #             result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
    #             sorted_list = sorted(result, key=lambda x: x[0])
    #             sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]

    #             counts = {'P': 0, 'A': 0}

    #             for _, value in sorted_list:
    #                 counts[value] += 1

    #             p_count = counts['P']
    #             a_count = counts['A']
    #             n=len(sorted_list)
    #             generate_list = lambda n: list(range(1, n+1))
    #             return render_template('home.html', sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,mst1=mst1,mst2=mst2,mst3=mst3)
    #         else:
    #             return render_template('founderror.html')
    #     except Exception as e:
    #         return f"Java Lab B Error"

    # else:
    #     return f"nhi chalda"

if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0',port=5000)
