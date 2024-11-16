// electron.js

const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let win;

function createWindow() {
  // Create the BrowserWindow
  win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Ensure this is the correct path to preload.js
      nodeIntegration: false,
      contextIsolation: true, // Adds security
    }
  });

  // Open Developer Tools after window is created
  win.webContents.openDevTools();

  // Load the React app running on localhost
  win.loadURL('http://localhost:3000').catch((err) => {
    console.error('Failed to load the React app:', err);
  });

  // Close the window when the user closes it
  win.on('closed', () => {
    win = null;
  });
}

// This is where the Python script gets executed from the main process
ipcMain.handle('run-python-script', () => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python', ['midi_convert.py']);  // Adjust this as necessary for your script

    pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
      if (code === 0) {
        resolve('Python script ran successfully');
      } else {
        reject(`Python script failed with code ${code}`);
      }
    });
  });
});

// Start the application when ready
app.whenReady().then(createWindow);

// Quit the app when all windows are closed (except on macOS)
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});