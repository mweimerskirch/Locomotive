def duplicates(src, tgt):
    """
    Remove lines where source is the same as target
    """
    return src == tgt

def char_length(src, tgt, min = 0, max = float("inf")):
    """
    Removes lines outside of a certain character length

    :param int min: Minimum length (inclusive)
    :param int max: Maximum length (inclusive)
    """
    return len(src) <= min or len(src) >= max or \
           len(tgt) <= min or len(tgt) >= max

def source_target_ratio(src, tgt, min = 0, max = float("inf")):
    """
    Removes lines when the ratio (len(source) / len(target)) is outside of bounds

    :param float min: Lower bound (inclusive)
    :param float max: Upper bound (inclusive)
    """ 
    ratio = len(src) / len(tgt)
    return ratio <= min or ratio >= max

def uppercase_count_mismatch(src, tgt):
    """
    Removes lines that have a different number of uppercase letters
    """
    return sum(1 for ch in src if ch.isupper()) !=  sum(1 for ch in tgt if ch.isupper())

def contains(src, tgt, words = []):
    """
    Removes lines that contain these words

    :param list(str) words: List of words
    """
    for w in words:
        if w in src or w in tgt:
            return True
    return False

def digits_ratio(src, tgt, max = 0.4):
    """
    Removes lines when the ratio of numerical characters to the total length of the line
    is greather than max.

    :param float max: Maximum ratio (default: 0.4)
    """
    return len([c for c in src if c.isdigit()]) / len(src) >= max or \
                len([c for c in tgt if c.isdigit()]) / len(tgt) >= max

def nonalphanum_ratio(src, tgt, max = 0.4):
    """
    Removes lines when the ratio of non-alphanumeric characters to the total length of the line
    is greather than max.

    :param float max: Maximum ratio (default: 0.4)
    """
    return len([c for c in src if not c.isalnum()]) / len(src) >= max or \
                len([c for c in tgt if not c.isalnum()]) / len(tgt) >= max

def digits_sum_mismatch(src, tgt):
    """
    Removes lines where the sum of the digits between source and target is not the same.
    """
    return sum(int(num) for num in src if num.isdecimal()) != sum(int(num) for num in tgt if num.isdecimal())

def nonalphanum_count_mismatch(src, tgt):
    """
    Removes lines where the sum of non-alphanumeric characters between source and target is not the same
    """
    return sum(1 for ch in src if not ch.isalnum()) !=  sum(1 for ch in tgt if not ch.isalnum())