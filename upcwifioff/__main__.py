import argparse
import upcwifioff


def main():
    parser = argparse.ArgumentParser(description='Turn UPC WiFi off.')
    parser.add_argument('driver_path', type=str, help='phantomjs driver path')

    args = parser.parse_args()
    upcwifioff.run(args.driver_path)

if __name__ == "__main__":
    main()
