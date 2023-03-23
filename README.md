## Download and Install Applications
This script automates the process of downloading and installing applications from a list of links. It works on Windows.

## Usage
- Download the executable file from the repository.
- Create a links.txt file in the same directory as the executable file.
-Add the links of the applications you want to download and install to the links.txt file, with each link on a new line.
- Run the executable file.
- Enter the expected download time in seconds when prompted. This is used to wait for the downloads to complete before installing the applications. If you don't provide an input, the default value of 60 seconds will be used.
- It will open the links in your default browser and install the downloaded applications.
- Wait for the script to finish running. The script will close automatically after 5 seconds.

## Notes
Invalid links will be skipped and not downloaded.
The script only installs applications that were downloaded within the expected download time.
The loading bar shows the progress of the waiting time and not the download or installation progress.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Vyary/apps-fetcher/blob/main/LICENSE) file for details.
