import { getConfig, setConfig } from "../config.js";
import { debounce, waitForElement } from "../utils.js";

const DISABLE_ICON = "/_upper_/resource/icons/channel_handup_speech_24.svg#channel_handup_speech_24";
const ENABLE_ICON = "/_upper_/resource/icons/channel_kick_red_16.svg#channel_kick_red_16";
const BUTTON_CLASS = "ll-ccnd-button";

export default async () => {
  initButton();
  window.navigation.addEventListener("navigate", initButton);
};

const initButton = debounce(async () => {
  if (!location.hash.includes("#/main") || document.querySelector(`.${BUTTON_CLASS}`)) return;

  const funcMenu = await waitForElement(".func-menu");
  if (!funcMenu) return;

  const button = (await waitForElement(".func-menu__item_wrap:last-child"))?.cloneNode(true);
  if (!button) return;

  button.classList.add(BUTTON_CLASS);
  button.querySelector(".q-badge-dot")?.remove();

  const updateButton = async () => {
    const config = await getConfig();
    button.querySelector("use").setAttribute("xlink:href", config.enabled ? ENABLE_ICON : DISABLE_ICON);
    button.title = config.enabled ? "不给看" : "看看你的";
    button.classList.toggle("enabled", config.enabled);
  };

  updateButton();
  LL_CCND.onUpdate(updateButton);

  button.addEventListener("click", async () => {
    const config = await getConfig();
    config.enabled = !config.enabled;
    setConfig(config);
  });
  console.log("initButton5");

  funcMenu.prepend(button);
});
