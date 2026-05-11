from prime_checker import is_prime


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(97)
    assert is_prime(7919)

    assert not is_prime(-5)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(9)
    assert not is_prime(100)
    assert not is_prime(7920)


if __name__ == "__main__":
    test_is_prime()
    print("All tests passed.")
