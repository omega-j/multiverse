// preload.js

const { contextBridge, ipcRenderer } = require('electron');

// Expose a function to the renderer (React app) that calls the Python script via ipcRenderer
contextBridge.exposeInMainWorld('electron', {
  runPythonScript: () => ipcRenderer.invoke('run-python-script')  // This is the channel where we will invoke the Python script
});