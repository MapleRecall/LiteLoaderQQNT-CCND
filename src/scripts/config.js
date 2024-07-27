export const getConfig = async () => await LiteLoader.api.config.get("CanCanNeed");

export const setConfig = async (_config) => {
  await LiteLoader.api.config.set("CanCanNeed", _config);
  await getConfig();
  LL_CCND.update();
};