from flask import Flask, render_template, request

app = Flask(__name__)

def classify_depression(scores):
    total_score = sum(scores)
    if total_score <= 4:
        return "لا يوجد اكتئاب", "لا تظهر علامات على وجود اكتئاب. يُفضل الاستمرار في العادات الصحية والمتابعة الدورية حسب الحاجة."
    elif total_score <= 9:
        return "اكتئاب بسيط", "قد تستفيد من استشارة نفسية خفيفة أو متابعة دون علاج. يُنصح بتحسين نمط الحياة وتقنيات تنظيم المزاج."
    elif total_score <= 14:
        return "اكتئاب متوسط", "من المفضل التحدث مع مختص نفسي لتقييم الحاجة لجلسات علاج معرفي سلوكي أو تدخل نفسي أعمق."
    elif total_score <= 19:
        return "اكتئاب متوسط إلى شديد", "يُنصح بمقابلة أخصائي نفسي أو طبيب نفسي. قد تحتاج إلى جلسات علاج نفسي منتظمة وربما تدخل دوائي."
    else:
        return "اكتئاب شديد جدًا", "يجب التوجه إلى مختص فورًا. التقييم الطبي العاجل مطلوب، وربما يكون هناك حاجة لخطة علاج شاملة تتضمن دواء وجلسات."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        scores = [int(request.form.get(f'q{i+1}', 0)) for i in range(9)]
        result, recommendation = classify_depression(scores)
        total = sum(scores)
        return render_template('index.html', result=result, total=total, recommendation=recommendation)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
