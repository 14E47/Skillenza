import pandas as pd

# input csv file location
input_file_loc = './on_the_move_test/Position.csv'

df = pd.read_csv(input_file_loc)
# grouping by user_id
grouped_data = df.groupby(by=['user_id'])

user_ids = []
distance = []

# iterating through groups
for group in grouped_data:
    user = group[0]
    d = 0
    start = (0, 0)
    for i in group[1]['coordinate']:
        x, y = tuple(map(int, i.split(',')))

        # calculating successive distance between co-ordinates
        d += abs(x-start[0]) + abs(y-start[1])
        start = (x, y)

    user_ids.append(user)
    distance.append(d)

ndf = pd.DataFrame()
ndf['user_id'] = user_ids
ndf['distance'] = distance

# solution output to csv file
ndf.to_csv('./on_the_move_test/Solution.csv', columns=['user_id', 'distance'], index=False)
