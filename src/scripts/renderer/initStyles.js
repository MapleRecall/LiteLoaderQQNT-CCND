import { getConfig } from "../config.js";

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

    document.querySelector("#app")?.classList.toggle("ll-ccnd-peekable", config.peekOnBody);
    document.querySelector(".recent-contact")?.classList.toggle("ll-ccnd-peekable", config.peekOnContact);
    document.querySelector(".aio")?.classList.toggle("ll-ccnd-peekable", config.peekOnAIO);
  };
  updateStyles();

  LL_CCND.onUpdate(updateStyles);
};
