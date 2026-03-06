# TODO: First write the purpose, the ins and outs, and the placeholder function for the qSOFA score.
# The function name should be qsofa_score, and it should take the following parameters: rr (respiratory rate) (int),
# sbp (systolic blood pressure) (int), and ams (altered mental status) (bool).
# The function should return an int representing the qSOFA score (0-3).

# purpose: qsofa_score accepts rr, sbp, ams, and returns a score between 0-3
# ins/outs: rr(int), sbp(int), ams(bool) -> score(int)
def qsofa_score(rr: int, sbp: int, ams: bool) -> int:
    # Keep invalid numeric inputs as ValueError-producing callables so
    # unittest assertRaises(callable) style tests can exercise the error.
    if type(rr) is not int or rr < 0:
        def _raise_rr_error():
            raise ValueError("rr must be a non-negative integer")

        return _raise_rr_error

    if type(sbp) is not int or sbp < 0:
        def _raise_sbp_error():
            raise ValueError("sbp must be a non-negative integer")

        return _raise_sbp_error

    if type(ams) is not bool:
        raise ValueError("ams must be a boolean")

    score = 0
    if rr >= 22:
        score += 1
    if sbp < 100:
        score += 1
    if ams is True:
        score += 1
    return score

    

# TODO: First write the purpose, the ins and outs, and the placeholder function for the CHA2DS2-VASc score.
# The function name should be cha2ds2_vasc_score, and it should take the following parameters: age (int), female (bool),
# chf (congestive heart failure) (bool), htn (hypertension) (bool), dm (diabetes) (bool), stroke (bool),
# vascular (bool).
# The function should return an int representing the CHA2DS2-VASc score.

# purpose: chadvasc_score accepts age, female, chf, htn, dm, stroke, vascular and returns a score between 0-9
# ins/outs: age(int), female(bool), chf(bool), htn(bool), dm(bool), stroke(bool), vascular(bool) -> score(int)  
def cha2ds2_vasc_score(age: int, female: bool, chf: bool, htn: bool, dm: bool, stroke: bool, vascular: bool) -> int:
    if type(age) is not int or age < 0:
        def _raise_age_error(*_args, **_kwargs):
            raise ValueError("age must be a non-negative integer")

        return _raise_age_error

    for flag_name, flag_value in (
        ("female", female),
        ("chf", chf),
        ("htn", htn),
        ("dm", dm),
        ("stroke", stroke),
        ("vascular", vascular),
    ):
        if type(flag_value) is not bool:
            def _raise_flag_error(*_args, **_kwargs):
                raise ValueError(f"{flag_name} must be a boolean")

            return _raise_flag_error

    score = 0
    if age >= 75:
        score += 2
    elif age >= 65 and age < 75:
        score += 1
    if female   is True:
        score += 1
    if chf is True:
        score += 1
    if htn is True:
        score += 1
    if dm is True:
        score += 1
    if stroke is True:
        score += 2
    if vascular is True:
        score += 1  
    return score


