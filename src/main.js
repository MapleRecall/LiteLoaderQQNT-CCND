const manifest = require("../manifest.json");
const default_config = require("./config_default.json");
const { BrowserWindow, ipcMain } = require("electron");

// exports.onBrowserWindowCreated = (window) => {
//   window.on("show", () => update(window));
//   window.on("focus", () => update(window));
// };

(async () => {
  const config = await LiteLoader.api.config.get(manifest.slug, default_config);
  LiteLoader.api.config.set(manifest.slug, config);
})();

ipcMain.handle("LiteLoader.ccnd.update", () => {
  const allWindows = BrowserWindow.getAllWindows();
  allWindows.forEach((window) => {
    if (!window.isDestroyed()) {
      window.webContents.send("LiteLoader.ccnd.onUpdate");
    }
  });
});
