import { getConfig } from "./scripts/config.js";
import onSettingWindowCreated from "./scripts/renderer/settings.js";
import initStyles from "./scripts/renderer/initStyles.js";
import initSideButton from "./scripts/renderer/sideButton.js";

(async () => {
  await getConfig();
  await initStyles();
  await initSideButton();
})();

export { onSettingWindowCreated };
