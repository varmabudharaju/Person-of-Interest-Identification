# Person of Interest Identification & Notification System

## Project Overview
This project develops a cloud-based system for identifying persons of interest from live video feeds in public spaces, enhancing security in areas like airports and malls. Utilizing C/C++, Python, Django, and OpenCV, the system streamlines detecting and notifying authorities about individuals based on predefined criteria.

### Technologies Used
- **Languages:** C/C++, Python
- **Frameworks/Libraries:** Django, OpenCV, NumPy, PIL (Python Imaging Library), and others
- **Hardware:** Raspberry Pi with a camera module
- **Other Tools:** CV2, NumPy, Pickle for data handling and processing

## System Components
1. **Database**: Stores facial data of persons of interest.
2. **Facial Recognition Service**: Analyzes video feeds to detect and compare faces with database entries.
3. **Web Interface**: For database management and monitoring identification events.
4. **Notification Service**: Alerts personnel when a person of interest is identified, with snapshot evidence.

## Setup and Installation
Ensure you have Python 3.7 or newer and pip installed on your system. 

1. Clone the repository:
```bash
git clone <repository-url>
