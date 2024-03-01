import exifread
import argparse
import sys

# Function for converting coordinates into decimal format
def convert_to_degrees(value):
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

def convert_to_coordinates(info):
    lat = info.get('GPS GPSLatitude')
    lat_ref = info.get('GPS GPSLatitudeRef')
    lon = info.get('GPS GPSLongitude')
    lon_ref = info.get('GPS GPSLongitudeRef')

    if lat and lon and lat_ref and lon_ref:
        lat = convert_to_degrees(lat.values)
        lon = convert_to_degrees(lon.values)

        if lat_ref.values != "N":
            lat = -lat
        if lon_ref.values != "E":
            lon = -lon
        return lat, lon
    else:
        return None, None

def get_gps_coordinates(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            # Logic for converting EXIF GPS data into coordinates
            lat, lon = convert_to_coordinates(tags)
            if lat and lon:
                return lat, lon
            else:
                raise ValueError("GPS information not found")

    except Exception as e:
        print(f"Error processing the image: {e}")
        return None, None


def decrypt(data):
    try:
        with open(data, "rb") as f:
            contents = f.read()
            start = contents.find(b'-----BEGIN PGP PUBLIC KEY BLOCK-----')
            end = contents.find(b'-----END PGP PUBLIC KEY BLOCK-----')            
            # Check that the indices are found correctly.
            if start != -1 and end != -1 and end > start:
                end += len(b'-----END PGP PUBLIC KEY BLOCK-----')  # Убедимся, что мы включаем весь конец блока
                pgp_key = contents[start:end].decode('ascii')
                return pgp_key
            else:
                return "PGP Key block not found in the file."
    except Exception as e:
        return f"Error processing the file: {e}"

def main():
    parser = argparse.ArgumentParser(description='Image Analysis Tool')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('-map', '--show_map', action='store_true', help='Display GPS coordinates')
    parser.add_argument('-steg', '--show_steg', action='store_true', help='Display steganographic data')
    args = parser.parse_args()

    # Check if any option was provided.
    if not (args.show_map or args.show_steg):
        parser.print_help()
        sys.exit(1)

    if args.show_map:
        try:
            lat, lon = get_gps_coordinates(args.image_path)
            if lat is not None and lon is not None:
                print(f"Lat/Lon: ({lat:.3f})/({lon:.3f})")
            else:
                print("No GPS coordinates found")
        except Exception as e:
            print(f"An error occurred while extracting GPS coordinates: {e}")

    if args.show_steg:
        try:
            pgp_key = decrypt(args.image_path)
            if pgp_key:
                print(pgp_key)
            else:
                print("PGP key not found or there was an error.")
        except Exception as e:
            print(f"An error occurred while extracting the PGP key: {e}")

if __name__ == "__main__":
    main()
