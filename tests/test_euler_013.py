import pytest

from euler_013 import first_ten_digits

number_to_first_ten_digits = {
    1234567890: 1234567890,
    544543254252554325425254325254324254: 5445432542,
    4252554325425254325254324254: 4252554325,
}
@pytest.mark.parametrize('number, expected_number', number_to_first_ten_digits.items())
def test_known_number_returns_expected(number, expected_number):
    assert expected_number == first_ten_digits(number)

# bad_values_to_expected_error = {
#     -1: ValueError,
#     0: ValueError,
#     1: ValueError,
#     'hello': ValueError,
# }
# @pytest.mark.parametrize('bad_value, expected_error', bad_values_to_expected_error.items())
# def test_known_value_returns_expected_error(bad_value, expected_error):
#     # Rendundant tests show alternate syntax.
# 
#     with pytest.raises(expected_error):
#         largest_factor(bad_value)
# 
#     # older syntax works with 2.4
#     pytest.raises(expected_error, "largest_factor(bad_value)")
# 
