
import datetime

# struct_time = time.strptime("30 12 2015", "%d %m %Y")
# print ("tuple : ", struct_time)


def watch(n, intervals):
    intervals.sort()

    merged = []
    for k in intervals:
        if len(merged) == 0:
            merged.append(k)
        else:
            prev = merged[-1]
            if k[0] > prev[1]:
                merged.append(k)
            else:
                merged[-1] = (min(prev[0], k[0]), max(prev[1], k[1]))

    duration = None
    for m in merged:
        m0 = list(map(int, m[0].split(':')))
        m1 = list(map(int, m[1].split(':')))

        t1 = datetime.timedelta(hours=m0[0], minutes=m0[1], seconds=m0[2])
        t2 = datetime.timedelta(hours=m1[0], minutes=m1[1], seconds=m1[2])

        if duration is None:
            duration = t2 - t1
        else:
            duration += t2 - t1

    if duration.days == 1:
        return '24:00:00'

    return str(duration)




if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        intervals = []
        for j in range(n):
            se = input().split()
            intervals.append((se[0], se[1]))

        print(watch(n, intervals))





# 4
# 3
# 07:00:00 09:30:00
# 09:00:00 10:30:00
# 11:00:00 11:30:00
# 1
# 00:00:00 24:00:00
# 1
# 20:30:00 21:00:00
# 1
# 00:00:00 23:59:59


# import datetime
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     intervals = []
#     for j in range(n):
#         se = input().split()
#         intervals.append((se[0], se[1]))
#
#     intervals.sort()
#     merged = []
#     for k in intervals:
#         if len(merged) == 0:
#             merged.append(k)
#         else:
#             prev = merged[-1]
#             if k[0] > prev[1]:
#                 merged.append(k)
#             else:
#                 merged[-1] = (min(prev[0], k[0]), max(prev[1], k[1]))
#
#     duration = None
#     for m in merged:
#         m0 = list(map(int, m[0].split(':')))
#         m1 = list(map(int, m[1].split(':')))
#
#         t1 = datetime.timedelta(hours=m0[0], minutes=m0[1], seconds=m0[2])
#         t2 = datetime.timedelta(hours=m1[0], minutes=m1[1], seconds=m1[2])
#
#         if duration is None:
#             duration = t2 - t1
#         else:
#             duration += t2 - t1
#
#     if duration.days == 1:
#         print('24:00:00')
#     else:
#         if len(str(duration)) != 8:
#             print('0' + str(duration))
#         else:
#             print(duration)
