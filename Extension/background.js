chrome.webRequest.onBeforeRequest.addListener(
  (details) => {
    if (details.type !== "main_frame") return;

    fetch("http://127.0.0.1:8000/api/", {
      method: "GET",
      headers: {
        "X-O-URL": details.url
      }
    })
    .then(res => {
      if (res.status === 403 && Number.isInteger(details.tabId) && details.tabId !== -1) {
        chrome.tabs.remove(details.tabId, () => {
          chrome.notifications.create({
            type: "basic",
            iconUrl: "icon.png",
            title: "Blocked.AI",
            message: "This URL may be harmful and has been blocked!",
            priority: 2
          });
        });
      }
    })
    .catch(err => {
      console.error("API error:", err);
    });
  },
  { urls: ["<all_urls>"] },
  []
);
