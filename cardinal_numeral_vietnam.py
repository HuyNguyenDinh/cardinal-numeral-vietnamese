base = { 1 : "nghìn ", 2 : "triệu ", 3 : "tỷ " }
baseT = { 0 : "không ", 1 : "một ", 2 : "hai ", 3 : "ba ", 4 : "bốn ", 5 : "năm ", 6 : "sáu ", 7 : "bảy ", 8 : "tám ", 9 : "chín "}
baseC = { 0 : "linh ", 1 : "mười ", 2 : "hai ", 3 : "ba ", 4 : "bốn ", 5 : "năm ", 6 : "sáu ", 7 : "bảy ", 8 : "tám ", 9 : "chín "}
baseDV = {1 : "mốt ", 2 : "hai ", 3 : "ba ", 4 : "bốn ", 5 : "lăm ", 6 : "sáu ", 7 : "bảy ", 8 : "tám ", 9 : "chín "}
def tach(n):
    a = []
    while(n > 0):
        d = n % 1000
        a.append(d)
        n //= 1000
    a.reverse()     #Xếp theo chiều từ trái sang phải giống như số tự nhiên chỉ tách theo nhóm 3 số
    return a

def dem(n):     # Đếm x trên cơ sở 10^(3 * x)
    c = 0
    n //= 1000
    while(n > 0):
        c += 1
        n //= 1000
    return c

def tram(n, vt):    #Truyền n theo 10^3, vt : vị trí, nếu tại 0 thì sẽ không có không trăm hay lẻ
    s = ""
    if n == 0:
        return s
    z = n // 100 #hàng trăm
    n %= 100
    for i in baseT:
        if z == 0 and vt == 0:    #Tại đây sẽ kiểm tra để bỏ qua không trăm
            continue
        if z == i:
            s += baseT[i]
            s += "trăm "
            break
    if n == 0:
        return s
    a = n // 10 #hàng chục
    n %= 10
    b = n #Hàng đơn vị
    if a < 2:
        for i in baseC:
            if a == 0 and z == 0 and vt == 0:  #Tại đây cũng kiểm tra để bỏ qua lẻ
                continue
            if a == i:
                s += baseC[i]
        if a == 0:
            for i in baseT:
                if b == i:
                    s += baseT[i]
                    return s
        if b == 0:
            return s
        elif b == 1:
                s += "một "
        else:
            for i in baseDV:
                if b == i:
                    s += baseDV[i]
    else:
        for i in baseC:
            if a == i:
                s += baseC[i]
                s += "mươi "
        if b == 0:
            return s
        else:
            for i in baseDV:
                if b == i:
                    s += baseDV[i]
    return s

def integer_to_vietnamese_numeral(n, region = "north"):
    if type(n) is not int or type(region) is not str:
        raise TypeError
    if n < 1 or region != "north" and region != "south":
      raise ValueError
    elif n > 999999999999:
        raise OverflowError
    else:
        a = tach(n)
        b = dem(n)
        s = ""
        for i in range(0, b + 1):
            s += tram(a[i], i)
            for j in base:
                if j == b - i and tram(a[i], i):    #Kiểm tra xem tram(a[i],i) có trả về không để thêm đơn vị trên base
                    s += base[j]
        if region == "south":
            s = s.replace("nghìn", "ngàn")
            s = s.replace("linh", "lẻ")
        return s
