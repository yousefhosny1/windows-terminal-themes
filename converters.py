from mappings import iterm_to_windows
import plistlib
import json


class Utils:

    @staticmethod
    def prase_theme_name(path):
        print(path.split('/'))

    @staticmethod
    def rgb_to_hex(vals, rgbtype=1):
        """Converts RGB values in a variety of formats to Hex values.

         @param  vals     An RGB/RGBA tuple
         @param  rgbtype  Valid valus are:
                              1 - Inputs are in the range 0 to 1
                            256 - Inputs are in the range 0 to 255

         @return A hex string in the form '#RRGGBB' or '#RRGGBBAA'
        """

        if len(vals) != 3 and len(vals) != 4:
            raise Exception(
                "RGB or RGBA inputs to RGBtoHex must have 3 or 4 elements")
        if rgbtype != 1 and rgbtype != 256:
            raise Exception("rgbtype must be 1 or 256!")

        # Convert from 0-1 RGB/RGBA to 0-255 RGB/RGBA
        if rgbtype == 1:
            vals = [255 * x for x in vals]

        # Ensure values are rounded integers, convert to hex, and concatenate
        return '#' + ''.join(['{:02X}'.format(int(round(x))) for x in vals])


class ITermToWindowsConverter:

    def _parse_theme_name(file_path):
        file_name = file_path.split('/')[-1]
        return file_name.split('.')[0]

    @staticmethod
    def convert(path: str):
        with open(path, 'rb') as fp:
            pl = plistlib.load(fp)

        theme_name = ITermToWindowsConverter._parse_theme_name(path)
        result = {}

        for key in iterm_to_windows.schema.keys():
            if key == 'name':
                result[key] = theme_name
                continue
            iterm_key = iterm_to_windows.schema[key]
            iterm_value = pl[iterm_key]
            r = iterm_value['Red Component']
            g = iterm_value['Green Component']
            b = iterm_value['Blue Component']
            hex = Utils.rgb_to_hex((r, g, b), rgbtype=1)

            result[key] = hex
        with open(f'windows-themes/{theme_name}.json', 'w') as fp:
            json.dump(result, fp, indent=2, sort_keys=True)
