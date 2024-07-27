const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("LL_CCND", {
  onUpdate: (callback) => ipcRenderer.on("LiteLoader.ccnd.onUpdate", callback),
  update: () => ipcRenderer.invoke("LiteLoader.ccnd.update"),

  BASE_PATH: LiteLoader.plugins["CanCanNeed"].path.plugin,
});
