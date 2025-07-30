# import pytest
# from app.services.calculator import pow_op, fib_op, fact_op

# # --------- Power Function Tests ---------
# def test_pow_positive():
#     assert pow_op(2, 3) == 8

# def test_pow_zero_exponent():
#     assert pow_op(5, 0) == 1

# def test_pow_zero_base():
#     assert pow_op(0, 5) == 0

# # --------- Fibonacci Function Tests ---------
# def test_fib_zero():
#     assert fib_op(0) == 0

# def test_fib_one():
#     assert fib_op(1) == 1

# def test_fib_ten():
#     assert fib_op(10) == 55

# def test_fib_negative():
#     with pytest.raises(ValueError):
#         fib_op(-1)

# # --------- Factorial Function Tests ---------
# def test_fact_zero():
#     assert fact_op(0) == 1

# def test_fact_positive():
#     assert fact_op(5) == 120

# def test_fact_negative():
#     with pytest.raises(ValueError):
#         fact_op(-3)
