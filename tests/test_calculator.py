import pytest
from src.calculator import add, subtract, multiply

# 1. KHAI BÁO DỮ LIỆU TEST
# Cấu trúc: (a, b, expected)
ADD_DATA = [
    (15, 25, 40),    # TC_01: Phân vùng dương
    (-5, -10, -15),  # TC_02: Phân vùng âm
]

SUBTRACT_DATA = [
    (20, 5, 15),     # TC_03
]

MULTIPLY_DATA = [
    (50, 0, 0),      # TC_04: Giá trị biên
]

DIVIDE_DATA = [
    (7, 2, 3.5),     # TC_05: Kiểu Float
]

# 2. ÁP DỤNG DỮ LIỆU VÀO LOGIC TEST
@pytest.mark.parametrize("a, b, expected", ADD_DATA)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", SUBTRACT_DATA)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", MULTIPLY_DATA)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected



# 3. KIỂM THỬ NGOẠI LỆ (Negative Tests)
def test_divide_by_zero():
    # TC_06: Kiểm thử ngoại lệ chia cho 0
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_invalid_type():
    # TC_07: Nhập sai kiểu dữ liệu
    with pytest.raises(TypeError):
        add("abc", 5)