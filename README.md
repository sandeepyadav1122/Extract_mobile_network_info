
# Phone Number Details Extractor

This project is a simple Python application that extracts details about a phone number, including its region, service provider, and time zone(s). The extracted details are displayed in a graphical user interface (GUI) and saved to a CSV file for future reference.

## Features

- **Phone Number Parsing**: Parse phone numbers to retrieve details like region, service provider, and time zones.
- **GUI Interface**: User-friendly interface built with Tkinter.
- **CSV Export**: Automatically saves the phone number details to a CSV file.

## Requirements

- Python 3.x
- `phonenumbers` library
- `tkinter` (comes pre-installed with Python)

## Installation

* Install the required packages:
   ```bash
   pip install phonenumbers
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Enter a phone number in the format `+<country_code><phone_number>` and click "Submit".
3. The region, service provider, and time zone(s) associated with the phone number will be displayed in the GUI and saved to `phone_details.csv`.

![network details ](https://github.com/user-attachments/assets/151be935-b72d-4b23-8f1e-e1610d4e0bcf)

## Future Enhancements

- **Web Interface**: Transition from Tkinter to a web-based interface using HTML, CSS, and JavaScript.
- **Validation Improvements**: Enhance phone number validation for better accuracy.
- **Bulk Processing**: Add functionality to process and extract details from multiple phone numbers at once.

## Contributing

Contributions are welcome! Here are a few ways you can help:

- **UI/UX Enhancements**: Help build a web-based interface with HTML and CSS.
- **Feature Development**: Suggest and implement new features.
- **Bug Fixes**: Report issues and contribute fixes.

If you're interested, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
