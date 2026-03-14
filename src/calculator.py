# def add(a, b):
#     return a + b

#=============== Trường hợp push fail ===============
def add(a, b):
    return a - b  # Sửa dấu + thành dấu -

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0")
    return a / b