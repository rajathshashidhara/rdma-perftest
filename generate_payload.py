# inlcude all the necessary libraries
import random
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-entries', type=int, help='Number of entries to process')

    args = parser.parse_args()

    proc = 0

    if args.num_entries:
        num_entries = args.num_entries
    else:
        print("Usage: python generate_payload.py --num_entries")
        sys.exit(1)

    output_file = open("./payload.txt", "w")
    for i in range(0, num_entries): 
        # random_num = random.randint(0, 0xFFFFFFFF)

        # if (i % 1024 == 0):
        #     output_file.write('0x{0:08x}'.format(proc) + ",")
        #     proc+=1
        # else:
        #     output_file.write('0x{0:08x}'.format(i) + ",") 

        output_file.write('0x{0:08x}'.format(i) + ",") 

    output_file.close()
