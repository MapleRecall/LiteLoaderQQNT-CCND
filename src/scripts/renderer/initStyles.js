import { getConfig } from "../config.js";
import { waitForElement } from "../utils.js";

const getFontStyle = (font) => {
  const FONT_PATH = `local:///${LL_CCND.BASE_PATH.replace(/\\/gi, "/")}/static/fonts/${font}.woff2?r=${Date.now()}`;
  return `@font-face {
        font-family: 'Messed Sans Pro';
        src: url('${FONT_PATH}');
    }`;
};

export default async () => {
  const baseStyle = document.createElement("link");
  baseStyle.rel = "stylesheet";
  baseStyle.id = "LL_CCND_Style";
  document.head.append(baseStyle);

  const fontStyle = document.createElement("style");
  fontStyle.id = "LL_CCND_Font";
  document.head.append(fontStyle);

  const updateStyles = async () => {
    const config = await getConfig();
    if (!config.enabled) {
      baseStyle.removeAttribute("href");
      return;
    }

    baseStyle.setAttribute("href", `local:///${LL_CCND.BASE_PATH}/src/styles/base.css?r=${Date.now()}`);
    fontStyle.textContent = getFontStyle(config.font);
    updateClass();
  };

  updateStyles();

  LL_CCND.onUpdate(updateStyles);

  window.navigation.addEventListener("navigate", updateClass);
};

async function updateClass(e) {
  const config = await getConfig();
  if (!config.enabled) return;

  const hash = e ? new URL(e.destination.url).hash : location.hash;

  waitForElement("#app").then((el) => {
    el?.classList.toggle("ll-ccnd-peekable", config.peekOnBody);
    el?.classList.toggle("ll-ccnd-perfmode", config.perfMode);
    el && (el.dataset["ccndAvatar"] = config.avatarStyle);
  });

  if (hash.includes("#/main")) {
    if (hash.includes("/message")) {
      waitForElement(".aio").then((el) => el?.classList.toggle("ll-ccnd-peekable", config.peekOnAIO));
      waitForElement(".recent-contact").then((el) => el?.classList.toggle("ll-ccnd-peekable", config.peekOnContact));
    }
    if (hash.includes("/contact")) {
      waitForElement(".contact-layout__content-area").then((el) => el?.classList.toggle("ll-ccnd-peekable", config.peekOnContact));
      waitForElement(".contact-layout__right-area").then((el) => el?.classList.toggle("ll-ccnd-peekable", config.peekOnAIO));
    }
  }

  if (hash.includes("#/forward") || hash.includes("#/record") ) {
    waitForElement("#app").then((el) => el?.classList.toggle("ll-ccnd-peekable", config.peekOnAIO));
  }
}
