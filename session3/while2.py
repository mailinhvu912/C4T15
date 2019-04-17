while True:
    new_password = input('Nhập mật khẩu mới: ')             #đủ 8 kí tự/ phải chứa số
    
    if len(new_password) >= 8:
        if new_password.isdigit():
            print('strong enough')
        elif new_password.isalpha():
            print('mật khẩu phải có số')
        else:
            print('strong enough')

    else:
        print('mật khẩu phải đủ 8 kí tự')


# sao m k nghĩ ngược lại: 2 dòng (k đủ 8 thì sai, toàn chữ thì sai)
    
