VERSION = (0, 9, 0, 'beta', 1)

def get_version(version=VERSION):
    "Returns a PEP 386-compliant version number from VERSION."
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
    sub = mapping[version[3]] + str(version[4])

    return str(main + sub)

