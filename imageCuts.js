const MODES = ["colored", "mono"];
const INTERVAL_MS = 100;
const ACTIVE_DURATION = 2000;
const REST_DURATION = 1500;

let hangleIndex = 0;

function rand(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function getHangleFromIndex(mode, vertical) {
  const hangleKeys = Object.keys(DATA[mode][vertical]);
  if (hangleKeys.length === 0) return null;
  const hangle = hangleKeys[hangleIndex % hangleKeys.length];
  return hangle;
}

function getRandomPath(mode, pos, vertical, hangle) {
  const fileList = DATA[mode][vertical][hangle]?.[pos];
  if (!fileList || fileList.length === 0) return "";
  const file = rand(fileList);
  return `images/cbrk/${mode}/${vertical}/${pos}/${hangle}/${file}`;
}

function preloadImages(urls, callback) {
  let loaded = 0;
  const total = urls.length;
  const images = [];

  urls.forEach((url, index) => {
    const img = new Image();
    img.onload = () => {
      loaded++;
      if (loaded === total) callback(images);
    };
    img.src = url;
    images[index] = img;
  });
}

function startLoop() {
  const startTime = Date.now();

  const intervalId = setInterval(() => {
    const now = Date.now();
    if (now - startTime >= ACTIVE_DURATION) {
      clearInterval(intervalId);
      return; // 자동 반복 없
    }

    const modeTop = rand(MODES);
    const modeBottom = rand(MODES);

    const verticalKeys = Object.keys(DATA[modeTop]);
    const vertical = rand(verticalKeys);

    const hangle = getHangleFromIndex(modeTop, vertical);
    if (!hangle) return;

    const topPath = getRandomPath(modeTop, "1", vertical, hangle);
    const bottomPath = getRandomPath(modeBottom, "2", vertical, hangle);

    preloadImages([topPath, bottomPath], ([topImg, bottomImg]) => {
      document.getElementById("img-top").src = topImg.src;
      document.getElementById("img-bottom").src = bottomImg.src;
    });

    hangleIndex++;
  }, INTERVAL_MS);
}

//startLoop();

function loadInitialImages() {
  const modeTop = rand(MODES);
  const modeBottom = rand(MODES);

  const verticalKeys = Object.keys(DATA[modeTop]);
  const vertical = rand(verticalKeys);

  const hangle = getHangleFromIndex(modeTop, vertical);
  if (!hangle) return;

  const topPath = getRandomPath(modeTop, "1", vertical, hangle);
  const bottomPath = getRandomPath(modeBottom, "2", vertical, hangle);

  preloadImages([topPath, bottomPath], ([topImg, bottomImg]) => {
    document.getElementById("img-top").src = topImg.src;
    document.getElementById("img-bottom").src = bottomImg.src;
  });

  hangleIndex++;
}

document.addEventListener("DOMContentLoaded", () => {
  loadInitialImages();

  document.getElementById("trigger-button").addEventListener("click", () => {
    startLoop();
  });
});
