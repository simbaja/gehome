# GE Home SDK Changelog

## 2025.11.5

- Added new light level converter for hoods (old and new had mismatched ordering)
- Fixed off-by-one issue in fan/light level availability

## 2025.11.4

- Fixed water heater mode setting
- Added dishwasher remote command configuration

## 2025.11.3

- Added branding improvements
- Miscellaneous minor bugfixes

## 2025.11.2

- Reduced websocket library requirements to allow for more HA installs to utilize

## 2025.11.1

- Minor Advantium and hood updates

## 2025.11.0

- BREAKING: Removed XMPP Client (unmaintained)
- Advantium support (@ehendrix23)
- Water heater support improvements (@heythisisnate)
- Additional Range hood ERD codes (@jth-67)
- Improved AC support (@dbrand666)
- Cleanup of code to remove pylance and other issues
- Updated websocket client to latest websocket library
- Switched from lxml to Beautiful Soup
- Added initial tests

## 2025.5.0

- Water heater support (@jtbnz)

## 2025.2.0

- Laundry bugfixes and support

## 0.5.30 - 0.5.42

- Additional laundry support (@tdfountain)
- Fridge hot water support (@vincent99)
- Miscellaneous bug and documentation fixes

## 0.5.15 - 0.5.29

- Miscellaneous bug fixes

## 0.5.14

- Support for Dehumidifiers
- Support for new cooktops (new format)
- Fix for missing values on F&P dishwashers
- Added warming drawer to ovens

## 0.5.10

- Added OIM descaling
- Added EcoDry conversion

## 0.5.9

- Fixed issues with Python 3.11
- Fixed dependency issues

## 0.5.8

- Added additional dishwasher functionality (@NickWaterton)
- Added exception handling for ValueErrors (@NickStallman)

## 0.5.5 - 0.5.7

- Added additional fridge codes
- Added geothermal heater codes (@seantibor)
- Added initial dual drawer dishwasher codes
- Bugfix: modified fridge hot water set temp to length = 2

## 0.4.25 - 0.5.0

- Added additional appliance types
- Added gehome-appliance-data application to assist with debugging

## 0.4.23 - 0.4.24

- Updated to fix authentication issues (EU vs US)

## 0.4.13 - 0.4.22

- Opal ice maker support
- Microwave support
- Water softener support
- Coffee maker support
- Data typing enhancements
- Example updates (to prevent common issues)

## 0.4.7 - 0.4.12

- Fridge, oven, and dishwasher enhancements

## 0.4.5 - 0.4.6

- Hood fixes and enhancements

## 0.4.4

- Advantium bug fixes
- Oven extended modes support
- Initial hood support

## 0.4.3

- Fixes for unknown unit types
- Additional A/C support

## 0.4.2

- Initial A/C support
- Additional bugfixes

## 0.4.0

- Additional bugfixes

## 0.3.14 - 0.3.21

- Additional laundry support/bugfixes
- Additional water filter support/bugfixes
- Additional Advantium support/bugfixes
- Enhanced connection debugging
- Enhanced authentication support
- Added feature retrieval support
- Miscellaneous bugfixes

## 0.3.13

- Initial laundry support
- Initial water filter support
- Initial Advantium support

## 0.3.12

- Renamed from gekitchensdk to gehomesdk

## 0.3.0 - 0.3.11

- Major refactoring

## 0.2.19

- Initial tracked version