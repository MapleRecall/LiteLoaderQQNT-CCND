import { getConfig, setConfig } from "../config.js";

export default async (view) => {
  const config = await getConfig();
  view.innerHTML = await (await fetch(`local:///${LL_CCND.BASE_PATH}/src/settings.html`)).text();

  [...view.querySelectorAll("setting-switch")].forEach((input) => {
    const configName = input.dataset["config"];
    input.toggleAttribute("is-active", config[configName]);

    input.addEventListener("click", async (event) => {
      event.target.toggleAttribute("is-active");
      config[configName] = event.target.hasAttribute("is-active");
      setConfig(config);
    });
  });

  LL_CCND.onUpdate(async () => {
    const config = await getConfig();
    [...view.querySelectorAll("setting-switch")].forEach((input) => {
      const configName = input.dataset["config"];
      input.toggleAttribute("is-active", config[configName]);
    });
  });

  [...view.querySelectorAll("setting-select")].forEach((input) => {
    const configName = input.dataset["config"];
    input.querySelector(`[data-value="${config[configName]}"]`)?.click();

    input.addEventListener("selected", async (event) => {
      config[configName] = event.detail.value;
      setConfig(config);
    });
  });
};
