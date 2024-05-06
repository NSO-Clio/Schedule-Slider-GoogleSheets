from flask import Flask, render_template, request, jsonify
from CreatTables import TableWorker
from datetime import datetime
import pandas as pd


DAY_DATA = {
    0: "понедельник",
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
    6: "понедельник",
    7: "понедельник" # "суббота"
}
application = Flask(__name__, template_folder='templates')
tw = TableWorker(
    url='YOUR_URL',
    id_gid_one_sm=[YOUR_ID],
    id_gid_two_sm=[YOUR_ID],
    id_gid_consult=[YOUR_ID],
    path_service_account='TimeTable_serviceAcc.json'
)


@application.route('/application/TableWorker/v2')
def application_TableWorker_v2():
    return jsonify(tw.geter())


@application.route('/')
def getTimeTableClass() -> str:
    tw.creatData()
    tw.creatDataClasses()

    now = datetime.now()
    day = datetime.isoweekday(now)
    classes = tw.get_classes()

    data_one = []
    data_classes_one = []
    for i in tw.get_Data(gid=True)['gid_one'].columns[3:].tolist():
        for j in classes:
            if i in classes[j]:
                data_classes_one.append(i)
    step_one = max([i for i in range(1, 10) if len(data_classes_one) % i == 0])
    for elem in range(0, len(data_classes_one), step_one):
        class_one = data_classes_one[elem:elem + step_one]
        tmp_one = tw.get_Data(gid=True)['gid_one'][['Дни', 'Уроки', 'Время'] + class_one]
        ind_elem = tmp_one[tmp_one['Дни'] == DAY_DATA[day]].index[0]
        tmp_one = [class_one] + tmp_one.iloc[ind_elem:ind_elem + 8, :].values.tolist()
        data_one.append(tmp_one)

    data_two = []
    data_classes_two = []
    for i in tw.get_Data(gid=True)['gid_two'].columns[3:].tolist():
        for j in classes:
            if i in classes[j]:
                data_classes_two.append(i)
    step_two = max([i for i in range(1, 10) if len(data_classes_one) % i == 0 or i < len(data_classes_two)])
    for elem in range(0, len(data_classes_two), step_two):
        class_one = data_classes_two[elem:elem + step_two]
        tmp_two = tw.get_Data(gid=True)['gid_two'][['Дни', 'Уроки', 'Время'] + class_one]
        ind_elem = tmp_two[tmp_two['Дни'] == DAY_DATA[day]].index[0]
        tmp_two = [class_one] + tmp_two.iloc[ind_elem:ind_elem + 8, :].values.tolist()
        data_two.append(tmp_two)

    for elem in data_one:
        print(elem)

    for elem in range(len(data_one)):
        print(elem, data_one[elem])

    print(len(data_one), len(data_two))
    for i in range(0, 1, 2) if len(data_two) > 0 else range(50):
        print(i)

    print(tw.get_Data(gid_consult=True))
    print(tw.get_Data(gid_consult=True).columns)
    print(tw.get_Data(gid_consult=True).iloc[46, :].values)
    print(len(tw.get_Data(gid_consult=True)))

    data_consult = []
    dt_cons = tw.get_Data(gid_consult=True)[['Учителя', DAY_DATA[day]]].copy()
    dt_cons = dt_cons[dt_cons[DAY_DATA[day]] != ' '].values.tolist()
    print(dt_cons)
    print(len(dt_cons))

    step_consult = max([i for i in range(1, 15) if len(dt_cons) % i == 0])
    print(step_consult)
    if step_consult == 1 and len(dt_cons) > 20:
        step_consult = 10

    for elem in range(0, len(dt_cons), step_consult):
        if elem // 10 == len(dt_cons) // 10:
            tmp = dt_cons[elem:len(dt_cons)]
            data_consult.append([(i[0], ''.join(i[-1].split()[:3]), i[-1].split()[-1]) for i in tmp])
        else:
            tmp = dt_cons[elem:elem + step_consult]
            data_consult.append([(i[0], ''.join(i[-1].split()[:3]), i[-1].split()[-1]) for i in tmp])

    for i in data_consult:
        print(i)

    return render_template(
        'time_table_for_class.html',
        dataLessons_gid_one=data_one,
        dataLessons_gid_two=data_two,
        data_TimeTable_Teacher=data_consult,
        len_one=len(data_one),
        len_two=len(data_two),
        len_cons=len(data_consult),
        day_week=DAY_DATA[day]
    )


if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5050)
