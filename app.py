import flask, json, pymysql, hcskr, random
from flask import *

jindan=Flask(__name__)

@jindan.route("/")
def index():
    return render_template("index.html")

@jindan.route("/p")
def privacy():
    return render_template("privacy.html")

@jindan.route("/r", methods=["POST"])
def success():
    if request.method=="POST":
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234qwer', db='selfcheck', charset='utf8')
        cursor=db.cursor()

        result=request.form
        
        check=hcskr.selfcheck(result["이름"], result["생년월일"], result["지역"], result["학교"], result["학교종류"], result["비밀번호"])
        if check["error"]==False:
            ran=["six", "seven", "eight"]
            dom=random.choice(ran)

            for t in ran:
                sql = f"SELECT * FROM {t} WHERE name='{result['이름']}'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                if rows:
                    message=f"등록에 실패하였습니다!"
                    error_message=f"이미 등록된 학생정보입니다."
                    return render_template("result.html", message=message, error_message=error_message)
                else:
                    pass
            sql = f'insert into {dom}(name, birth, region, school, schooltype, password) values (%s, %s, %s, %s, %s, %s);'
            cursor.execute(sql, (result["이름"], result["생년월일"], result["지역"], result["학교"], result["학교종류"], result["비밀번호"]))
            db.commit()
            message="성공적으로 등록되었습니다!"
            return render_template("result.html", message=message)
            
        elif check["error"]==True:
            message=f"등록에 실패하였습니다!"
            return render_template("result.html", result=result, message=message, error_message=check['message'])
