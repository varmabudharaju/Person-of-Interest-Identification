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


### Install Required Libraries

Navigate to the project directory and install the required Python libraries listed in the `requirements.txt` file.


### Setup the Django Web Server

Ensure Django is installed; if not, you can install it using pip. Then, initiate the database migrations and start the server.


### Configure the Raspberry Pi Camera Module

Make sure your Raspberry Pi is set up with the latest OS, and the camera module is connected properly. Refer to the official Raspberry Pi documentation for detailed setup instructions.

## Running the System

### Start the Django Web Server

To start the server, navigate to your project directory and run:


### Run the Facial Recognition Script

Ensure your Raspberry Pi and camera are correctly set up and connected. Then, run the facial recognition script:


### Access the Web Interface

Navigate to `http://localhost:8000` on your browser to monitor and manage the system.

## Future Scope

- Exploration of spherical canonical images for enhanced matching accuracy.
- Advanced study on the fusion of color and depth information for improved recognition capabilities.
- Investigating genetic algorithms for robust facial expression recognition applicable in high-security contexts.

## Conclusion

This project demonstrates the effective use of facial recognition technology for public safety, offering a scalable and cost-effective solution for the real-time identification of persons of interest.

## Contributors

- B. Sai Ram Varma
- M. Atal Bhupathi Varma

## Special Thanks

- Mr. Raghu Ram Reddy Tera, Chairman & Managing Director, Cassini Systems

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.



