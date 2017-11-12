from os import walk
import pandas as pd
from tqdm import tqdm

f = []
for (dirpath, dirnames, filenames) in walk('./sessions/'):
    f = filenames
    break
# data = []
with open('data.csv', mode='w') as k:
    print('events, command', file=k)
    for f in tqdm(filenames, ascii=True, desc='Files'):
        group = pd.read_csv('./sessions/' + f)
    #     for index, group in pd.read_csv(f).groupby('idesessionuuid', as_index=False):
        events = group['event_type_complete'].tolist()
        indices = [i for i, x in enumerate(
            events) if x.split('-')[0] == "CommandEvent"]

        for ind in indices:
            x = events[:ind][:-10]  # Max length of event chains to 10
            y = events[ind]
            if len(x) > 0:
                print(' '.join(x) + ',' + y, file=k)
                # data.append([' '.join(x), y])
# del group
# del events
# del indices

# pd.DataFrame(data, columns=['events', 'command']
#              ).to_csv('data.csv', index=False)
# data.to_csv('data.csv', index=False)
