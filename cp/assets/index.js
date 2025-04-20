fetch(
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt"
  )
    .then((response) => response.text())
    .then((text) => {
      const table = document.getElementById("proxy-table");
      const lines = text.split("\n");
      lines.forEach((proxyLink, index) => {
        if (!proxyLink.trim()) return;
        if (proxyLink.indexOf("#") === 0) return;

        const row = table.insertRow();
        const countCell = row.insertCell();
        const linkCell = row.insertCell();

        countCell.innerText = index - 5;
        linkCell.innerHTML = `<div class="link-preview" data-link="${proxyLink}">${proxyLink}</div>`;
      });

      document.querySelectorAll(".link-preview").forEach((linkPreview) => {
        linkPreview.addEventListener("click", () => {
          const linkToCopy = linkPreview.getAttribute("data-link");
          copyToClipboard(linkToCopy);
        });
      });

      function copyToClipboard(text) {
        const textarea = document.createElement("textarea");
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand("copy");
        document.body.removeChild(textarea);
        alert(`Copied to clipboard: ${text}`);
      }
    })
    .catch((error) => console.error(error));