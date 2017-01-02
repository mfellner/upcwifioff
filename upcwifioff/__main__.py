import argparse
import upcwifioff

parser = argparse.ArgumentParser(description='Turn UPC WiFi off.')
parser.add_argument('driver_path', type=str, help='phantomjs driver path')

args = parser.parse_args()
upcwifioff.main(args.driver_path)
