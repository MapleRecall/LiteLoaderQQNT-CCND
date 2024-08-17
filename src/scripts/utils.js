export const waitForElement = async function (selector, timeout = 10000) {
  return new Promise((resolve, reject) => {
    const interval = setInterval(() => {
      const element = document.querySelector(selector);
      if (element) {
        clearInterval(interval);
        clearTimeout(timeout);
        resolve(element);
      }
    }, 100);

    setTimeout(() => {
      clearInterval(interval);
      resolve(undefined);
    }, timeout);
  });
};

export const debounce = function (fn, time = 100) {
  let timer = null;
  return function (...args) {
    timer && clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, time);
  };
};
