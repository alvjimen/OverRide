def compute_serial(s: bytes) -> int:
    if len(s) < 6:
        raise ValueError("s must have length >= 6")
    if any(c <= 31 for c in s):
        raise ValueError("s contains control bytes")
    v4 = (s[3] ^ 0x1337) + 6221293
    # operate in 32-bit unsigned wraparound like C unsigned
    for c in s:
        v4 = (v4 + ((v4 ^ c) % 0x539)) & 0xffffffff
    return v4

def main():
    # choose a printable username of length >=6
    s = b'level06'   # must be bytes
    serial = compute_serial(s)
    print "compute_serial: ", serial
