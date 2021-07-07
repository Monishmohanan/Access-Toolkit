# Access-Toolkit
A tool developed in python for mapping files, folders and urls

### About
The tool is developed for providing ease of access for the important files,
folders and urls which are frequently accessed in a work environment
The tool comes with a collection of five default buttons and the screen 
size of 280 x 450 while facilitating the ability to add or remove buttons
and also change the screen size

### What can you do with this tool?
1. You can create customized one-pager that maps
  a. Folder links
  b. File links
  c. Urls
2. Easy transfer of resources to new members in your team

### Initial Configuration

![image](https://user-images.githubusercontent.com/60011463/124712163-92ce3d00-df1c-11eb-859a-5438611ab07a.png)


- The initial configuration window is opened when the tool is run for the
  first time
- The user will be requested to setup the links for five button at the start
- The names of the buttons can be provided in the text boxes under the
  Buttons column
- The links can be provided in the respective text boxes near the button names
- Once the initial configuration is setup and saved, the configuration window
  is closed and the main window pops up
<u>Note:</u> 
The link boxes can also be left blank where in case the user does not
require all thefive buttons to be mapped

### Features

### Main Window

![image](https://user-images.githubusercontent.com/60011463/124713192-dc6b5780-df1d-11eb-95be-e9fe7b5744e4.png)

<u>Note:</u> 
The names of the buttons in the main window may vary depending upon user's initial config

### Settings Window

![image](https://user-images.githubusercontent.com/60011463/124713492-408e1b80-df1e-11eb-9894-fa12066eda6c.png)

### Window resizing
- Open the settings window from the File menu
- Enter the desired width and height into the text area
- User preview button for visualizing the new window size
- Save the new window size using the save button

### FAQ - Related to Build

1. What to do if tcl and tk errors shows up?
   Make sure that you have required tck and tk folders in the path
   specified by the error message. If not, try building the tool 
   using a different cx-freeze version
   
2. What to do if the tool shows warning message when opened?
   Reset the toolkit manually
   
3. How to manually reset the toolkit?
   Delete the accessData.db file and restart the toolkit
