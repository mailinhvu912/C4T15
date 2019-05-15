diem = ['sử', 'anh', 'tin']

# # 1: index based
# i = int(input('môn loại bỏ: ', ))
# diem.pop(i)
# print(*diem, sep=', ')

# 2: value based
mon_loai_bo = input('môn loại bỏ: ', )
diem.remove(mon_loai_bo)
print(*diem, sep=', ')