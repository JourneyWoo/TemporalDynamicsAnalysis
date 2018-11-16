import pandas as pd


def takeSecond(elem):
    return elem[1]

def time2second(str):
    hour = int(str[0:2])
    mi = int(str[3:5])
    sec = int(str[6:8])
    return hour * 60 * 60 + mi * 60 + sec


def data_process(data_path):
    print 'Read the Data...'
    csv_data = pd.read_csv(data_path)

    values = csv_data.values.tolist()
    values_dict = dict()

    for line in values:
        day = line[0][:10]
        repo = line[2]
        key = tuple([day, repo])
        time = time2second(line[0][11:19])

        save = [line[2], time, line[1], line[3]]
        if values_dict.has_key(key):
            add = values_dict[key]
            add.append(save)
            values_dict.update([(key, add)])
        else:
            add = []
            add.append(save)
            values_dict.update([(key, add)])

    return values_dict


if __name__ == '__main__':
    print 'Great!'
    values_dict = data_process('/Users/wuzhenglin/PycharmProjects/TemporalDynamicsAnalysis-data/'
                              'latent-hawkes-data/201705-07_qualified-repo-event.csv')

    values = []
    for d in values_dict:
        if len(values_dict[d]) < 3:
            continue
        temp = []
        for item in values_dict[d]:
            tem = [item[2], item[1]]
            temp.append(tem)
        values.append(temp)

    sequences = []
    for t1 in values:
        t1.sort(key=takeSecond)
        t = []
        for te in t1:
            t.append([te[0]])
        sequences.append(t)















