from mars.bitboard import Bitboard

def main():
    bitboard = Bitboard(0)
    bitboard.set_bit(3) # set D1
    bitboard.pprint()
    return

if __name__ == '__main__':
    main()
