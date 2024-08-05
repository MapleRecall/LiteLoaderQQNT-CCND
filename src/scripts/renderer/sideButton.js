import { getConfig, setConfig } from "../config.js";

const DISABLE_ICON = "/_upper_/resource/icons/channel_handup_speech_24.svg#channel_handup_speech_24";
const ENABLE_ICON = "/_upper_/resource/icons/channel_kick_red_16.svg#channel_kick_red_16";

export default async () => {
  const addButtonInterval = setInterval(() => {
    if (location.hash.includes("#/main")) {
      const funcMenu = document.querySelector(".func-menu");
      if (!funcMenu) return;

      const button = funcMenu.querySelector(".func-menu__item_wrap")?.cloneNode(true);
      if (!button) return;

      button.classList.add("ll-ccnd-button");

      const updateButton = async () => {
        const config = await getConfig();
        button.querySelector("use").setAttribute("xlink:href", config.enabled ? ENABLE_ICON : DISABLE_ICON);
        button.title = config.enabled ? "不给看" : "看看你的";
        button.querySelector(".icon-item").setAttribute("aria-label", button.title);
        button.classList.toggle("enabled", config.enabled);
      };
      
      updateButton();
      LL_CCND.onUpdate(updateButton);

      button.addEventListener("click", async () => {
        const config = await getConfig();
        config.enabled = !config.enabled;
        setConfig(config);
      });
      funcMenu.prepend(button);

      clearInterval(addButtonInterval);
    }
  }, 100);
  setTimeout(() => clearInterval(addButtonInterval), 10000);
};
